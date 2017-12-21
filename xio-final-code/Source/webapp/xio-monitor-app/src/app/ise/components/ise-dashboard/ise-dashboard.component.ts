import {Component, OnInit, OnDestroy, Pipe, PipeTransform,  ViewChild} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { $WebSocket } from 'angular2-websocket/angular2-websocket';
import { AppSettings } from '../../../app-setting';
import { PoolsService } from './../../services/pools.service';
import { StoragevolumeService } from './../../services/storagevolume.service';
import { Store } from '@ngrx/store';
import { GetAllPoolsAction } from '../../../actions/pools.actions';
import { State, getAllVolumesState, getAllPoolsState } from '../../../reducers';
import { SetISEId } from '../../../actions/ise-management.actions';
import { GetRatioAction } from '../../../actions/pools.actions';
import { GetAllVolumesAction } from '../../../actions/volume.actions';
import { log } from '../../../common/utils/logger';
import { Pools } from '../../models/pools';
import { IopsComponent } from '../../../ise/components/charts/iops/iops.component';
import { LatencyComponent } from '../../../ise/components/charts/latency/latency.component';
import { DataRateComponent } from '../../../ise/components/charts/data-rate/data-rate.component';
import { IVolume } from '../../models/perofmace-volume.model';
import { IBar } from '../../models/ibar.model';
import { IBarContainer } from '../../models/ibarcontainer.model';

@Pipe({ name: 'nonEmptyContainers' })
export class NonEmptyContainersPipe implements PipeTransform {
  transform(containers: IBarContainer[]) {
    return containers.filter(container => container.bars.length && container.storageSize > 0);
  }
}

@Component({
  selector: 'app-ise-dashboard',
  templateUrl: './ise-dashboard.component.html',
  styleUrls: ['./ise-dashboard.component.scss']
})
export class IseDashboardComponent implements OnInit, OnDestroy {

  public iops_new_data: any;
  public latency_new_data: any;
  public datarate_new_data: any;
  public ise_id: number;
  public loading_stack: any;
  public ws: any;
  public range_Tb: any;
  public measure_used: any;
  public measure_Tb: any;
  public current_used: any;
  public current_r: any;
  public measure_reduction: any;
  public available: any;
  public available_r: any;
  public available_Tb: any;
  public current: any;
  public current_Tb: any;
  public host_used: any;
  public allocpercent: any;
  public allocatepercent: any;
  public host_Tb: any;
  public alloc_Tb: any;
  public used_Tb: any;
  public system_capacity: any;
  public bullet_chart = true;
  public storageUtilization = {
    pools: null,
    ratio: null
  };
  public count = 0;
  public total_size$;
  public volumes_list$;
  public volume_list;
  public capacitiesView = 'graph';
  public containers: IBarContainer[];
  public scaleContainerSize: number;
  public scaleContainers: number[];
  public all_pools_state_obs$;
  public totalPoolData = {
    size: 0,
    used: 0,
    free: {
      raw: 0,
      raid1: 0,
      raid5: 0
    }
  };
  public barColors = {
    blue: {
      rgb: { R: 0, G: 104, B: 179 },
      gradient: 'linear-gradient(to bottom, rgba(0,104,179,1) 0%, rgba(23,88,120,1) 49%,' +
      ' rgba(23,88,120,1) 51%, rgba(0,104,179,1) 100%)'
    }, green: {
      rgb: { R: 44, G: 160, B: 44 },
      gradient: 'linear-gradient(to bottom, rgba(44,160,44,1) 0%, rgba(31,130,31,1) 49%, ' +
      'rgba(31,130,31,1) 51%, rgba(44,160,44,1) 100%)'
    }, teal: {
      rgb: { R: 68, G: 138, B: 150 },
      gradient: 'linear-gradient(to bottom, rgba(68,138,150,1) 0%, rgba(46, 107, 117, 1) 49%,' +
      ' rgba(46, 107, 117, 1) 51%, rgba(68,138,150,1) 100%)'
    }, yellow: {
      rgb: { R: 192, G: 215, B: 45 },
      gradient: 'linear-gradient(to bottom, rgba(192,215,45,1) 0%, rgba(145,167,2,1) 49%, ' +
      'rgba(145,167,2,1) 51%, rgba(192,215,45,1) 100%)'
    }, pink: {
      rgb: { R: 197, G: 22, B: 191 },
      gradient: 'linear-gradient(to bottom, rgba(197,22,191,1) 0%, rgba(156,0,143,1) 49%,' +
      ' rgba(156,0,143,1) 51%, rgba(197,22,191,1) 100%)'
    }
  };

  public screen_name: string;
  @ViewChild(IopsComponent) iopscomponent: IopsComponent;
  @ViewChild(LatencyComponent) latencycomponent: LatencyComponent;
  @ViewChild(DataRateComponent) datarateComponent: DataRateComponent;

  constructor(public route: ActivatedRoute,
    public router: Router,
    public ps: PoolsService,
    public svs: StoragevolumeService,
    public store: Store<State>) {
    this.screen_name = 'dashboard';
    this.loading_stack = {
      dashboard_details: false,
      capacity_details: false,
      dashboard_details_text: 'Loading...'
    };
  }

  setContainerWidths() {
    let divisors = [1000, 750, 500, 250, 100, 75, 50, 40, 30, 20, 10, 5, 2], maxCapacity;
    maxCapacity = Math.max(...this.containers.map(container => container.storageSize));
    this.scaleContainerSize = divisors.find(divisor => maxCapacity / divisor >= 4);
    if (maxCapacity && this.scaleContainerSize) {
      let containerSizeAsPercent = (this.scaleContainerSize / maxCapacity) * 100;
      this.scaleContainers = Array(Math.ceil(maxCapacity / this.scaleContainerSize))
                            .fill(containerSizeAsPercent);
      this.containers.forEach(container => {
            container.width = ((container.storageSize / maxCapacity) * 100).toFixed(1);
      });
    }
  }


  ngOnInit() {
    this.containers = [{
        storageSize: 0, // in TB
        storageType: 'Virtual',
        capacityLabel: 'Provisioned',
        labelOffset: 'bottom',
        width: '',
        color: { R: 150, G: 180, B: 238 }, // blue
        bars: []
      }, {
        storageSize: 0, // in TB
        storageType: 'Physical',
        capacityLabel: 'Total Capacity',
        labelOffset: 'top',
        width: '',
        color: { R: 167, G: 210, B: 140 }, // green
        bars: [{
            data: { value: 0, label: 'Allocated', labelOffset: 'top' },
            color: this.barColors.yellow.rgb,
            gradient: this.barColors.yellow.gradient
        }]
      }
    ];

    this.iops_new_data = '';
    this.route.parent.params.subscribe(params => {
      this.ise_id = parseInt(params['ise_id'], 10);
      this.store.dispatch(new SetISEId(this.ise_id));
      this.loading_stack.capacity_details = true;

      let virtual = this.containers.find(container => container.storageType === 'Virtual');
          virtual.storageSize = 0;
          virtual.bars.splice(0);
      this.loadIseDashBoardData();
    });
  }


  loadIseDashBoardData() {
    Promise
      .all([this.getRatio(), this.subcribeVolumeList(), this.getPoolsList(this.ise_id), this.getVirtualSize()])
      .then(([ratioData, volumeListResponse, poolsListResponse, virtualSizeResponse]: any[]) => { })
      .then(() => {
        this.loading_stack.capacity_details = false;
      });
  }

  getRatio() {
    return new Promise((resolve, reject) => {
      this.store.dispatch(new GetRatioAction({
        ise_id: this.ise_id,
        cb: (data, err) => {
          if (err) {
            this.bullet_chart = false;
            log(err, 'error');
            reject(err);
          } else {
            this.storageUtilization.ratio = data.datareduction.dedup.ratio;
            resolve();
          }
        }
      }));
    });
  }

  ngOnDestroy() {
    if (this.volumes_list$) {
      this.volumes_list$.unsubscribe();
    }
    if (this.all_pools_state_obs$) {
      this.all_pools_state_obs$.unsubscribe();
    }
    if (this.total_size$) {
      this.total_size$.unsubscribe();
    }
  }

  getCallsCount() {
    this.getRTData();
  }

  getVirtualSize() {
    let host_visible;
    return new Promise((resolve, reject) => {
      if (this.total_size$) {
        this.total_size$.unsubscribe();
      }
      this.total_size$ = this.svs.getTotalSize(this.ise_id).subscribe(
        result => {
          host_visible = result.overall_size;
          this.allocpercent = result.overall_allocpercent / 100;
          this.allocatepercent = ((this.allocpercent / host_visible) * 100);
          this.allocatepercent += '%';
          this.alloc_Tb = (this.allocpercent / 1024).toFixed(4);
          this.alloc_Tb += ' TB';
          this.host_used = ((host_visible - this.allocpercent) / 1000) * 100;
          this.used_Tb = (this.host_used / 1024).toFixed(4);
          this.host_used += '%';
          this.host_Tb = (host_visible / 1024).toFixed(4);
          this.host_Tb += ' TB';
          this.used_Tb += ' TB';
          let virtual = this.containers.find(container => container.storageType === 'Virtual');
          if (virtual) {
            virtual.storageSize = result.overall_size / 1024;
            this.setContainerWidths();
          }
          resolve();
        }, error => {
          this.bullet_chart = false;
          reject(error);
        });
    });
  }

  subcribeVolumeList() {
    return new Promise((resolve, reject) => {
      if (this.volumes_list$) {
        this.volumes_list$.unsubscribe();
      }

      this.store.dispatch(new GetAllVolumesAction({
        ise_id: this.ise_id,
        cb: (success, error) => {
          if (!error) {
            this.volumes_list$ = this.store.select(getAllVolumesState).subscribe(data => {
              let bars: IBar[] = [{
                  data: { value: 0, label: 'Dedupe Allocated', labelOffset: 'bottom' },
                  color: this.barColors.blue.rgb,
                  gradient: this.barColors.blue.gradient
                }, {
                  data: { value: 0, label: 'RAID1 Allocated', labelOffset: 'bottom' },
                  color: this.barColors.pink.rgb,
                  gradient: this.barColors.pink.gradient
                }, {
                  data: { value: 0, label: 'RAID5 Allocated', labelOffset: 'bottom' },
                  color: this.barColors.teal.rgb,
                  gradient: this.barColors.teal.gradient
              }];
              let reduced = data.reduce(function(result, current: IVolume) {
                let allocated = ((current.size / 1024) * (current.allocpercent / 100)),
                  category: string;
                if (current.type === 'Dedupe') {
                  category = 'Dedupe Allocated';
                } else if (current && current.configurationpolicy &&
                  current.configurationpolicy.redundancy._attr.string === 'RAID-5') {
                  category = 'RAID5 Allocated';
                } else if (current && current.configurationpolicy &&
                  current.configurationpolicy.redundancy._attr.string === 'RAID-1') {
                  category = 'RAID1 Allocated';
                }

                if (!result[category]) {
                  result[category] = 0;
                }
                result[category] += allocated;
                return result;
              }, {});

              let categoryBars = bars.map(function(bar) {
                bar.data.value = reduced[bar.data.label];
                return bar;
              });
              let virtual = this.containers.find(container => container.storageType === 'Virtual');
                  virtual.bars = categoryBars.filter(bar => bar.data.value > 0);
              this.setContainerWidths();
              resolve();
            },   _error => {
              console.log(_error);
              reject(_error);
            });
          } else {
            if (error.status === 401) {
              let path = '/ise/' + this.ise_id + '/set-password/';
              this.router.navigate([path]);
            }
          }
        }
      }));
    });
  }

  getPoolsList(ise_id: number) {
    interface IPoolStateData {
      /* INCOMPLETE INTERFACE */
      available: {
        byredundancy: {
          'raid-0': number;
          'raid-1': number;
          'raid-5': number;
        }
      };
      ThinThreshold: number;
      name: string;
      size: number;
      DedupUsed: {
        SystemData?: number;
        UserData?: number;
      };
      used: {
        byredundancy?: {
          'raid-1': number;
          'raid-5': number;
        };
        _attr: {
          total: string; // total GB used as a string
        }
      };
    }
    return new Promise((resolve, reject) => {
      if (this.all_pools_state_obs$) {
        this.all_pools_state_obs$.unsubscribe();
      }
      this.store.dispatch(new GetAllPoolsAction(this.ise_id));
      this.all_pools_state_obs$ = this.store.select(getAllPoolsState).subscribe((poolsListData: Array<Pools>) => {
        if (poolsListData && poolsListData.length) {
          this.totalPoolData = poolsListData.reduce((result, current) => {
            if (current.available) {
              let redundancyTypes = current.available.byredundancy;
              result.free.raw += redundancyTypes['raid-0'] || 0;
              result.free.raid1 += redundancyTypes['raid-1'] || 0;
              result.free.raid5 += redundancyTypes['raid-5'] || 0;
            }
            if (current.used) {
              result.used += Number(current.used['_attr'].total) || 0;
            }
            result.size += current.size || 0;

            return result;
          }, { size: 0, used: 0, free: { raw: 0, raid1: 0, raid5: 0 } });

          let physical = this.containers.find(container => container.storageType === 'Physical');
          if (physical) {
              physical.storageSize = this.totalPoolData.size / 1024;
              let allocated = physical.bars.find(bar => bar.data.label === 'Allocated');
              if (allocated) {
                allocated.data.value = this.totalPoolData.used / 1024;
             }
             this.setContainerWidths();
          }
          resolve(poolsListData || []);
        }
      }, error => {
          reject(error);
      });
    });
  }

  /**
   * this method identifying
   * the ise_id from the given data
   */
  getRTData() {
    this.ws = new $WebSocket(AppSettings.WS_ENDPOINT);
    this.ws.onMessage(
      (msg: MessageEvent) => {
        let data = JSON.parse(msg.data);
        for (let d of data) {
          if (d.ise_id === this.ise_id) {
            this.setRTData(d.data);
            break;
          }
        }
      }, { autoApply: false });
  }

  setRTData(data: any) {
    this.iops_new_data = data;
    this.latency_new_data = data;
    this.datarate_new_data = data;
  }

  refreshDashBoard() {       
    this.iopscomponent.getData();
    this.latencycomponent.getData();
    this.datarateComponent.getData();      
  }
}

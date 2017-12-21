import {AfterViewInit, Component, ElementRef, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {IseService} from '../../services/ise.service';
import {StoragevolumeService} from '../../services/storagevolume.service';
import {
  GetDataRateChartData,
  GetIOPSChartData,
  GetLatencyChartData,
  GetQDepthChartData, SetISEId
} from '../../../actions/ise-management.actions';
import {
  getAllVolumesState,
  getDataRateData,
  getIOPsData, getISEId,
  getLatencyData,
  getqDepthData,
  State
} from '../../../reducers/index';
import {Store} from '@ngrx/store';
import {GetAllVolumesAction} from '../../../actions/volume.actions';
import { SharedDataService } from '../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';

declare let d3, nv: any;

@Component({
  selector: 'app-performance-volume',
  templateUrl: './ise-performance-volume.component.html',
  styleUrls: ['./ise-performance-volume.component.scss']
})
export class PerformanceVolumeComponent implements OnInit, AfterViewInit, OnDestroy {

  public line_chart_options;
  public iops_data: any;
  public data_rate_options;
  public data_rate_data: any;
  public queue_depth_options;
  public queue_depth_data: any;
  public latency_options;
  public latency_data: any;
  public ise_id: any;
  public volume_list: any;
  public id;
  public name;
  public v;
  public isChart: boolean;
  public loading_stack: any;
  public getIOPsData$;
  public getDataRateData$;
  public getLatencyData$;
  public getqDepthData$;
  public volume_list$;
  public currentSelectedVolume;

  @ViewChild('mdvolume') mdvolumneSelect: ElementRef;

  constructor(public ises: IseService,
              public sv: StoragevolumeService,
              public route: ActivatedRoute,
              public router: Router,
              public store: Store<State>,
              public _sharedDataService: SharedDataService) {  


    this.line_chart_options = {
      chart: {
        type: 'lineChart',
        height: 250,
        margin: {
          top: 20,
          right: 20,
          bottom: 40,
          left: 60
        },
        lines: {
          forceY: [0, 100]
        },
        x: function(d) {
          return new Date(d['x']);
        },
        y: function(d) {
          return d.y;
        },

        useInteractiveGuideline: true,
        xAxis: {
          axisLabel: 'Time (hh:mm)',
          tickFormat: function(d) {
            return d3.time.format.utc('%H:%M')(new Date(d));
          }
        },
        yAxis: {
          axisLabel: 'Number of IO/s',
        },
      }
    };
    
    this.data_rate_options = {
      chart: {
        type: 'lineChart',
        height: 250,
        margin: {
          top: 20,
          right: 20,
          bottom: 40,
          left: 60
        },
        lines: {
          forceY: [0, 100]
        },
        x: function(d) {
          return new Date(d['x']);
        },
        y: function(d) {
          return d.y;
        },

        useInteractiveGuideline: true,
        xAxis: {
          axisLabel: 'Time (hh:mm)',
          tickFormat: function(d) {
            return d3.time.format.utc('%H:%M')(new Date(d));
          }
        },
        yAxis: {
          axisLabel: '(KB/s)',
        },
      }
    };

    this.queue_depth_options = {
      chart: {
        type: 'lineChart',
        height: 250,
        margin: {
          top: 20,
          right: 20,
          bottom: 40,
          left: 60
        },
        lines: {
          forceY: [0, 100]
        },
        x: function(d) {
          return new Date(d['x']);
        },
        y: function(d) {
          return d.y;
        },
        useInteractiveGuideline: true,
        xAxis: {
          axisLabel: 'Time (hh:mm)',
          tickFormat: function(d) {
            return d3.time.format.utc('%H:%M')(new Date(d));
        },
      },
        yAxis: {
          axisLabel: 'Number of Queues',
        },
      }
    };    

    this.latency_options = {
      chart: {
        type: 'lineChart',
        height: 250,
        margin: {
          top: 20,
          right: 20,
          bottom: 40,
          left: 60
        },
        lines: {
          forceY: [0, 100]
        },
        x: function(d) {
          return new Date(d['x']);
        },
        y: function(d) {
          return d.y;
        },

        useInteractiveGuideline: true,
        xAxis: {
          axisLabel: 'Time (hh:mm)',
          tickFormat: function(d) {
            return d3.time.format.utc('%H:%M')(new Date(d));
          }
        },
        yAxis: {
          axisLabel: 'Response Time(ms)',
        },
      }
    };
    
    this.volume_list = [];
    this.loading_stack = {
      performance_vol_details: false,
      performance_vol_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.initIOPs();
    this.initDataRate();
    this.initLatency();
    this.initqDepth();

    this.loading_stack.performance_vol_details = true;
    this.isChart = true;
    this.line_chart_options.chart.lines = {
      forceY: [0, 100],
    };
    this.route.parent.params.subscribe(params => {      
      this.ise_id = params['ise_id'];
      if(!this.ise_id){
        this._sharedDataService.getData().subscribe((data)=>{
            this.ise_id = data;      
        });
      } 
      this.store.dispatch(new SetISEId(this.ise_id));
      this.setvolumeDropdown();
    });    
  }

  ngAfterViewInit() {
    if (this.volume_list.length > 0) {
      this.loadIseVolume();
    }
  }

  loadIseVolume() {
    if (!this.currentSelectedVolume) {
      this.getData(this.currentSelectedVolume);
    }    
  }

  initIOPs() {
    this.getIOPsData$ = this.store.select(getIOPsData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.loading_stack.performance_vol_details = false;
          this.iops_data = data;
        } else if (data != null) {
          this.loading_stack.performance_vol_details = false;
        }
      }
    );
  }

  initDataRate() {
    this.getDataRateData$ = this.store.select(getDataRateData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.loading_stack.performance_vol_details = false;
          this.data_rate_data = data;
        } else if (data != null) {
          this.loading_stack.performance_vol_details = false;
        }
      }
    );
  }

  initLatency() {
    this.getLatencyData$ = this.store.select(getLatencyData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.loading_stack.performance_vol_details = false;
          this.latency_data = data;
        } else if (data != null) {
          this.loading_stack.performance_vol_details = false;
        }
      }
    );
  }

  initqDepth() {
    this.getqDepthData$ = this.store.select(getqDepthData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.loading_stack.performance_vol_details = false;
          this.queue_depth_data = data;
        } else if (data != null) {
          this.loading_stack.performance_vol_details = false;
        }
      }
    );
  }


  /**
   * Get's ISE Performance Volume Chart data
   * @namespace xio.PerformanceVolumeComponent
   * @method getData
   * @return {void}
   */
  getData(volumeId) {

    let IOPSPayLoad = {
      url : 'ise/' + this.ise_id + '/volumes-iops-chart/' + volumeId ,
        cb: (success, error) => {
         if (!error) {

         } else {
           if (error.status === 401) {
              let path = '/ise/' + this.ise_id + '/set-password/';
              this.router.navigate([path]);
            }
         }
      }
    };
     this.store.dispatch(new GetIOPSChartData(IOPSPayLoad));

     let DataRatePayLoad = {
       url: 'ise/' + this.ise_id + '/volumes-datarate-chart/' + volumeId
     };
     this.store.dispatch(new GetDataRateChartData(DataRatePayLoad));

     let QDepthPayLoad = {
       url: 'ise/' + this.ise_id + '/volumes-queuedepth-chart/' + volumeId
     };
     this.store.dispatch(new GetQDepthChartData(QDepthPayLoad));

     let LatencyPayLoad = {
       url: 'ise/' + this.ise_id + '/volumes-latency-chart/' + volumeId
     };
     this.store.dispatch(new GetLatencyChartData(LatencyPayLoad));
  }

  /**
   * set Volume Drop component data list
   * @namespace xio.PerformanceVolumeComponent
   * @method sethostDropdown
   * @return {void}
   */
  setvolumeDropdown() {
    this.store.dispatch(new GetAllVolumesAction({
      ise_id : this.ise_id
    }));
    this.volume_list$ = this.store.select(getAllVolumesState).subscribe((data: any) => {
      this.loading_stack.performance_vol_details = false;
      this.volume_list = data;
      for (let v of data) {
        this.volume_list[v.globalid] = v.name;
      }
    }, error => {
      console.log(error);
    });

    /*this.sv.getAll(this.ise_id).subscribe(
     data => {
     this.loading_stack.performance_vol_details = false;
     this.volume_list = data;
     for (let v of data) {
     console.log(v.globalid);
     this.volume_list[v.globalid] = v.name;
     }
     });*/
  }

  /**
   * on host change on volumeDropdown refresh data set
   * @namespace xio.PerformanceVolumeComponent
   * @method onVolumeChange
   * @return {void}
   */
  onVolumeChange(volume) {
    this.isChart = false;
    this.currentSelectedVolume = volume.value;
    this._sharedDataService._volume_info.next(volume);
    this.getData(volume.value);
  }

  ngOnDestroy() {
    if (this.getIOPsData$) {
      this.getIOPsData$.unsubscribe();
    }
    if (this.getDataRateData$) {
      this.getDataRateData$.unsubscribe();
    }
    if (this.getLatencyData$) {
      this.getLatencyData$.unsubscribe();
    }
    if (this.getqDepthData$) {
      this.getqDepthData$.unsubscribe();
    }
    if (this.volume_list$) {
      this.volume_list$.unsubscribe();
    }
  }
}

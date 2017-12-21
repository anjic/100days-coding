import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {IseService} from '../../services/ise.service';
import {HostService} from '../../services/host.service';
import {FormBuilder, FormGroup} from '@angular/forms';
import {
  GetDataRateChartData,
  GetIOPSChartData,
  GetLatencyChartData,
  GetQDepthChartData, SetISEId
} from '../../../actions/ise-management.actions';
import {getDataRateData, getIOPsData, getISEId, getLatencyData, getqDepthData, State} from '../../../reducers/index';
import {Store} from '@ngrx/store';
import { SharedDataService } from '../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';
declare let d3, nv: any;

@Component({
  selector: 'app-performance-host',
  templateUrl: './ise-performance-host.component.html',
  styleUrls: ['./ise-performance-host.component.scss']
})
export class PerformanceHostComponent implements OnInit, OnDestroy {

  public line_chart_options;
  public iops_data: any;
  public data_rate_options;
  public data_rate_data: any;
  public queue_depth_options;
  public queue_depth_data: any;
  public latency_options;
  public latency_data: any;
  public ise_id: any;
  public host_list: any;
  public id;
  public h;
  public params: any;
  public hostForm: FormGroup;
  public isChart: boolean;
  public loading_stack: any;
  public getIOPsData$;
  public getDataRateData$;
  public getLatencyData$;
  public getqDepthData$;
  public currentSelectedHost;

  constructor(public ises: IseService,
              public route: ActivatedRoute,
              public router: Router,
              public hs: HostService,
              public fb: FormBuilder,
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
          }
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
    this.loading_stack = {
      performance_host_details: false,
      performance_host_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.getqDepthData$ = this.store.select(getqDepthData);
    this.getDataRateData$ = this.store.select(getDataRateData);
    this.getLatencyData$ = this.store.select(getLatencyData);
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
      this.initIOPs();
      this.initDataRate();
      this.initLatency();
      this.initqDepth();
      this.sethostDropdown();
    });
    this.hostForm = this.fb.group({
      host: ['']
    });
  }

  initIOPs() {
    this.getIOPsData$ = this.store.select(getIOPsData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.loading_stack.performance_vol_details = false;
          this.iops_data = data;
        } else if ( data != null) {
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
          this.queue_depth_data = data;
          this.loading_stack.performance_vol_details = false;
        } else if (data != null) {
          this.loading_stack.performance_vol_details = false;
        }
      }
    );
  }

  /**
   * Get's ISE Performance Host Chart data
   * @namespace xio.PerformanceHostComponent
   * @method getData
   * @return {void}
   */
  getData(hostId) {    

    let IOPSpayload = {
      url : 'ise/' + this.ise_id + '/hosts-iops-chart/' +hostId ,
       cb: (success, error ) => {
         if (!error) {

         } else {
           if (error.status === 401) {
              let path = '/ise/' + this.ise_id + '/set-password/';
              this.router.navigate([path]);
            }
         }
      }
    };
    this.store.dispatch(new GetIOPSChartData(IOPSpayload));

    let DataRatepayload = {
      url : 'ise/' + this.ise_id + '/hosts-datarate-chart/' + hostId
    };
    this.store.dispatch(new GetDataRateChartData(DataRatepayload));

    let QDepthpayload = {
       url: 'ise/' + this.ise_id + '/hosts-queuedepth-chart/' + hostId
    };
    this.store.dispatch(new GetQDepthChartData(QDepthpayload));

    let Latencypayload = {
      url : 'ise/' + this.ise_id + '/hosts-latency-chart/' + hostId
    };
    this.store.dispatch(new GetLatencyChartData(Latencypayload));

  }

  /**
   * set Host Drop component data list
   * @namespace xio.PerformanceHostComponent
   * @method sethostDropdown
   * @return {void}
   */
  sethostDropdown() {
    let payLoad = {
      'ise_id' :  this.ise_id
    };
    this.hs.getAll(payLoad).subscribe(
      data => {
        this.loading_stack.performance_host_details = false;
        this.host_list = data;
        for (let h of data) {
          this.host_list[h.name] = h.id;
        }
      });
  }

  /**
   * on host change on hostDropdown refresh data set
   * @namespace xio.PerformanceHostComponent
   * @method onHostChange
   * @return {void}
   */
  onHostChange(host) {
    this.isChart = false;
    this.currentSelectedHost = host.value;
    this._sharedDataService._host_info.next(host);
    this.getData(host.value);
  }

  loadHost() {
    if (!this.currentSelectedHost) {
        this.getData(this.currentSelectedHost);
    }    
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
  }
}

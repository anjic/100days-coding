import {Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {Store} from '@ngrx/store';
import {getISEId, getLatencyData, State} from '../../../../reducers/index';
import {GetLatencyChartData, SetISEId} from '../../../../actions/ise-management.actions';
import { SharedDataService } from '../../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';
declare let d3, nv: any;

@Component({
  selector: 'app-latency',
  templateUrl: './latency.component.html',
  styleUrls: ['./latency.component.scss']
})
export class LatencyComponent implements OnInit, OnDestroy, OnChanges {
  public latency_options;
  public array_data: any;
  public ise_id: any;
  public loading_stack: any;
  public getLatencyData$;
  @Input() new_latency_data: any;
  @Output() latencyCallCountEmmiter = new EventEmitter();


  constructor(public route: ActivatedRoute,
              public router: Router,
              public store: Store<State>,
              public _sharedDataService: SharedDataService) {
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
       lines : {
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
           axisLabel: 'Response Time (ms)',
        },
     }
   };
    this.loading_stack = {
      latency_details: false,
      latency_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.initLatency();
    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.loading_stack.latency_details = true;
      this.getData();
    });
    
 
  }

  initLatency() {
    this.getLatencyData$ = this.store.select(getLatencyData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.array_data = data;
          this.latencyCallCountEmmiter.emit();
          this.loading_stack.latency_details = false;
        } else if (data != null) {
          this.loading_stack.latency_details = false;
        }
      }, error => {
        this.latencyCallCountEmmiter.emit();
      }
    );
  }
  

  /**
   * Get's ISE Latency Chart data
   * @namespace xio.LatencyComponent
   * @method getData
   * @return {void}
   */
  getData() {
    if(!this.ise_id){
      this._sharedDataService.getData().subscribe((data)=>{
          this.ise_id = data;      
      });  
    }
    let payLoad = {
      url : 'ise/' + this.ise_id + '/array-latency-chart/',
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
    this.store.dispatch(new GetLatencyChartData(payLoad));
  }

  ngOnDestroy() {
    this.getLatencyData$.unsubscribe();
  }


  ngOnChanges(...args: any[]) {
    if (this.new_latency_data) {
      // 24 hour logic
      let d1 = new Date(this.array_data[0]['values'][1]['x']).getTime();
      let d2 = new Date(this.new_latency_data[0]['values'][0]['x']).getTime();
      let diff = Math.abs(d2 - d1) / 36e5;

      if (diff > 24) {
        this.array_data[0]['values'].shift();
        this.array_data[1]['values'].shift();
      }

      this.array_data[0]['values'].push(this.new_latency_data[3]['values'][0]);
      this.array_data[1]['values'].push(this.new_latency_data[4]['values'][0]);

      let event = document.createEvent('UIEvents');
      event.initUIEvent('resize', true, false, window, 0);
      window.dispatchEvent(event);
    }
  }

}

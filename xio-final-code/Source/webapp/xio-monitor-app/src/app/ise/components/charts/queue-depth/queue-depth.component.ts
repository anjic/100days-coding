import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {IseService} from './../../../services/ise.service';
import {GetQDepthChartData, SetISEId} from '../../../../actions/ise-management.actions';
import {Store} from '@ngrx/store';
import {getISEId, getqDepthData, State} from '../../../../reducers/index';
import { SharedDataService } from '../../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';

declare let d3, nv: any;

@Component({
  selector: 'app-queue-depth',
  templateUrl: './queue-depth.component.html',
  styleUrls: ['./queue-depth.component.scss']
})
export class QueueDepthComponent implements OnInit, OnDestroy {
  public queue_depth_options;
  public array_data: any;
  public ise_id: any;
  public loading_stack: any;
  public getqDepthData$;

  constructor(public ises: IseService,
              public route: ActivatedRoute,
              public router: Router,
              public store: Store<State>,
              public _sharedDataService: SharedDataService) {
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

    this.loading_stack = {
      queuedepth_details: false,
      queuedepth_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.initqDepth();
      this.getData();
      this.store.dispatch(new SetISEId(this.ise_id));
      this.loading_stack.queuedepth_details = true;
    });
  }

  initqDepth() {
    this.getqDepthData$ = this.store.select(getqDepthData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.array_data = data;
          this.loading_stack.queuedepth_details = false;
        } else if (data != null) {
          this.loading_stack.queuedepth_details = false;
        }
      }
    );
  }

  /**
   * Get's ISE queue depth data Chart data
   * @namespace xio.QueueDepthComponent
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
      url : 'ise/' + this.ise_id + '/array-queuedepth-chart/',
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
    this.store.dispatch(new GetQDepthChartData(payLoad));
   }

  ngOnDestroy() {
    this.getqDepthData$.unsubscribe();
  }
}

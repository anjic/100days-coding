import {Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {IseService} from './../../../services/ise.service';
import {GetDataRateChartData, SetISEId} from '../../../../actions/ise-management.actions';
import {getDataRateData, getISEId, State} from '../../../../reducers';
import {Store} from '@ngrx/store';
import { SharedDataService } from '../../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';
declare let d3, nv: any;

@Component({
  selector: 'app-data-rate',
  templateUrl: './data-rate.component.html',
  styleUrls: ['./data-rate.component.scss']
})
export class DataRateComponent implements OnInit, OnDestroy, OnChanges {
  public data_rate_options;
  public array_data: any;
  public ise_id: any;
  public loading_stack: any;
  public getDataRateData$;
  @Input() datarate_data: any;
  @Output() dataRateCallCountEmmiter = new EventEmitter();

  constructor(public ises: IseService,
              public route: ActivatedRoute,
              public router: Router,
              public store: Store<State>,
              public _sharedDataService: SharedDataService) {
    this.data_rate_options = {
      chart: {
        type: 'lineChart',
        height: 250,
        margin: {
          top: 20,
          right: 20,
          bottom: 40,
          left: 80
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
          axisLabelDistance: 8
        },

      }
    };
    this.loading_stack = {
      datarate_details: false,
      datarate_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.initDataRate();
    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.loading_stack.datarate_details = true;
      this.getData();
    }, error => {

    });
  }

  initDataRate() {
    this.getDataRateData$ = this.store.select(getDataRateData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.array_data = data;
          this.dataRateCallCountEmmiter.emit();
          this.loading_stack.datarate_details = false;
        }else if (data != null) {
          this.loading_stack.datarate_details = false;
        }
      }, error => {
        this.dataRateCallCountEmmiter.emit();
      }
    );
  }

  /**
   * Get's ISE Data rate Chart data
   * @namespace xio.DataRateComponent
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
      url : 'ise/' + this.ise_id + '/array-datarate-chart/',
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
    this.store.dispatch(new GetDataRateChartData(payLoad));
  }

  ngOnDestroy() {
    this.getDataRateData$.unsubscribe();
  }

  ngOnChanges(...args: any[]) {

    if (this.datarate_data) {

      // 24 hour logic
      let d1 = new Date(this.array_data[0]['values'][1]['x']).getTime();
      let d2 = new Date(this.datarate_data[0]['values'][0]['x']).getTime();
      let diff = Math.abs(d2 - d1) / 36e5;

      if (diff > 24) {
        this.array_data[0]['values'].shift();
        this.array_data[1]['values'].shift();
        this.array_data[2]['values'].shift();
      }

      this.array_data[0]['values'].push(this.datarate_data[7]['values'][0]);
      this.array_data[1]['values'].push(this.datarate_data[8]['values'][0]);
      this.array_data[2]['values'].push(this.datarate_data[9]['values'][0]);

      let event = document.createEvent('UIEvents');
      event.initUIEvent('resize', true, false, window, 0);
      window.dispatchEvent(event);
    }
  }
}

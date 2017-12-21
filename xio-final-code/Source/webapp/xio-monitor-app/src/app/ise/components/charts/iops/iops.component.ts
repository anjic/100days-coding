import {Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output, ViewChild} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {nvD3} from '../../../../common/utils/ng2-nvd3';
import {IseService} from './../../../services/ise.service';
import {getIOPsData, getISEId, State} from '../../../../reducers/index';
import {Store} from '@ngrx/store';
import {GetIOPSChartData, SetISEId} from '../../../../actions/ise-management.actions';
import { SharedDataService } from '../../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';
declare let d3, nv: any;

@Component({
  selector: 'app-iops',
  templateUrl: './iops.component.html',
  styleUrls: ['./iops.component.scss']
})
export class IopsComponent implements OnInit , OnDestroy, OnChanges  {
  public line_chart_options;
  public ise_id: any;
  public array_data: any;
  public loading_stack: any;
  public getIOPsData$;
  @Input() iop_data: any;
  @Output() iopCallCountEmmiter = new EventEmitter();
  public temp_array_data1: any;
  public flag = false;
  @ViewChild('iopNvd3') iopNvd3: nvD3;

  constructor(public ises: IseService,
              public activatedRoute: ActivatedRoute,
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
        }

      }
    };
    this.loading_stack = {
      iops_details: false,
      iops_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    let temp = '' ;
    this.initIOPs();    
    this.activatedRoute.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.loading_stack.iops_details = true;
      this.getData();
    });   
    this._sharedDataService.notify().subscribe((data)=>{
          this.getData();     
    });
  }

  initIOPs() {
    this.getIOPsData$ = this.store.select(getIOPsData).subscribe(
      data => {
        if (data && data.length > 0) {
          this.temp_array_data1 = data;
          this.array_data = data;
          this.iopCallCountEmmiter.emit();
          this.loading_stack.iops_details = false;
        } else if (data != null) {
          this.loading_stack.iops_details = false;
        }
      }, error => {
        this.iopCallCountEmmiter.emit();
      }
    );
  }

  /**
   * Get's ISE IOP's Chart data
   * @namespace xio.IopsComponent
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
      url : 'ise/' + this.ise_id + '/array-iops-chart/',
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
    this.store.dispatch(new GetIOPSChartData(payLoad));
  }

  ngOnDestroy() {
    this.getIOPsData$.unsubscribe();
  }


  ngOnChanges(...args: any[]) {
    if (this.iop_data) {
      // 24 hour logic
      let d1 = new Date(this.array_data[0]['values'][1]['x']).getTime();
      let d2 = new Date(this.iop_data[0]['values'][0]['x']).getTime();
      let diff = Math.abs(d2 - d1) / 36e5;

      if (diff > 24) {
        this.array_data[0]['values'].shift();
        this.array_data[1]['values'].shift();
        this.array_data[2]['values'].shift();
      }

      this.array_data[0]['values'].push(this.iop_data[0]['values'][0]);
      this.array_data[1]['values'].push(this.iop_data[1]['values'][0]);
      this.array_data[2]['values'].push(this.iop_data[2]['values'][0]);

      let event = document.createEvent('UIEvents');
      event.initUIEvent('resize', true, false, window, 0);
      window.dispatchEvent(event);
    }
  }
}

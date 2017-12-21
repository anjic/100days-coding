import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { Store } from '@ngrx/store';
import { State } from '../../../reducers/index';
import { GetIOPSChartData, SetISEId, GetDataRateChartData, GetLatencyChartData, GetQDepthChartData } from '../../../actions/ise-management.actions';
import { SharedDataService } from '../../../ise/components/hardwareinfo/hardware-tabs/shared-data.service';
import { OnDestroy } from '@angular/core/src/metadata/lifecycle_hooks';
import { CommonUtil } from '../../../common/utils/CommonUtil';

@Component({
  selector: 'app-ise-performance-chart',
  templateUrl: './ise-performance-chart.component.html',
  styleUrls: ['./ise-performance-chart.component.scss']
})
export class IsePerformanceChartComponent extends CommonUtil implements OnInit {

  public tabs: any = [
    'ise',
    'volume',
    'wwngroup'
  ];
  public ise_id: any;
  public screen_name: string;
  public selected_index: number;

  constructor(public activatedRoute: ActivatedRoute,
    public router: Router,
    public store: Store<State>,
    public _sharedDataService: SharedDataService) {
    super();
    this.ise_id = '';
    this.screen_name = 'performance';
    this.selected_index = 0;
    this.activatedRoute.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this._sharedDataService._data.next(this.ise_id);
    });
  }

  ngOnInit() {
    this.selected_index = this.tabs.indexOf(this.router.url.split('/')[4]);
  }

  changeTab(event) {
    if (this.tabs[event.index]) {
      let url = '/ise/' + this.ise_id + '/performance/' + this.tabs[event.index];
      this.selected_index = event.index;
      this.router.navigateByUrl(url);
    }
  }

  refreshIsePerformance(event) {
    let currObj = this;
    switch (this.selected_index) {
      case 0:
        let iopsPayload = {
          url: 'ise/' + this.ise_id + '/array-iops-chart/'
        };
        this.store.dispatch(new GetIOPSChartData(iopsPayload));

        let dataratePayload = {
          url: 'ise/' + this.ise_id + '/array-datarate-chart/'
        };
        this.store.dispatch(new GetDataRateChartData(dataratePayload));

        let latencyPayload = {
          url: 'ise/' + this.ise_id + '/array-latency-chart/'
        };
        this.store.dispatch(new GetLatencyChartData(latencyPayload));

        let queueDepthPayload = {
          url: 'ise/' + this.ise_id + '/array-queuedepth-chart/'
        };
        this.store.dispatch(new GetQDepthChartData(queueDepthPayload));
        break;
      case 1:
        // Subscribe to volume info and trigger api calls
        this._sharedDataService.getVolumeInfo().subscribe(function (volumeObj) {
          if (!currObj.isEmpty(volumeObj)) {
            let volumePayLoad = {
              url: 'ise/' + currObj.ise_id + '/volumes-iops-chart/' + volumeObj.value
            };
            currObj.store.dispatch(new GetIOPSChartData(volumePayLoad));

            let DataRatePayLoad = {
              url: 'ise/' + currObj.ise_id + '/volumes-datarate-chart/' + volumeObj.value
            };
            currObj.store.dispatch(new GetDataRateChartData(DataRatePayLoad));

            let QDepthPayLoad = {
              url: 'ise/' + currObj.ise_id + '/volumes-queuedepth-chart/' + volumeObj.value
            };
            currObj.store.dispatch(new GetQDepthChartData(QDepthPayLoad));

            let LatencyPayLoad = {
              url: 'ise/' + currObj.ise_id + '/volumes-latency-chart/' + volumeObj.value
            };
            currObj.store.dispatch(new GetLatencyChartData(LatencyPayLoad));
          }
        });
        break;
      case 2:
        // Subscribe to host info and trigger api calls
        this._sharedDataService.getHostInfo().subscribe(function (hostObj) {
          if (!currObj.isEmpty(hostObj)) {
            let hostPayLoad = {
              url: 'ise/' + currObj.ise_id + '/hosts-iops-chart/' + hostObj.value
            };
            currObj.store.dispatch(new GetIOPSChartData(hostPayLoad));

            let DataRatePayLoad = {
              url: 'ise/' + currObj.ise_id + '/hosts-datarate-chart/' + hostObj.value
            };
            currObj.store.dispatch(new GetDataRateChartData(DataRatePayLoad));

            let QDepthPayLoad = {
              url: 'ise/' + currObj.ise_id + '/hosts-queuedepth-chart/' + hostObj.value
            };
            currObj.store.dispatch(new GetQDepthChartData(QDepthPayLoad));

            let LatencyPayLoad = {
              url: 'ise/' + currObj.ise_id + '/hosts-latency-chart/' + hostObj.value
            };
            currObj.store.dispatch(new GetLatencyChartData(LatencyPayLoad));
          }
        });
        break;
    }
  }
}

import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {HostService, IseService} from './../../../services/';
import {getISECardInfo, State} from "../../../../reducers/index";
import {Store} from '@ngrx/store';
import {GetISECardInfo} from "../../../../actions/ise-management.actions";
import {Observable} from 'rxjs/Observable';
 import {listConfig} from './host-landing-options';
import {GridOptions} from "../../../../common/Metadata/xio.dataTable";

@Component({
  selector: 'app-host-landing-page',
  templateUrl: './host-landing-page.component.html',
  styleUrls: ['./host-landing-page.component.scss']
})
export class HostLandingPageComponent implements OnInit, OnDestroy {
  public gridOptions;
  public columnDefs: any;
  public id;
  public host_id;
  public ise_id;
  public host_name: string;
  public endpoints: any;
  public ise_card_details;
  public iseCardInfo$;

  constructor(public route: ActivatedRoute,
              public hs: HostService,
              public store: Store<State>) {
  }

  ngOnInit() {
    // this.initGrid();
    this.gridOptions = listConfig;
    this.route.params.subscribe(params => {
      this.id = params['sg_id'];
      this.host_id = params['host_id'];
      this.ise_id = params['ise_id'];
      this.initCardInfo();
      this.getVolumeList(this.host_id, this.ise_id);
      this.store.dispatch(new GetISECardInfo(this.ise_id));
    });
  }

  initCardInfo() {
    this.iseCardInfo$ = this.store.select(getISECardInfo).subscribe(
      data => {
        this.ise_card_details = data;
      }
    );
  }

  /**
   * util method to getMenuContent volume list as row data
   * @namespace xio.HostLandingPageComponent
   * @param {number} host_id - Host Id
   * @param {number} ise_id - Ise Id
   * @method subcribeVolumeList
   * @return {void}
   */
  getVolumeList(host_id: number, ise_id: number) {
    let d = this.hs.getHostVolume(host_id, ise_id).subscribe(
      res => {
        if (!this.isEmptyObject(res)) {
          // this.gridOptions.api.setRowData(res['volumes']);

          for(var i = 0; i< res['volumes'].length; i++){

            res['volumes'][i]['globalid'] = res['volumes'][i]['globalid'].slice(0, 31);

           }
          this.gridOptions.rowData = res['volumes'];
          this.endpoints = res['endpoints'];
          this.host_name = res['host_name'];
        }
      },
      err => {
        console.error(err);
      }
    );
  }

  isEmptyObject(obj) {
    return Object.keys(obj).length === 0;
  }



  ngOnDestroy() {
    this.iseCardInfo$.unsubscribe();
  }
}


import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SubscriptionService, IseService } from './../../../services/';
import { SubscriptionDeleteComponent } from './../../../components/ise-settings/subscription-list/subscription-delete/subscription-delete.component';
import { SubscriptionEditComponent } from './../../../components/ise-settings/subscription-list/subscription-edit/subscription-edit.component';
import { Store } from '@ngrx/store';
import { getISESubcription, State } from './../../../../reducers/';
import { GetAllSubscription } from '../../../../actions/ise-settings.actions';
import { SetISEId } from "../../../../actions/ise-management.actions";
import { listConfig } from './subscription-list-options';
import { GridOptions } from "../../../../common/Metadata/xio.dataTable";
import { XioDialogComponent } from "../../../../theme/xio-dialog/xio-dialog.component";
import { MdDialog } from "@angular/material";
import { XioProgressComponent } from "../../../../theme/xio-progress/xio-progress.component";
import { XioAlertComponent } from "../../../../theme/xio-alert/xio-alert.component";
import { SnackbarService } from "../../../../theme/services/snackbar.service";
import { DeleteSubscription } from '../../../../actions/ise-settings.actions';
import * as _ from 'lodash';


@Component({
  selector: 'app-subscription-list',
  templateUrl: './subscription-list.component.html',
  styleUrls: ['./subscription-list.component.scss']
})
export class SubscriptionListComponent implements OnInit, OnDestroy {

  public ise_id: number;

  public sub_gridOptions;
  public iseSubcriptionLst$;
  public is_sub_list: Boolean = true;
  public is_sub_list_loaded: Boolean = false;
  public loading_stack: any;
  public gridData = [];
  public columnDefs: any;

  constructor(public sub: SubscriptionService,
    public ises: IseService,
    public route: ActivatedRoute,
    public dialog: MdDialog,
    public snackbarService: SnackbarService,
    public store: Store<State>) {
    this.loading_stack = {
      subscription_details: false,
      subscription_details_text: 'Loading.....'
    }
  }

  ngOnInit() {
    this.sub_gridOptions = listConfig;
    this.sub_gridOptions['deleteCb'] = this.bindSubDeleteCb.bind(this);
    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetAllSubscription({
        ise_id: this.ise_id
      }));
    });
    let types_data = [];
    this.iseSubcriptionLst$ = this.store.select(getISESubcription).subscribe(
      data => {
        console.log(data);
        for (let i = 0; i < data.length; i++) {
          data[i]['ise_id'] = this.ise_id;
          data[i]['setting'] = data[i]['string'];
          data[i]['type'] = data[i]['type'];
          data[i]['ssl'] = data[i]['ssl'];
          data[i]['proxy'] = data[i]['proxy'];
          data[i]['proxy_address'] = data[i]['proxyaddress'];
          data[i]['proxy_username'] = data[i]['proxyusername'];
          data[i]['proxy_password'] = data[i]['proxypassword'];
          if (data[i]['types'] && data[i]['types']['type']) {
            if (!Array.isArray(data[i]['types'])) {
              data[i]['setting'] = data[i]['types']['type']['setting']['_attr']['string'];
              data[i]['type'] = data[i]['types']['type']['_attr']['name'];
              data[i]['ssl'] = data[i]['types']['type']['ssl']['_attr']['string'];
              data[i]['proxy'] = data[i]['types']['type']['proxy']['_attr']['string'];
              data[i]['proxy_address'] = data[i]['types']['type']['proxyaddress'];
              data[i]['proxy_username'] = data[i]['types']['type']['proxyusername'];
              data[i]['proxy_password'] = data[i]['types']['type']['proxypassword'];
            }
          }
        }

        types_data = [];
        for (let n = 0; n < data.length; n++) {
          let id = data[n]['id'];
          if (Array.isArray(data[n]['types'])) {
            for (let k = 0; k < data[n]['types'].length; k++) {
              let dataObj = data[n]['types'][k];
              types_data.push({
                'ise_id': this.ise_id,
                'id': id,
                'setting': dataObj['setting']['_attr']['string'],
                'type': dataObj['_attr']['name'],
                'ssl': dataObj['ssl']['_attr']['string'],
                'proxy': dataObj['proxy']['_attr']['string'],
                'proxy_address': dataObj['proxyaddress'],
                'proxy_username': dataObj['proxyusername'],
                'proxy_password': dataObj['proxypassword']
              });
            }
          }
        }

        let concated_data = [];
        /*if(types_data.length > 0){
           concated_data = data.concat(types_data);
        }*/
        if(data && data.length >0){
        concated_data = data.concat(types_data);
       }

        let gData = [];
        for (let s = 0; s < concated_data.length; s++) {
          if (!Array.isArray(concated_data[s]['types'])) {
            gData.push(concated_data[s]);
          }
        }

        this.sub_gridOptions.rowData = gData;
        this.is_sub_list_loaded = true;
        this.loading_stack.subscription_details = true;
      }

    );
    this.getSubscriptionList();
  }

  bindSubDeleteCb(data) {
    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Delete Subscription';
    dialogRef.componentInstance.message = 'Do you want to Delete Subscription ?';
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
      if (result == 'yes') {
        let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        let progress_data = 'processing'
        progressRef.componentInstance.progress_data = progress_data;
        this.sub.deleteSubscription(this.ise_id, data.id, data.type).subscribe(res => {
          progressRef.close();
          this.getSubscriptionList();
          // this.params.api.removeItems([this.params.node]);
          this.snackbarService.toastMe('Subscription deleted Successfully', 2000);
        },
          err => {
            progressRef.close();
            let err_msg = err.json();
            let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
            alertRef.componentInstance.title = 'Subscription';
            alertRef.componentInstance.message = err_msg.result.error.message;
          })

      }
    });
  }


  /**
   * toggle sub's list
   * @namespace xio.SubscriptionListComponent
   * @method toogleSubList
   * @return {void}
   */
  toogleSubList() {
    this.is_sub_list = !this.is_sub_list;
    this.getSubscriptionList();
  }

  /**
   * getMenuContent subscription list from Db
   * @namespace xio.SubscriptionListComponent
   * @method getSubscriptionList
   * @return {void}
   */
  getSubscriptionList() {
    this.is_sub_list_loaded = false;
    this.store.dispatch(new GetAllSubscription({
      ise_id: this.ise_id
    }));
  }

  ngOnDestroy() {
    this.iseSubcriptionLst$.unsubscribe();
  }
}


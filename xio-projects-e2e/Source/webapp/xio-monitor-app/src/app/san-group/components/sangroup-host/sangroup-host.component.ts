import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GetSanGroupHostAction, GetAllAction } from '../../../actions/sangroup.action';
import { Store } from '@ngrx/store';
import { getSanGroupHostLst, State, getISEId } from '../../../reducers/';
import { sangroupListOptions } from "./sangroup-list-options";
import { GridOptions } from "../../../common/Metadata/xio.dataTable";
import { XioDialogComponent } from "../../../theme/xio-dialog/xio-dialog.component";
import { MdDialog } from "@angular/material";
import { XioProgressComponent } from "../../../theme/xio-progress/xio-progress.component";
import { SnackbarService } from "../../../theme/services/snackbar.service";
import { XioAlertComponent } from "../../../theme/xio-alert/xio-alert.component";
import { DeleteVolumeAction } from "../../../actions/volume.actions";
import { HostService } from "../../../ise/services/host.service";

@Component({
  selector: 'app-sangroup-host',
  templateUrl: './sangroup-host.component.html',
  styleUrls: ['./sangroup-host.component.scss']
})

export class SangroupHostComponent implements OnInit, OnDestroy {

  public sangroup_id: number;
  public host: any;
  public ise_id: any;
  public gridOptions;
  public sanGroupHost$;
  public progressRef;

  constructor(public activatedRoute: ActivatedRoute,
              public store: Store<State>,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public hs: HostService) { }

  ngOnInit() {

    this.activatedRoute.params.subscribe(params => {
      this.sangroup_id = params['sg_id'];
      this.gridOptions = Object.assign({}, sangroupListOptions);
      this.gridOptions['deleteCb'] = this.bindHostDeleteCb.bind(this);
      this.store.select(getISEId).subscribe(data => {
        this.ise_id = data;
      });
    });
    this.getHostList();

    this.store.dispatch(new GetSanGroupHostAction(this.sangroup_id));
    this.sanGroupHost$ = this.store.select(getSanGroupHostLst).subscribe(
      data => {
        let rowData = [];

        for (let i = 0; i < data.length; i++) {
          rowData.push({
            'host_id': data[i]['id'],
            'ise_name': data[i]['ise_name'],
            'host_comment': data[i]['host_comment'],
            'name': data[i]['name'],
            'ise_id': data[i]['ise_id'],
          })
        }
        this.gridOptions.rowData = rowData;
      }
    );
  }

  /**
  * Desc  : For deleting sangroupHost
  * Params : { host_id : ''}   
  * @param data
  */

  bindHostDeleteCb(data) {

    let host_id = data['host_id'];
    this.host = data.name;
    const dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Delete Host';
    dialogRef.componentInstance.message = 'Do you want to Delete ' + this.host + ' Host ?';
    dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'Processing';
        this.hs.deleteHost(data.host_id, data.ise_id).subscribe(
          data => {
            progressRef.close();
            this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
              if (d['host_id'] != host_id) {
                return d;
              }
            });
            this.snackbarService.toastMe('Host deleted successfully', 2000);
            this.store.dispatch(new GetAllAction({}));
          },
          err => {
            progressRef.close();
            const alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
            alertRef.componentInstance.title = 'Host';
            alertRef.componentInstance.message = err.json().result.error.message;
          });
      }
    });
  }

  /**
   * get's list Host system to be displayed on the listView
   * @namespace xio.SangroupHostComponent
   * @method getHostList
   * @return {void}
   */
  getHostList() {
    this.store.dispatch(new GetSanGroupHostAction(this.sangroup_id));
  }

  ngOnDestroy() {

    if (this.sanGroupHost$) {
      this.sanGroupHost$.unsubscribe();
    }
  }
}

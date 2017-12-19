import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HostService } from './../../services/host.service';
import { listConfig } from './host-list-options';

//REDUX
import { Store } from '@ngrx/store';
import { State, getAllHostsList } from '../../../reducers/';
import { GetAllHostsAction } from "../../../actions/hosts.actions";
import { SetISEId } from "../../../actions/ise-management.actions";
import { GridOptions } from "../../../common/Metadata/xio.dataTable";
import { XioDialogComponent } from "../../../theme/xio-dialog/xio-dialog.component";
import { MdDialog } from "@angular/material";
import { XioProgressComponent } from "../../../theme/xio-progress/xio-progress.component";
import { SnackbarService } from "../../../theme/services/snackbar.service";
import { XioAlertComponent } from "../../../theme/xio-alert/xio-alert.component";
import { GetAllAction } from "app/actions/sangroup.action";

@Component({
  selector: 'app-host',
  templateUrl: './host.component.html',
  styleUrls: ['./host.component.scss']
})
export class HostComponent implements OnInit, OnDestroy {

  public columnDefs: any;
  public gridOptions;
  public ise_id: number;
  public all_host_obs$;

  constructor(public route: ActivatedRoute,
    public router: Router,
    public hs: HostService,
    public dialog: MdDialog,
    public snackbarService: SnackbarService,
    public store: Store<State>) {
  }

  ngOnInit() {

    this.gridOptions = listConfig;
    this.gridOptions['deleteCb'] = this.bindISEDeleteCb.bind(this);
    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.getHostList();
    });
  }

  bindISEDeleteCb(data) {
    const dialogRef = this.dialog.open(XioDialogComponent),
      host_id = data.id;

    dialogRef.componentInstance.title = 'Delete WWN Group';
    dialogRef.componentInstance.message = 'Do you want to Delete ' + data.name + ' WWN Group ?';
    dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'Processing';
        this.hs.deleteHost(data.id, this.ise_id).subscribe(
          data => {
            progressRef.close();
            this.snackbarService.toastMe('WWN Group deleted successfully', 2000);
            this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
              if (d['id'] != host_id) {
                return d;
              }
            });
            this.store.dispatch(new GetAllAction({}));
          },
          err => {
            progressRef.close();
            const alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
            alertRef.componentInstance.title = 'WWN Group';
            alertRef.componentInstance.message = err.json().result.error.message;
          });
      }
    });
  }

  /**
   * Gets a List of Host's
   * @namespace xio.HostComponent
   * @method getHostList
   * @return {void}
   */
  getHostList() {

    this.store.dispatch(new GetAllHostsAction({
      ise_id: this.ise_id,
      cb: (success, error) => {
        if (!error) {

          this.all_host_obs$ = this.store.select(getAllHostsList).subscribe(data => {
            var rowData = data;

            for (let i = 0; i < rowData.length; i++) {
              let volume_arr = [];
              let volume_arr_name = [];

              for (let k = 0; k < rowData[i]['allocation'].length; k++) {

                if (volume_arr_name.indexOf(rowData[i]['allocation'][k]['volumename']) < 0) {

                  volume_arr.push(rowData[i]['allocation'][k]);
                  volume_arr_name.push(rowData[i]['allocation'][k]['volumename']);
                  data[i]['allocation'][k]['globalid'] = rowData[i]['allocation'][k]['globalid'].slice(0, 32);

                }

              }

              data[i]['allocation'] = volume_arr;

            }

            this.gridOptions.rowData = data;
          }, error => {
            console.error(error);
          }, () => {
            console.log("finished");
          })
        } else {
          if (error.status === 401) {
            let path = '/ise/' + this.ise_id + '/set-password/';
            this.router.navigate([path]);
          }

        }
      }
    }));

  }

  ngOnDestroy() {
    if(this.all_host_obs$){  
    this.all_host_obs$.unsubscribe();
    }
  }
}


 // if (allocations.length) {
 //      let volume_arr = [];
 //      for (let i = 0; i < allocations.length; i++) {

 //        if (volume_arr.indexOf(allocations[i].volumename) < 0) {
 //          volume_arr.push(allocations[i].volumename)
 //          template += '<div class="row " style="padding-left: 4%;" >'
 //            + '<div class="col-sm-4 ">' + allocations[i].volumename + '</div>'
 //            + '<div class="col-sm-4">' + allocations[i].lun + '</div>'
 //            + '<div class="col-sm-4">' + allocations[i].globalid.slice(0, 31) + '</div>'
 //            + '</div>';
 //        }
 //      }
 //    } else {
 //      template += '<div class="row " style="padding-left: 4%;padding-top:15px;" >'
 //        + '<div class="col-sm-12 text-warnning">Volumes yet to be allocated</div>'
 //        + '</div>';
 //    }

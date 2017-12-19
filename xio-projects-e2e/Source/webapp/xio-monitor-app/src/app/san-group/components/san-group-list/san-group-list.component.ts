import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MdDialog } from '@angular/material';
import { getSanGroupLst, State } from '../../../reducers';
import { Store } from '@ngrx/store';
import { GetAllAction, DeleteSanGroupAction } from '../../../actions/sangroup.action';
import { sanGroupListConfig } from './san-grp-list-options';
import { XioDialogComponent } from '../../../theme/xio-dialog/xio-dialog.component';
import { XioProgressComponent } from '../../../theme/xio-progress/xio-progress.component';
import { SnackbarService } from '../../../theme/services/snackbar.service';
import { XioAlertComponent } from '../../../theme/xio-alert/xio-alert.component';
import { GetMenuAction } from '../../../actions/menu.action';
import { SANGroup } from '../../models/san-group';

@Component({
  selector: 'app-san-group-list',
  templateUrl: './san-group-list.component.html',
  styleUrls: ['./san-group-list.component.scss']
})

export class SanGroupListComponent implements OnInit, OnDestroy {
  public gridOptions;
  public sanGroup$;

  constructor(public router: Router,
              public dialog: MdDialog,
              public store: Store<State>,
              public snackbarService: SnackbarService) {

  }

  /**
   * Desc : Used for getting sangroup list on load when component
   *        gets initialized.
   * Store State Name : getSanGroupLst
   */
  init() {
    this.sanGroup$ = this.store.select(getSanGroupLst).subscribe(
      (data: Array<SANGroup>) => {
        if (data && data.length > 0 && Array.isArray(data)) {
          this.gridOptions.rowData = data;
        }
      },
      err => {
        console.log(err);
      });
  }

  ngOnInit() {
    this.gridOptions = sanGroupListConfig;
    this.gridOptions['deleteCb'] = this.bindSANDeleteCb.bind(this);
    this.store.dispatch(new GetAllAction());
    this.init();
  }

  /**
   * Desc  : For deleting sangroup
   * Params : { sangroup_id : ''}   
   * @param data
   */
  bindSANDeleteCb(data) {
    let that = this;
    const san = data.sangroup_name,
      dialogRef = this.dialog.open(XioDialogComponent);
      dialogRef.componentInstance.title = 'Delete SAN Group';
      dialogRef.componentInstance.message = 'Do you want to Delete ' + san + ' SAN Group';
      dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'Loading....';
        this.store.dispatch(new DeleteSanGroupAction({
          sangroup_id: data.sangroup_id,
          cb: (_data, err) => {
            if (!err) {
              progressRef.close();
              this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
                if (d.id !== _data.sangroup_id) {
                  return d;
                }
              });
              this.snackbarService.toastMe('SAN Group Deleted Successfully', 2000);
              this.store.dispatch(new GetAllAction());
              this.store.dispatch(new GetMenuAction({}));
            } else {
              this.store.dispatch(new GetAllAction());
              progressRef.close();
              setTimeout(() => {
                let err_msg = err.json();
                let alertRef = that.dialog.open(XioAlertComponent, { disableClose: true });
                alertRef.componentInstance.title = 'SAN Group';
                alertRef.componentInstance.message = err_msg.result.error.message;
              }, 500);
            }
          }
        }));
      }

    });
  }


  /**
  * Desc : util method to re-direct to particular route
  * @method navigateTo
  * @param {any} event - event
  * @param {string} path - relative / route path to re-direct to
  * @return {void}
  */

  navigateTo(event: any, path: string) {
    event.stopPropagation();
    this.router.navigate([path]);
  }

  ngOnDestroy() {
    if (this.sanGroup$) {
      this.sanGroup$.unsubscribe();
    }
  }

}

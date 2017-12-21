import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { listConfig } from './user-list-option';
import { Store } from '@ngrx/store';
import { State } from '../../../reducers/';
import { Observable } from 'rxjs/Observable';
import { getUserLstState } from '../../../reducers/index';
import { GetAllUsersAction } from '../../../actions/user.actions';
import { XioDialogComponent } from "../../../theme/xio-dialog/xio-dialog.component";
import { MdDialog } from "@angular/material";
import { XioProgressComponent } from "../../../theme/xio-progress/xio-progress.component";
import { XioAlertComponent } from "../../../theme/xio-alert/xio-alert.component";
import { SnackbarService } from "../../../theme/services/snackbar.service";
import { DeleteUserAction } from "../../../actions/user.actions";
import { User } from "./../../models/user";

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})

export class UserListComponent implements OnInit, OnDestroy {

  public gridOptions;
  public user$;

  constructor(public router: Router,
              public store: Store<State>,
              public dialog: MdDialog,
              public snackbarService: SnackbarService) {

    this.store.dispatch(new GetAllUsersAction());

  }

  ngOnInit() {
    this.gridOptions = listConfig;
    this.gridOptions['deleteCb'] = this.bindUserDeleteCb.bind(this);
    this.store.dispatch(new GetAllUsersAction());

    /**
     * Desc : Used for getting User list on load when component
     *        gets initialized.
     * Store State Name : getUserLstState
     */

    this.user$ = this.store.select(getUserLstState).subscribe(
      (data: Array<User>) => {
        if (data) {
          this.gridOptions.rowData = data;
        }
      });
  }

  /**
  * Desc  : For deleting User
  * Params : { user_id : ''}   
  * @param data
  */

  bindUserDeleteCb(data) {

    const dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Delete User';
    dialogRef.componentInstance.message = 'Do you want to Delete ' + data.username + ' User ?';

    dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'processing';
        this.store.dispatch(new DeleteUserAction({
          id: data.id,
          cb: (res, error) => {

            if (res) {
              progressRef.close();
              this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
                if (d.id != data.id) {
                  return d;
                }
              });
              this.snackbarService.toastMe('User deleted successfully', 2000);

            } else if (error) {
              progressRef.close();
               let err_msg = ( error.json !== '' || error.json !== undefined || error.json !== null) ? error.json() : ''; 
               let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true }); 
                   alertRef.componentInstance.title = 'User'; 
                   alertRef.componentInstance.message = err_msg !== '' ? err_msg.result.error.message : 'Bad Request'; 
            }
          }
        }));
      }
    });
  }

  /**
   * Desc : util method to re-direct to particular route
   * @namespace xio.UserListComponent
   * @method navigateTo
   * @param {any} event - event
   * @return {void}
   */

  navigateTo(event, path) {
    event.stopPropagation();
    this.router.navigate([path]);
  }

  ngOnDestroy() {
    if (this.user$) {
      this.user$.unsubscribe();
    }
  }

}



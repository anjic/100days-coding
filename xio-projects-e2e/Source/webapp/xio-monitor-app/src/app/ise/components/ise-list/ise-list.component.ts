import { Component, OnInit, OnDestroy } from '@angular/core';
import { IseService } from './../../services/';
import { listConfig } from './ise-list-options';
import { GridOptions } from '../../../common/Metadata/xio.dataTable';
import { Store } from '@ngrx/store';
import { getAllIseLst, State } from '../../../reducers/index';
import { DeleteISE, GetAllISEList } from '../../../actions/ise-management.actions';
import { XioDialogComponent } from '../../../theme/xio-dialog/xio-dialog.component';
import { MdDialog } from '@angular/material';
import { XioProgressComponent } from '../../../theme/xio-progress/xio-progress.component';
import { XioAlertComponent } from '../../../theme/xio-alert/xio-alert.component';
import { SnackbarService } from '../../../theme/services/snackbar.service';
import { ISE } from './../../models/ise';

@Component({
  selector: 'app-ise-list',
  templateUrl: './ise-list.component.html',
  styleUrls: ['./ise-list.component.scss'],
})
export class IseListComponent implements OnInit, OnDestroy {
  public gridOptions;
  public iseLst$;

  /**
   * 
   * @param {IseService} ises
   * @param {MdDialog} dialog
   * @param {SnackbarService} snackbarService
   * @param {Store<State>} store
   */

  constructor(public ises: IseService,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
  }

  /* Desc : Method used for setting grid options
   *
   */
  setGridOptions() {
    this.iseLst$ = this.store.select(getAllIseLst);
    this.gridOptions = listConfig;
    this.gridOptions['deleteCb'] = this.bindISEDeleteCb.bind(this);
  }

  ngOnInit() {
    let _this = this;
    this.store.dispatch(new GetAllISEList());
    this.setGridOptions();
    this.iseLst$ = this.store.select(getAllIseLst).subscribe(
      (data: ISE[]) => {
        _this.gridOptions.rowData = data;
      }
    );
  }

  /**
  * Desc  : For deleting Ise
  * Params : { ise_id : ''}   
  * @param data
  */

  bindISEDeleteCb(data) {
    const ise = data.ise_name,
      dialogRef = this.dialog.open(XioDialogComponent);
      dialogRef.componentInstance.title = 'Delete ISE';
      dialogRef.componentInstance.message = 'Do you want to Delete ' + ise + ' ISE ?';
      dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'processing';
        this.store.dispatch(new DeleteISE({
          ise_id: data.id,
          cb: (success, error) => {
            if (success) {
              progressRef.close();
              this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
                if (d.id != data.id) {
                  return d;
                }
              });
              this.snackbarService.toastMe('ISE deleted Successfully', 2000);
            } else {
              progressRef.close();
              let err_msg = (error.json !== '' || error.json !== undefined
                || error.json !== null) ? error.json() : '';
              let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
              alertRef.componentInstance.title = 'ISE';
              alertRef.componentInstance.message = err_msg !== '' ?
                                                   err_msg.result.error.message :
                                                   'Bad Request';
            }
          }
        }));
      }
    });
  }

  ngOnDestroy() {
    if(this.iseLst$){
    this.iseLst$.unsubscribe();
  }
  }
}

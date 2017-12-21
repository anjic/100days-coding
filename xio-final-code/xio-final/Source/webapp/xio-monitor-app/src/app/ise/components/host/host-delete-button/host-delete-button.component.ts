import {Component, Input} from '@angular/core';

import {HostService} from '../../../services/host.service';
import {IseService} from './../../../services/ise.service';
import {MdDialog} from '@angular/material';
import {
  XioDialogComponent,
  XioProgressComponent,
  XioAlertComponent,
  MenuContentService,
  SnackbarService
} from './../../../../theme/';

//REDUX
import {Store} from '@ngrx/store';
import {State, getISEId} from "../../../../reducers";
import {GetAllAction} from "../../../../actions/sangroup.action";

@Component({
  selector: 'ag-delete-clickable',
  templateUrl: './host-delete-button.component.html',
  styleUrls: ['./host-delete-button.component.scss']
})
export class HostDeleteButtonComponent {
  @Input() cell: any;

  public params: any;
  public ise_id: any;
  public host: any;
  public ise_id_obs$;

  constructor(public hs: HostService,
              public ises: IseService,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public mcs: MenuContentService,
              public store: Store<State>) {
  }

  agInit(params: any): void {

    this.params = params;
    this.cell = {row: params.value, col: params.colDef.headerName};
    if (this.params.data.ise_id)
      this.ise_id = this.params.data.ise_id;
    else {
      this.ise_id_obs$ = this.store.select(getISEId).subscribe(data => {
        this.ise_id = data;
      })
    }
  }

  /**
   * opens a confirmation dialog before deleting the sans-group
   * @namespace xio.HostDeleteButtonComponent
   * @method openDialog
   * @return {void}
   */
  openDialog() {
    this.host = this.params.data.name;
    const dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Delete Host';
    dialogRef.componentInstance.message = 'Do you want to Delete ' + this.host + ' Host ?';
    dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
        progressRef.componentInstance.progress_data = 'Processing';
        this.hs.deleteHost(this.params.data.id, this.ise_id).subscribe(
          data => {
            progressRef.close();
            this.snackbarService.toastMe('Host deleted successfully', 2000);
            this.params.api.removeItems([this.params.node]);
            this.store.dispatch(new GetAllAction({}));
          },
          err => {
            progressRef.close();
            const alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title = 'Host';
            alertRef.componentInstance.message = err.json().result.error.message;
          });
      }
    });
  }

  ngOnDestroy() {
    if (this.ise_id_obs$)
      this.ise_id_obs$.unsubscribe();
  }

}

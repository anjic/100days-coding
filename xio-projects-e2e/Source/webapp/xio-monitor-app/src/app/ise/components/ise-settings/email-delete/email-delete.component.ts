import {Component, Input, Output, EventEmitter, OnDestroy} from '@angular/core';
import {MdDialog} from '@angular/material';
import {XioDialogComponent} from './../../../../theme/xio-dialog/xio-dialog.component';
import {XioProgressComponent} from './../../../../theme/xio-progress/xio-progress.component';
import {EmailService} from './../../../services/email.service';
import {IseService} from './../../../services/ise.service';
import {SnackbarService} from './../../../../theme/services/snackbar.service';
import {Md2Toast} from 'md2/toast/toast';
import {XioAlertComponent} from './../../../../theme/xio-alert/xio-alert.component';

//REDUX
import {Store} from '@ngrx/store';
import {State, getISEId} from "../../../../reducers";
import {Observable} from 'rxjs/Observable'


@Component({
  selector: 'app-email-delete',
  templateUrl: './email-delete.component.html',
  styleUrls: ['./email-delete.component.scss']
})
export class EmailDeleteComponent implements OnDestroy {
  @Input() cell: any;
  @Output() onClicked = new EventEmitter<boolean>();

  public params: any;
  public closeResult: any;
  public ise_id: Number;
  public ise_id_obs$;

  constructor(public dialog: MdDialog,
              public ises: IseService,
              public es: EmailService,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
  }

  agInit(params: any): void {
    this.params = params;
    this.cell = {row: params.value, col: params.colDef.headerName};
    this.ise_id_obs$ = this.store.select(getISEId).subscribe(data => {
      this.ise_id = +data;
    }, error => {

    })

  }

  click(): void {
    console.log('Clicked');
    console.log(this.params.colDef.fnName);
    this.onClicked.emit(this.cell);
  }

  openDialog() {

    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = "Delete";
    dialogRef.componentInstance.message = "Do you want to Delete ?";
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
      if (result == 'yes') {
        let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
        progressRef.componentInstance.progress_data = "Loading....";
        this.es.deleteEmail(this.ise_id, this.params.data.id).subscribe(
          data => {
            progressRef.close();
            this.snackbarService.toastMe('User Deleted Successfully', 2000);
            this.params.api.removeItems([this.params.node]);
          },
          err => {
            progressRef.close();
            let err_msg = err.json();
            console.log(err_msg);
            let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title = "Email";
            alertRef.componentInstance.message = err_msg.result.response.data;
          });
      }

    });

  }

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }

}

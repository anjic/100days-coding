import {Component, Input, Output, EventEmitter, OnDestroy} from '@angular/core';
import {IseService} from './../../../../services/ise.service';
import {SubscriptionService} from './../../../../services/subscription.service';
import {MdDialog} from '@angular/material';
import {SnackbarService} from './../../../../../theme/services/snackbar.service';
import {XioAlertComponent, XioProgressComponent, XioDialogComponent} from './../../../../../theme/';
import {Store} from '@ngrx/store';
import {State, getISEId} from '../../../../../reducers/';
import {DeleteSubscription} from '../../../../../actions/ise-settings.actions';

//REDUX
import { Observable } from 'rxjs/Observable'

@Component({
  selector: 'app-subscription-delete',
  templateUrl: './subscription-delete.component.html',
  styleUrls: ['./subscription-delete.component.scss']
})
export class SubscriptionDeleteComponent implements OnDestroy {
  @Input() cell: any;
  @Output() onClicked = new EventEmitter<boolean>();

  public params: any;
  public closeResult: any;
  public ise_id: number;
  public ise_id_obs$;

  constructor(public dialog: MdDialog,
              public ises: IseService,
              public sub: SubscriptionService,
              public snackbarService: SnackbarService,
              public store: Store<State>) {

    //this.ise_id = this.ises.getCurrentISEId();

  }

  agInit(params: any): void {

    this.params = params;
    this.cell = {row: params.value, col: params.colDef.headerName};
    this.ise_id_obs$ = this.store.select(getISEId).subscribe( data => {
      this.ise_id = +data;
    },error => {

    })

  }

  click(): void {
    this.onClicked.emit(this.cell);
  }

  /**
   * open Dialog controller
   * @namespace xio.SubscriptionDeleteComponent
   * @method openDialog
   * @return {void}
   */
  openDialog() {

    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Delete Subscription';
    dialogRef.componentInstance.message = 'Do you want to Delete Subscription ?';
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
      if (result == 'yes') {
        let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
        let progress_data = 'processing'
        progressRef.componentInstance.progress_data = progress_data;
        this.store.dispatch(new DeleteSubscription({
          ise_id: this.ise_id,
          id: this.params.data.id,
          cb: (data, err) => {
            if(data) {
              progressRef.close();
              this.params.api.removeItems([this.params.node]);
              this.snackbarService.toastMe('Subscription deleted Successfully', 2000);
            }
            else if(err) {

              progressRef.close();
              let err_msg = err.json();
              let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
              alertRef.componentInstance.title = 'Subscription';
              alertRef.componentInstance.message = err_msg.result.error.message;
            }
          }
        }));
        // this.sub.deleteSubscription(this.ise_id, this.params.data.id).subscribe(
        //   data => {
        //   },
        //   err => {
        //
        //   });
      }

    });

  }
  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }


}



import {Component, Input, Output, EventEmitter, OnDestroy} from '@angular/core';
import {IseService} from '../../../services/ise.service';
import {StoragevolumeService} from '../../../services/storagevolume.service';
import {MdDialog} from '@angular/material';
import {XioProgressComponent, XioDialogComponent, SnackbarService, XioAlertComponent} from './../../../../theme/';

//Redux
import {Store} from '@ngrx/store';
import {State, getISEId} from "../../../../reducers/";
import {DeleteVolumeAction} from "../../../../actions/volume.actions";
import {Observable} from 'rxjs/Observable';

@Component({
  selector: 'app-volume-delete-button',
  templateUrl: './volume-delete-button.component.html',
  styleUrls: ['./volume-delete-button.component.scss'],
  providers: [SnackbarService]
})
export class VolumeDeleteButtonComponent implements OnDestroy {
  @Input() cell: any;
  @Output() onClicked = new EventEmitter<boolean>();

  public params: any;
  public closeResult: any;
  public ise_id: number;
  public ise_id_obs$;
  public progressRef;

  constructor(public dialog: MdDialog,
              public ises: IseService,
              public svs: StoragevolumeService,
              public snackbarService: SnackbarService,
              public store:Store<State>) {
  }

  agInit(params: any): void {
    this.params = params;
    this.cell = {row: params.value, col: params.colDef.headerName};
    this.ise_id_obs$ = this.store.select(getISEId).subscribe( data => {
      this.ise_id = +data;
    },error => {

    })
    //this.ise_id = this.ises.getCurrentISEId();
  }

  /**
   * click event to emit cell data
   * @namespace xio.VolumeDeleteButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    this.onClicked.emit(this.cell);
  }

  onDeleteCallBack =  this.onDeleteCallBack || ((success,error)=> {
      if(!error){
        this.progressRef.close();
        this.progressRef = null;
        this.params.api.removeItems([this.params.node]);
        this.snackbarService.toastMe('Volume Deleted Successfully', 15000);
      }else{
        this.progressRef.close();
        this.progressRef = null;
        let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = "Volume";
        alertRef.componentInstance.message = error.json().result.error.message;
      }})

  /**
   * open Dialog controller
   * @namespace xio.VolumeDeleteButtonComponent
   * @method openDialog
   * @return {void}
   */
	openDialog() {
		let name = this.params.data.name;
		let dialogRef = this.dialog.open(XioDialogComponent);
		dialogRef.componentInstance.message = 'Do you really want to delete "' + name + '" ?';
		dialogRef.componentInstance.title = "Delete Volume";
		dialogRef.afterClosed().subscribe(result => {
			console.log(result);
			if (result == 'yes') {
				this.progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
				this.progressRef.componentInstance.progress_data = "Loading....";
        let payLoad = {
          "ise_id":this.ise_id,
          "id":this.params.data.id,
          "cb":this.onDeleteCallBack
        }
				this.store.dispatch( new DeleteVolumeAction(payLoad));

				/*this.svs.deleteVolumeDetails(payLoad).subscribe(
					data => {
						progressRef.close();
						this.params.api.removeItems([this.params.node]);
						this.snackbarService.toastMe('Volume Deleted Successfully', 15000);
					},
					err => {
						progressRef.close();
						let err_msg = err.json();
						// console.log(err_msg);
						let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
						alertRef.componentInstance.title = "Volume";
						alertRef.componentInstance.message = err_msg.response.data;
					});*/
			}
		});
	}

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }
}

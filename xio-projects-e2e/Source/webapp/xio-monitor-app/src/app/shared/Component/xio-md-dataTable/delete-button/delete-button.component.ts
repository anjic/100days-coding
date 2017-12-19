import {Component, Input} from '@angular/core';


@Component({
  selector: 'xio-md-row-delete ',
  templateUrl: './delete-button.component.html',
  styleUrls: ['./delete-button.component.scss']
})
export class DeleteButtonComponent {
  @Input() deleteCb: Function;
  @Input() data;
  @Input() headerName: any;


  /**
   * opens a confirmation dialog before deleting the sans-group
   * @namespace xio.IseDeleteButtonComponent
   * @method openDialog
   * @return {void}
   */
  // openDialog() {
  //   const ise = this.params.data.ise_name,
  //   dialogRef = this.dialog.open(XioDialogComponent);
  //   dialogRef.componentInstance.title = 'Delete ISE';
  //   dialogRef.componentInstance.message = 'Do you want to Delete ' + ise + ' ISE ?';
  //   dialogRef.afterClosed().subscribe(result => {
  //
  //     if (result === 'yes') {
  //       const progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
  //       progressRef.componentInstance.progress_data = 'processing';
  //       //TODO Dominic Verify
  //       this.store.dispatch(new DeleteISE({
  //         ise_id: this.params.data.id,
  //         cb: (res, err) => {
  //           if(res) {
  //             progressRef.close();
  //             this.params.api.removeItems([this.params.node]);
  //             this.snackbarService.toastMe('ISE deleted Successfully', 1000);
  //           }
  //           else if(err) {
  //             progressRef.close();
  //             const alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
  //             alertRef.componentInstance.title = 'ISE';
  //             alertRef.componentInstance.message = err.json().result.error.message;
  //           }
  //         }
  //       }));
  //     }
  //   });
  // }

  /**
   * click event
   * @namespace xio.IseEditButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    if(this.deleteCb) {
      this.deleteCb(this.data);
    }
  }
}



import {Component, Input} from '@angular/core';
import {MdDialogRef} from '@angular/material';
@Component({
  selector: 'app-xio-dialog',
  templateUrl: './xio-dialog.component.html',
  styleUrls: ['./xio-dialog.component.scss']
})
export class XioDialogComponent {
  @Input() message;
  @Input() title;

  constructor(public dialogRef: MdDialogRef<XioDialogComponent>) {
  }

  /**
   * Closex dialog on click
   */
  onYes() {
    this.dialogRef.close('yes');
  }

  /**
   * Closex dialog on click
   */
  onNo() {
    this.dialogRef.close('no');
  }
}

import {Component, Input} from '@angular/core';
import {MdDialogRef} from '@angular/material';

@Component({
  selector: 'app-xio-alert',
  templateUrl: './xio-alert.component.html',
  styleUrls: ['./xio-alert.component.scss']
})
export class XioAlertComponent {
  @Input() title;
  @Input() message;

  constructor(public alertRef: MdDialogRef<XioAlertComponent>) {
  }

  /**
   * Closed the alert box
   */
  onOk() {
    this.alertRef.close('Ok');
  }

}

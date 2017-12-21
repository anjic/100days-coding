import {Component, Input} from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'xio-md-row-edit',
  templateUrl: './edit-button.component.html',
  styleUrls: ['./edit-button.component.scss']
})
export class EditButtonComponent {
  @Input() path: string;
  @Input() headerName: any;

  constructor(public router: Router) {
  }

  /**
   * click event
   * @namespace xio.IseEditButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    this.router.navigate([this.path]);
  }
}

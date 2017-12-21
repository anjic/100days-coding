import {Component, Input} from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-ise-present-button',
  templateUrl: './present-button.component.html',
  styleUrls: ['./present-button.component.scss']
})
export class PresentButtonComponent {

  @Input() path: string;
  @Input() headerName: any;

  constructor(public router: Router) {
  }


  /**
   * click event
   * @namespace xio.IsePresentButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    // let path = '/ise/' + this.ise_id + '/san-group/link/';
    this.router.navigate([this.path]);
  }
}

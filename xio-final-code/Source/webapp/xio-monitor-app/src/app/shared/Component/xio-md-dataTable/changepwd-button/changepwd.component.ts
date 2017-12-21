import {Component, Input} from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'xio-md-row-change-pwd',
  templateUrl: './changepwd.component.html'
})
export class ChangepwdComponent {

  @Input() path: any;
  @Input() headerName: any;

  constructor(public router: Router) {
  }

  /**
   * click event
   * @namespace xio.IseChangePwdComponent
   * @method click
   * @return {void}
   */
  click(): void {
    this.router.navigate([this.path]);
  }
}

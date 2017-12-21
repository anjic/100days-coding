import { Component, Input } from '@angular/core';
import {Router} from '@angular/router';


@Component({
  selector: 'app-modify-button',
  templateUrl: './modify-button.component.html',
  styleUrls: ['./modify-button.component.scss']
})
export class ModifyButtonComponent {

 @Input() path: any;
 @Input() headerName: any;

  constructor(public router: Router) {
  }

  /**
   * click event
   * @namespace xio.ModifyButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    this.router.navigate([this.path]);
  }

}

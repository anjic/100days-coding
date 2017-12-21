import {Component, Input, Output, EventEmitter} from '@angular/core';
import {Router} from '@angular/router';
import {IseService} from '../../../services/ise.service';

@Component({
  selector: 'app-ise-edit',
  templateUrl: './user-edit-button.component.html',
  styleUrls: ['./user-edit-button.component.scss'],
  providers: [IseService]
})
export class UserEditButtonComponent {

  public params: any;
  public ise_id: number;

  constructor(public router: Router) {
  }

  agInit(params: any): void {
  }
}

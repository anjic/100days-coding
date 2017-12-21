import {Component, Input, Output, EventEmitter, OnDestroy } from '@angular/core';
import {Router} from '@angular/router';
import {IseService} from '../../../services/ise.service';

//REDUX
import { Store } from '@ngrx/store';
import {State, getISEId} from "../../../../reducers/";
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-volume-edit-button',
  templateUrl: './volume-edit-button.component.html',
  styleUrls: ['./volume-edit-button.component.scss']

})
export class VolumeEditButtonComponent implements OnDestroy {

  @Input() cell: any;
  @Output() onClicked = new EventEmitter<boolean>();

  public params: any;
  public ise_id: number;
  public ise_id_obs$;

  constructor(public ises: IseService, public router: Router, public store:Store<State>) {
  }

  agInit(params: any): void {
    this.params = params;
    this.cell = {row: params.value, col: params.colDef.headerName};
    this.ise_id_obs$ = this.store.select(getISEId).subscribe( data => {
      this.ise_id = +data;
    })
  }

  /**
   * click event
   * @namespace xio.VolumeEditButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    let path = '/ise/' + this.ise_id + '/volume/edit/' + this.params.data.id;
    this.onClicked.emit(this.cell);
    this.router.navigate([path]);
  }

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }
}

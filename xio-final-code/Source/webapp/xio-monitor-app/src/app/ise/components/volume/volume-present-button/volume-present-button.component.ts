import {Component, Input, Output, EventEmitter, OnDestroy} from '@angular/core';
import {Router} from '@angular/router';
import {IseService} from './../../../services/ise.service';

//REDUX
import { Store } from '@ngrx/store';
import {State, getISEId} from "../../../../reducers/";
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-volume-present-button',
  templateUrl: './volume-present-button.component.html',
  styleUrls: ['./volume-present-button.component.scss']
})
export class VolumePresentButtonComponent implements OnDestroy {
  @Input() cell: any;
  @Output() onClicked = new EventEmitter<boolean>();

  public params: any;
  public ise_id: number;
  public ise_id_obs$;

  constructor(public ises: IseService,
              public router: Router,
              public store:Store<State>) {

   // this.ise_id = this.ises.getCurrentISEId();
  }

  agInit(params: any): void {
    this.params = params;
    this.cell = {row: params.value, col: params.colDef.headerName};
    this.ise_id_obs$ = this.store.select(getISEId).subscribe( data => {
      this.ise_id = +data;
    },error => {

    })
  }

  /**
   * click event to emit cell data
   * @namespace xio.VolumePresentButtonComponent
   * @method click
   * @return {void}
   */
  click(): void {
    let path = '/ise/' + this.ise_id + '/volume/present/' + this.params.data.id;
    this.router.navigate([path]);
    this.onClicked.emit(this.cell);
  }

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }

}

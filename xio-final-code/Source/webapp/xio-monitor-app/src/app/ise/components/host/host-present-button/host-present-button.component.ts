import {Component, Input, OnDestroy} from '@angular/core';
import {Router} from '@angular/router';
import {IseService} from './../../../services/ise.service';

//REDUX
import { Store } from '@ngrx/store';
import { State, getISEId } from "../../../../reducers";
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-host-present-button',
  templateUrl: './host-present-button.component.html',
  styleUrls: ['./host-present-button.component.scss']
})
export class HostPresentButtonComponent implements OnDestroy {
  @Input() cell: any;
  public params: any;
  public ise_id;
  public ise_id_obs$;

  constructor(public ises: IseService,
              public router: Router,
              public store:Store<State>) {
    //this.ise_id = this.ises.getCurrentISEId();
  }

  agInit(params: any): void {
      this.params = params;
      this.cell = {row: params.value, col: params.colDef.headerName};
      this.ise_id_obs$ = this.store.select(getISEId).subscribe( data => {
        this.ise_id = data;
      },error => {

      });
    }

  /**
   * click Event to navigate to ise/host:id/present
   * @namespace xio.AuthService
   * @method click
   * @return {void}
   */
  click(): void {
    let path = '/ise/' + this.ise_id + '/host/' + this.params.data.id + '/present';
    this.router.navigate([path]);
  }

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }
}

import { Component, Input, OnDestroy } from '@angular/core';
import { IseService } from './../../../services/ise.service';
import { Router, ActivatedRoute } from '@angular/router';

//REDUX
import { Store } from '@ngrx/store';
import { State, getISEId } from "../../../../reducers";
import { Observable } from 'rxjs/Observable'

@Component({
  selector: 'ag-edit-clickable',
  templateUrl: './host-edit-button.component.html',
  styleUrls: ['./host-edit-button.component.scss'],

})

export class HostEditButtonComponent implements OnDestroy {
  @Input() cell: any;

  public params: any;
  public ise_id: number ;
  public ise_id_obs$;

  constructor(public ises: IseService,
              public route: ActivatedRoute,
              public router: Router,
              public store:Store<State>) {
    this.route.params.subscribe(params => {
      if (!params.hasOwnProperty('sg_id')) {
        //this.ise_id = this.ises.getCurrentISEId();
      }
    });
  }

  agInit(params: any): void {
    this.params = params;

    /*if (!this.ise_id) {
      this.ise_id = this.params.data.ise_id;
    }*/

    this.cell = { row: params.value, col: params.colDef.headerName };
    this.ise_id_obs$ = this.store.select(getISEId).subscribe( data => {
      this.ise_id = +data;
    },error => {

    })
  }

  click(): void {
    let path = '/ise/' + this.ise_id + '/host/edit/' + this.params.data.id + '/';
    this.router.navigate([path]);
  }

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }
}

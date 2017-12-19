import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Store } from '@ngrx/store';
import { getSanGroupLst, getSanGroupInfoLst, State } from '../../../reducers/';
import {
  GetSanGroupAction,
  SanGroupISEInfoReset
} from '../../../actions/sangroup.action';
import { SANGroup } from '../../models/san-group';


@Component({
  selector: 'app-sangroup-dashboard',
  templateUrl: './sangroup-dashboard.component.html',
  styleUrls: ['./sangroup-dashboard.component.scss']
})
export class SangroupDashboardComponent implements OnInit, OnDestroy {

  public sangroup_ise_list = [];
  public _san = [];
  public loading_stack;
  public sg_id:number;
  public sanGroupISE$;
  public sanGroup$;
  public san_name:string;
  public ise_list:number;

  constructor(public router: Router,
              public activateRoute: ActivatedRoute,
              public store: Store<State>) {

    this.loading_stack = {
      sangroup_details: false,
      sangroup_details_text: 'Loading.....'
    };
  }

  ngOnInit() {

    this.activateRoute.params.subscribe(params => {
      this.sg_id = params.sg_id;
      this.loading_stack.sangroup_details = true;
      this.store.dispatch(new SanGroupISEInfoReset());

      if (this.sanGroup$)
        this.sanGroup$.unsubscribe();

      /**
      * Desc : Used for getting sangroup list on load when component
      *        gets initialized.
      * Store State Name : getSanGroupLst
      */
      this.sanGroup$ = this.store.select(getSanGroupLst).subscribe(
        (data: Array<SANGroup>) => {
          this._san = data.filter((s: any) => {

            if (s.sangroup_id == this.sg_id) {
              this.san_name = s.sangroup_name;
              this.ise_list = s.ise.length;
              return s;
            }
          });

          if (this._san.length > 0 && this._san[0].hasOwnProperty('ise') && this._san[0]['ise'].length > 0) {
            this.loading_stack.sangroup_details = true;
            this._san[0]['ise'].forEach((_ise) => {
              this.store.dispatch(new GetSanGroupAction({
                ise_id: _ise.id,
                cb: (data) => {
                  this.loading_stack.sangroup_details = false;
                }
              }));
            });
          }
          else if (this._san.length == 0 || (this._san.length > 0 &&
            this._san[0]['ise'] && this._san[0]['ise'].length == 0)) {

            this.loading_stack.sangroup_details = false;
          }
        });

      if (this.sanGroupISE$)
        this.sanGroupISE$.unsubscribe();

      this.sangroup_ise_list.length = 0;
      this.sanGroupISE$ = this.store.select(getSanGroupInfoLst).subscribe(data => {
        if (this._san.length > 0) {
          let ise = this._san[0].ise.map((i) => {
            return i.id;
          });
          this.sangroup_ise_list = data.filter((d) => {
            if (ise.indexOf(d['id']) >= 0)
              return d;
          });
        } else {

          this.sangroup_ise_list = data;
        }
      });
    });
  }

  /**
  * Desc : util method to re-direct to particular route
  * @namespace xio.SangroupDashboardComponent
  * @method navigateTo
  * @param {any} event - event
  * @return {void}
  */

  navigateTo(event: any) {
    event.stopPropagation();
    const path: String = '/san-group/' + this.sg_id + '/ise/link';
    this.router.navigate([path]);
  }

  ngOnDestroy() {
    if (this.sanGroupISE$) {
      this.sanGroupISE$.unsubscribe();
    }
    if (this.sanGroup$) {
      this.sanGroup$.unsubscribe();
    }

    this.sangroup_ise_list.length = 0;
    this._san.length = 0;
  }
}

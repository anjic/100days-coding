import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Store } from '@ngrx/store';
import { State, getFansState } from '../../../../../reducers';
import { UpdateFansAction, GetFansAction } from '../../../../../actions/hardware.actions';
import { SetISEId } from '../../../../../actions/ise-management.actions';
import { MdDialog } from '@angular/material';
import { XioAlertComponent } from '../../../../../theme';

@Component({
  selector: 'app-fans',
  templateUrl: './fans.component.html',
  styleUrls: ['./fans.component.scss']
})
export class FansComponent implements OnInit, OnDestroy {

  public fans_identify: Array<any>;
  public fansList: any = [];
  public loading_stack;
  public ise_id;
  public fansList$;


  /**
  * @param {ActivatedRoute} activatedRoute
  * @param {MdDialog} dialog
  * @param {Store<State>} store
  */

  constructor(public activatedRoute: ActivatedRoute,
              public mdDialog: MdDialog,
              public store: Store<State>) {
    
    this.fans_identify = [];

    this.loading_stack = {
      fans_details: false,
      fans_details_text: 'Loading.....'
    }
  }

  ngOnInit() {
    this.loading_stack.fans_details = true;
    this.activatedRoute.parent.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetFansAction(this.ise_id));
    });


    /**
    * Desc : Used for getting particular ise fan details on load when component
    *        gets initialized.
    * Store State Name : getFansState
    */

    this.fansList$ = this.store.select(getFansState).subscribe(data => {
        
      this.loading_stack.fans_details = false;
      this.fans_identify = [];
      if (data instanceof Array ) {
        for (let fan of data) {
          let d = {
              value: true,
              loading: false
          };
          if (fan['led']['_attr']['string'] === 'disabled') {
            d.value = false;
          }
          this.fans_identify.push(d);        
        }
        this.fansList = data;  
      }
      
    }, error => {
          this.catchError(error);
    });
  }

  /**
   * Desc : change event to update Fan's Identify
   * @namespace xio.FansComponent
   * @method identifyFans
   * @param {Number} pos
   * @param {Number} id
   * @return {void}
   **/

  identifyFans(pos: number, id: number) {

    let data = { led: 'enabled' };
    
    if (!this.fans_identify[pos]['value']) {
      data['led'] = 'disabled';
    }

    this.fans_identify[pos]['loading'] = true;
    let that = this;

    this.store.dispatch(new UpdateFansAction({
      ise_id: this.ise_id,
      id: id,
      data: data,
      cb: (success, error) => {

        if (!error) {
          that.fans_identify[pos]['loading'] = false;
        } else {
          that.fans_identify[pos]['loading'] = false;
        }
      }
    }));
  }


   /**
   * Desc : Change particular status color
   * @namespace xio.FansComponent
   * @method statusClass
   * @param {String} status
   * @return {void}
   **/

  statusClass(status) {
    return (status === 'Non-Operational') ? 'ise_red' : '';
  }

   /**
   * Desc : Change toolbar color for particular status 
   * @namespace xio.FansComponent
   * @method toolBarClass
   * @param {String} status
   * @return {void}
   **/
  toolBarClass(status) {
    return (status === 'Non-Operational') ? 'toolbar_red' : 'toolbar_green';
  }

  /**
   * Desc : catching Error and Displaying in popup
   * @namespace xio.FansComponent
   * @method catchError
   * @param {any} error
   * @return {void}
   **/

  catchError(error) {
    let err_msg = (error.json !== '' || error.json !== undefined
                  || error.json !== null) ? error.json() : '';

    let alertRef = this.mdDialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'Fan';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             err_msg.result.error.message :
                                             'Bad Request';


  }

  ngOnDestroy() {

    if (this.fansList$) {
      this.fansList$.unsubscribe();
    }
    // Un binding listeners
    window.removeEventListener('change', this.identifyFans.bind(this), false);

  }
}


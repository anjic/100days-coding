/**
 * Created by Venkatesh on 7/19/2017.
 */
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Store } from '@ngrx/store';
import { State, gePowerSupplyState } from '../../../../../reducers/';
import { GetPowerSupplyAction, UpdatePowerSupplyAction } from '../../../../../actions/hardware.actions';
import { SetISEId } from '../../../../../actions/ise-management.actions';
import { XioAlertComponent } from '../../../../../theme';
import { MdDialog } from '@angular/material';
import { Powersupply } from '../../../../../ise/models/powersupply';


@Component({
  selector: 'app-powersupply',
  templateUrl: './powersupply.component.html',
  styleUrls: ['./powersupply.component.scss']
})
export class PowersupplyComponent implements OnInit, OnDestroy {

  public powerSupply_identify: Array<any>;
  public powerSupplyList: Array<Powersupply>;
  public ise_id;
  public loading_stack;
  public powerSupplyData$;

  /**
  * @param {ActivatedRoute} activatedRoute
  * @param {MdDialog} dialog
  * @param {Store<State>} store
  */

  constructor(public route: ActivatedRoute,
              public dialog: MdDialog,
              public store: Store<State>) {

    this.powerSupplyList = [];
    this.powerSupply_identify = [];

    this.loading_stack = {
      powersupply_details: false,
      powersupply_details_text: 'Loading.....'
    };
  }

  ngOnInit() {

    this.loading_stack.powersupply_details = true;
    this.route.parent.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.loading_stack.powersupply_details = true;
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetPowerSupplyAction(this.ise_id));
    });


    /**
    * Desc : Used for getting powersupply details on load when component
    *        gets initialized.
    * Store State Name : gePowerSupplyState
    */
    this.powerSupplyData$ = this.store.select(gePowerSupplyState).subscribe(
      (data: Array<Powersupply>) => {
        this.loading_stack.powersupply_details = false;
        this.powerSupply_identify = [];
        for (let powerSupply of data) {
            let e = {
              value: true,
              loading: false
            };
            if (powerSupply['led']['_attr']['string'] == 'disabled') {
              e.value = false;
            }
            this.powerSupply_identify.push(e);
        }
        this.powerSupplyList = data;

      }, error => {
        
        this.catchError(error);
      });
  }

  /**
  * Desc : change event to update PowerSupply Identify
  * @namespace xio.PowersupplyComponent
  * @method identifyFans
  * @param {Number} pos
  * @param {Number} id
  * @return {void}
  **/
  identifyPowerSupply(pos: number, id: number) {

    let data = { led: 'enabled' };
    if (!this.powerSupply_identify[pos]['value']) {
      data['led'] = 'disabled';
    }

    this.powerSupply_identify[pos]['loading'] = true;
    this.store.dispatch(new UpdatePowerSupplyAction({
      ise_id: this.ise_id,
      id: id,
      data: data,
      cb: (succes, error) => {
        if (!error) {
          this.powerSupply_identify[pos]['loading'] = false;
        } else {
          this.powerSupply_identify[pos]['loading'] = false;
        }
      }
    }));
  }

  /**
  * Desc : Change particular status color
  * @namespace xio.PowersupplyComponent
  * @method statusClass
  * @param {String} status
  * @return {void}
  **/

  statusClass(status) {
    return (status === 'Non-Operational') ? 'ise_red' : '';
  }

   /**
   * Desc : Change toolbar color for particular status 
   * @namespace xio.PowersupplyComponent
   * @method toolBarClass
   * @param {String} status
   * @return {void}
   **/

  toolBarClass(status) {
    return (status === 'Non-Operational') ? 'toolbar_red' : 'toolbar_green';
  }

  /**
   * Desc : catching Error and Displaying in popup
   * @namespace xio.PowersupplyComponent
   * @method catchError
   * @param {any} error
   * @return {void}
   **/

  catchError(error) {

    let err_msg = (error.json !== '' || error.json !== undefined
                  || error.json !== null) ? error.json() : '';

    let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'PowerSupply';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             err_msg.result.error.message :
                                             'Bad Request';
  }

  ngOnDestroy() {
    if (this.powerSupplyData$) {
      this.powerSupplyData$.unsubscribe();
    }

    // Unbinding listerners
    window.removeEventListener('change', this.identifyPowerSupply.bind(this), false);
  }
}


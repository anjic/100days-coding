/**
 * Created by Venkatesh on 7/19/2017.
 */
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Store } from '@ngrx/store';
import { State, geDataPAcState } from '../../../../../reducers';
import { UpdateDataPacAction, GetDataPACAction } from '../../../../../actions/hardware.actions';
import { SetISEId } from '../../../../../actions/ise-management.actions';
import { XioAlertComponent } from '../../../../../theme';
import { MdDialog } from '@angular/material';
import { Datapac } from '../../../../../ise/models/datapac';


@Component({
  selector: 'app-opendatapac',
  templateUrl: './opendatapac.component.html',
  styleUrls: ['./opendatapac.component.scss']
})
export class OpendatapacComponent implements OnInit, OnDestroy {

  public dataPac_identify: Array<any>;
  public dataPacList: Array<Datapac>;
  public ise_id;
  public loading_stack;
  public dataPacList$;

  /**
  * @param {ActivatedRoute} activatedRoute
  * @param {MdDialog} dialog
  * @param {Store<State>} store
  */
  constructor(public activatedRoute: ActivatedRoute,
              public dialog: MdDialog,
              public store: Store<State>) {

  this.dataPac_identify = [];
  this.dataPacList = [];
  this.loading_stack = {
    hardinfo_details: false,
    hardinfo_details_text: 'Loading.....'
  };
  }

  ngOnInit() {

    this.loading_stack.hardinfo_details = true;
    this.activatedRoute.parent.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetDataPACAction(this.ise_id));
     });


      /**
      * Desc : Used for getting Datapac details on load when component
      *        gets initialized.
      * Store State Name : geDataPAcState
      */

      this.dataPacList$ = this.store.select(geDataPAcState).subscribe(
        (data: Array<Datapac>) => {
            this.loading_stack.hardinfo_details = false;
            this.dataPac_identify = [];
            for (let dataPac of data) {
                let d = {
                  value: true,
                  loading: false
                };
                if (dataPac['led']['_attr']['string'] === 'disabled') {
                  d.value = false;
                }
                this.dataPac_identify.push(d);
            }
            this.dataPacList = data;
      }, error => { 
            this.catchError(error);        
      });
  }

  /**
  * Desc : change event to update Datapac Identify
  * @namespace xio.OpendatapacComponent
  * @method identifyFans
  * @param {Number} pos
  * @param {Number} id
  * @return {void}
  **/

  identifyDataPac(pos: number, id: number) {

    let data = { led: 'enabled' };
    if (!this.dataPac_identify[pos]['value']) {
      data['led'] = 'disabled';
    }

    this.dataPac_identify[pos]['loading'] = true;
    this.store.dispatch(new UpdateDataPacAction({
      ise_id: this.ise_id,
      id: id,
      data: data,
      cb: (success, error ) => {

        if (!error) {
          this.dataPac_identify[pos]['loading'] = false;
        } else {
          this.dataPac_identify[pos]['loading'] = false;
        }
      }
    }));
  }

  /**
  * Desc : Change particular status color
  * @namespace xio.OpendatapacComponent
  * @method statusClass
  * @param {String} status
  * @return {String}
  **/

  statusClass(status) {
    return (status === 'Needs Service' ||
            status === 'Non-Operational') ?  'ise_red' : '';
  }

   /**
   * Desc : Change toolbar color for particular status 
   * @namespace xio.OpendatapacComponent
   * @method toolBarClass
   * @param {String} status
   * @return {void}
   **/

  toolBarClass(status) {
    return (status === 'Non-Operational') ? 'toolbar_red' : 'toolbar_green';
  }

  /**
   * Desc : catching Error and Displaying in popup
   * @namespace xio.OpendatapacComponent
   * @method catchError
   * @param {any} error
   * @return {void}
   **/

  catchError (error) {

    let err_msg = (error.json !== '' || error.json !== undefined
                  || error.json !== null) ? error.json() : '';

    let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'OpenDataPac';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             err_msg.result.error.message :
                                             'Bad Request';
  }

  ngOnDestroy() {
    if (this.dataPacList$) {
      this.dataPacList$.unsubscribe();
    }
    // Un binding listeners
    window.removeEventListener('change', this.identifyDataPac.bind(this), false);
  }



}

/**
 * Created by Venkatesh on 7/19/2017.
 */
import { Component, OnInit, OnDestroy } from '@angular/core';
import { SnackbarService } from '../../../../../theme/services/snackbar.service';
import { MdDialog } from '@angular/material';
import { XioAlertComponent, XioProgressComponent } from '../../../../../theme';
import { ActivatedRoute, Router } from '@angular/router';
import { Store } from '@ngrx/store';
import { State, getControllerListState } from '../../../../../reducers/';
import {
  GetAllControllersAction,
  UpdateMRCAction,
  UpdateSpeedAction,
  UpdateFcPortSpeedAction
} from '../../../../../actions/hardware.actions';
import { SetISEId } from '../../../../../actions/ise-management.actions';
import { Controller } from '../../../../../ise/models/controllers';



@Component({
  selector: 'app-mrc',
  templateUrl: './mrc.component.html',
  styleUrls: ['./mrc.component.scss']
})
export class MrcComponent implements OnInit, OnDestroy {

  public controllers_identify: Array<any>;
  public controllersList: Array<Controller>;
  public ise_id;
  public loading_stack;
  public fcPortSpeed;
  public fcPort;
  public interval_id;
  public allControllers$;


  /**
  * @param {MdDialog} dialog
  * @param {SnackbarService} snackbarService
  * @param {ActivatedRoute} activatedRoute
  * @param {Router} router
  * @param {Store<State>} store
  */

  constructor(public mdDialog: MdDialog,
              public snackBarService: SnackbarService,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public store: Store<State>) {

    this.controllersList = [];
    this.controllers_identify = [];

    this.loading_stack = {
      hardinfo_details: false,
      hardinfo_details_text: 'Loading.....'
    };
    this.fcPort = {
      loading: false
    };
  }

  ngOnInit() {

    this.loading_stack.hardinfo_details = true;
    this.activatedRoute.parent.parent.params.subscribe(params => {

      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetAllControllersAction({
        ise_id: this.ise_id,
        cb: (success, error) => {
          if (!error) {

            /**
            * Desc : Used for getting Mrc details on load when component
            *        gets initialized.
            * Store State Name : getControllerListState
            */

            this.allControllers$ = this.store.select(getControllerListState).subscribe(
              (data: Array<Controller>) => {
                this.loading_stack.hardinfo_details = false;
                this.controllers_identify = [];
                let speed_list = [];
                for (let controller of data) {
                  let e = {
                    value: true,
                    loading: false
                  };

                  if (controller['led']['_attr']['string'] === 'disabled') {
                    e.value = false;
                  }

                  this.controllers_identify.push(e);
                  for (let fcPort of controller.fcports.fcports) {
                    fcPort.editFlag = false;
                    speed_list.push(fcPort.speed);
                  }

                  let unique_speed = speed_list.filter((v, i, a) => a.indexOf(v) === i);
                  this.fcPortSpeed = unique_speed.length === 1 ? '' + unique_speed[0] : 'auto';
                }
                this.controllersList = data;

              }, _error => {
                let title = 'Controller';
                this.catchError(_error, title);
              });
          } else {
            let title = '';
            this.catchError(error, title);
          }
        }
      }));
    });
  }


  /**
  * Desc : change event to update Mrc Identify
  * @namespace xio.MrcComponent
  * @method identifyFans
  * @param {Number} pos
  * @param {Number} id
  * @return {void}
  **/


  identifyMRC(pos: number, id: number) {
    let data = { led: 'enabled' };

    if (!this.controllers_identify[pos]['value']) {
      data['led'] = 'disabled';
    }
    this.controllers_identify[pos]['loading'] = true;
    this.store.dispatch(new UpdateMRCAction({
      ise_id: this.ise_id,
      id: id,
      data: data,
      cb: (succes, error) => {
        if (!error) {
          this.controllers_identify[pos]['loading'] = false;
        } else {
          this.controllers_identify[pos]['loading'] = false;
        }
      }
    }));
  }

  /**
  * Desc :Button click event to update Fcportspeed
  * @namespace xio.MrcComponent
  * @method onSave
  * @return {void}
  **/

  onSave() {
    let data = {
      fcportspeed: this.fcPortSpeed
    };

    this.fcPort['loading'] = true;
    this.store.dispatch(new UpdateSpeedAction({
      ise_id: this.ise_id,
      data: data,
      cb : (success, error) => {

        if (!error) {
          this.snackBarService.toastMe('FCPortspeed Updated Successfully', 2000);
        } else {

          let err_msg = error.json();
          if (err_msg.result.error.status_code === 504) {
            let count = 0;

            // Retry for 4 time with 1 second interval .
            this.interval_id = setInterval(() => {

              if (data['fcportspeed'] === this.getFcPort()) {
                clearInterval(this.interval_id);
                this.fcPort['loading'] = false;
                this.snackBarService.toastMe('FCPortspeed Updated Successfully', 2000);
              }
              count += 1;
              if (count === 4) {
                clearInterval(this.interval_id);
                this.fcPort['loading'] = false;
                count = 0;
              }
            }, 10000);
          } else {
            this.fcPort['loading'] = false;
            let title = 'FCPortSpeed';
            this.catchError(error, title);
          }
        }
      }
    }));
  }


  /**
  * Desc : To get Fcportspeed data
  * @namespace xio.MrcComponent
  * @method getFcPort
  * @return {void}
  **/

  getFcPort() {
    this.allControllers$ = this.store.select(getControllerListState).subscribe(
      data => {

        this.controllersList = data;
        let speed_list = [];
        for (let controller of this.controllersList) {
          for (let fcPort of controller.fcports.fcports) {
            speed_list.push(fcPort.speed);
          }
          let unique_speed = speed_list.filter((v, i, a) => a.indexOf(v) === i);
          this.fcPortSpeed = unique_speed.length === 1 ? '' + unique_speed[0] : 'auto';
        }
      });

    let payLoad = {
      ise_id: this.ise_id
    };

    this.store.dispatch(new GetAllControllersAction(payLoad));
    return this.fcPortSpeed;
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
  * Desc : Click event to toggle
  * @namespace xio.FansComponent
  * @method toggle
  * @param {Object} fcObj
  * @return {void}
  **/

  toggle(fcObj) {
    fcObj.editFlag = true;
    // This loop is for updating speed
    for (let controller of this.controllersList) {
      for (let fcPort of controller.fcports.fcports) {
        if (fcPort.id === fcObj.id) {
            fcPort.speed = fcObj.speed;
            return true;
        }
      }
    }
  }


  /**
  * Desc :Button click event to update particular Fcportspeed
  * @namespace xio.MrcComponent
  * @method onUpdate
  * @param {Object} fcObj
  * @return {void}
  **/

  onUpdate(fcObj) {

    let data = {
      fcportspeed: fcObj['speed'],
      id: fcObj['id']
    };

    let progressRef = this.mdDialog.open(XioProgressComponent, {disableClose: true});
        progressRef.componentInstance.progress_data = 'processing';


    this.store.dispatch(new UpdateFcPortSpeedAction({
      ise_id : this.ise_id,
      data : data,
      cb : (success, error) => {
        if (!error) {

          for (let controller of this.controllersList) {
            for (let fcPort of controller.fcports.fcports) {

              if (fcPort.id === fcObj.id) {
                progressRef.close();
                this.snackBarService.toastMe('FC Port ' + fcObj.id + ' Updated successfully', 2000);
                fcPort.editFlag = false;
              }
            }
          }
        } else {

          progressRef.close();
          let title = 'FCPortSpeed';
          this.catchError(error, title);
        }

      }

    }));
  }

   /**
   * Desc : Change toolbar color for particular status 
   * @namespace xio.MrcComponent
   * @method toolBarClass
   * @param {String} status
   * @return {void}
   **/

  toolBarClass(status) {
    return (status === 'Non-Operational') ? 'toolbar_red' : 'toolbar_green';
  }

  /**
   * Desc : catching Error and Displaying in popup
   * @namespace xio.MrcComponent
   * @method catchError
   * @param {any} error
   * @return {void}
   **/

  catchError(error , title) {

    if (error.status === 401) {
      let path = '/ise/' + this.ise_id + '/set-password/';
      this.router.navigate([path]);
    } else {
      let err_msg = (error.json !== '' || error.json !== undefined
                    || error.json !== null) ? error.json() : '';
      
      let alertRef = this.mdDialog.open(XioAlertComponent, { disableClose: true });
          alertRef.componentInstance.title = title;
          alertRef.componentInstance.message = err_msg !== '' ?
                                               err_msg.result.error.message :
                                               'Bad Request';
    }
  }


  ngOnDestroy() {
    if (this.allControllers$) {
      this.allControllers$.unsubscribe();
    }
    // Unbinding listeners
    window.removeEventListener('click', this.onUpdate.bind(this), false);
    window.removeEventListener('click', this.onSave.bind(this), false);
    window.removeEventListener('click', this.toggle.bind(this), false);
    window.removeEventListener('change', this.identifyMRC.bind(this), false);


  }

}

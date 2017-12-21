/**
 * Created by Venkatesh on 7/19/2017.
 */
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MdDialog } from '@angular/material';
import { XioProgressComponent } from './../../../../../theme/xio-progress/xio-progress.component';
import { XioAlertComponent } from './../../../../../theme/xio-alert/xio-alert.component';
import { SnackbarService } from './../../../../../theme/services/snackbar.service';
import { Store } from '@ngrx/store';
import { State, geNetworkState } from '../../../../../reducers/';
import { FormGroup, FormArray, FormBuilder, Validators } from '@angular/forms';
import { GetNetworkAction, UpdateNetworkAction } from '../../../../../actions/hardware.actions';
import { SetISEId } from '../../../../../actions/ise-management.actions';
import { Network } from '../../../../../ise/models/network';
import { CommonUtil } from '../../../../../common/utils/CommonUtil';


@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.scss']
})
export class NetworkComponent extends CommonUtil implements OnInit, OnDestroy {

  public networkForm: FormGroup;
  public port_list: Array<any>;
  public DNS_list: Array<Network>;
  public ise_id;
  public network_identify;
  public loading_stack;
  public list$;

  /**
  * @param {ActivatedRoute} activatedRoute
  * @param {FormBuilder} formBuilder
  * @param {MdDialog} dialog
  * @param {SnackbarService} snackbarService
  * @param {Store<State>} store
  */

  constructor(public activatedRoute: ActivatedRoute,
              public formBuilder: FormBuilder,
              public mdDialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
    super();
    this.DNS_list = [];
    this.port_list = [];

    this.loading_stack = {
      hardinfo_details: false,
      hardinfo_details_text: 'Loading.....'
    };
    this.network_identify = {
      dhcp: true,
      loading: false
    };
  }

  ngOnInit() {
    this.networkForm = this.formBuilder.group({
      domainserver: ['', [Validators.pattern(/^(?!.*[._]{2})[a-zA-Z0-9.-]+[a-zA-Z0-9.-]+$/)]],
      dns_nameserver1: ['', [Validators.pattern((/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/))]],
      dns_nameserver2: ['', [Validators.pattern((/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/))]],
      dhcp: [''],
      network: this.formBuilder.array([

      ])
    });

    this.loading_stack.hardinfo_details = true;
    this.activatedRoute.parent.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetNetworkAction(params['ise_id']));


    /**
    * Desc : Used for getting network details on load when component
    *        gets initialized.
    * Store State Name : geNetworkState
    */

      let counter = 0;
      this.list$ = this.store.select(geNetworkState).subscribe(
        (data: Array<Network>) => {

          counter++;
          this.loading_stack.hardinfo_details = false;
          this.DNS_list = data;
          this.setDNSData(data);

          if (data && data['ports']) {
            if (data['ports'].hasOwnProperty('ports') && counter === 2) {
              counter = 0;
              this.port_list = data['ports'].ports;
              this.addNetwork(this.port_list);
            }

            if (data['ports'].hasOwnProperty('port') && counter === 2) {
              counter = 0;
              this.port_list = [data['ports'].port];
              this.addNetwork(this.port_list);
            }

            this.network_identify.dhcp =
                            this.DNS_list['dhcp']['_attr']['string'] === 'disabled'
                            ? false
                            : true;

          }
        }, error => {
            this.catchError(error);
        });
    });
  }


  /**
  * Desc :
  * @namespace xio.NetworkComponent
  * @method setDNSData
  * @param {Object} data
  * @return {void}
  **/

  setDNSData(data) {
    if (data && data.dns) {

      if (data.dns.domainserver === 'String not found') {
        this.networkForm['controls']['dns_nameserver1'].setValue('');
      } else {
        this.networkForm['controls']['domainserver'].setValue(data.dns.domainserver);
      }

      if (data && data.dns && data.dns.nameservers) {
        if (data.dns.nameservers[0] === 'String not found') {
          this.networkForm['controls']['dns_nameserver1'].setValue('');
        }else {
          this.networkForm['controls']['dns_nameserver1'].setValue(data.dns.nameservers[0]);
        }
        if (data.dns.nameservers[1] === 'String not found') {
          this.networkForm['controls']['dns_nameserver2'].setValue('');
        }else {
          this.networkForm['controls']['dns_nameserver2'].setValue(data.dns.nameservers[1]);
        }

      }
    }
  }

  /*
  Declaration of Formcontrols
  */
  initNetwork(port) {

    return this.formBuilder.group({
      ipaddress: [port.ipaddress, [Validators.required,
                                   Validators.pattern((/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/))]],
      ipmask: [port.ipmask, []],
      gateway: [port.gateway, []]
    });

  }

  /*
  This method used to add Formcontrols
  */
  addNetwork(portList) {
    let control = <FormArray>this.networkForm.controls['network'];
    for (let i = 0; i < portList.length; i++) {
      control.push(this.initNetwork(portList[i]));
    }
  }


  /**
  * Desc : change event to set controls value
  * @namespace xio.NetworkComponent
  * @method dhcpChange
  * @return {void}
  **/


  dhcpChange() {

    if (this.networkForm['controls']['dhcp'].value) {
        this.networkForm.controls.network['controls'][0]['controls']['ipaddress'].disable();
        this.networkForm.controls.network['controls'][0]['controls']['ipmask'].disable();
        this.networkForm.controls.network['controls'][0]['controls']['gateway'].disable();
        this.networkForm.controls.network['controls'][1]['controls']['ipaddress'].disable();
        this.networkForm.controls.network['controls'][1]['controls']['ipmask'].disable();
        this.networkForm.controls.network['controls'][1]['controls']['gateway'].disable();
        this.networkForm['controls']['domainserver'].disable();
        this.networkForm['controls']['dns_nameserver1'].disable();
        this.networkForm['controls']['dns_nameserver2'].disable();
        this.networkForm.markAsUntouched();
    } else {
        this.networkForm.controls.network['controls'][0]['controls']['ipaddress'].enable();
        this.networkForm.controls.network['controls'][0]['controls']['ipmask'].enable();
        this.networkForm.controls.network['controls'][0]['controls']['gateway'].enable();
        this.networkForm.controls.network['controls'][1]['controls']['ipaddress'].enable();
        this.networkForm.controls.network['controls'][1]['controls']['ipmask'].enable();
        this.networkForm.controls.network['controls'][1]['controls']['gateway'].enable();
        this.networkForm['controls']['domainserver'].enable();
        this.networkForm['controls']['dns_nameserver1'].enable();
        this.networkForm['controls']['dns_nameserver2'].enable();
    }

  }

  /**
  * Desc : Click event to toggle
  * @namespace xio.FansComponent
  * @method toogleForm
  * @param {Object} data
  * @return {void}
  **/

  toogleForm(data) {
    if (data === 'enabled') {
      this.network_identify.dhcp = !this.network_identify.dhcp;
    }
  }

  /**
  * Desc : Button click event to update network details
  * @namespace xio.NetworkComponent
  * @method onSubmit
  * @return {void}
  **/

  onSubmit() {

    let progressRef = this.mdDialog.open(XioProgressComponent, { disableClose: true }),
        progress_data = 'processing';
        progressRef.componentInstance.progress_data = progress_data;
    let data = this.getDirtyValues(this.networkForm);
        data['dhcp'] = (data['dhcp']) ? 'enabled' : 'disabled';
    let payLoad = {
          dhcp: '',
          network: [],
          domainserver: '',
          nameserver: []
    };
    payLoad['dhcp'] = data['dhcp'];
    payLoad['network'] = data['network'];
    payLoad['domainserver'] = data['domainserver'];

    if (data['dns_nameserver1'] !== '' &&
        data['dns_nameserver1'] !== null &&
        data['dns_nameserver1'] !== undefined) {
        payLoad['nameserver'][0] = data['dns_nameserver1'];
    } else {
        payLoad['nameserver'][0] = this.networkForm['controls']['dns_nameserver1'].value;
    }

    if (data['dns_nameserver2'] !== '' &&
        data['dns_nameserver2'] !== null &&
        data['dns_nameserver2'] !== undefined) {
        payLoad['nameserver'][1] = data['dns_nameserver2'];
    } else {
        payLoad['nameserver'][1] = this.networkForm['controls']['dns_nameserver2'].value;
    }


    this.store.dispatch(new UpdateNetworkAction({
      ise_id: this.ise_id,
      data: payLoad,
      cb: (success, error) => {
        if (!error) {
          progressRef.close();
          this.toogleForm(data['dhcp']);
          this.snackbarService.toastMe('Network Settings Updated Successfully', 2000);
          this.store.dispatch(new GetNetworkAction(this.ise_id));
          this.networkForm.markAsPristine();
          this.networkForm.markAsUntouched();
        } else {
          progressRef.close();
          this.catchError(error);
          
        }
      }
    }));
  }

  /**
   * Desc : catching Error and Displaying in popup
   * @namespace xio.NetworkComponent
   * @method catchError
   * @param {any} error
   * @return {void}
   **/


  catchError (error) {

    let err_msg = (error.json !== '' || error.json !== undefined
                  || error.json !== null) ? error.json() : '';

    let alertRef = this.mdDialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'Network';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             err_msg.result.error.message :
                                             'Bad Request';
  }
  ngOnDestroy() {
    if (this.list$) {
      this.list$.unsubscribe();
    }
    // Un binding listeners
    window.removeEventListener('click', this.toogleForm.bind(this), false);
    window.removeEventListener('click', this.onSubmit.bind(this), false);
    window.removeEventListener('change', this.dhcpChange.bind(this), false);

  }

}

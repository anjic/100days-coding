import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MdDialog } from '@angular/material';
import { XioAlertComponent, SnackbarService, MenuContentService, XioProgressComponent } from './../../../theme/';
import { SanGroupUtil } from '../../../common/utils/SanGroupUtil';
import { getSanGroupLst, getIseDiscovery, State } from '../../../reducers';
import { Store } from '@ngrx/store';
import { GetAllAction } from '../../../actions/sangroup.action';
import { Observable } from 'rxjs/Observable';
import { AddISE, GetDiscovery } from '../../../actions/ise-management.actions';
import { GetMenuAction } from '../../../actions/menu.action';
import { SANGroup } from '../../../san-group/models/san-group';

@Component({
  selector: 'app-ise-discover',
  templateUrl: './ise-discover.component.html',
  styleUrls: ['./ise-discover.component.scss'],

})
export class IseDiscoverComponent extends SanGroupUtil implements OnInit, OnDestroy {
  public findForm: FormGroup;
  public discoveryForm: FormGroup;
  public discovery_detail: any;
  public sangroup_loaded: Boolean = false;
  public sangroup_list: any = [];
  public sanGroup$;
  public selected_sgLst = [];

  constructor(public fb: FormBuilder,
    public router: Router,
    public dialog: MdDialog,
    public snackbarService: SnackbarService,
    public store: Store<State>) {
    super();
    this.discovery_detail = '';
  }

  ngOnInit() {
    let _self = this;
    _self.sangroup_loaded = true;
    this.findForm = this.fb.group({
      primary_ip: ['', [Validators.required]],
      user_name: ['administrator', Validators.required,
      ],
      user_password: ['administrator', Validators.required],
    }, { validator: this.validateIseIP('primary_ip') });

    this.discoveryForm = this.fb.group({
      ise_name: [''],
      user_name: [''],
      user_password: [''],
      sg: this.fb.array([]),
      id: [''],
      prefered_ise: [''],
      contactname: ['', [Validators.maxLength(60),
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      address: ['', [Validators.maxLength(60)]],
      location: ['',  [Validators.maxLength(32)]],
      contactemail: ['',
        [Validators.pattern(/^(([^<>()\[\]\\.,;:\s@']+(\.[^<>()\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/),
        ]],
      contactphone: ['',[Validators.maxLength(16)]],
      sangroup_name: ['', [Validators.required,
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      comment: [''],
    });

    this.sanGroup$ = this.store.select(getSanGroupLst).subscribe(
      (data: Array<SANGroup>) => {
        if (!this.isEmpty(data)) {
          _self.sangroup_loaded = true;
          _self.discoveryForm['controls']['sg'] = this.fb.array([]);
          for (let i = 0; i < data.length; i++) {
              let v = data[i]['sangroup_id'];
              let lbl = data[i]['sangroup_name'];
              _self.addSG(v, lbl, 'sg', false);
          }
         _self.sangroup_list = data;
        }
      });
  }
   /**
   * on ISE Discover Selecting SanGroup 
   * @namespace xio.IseDiscoverComponent
   * @method sanCheckBoxChange
   * @params {any}event
   */
  sanCheckBoxChange(event) {
    this.sangroup_list.forEach((sanGroup) => {
      if (sanGroup.sangroup_id == event.source.value) {
        sanGroup['selected'] = event.checked;
      }
    });
  }
  
 

  /**
   * on ISE Discover getMenuContent all ise and sgs data
   * @namespace xio.IseDiscoverComponent
   * @method onDiscover
   * @return {void}
   */
  onDiscover() {
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'processing';
    this.store.dispatch(new GetDiscovery ({
      data: this.findForm.value,
      cb: (response, error) => {
        if (!error) {
          progressRef.close();
          this.discovery_detail = response.result.response.data.array;
          this.discoveryForm['controls']['ise_name'].setValue(this.discovery_detail.name);
          this.discoveryForm['controls']['user_name'].setValue(this.findForm.value.user_name);
          this.discoveryForm['controls']['user_password'].setValue(this.findForm.value.user_password);
          this.discoveryForm['controls']['contactname'].setValue(this.discovery_detail.contactname);
          this.discoveryForm['controls']['location'].setValue(this.discovery_detail.location);
          this.discoveryForm['controls']['address'].setValue(this.discovery_detail.address);
          this.discoveryForm['controls']['contactemail'].setValue(this.discovery_detail.contactemail);
          this.discoveryForm['controls']['contactphone'].setValue(this.discovery_detail.contactphone);
        } else {
          progressRef.close();
          this.catchError(error); 
        }
        if (error) {
           progressRef.close();
           this.catchError(error);
        }
      }
    }));
  
  }

  /**
   * submit add ISE
   * @namespace xio.IseDiscoverComponent
   * @method onSubmitData
   * @return {void}
   */
  onSubmitData() {
    let selected_sg = this.getSelectedSanGroup(),
      data = {
        array: this.discovery_detail,
        sangroup_id: selected_sg,
        string_data: JSON.stringify(this.discovery_detail)
      },
      progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
       Object.keys(this.discoveryForm.value).forEach((discovery) => {
       data[discovery] = this.discoveryForm.value[discovery];
    });

    progressRef.componentInstance.progress_data = 'processing';
    this.store.dispatch(new AddISE({
      data: data,
      cb: (response, error) => {
        if (response) {
          progressRef.close();
          this.snackbarService.toastMe('ISE created Successfully', 2000);
          this.store.dispatch(new GetMenuAction({}));
          this.goToIseList();
        } else if (error) {
          progressRef.close();
          setTimeout(() => {
           this.catchError(error);
          }, 500);
        }
      }
    }));
  
  }

   /**
    * Validating Domain name and Ip
    * @namespace xio.IseDiscoverComponent
    * @method validateIseIP
    * @return {void}
    */

    validateIseIP(primary_ipkey) {
      return (group: FormGroup): { [key: string]: any } => {
        let ip_domain_value = group.root['controls'][primary_ipkey].value;
        let ip_addr_first_char = parseInt(ip_domain_value.charAt(0), 10);
        const domainPattern = /^(?!.*[._]{2})[a-zA-Z0-9.-]+[a-zA-Z0-9.-]+$/;
        const regexIP = /^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/;
  
        if (ip_domain_value.length !== 0) {
          if (ip_addr_first_char) {
            if (regexIP.test(ip_domain_value)) {
              return null;
            }else {
              return {
                regexIP: {
                  valid: false
                }
              };
            }
          }else {
            if (domainPattern.test(ip_domain_value)) {
              return null;
            }else {
              return {
                regexIP: {
                  valid: false
                }
              };
            }
          }
        }
      };
    }


  /**
    * Get Selected San Group
    * @namespace xio.IseDiscoverComponent
    * @method getSelectedSanGroup
    * @return {void}
    */
  getSelectedSanGroup() {
    return this.sangroup_list.map((sanselect) => {
      if (sanselect.selected) {
        return sanselect.sangroup_id;
      }
    }).filter(Number);
  }

   /**
    * Naviagtion of path
    * @namespace xio.IseDiscoverComponent
    * @method goToIseList
    */
  goToIseList() {
    this.router.navigate(['/ise']);
  }

    /**
    * Catching Error
    * @namespace xio.IseDiscoverComponent
    * @method catchError
    */

  catchError(error) {
      
    let err_msg = (error.json !== '' || error.json !== undefined
                                     || error.json !== null) ? error.json : '';
    let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'ISE';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             'Please try again, giving request': 
                                             err_msg.result.error.message;
  }

  ngOnDestroy() {
    if ( this.sanGroup$ ) {
      this.sanGroup$.unsubscribe();
    }
    // Unbinding Event Listeners
    window.removeEventListener('click', this.goToIseList.bind(this), false); 
  }
}
import { Component, OnInit, Output, EventEmitter, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { IseService, SubscriptionService } from './../../../services/';
import { MdDialog } from '@angular/material';
import { SnackbarService, XioAlertComponent, XioProgressComponent } from './../../../../theme/';
import { AddSubscription, UpdateSubscription } from '../../../../actions/ise-settings.actions';
import { Store } from '@ngrx/store';
import { State, getISEInfo } from '../../../../reducers/';
import { GetISEInfo } from "../../../../actions/ise-management.actions";

@Component({
  selector: 'app-subscription-form',
  templateUrl: './subscription-form.component.html',
  styleUrls: ['./subscription-form.component.scss']
})
export class SubscriptionFormComponent implements OnInit, OnDestroy {
  @Output() showSubList = new EventEmitter();

  public subscriptionForm: FormGroup;
  public id;
  public ise_id;
  public isAddForm: boolean;
  public ise_details;
  public ise_ip;
  public type;
  public port;
  public interval;
  public form_title: any;
  public iseInfo$;
  public isEdit = false;

  constructor(public fb: FormBuilder,
    public route: ActivatedRoute,
    public router: Router,
    public dialog: MdDialog,
    public sub: SubscriptionService,
    public ises: IseService,
    public snackbarService: SnackbarService,
    public store: Store<State>) {
  }

  ngOnInit() {
    this.form_title = 'Create Subscriptions';
    this.port = 443;
    this.interval = 1440;
    this.subscriptionForm = this.fb.group({
      storage_system: [''],
      type: ['', Validators.required],
      id: ['', [Validators.required, Validators.pattern(/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*|([A-za-z0-9])$/)]],
      port_number: [''],
      setting: true,
      interval: [''],
      proxy: [''],
      proxyusername: [''],
      proxyaddress: [''],
      proxypassword: [''],
    });

    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.iseInfo$ = this.store.select(getISEInfo).subscribe(
        data => {
          if (data) {
            this.ise_details = data;
            this.ise_ip = data['ip_primary'];
            this.subscriptionForm['controls']['storage_system'].setValue(this.ise_ip);
            this.subscriptionForm['controls']['storage_system'].disable();
          }
        }
      );
      this.route.params.subscribe(params => {
        this.id = params['id'];
        this.type = params['type'];
        if (this.id) {
          this.isEdit = true;
          this.form_title = 'Edit Subscriptions';
          this.editSubscription();
        } else {
          this.isEdit = false;
        }
        this.subscriptionForm['controls']['port_number'].setValue(this.port);
        this.subscriptionForm['controls']['proxy'].setValue(('disabled') ? false : true);
      });
      let payLoad = {
        ise_id: this.ise_id
      }
      this.store.dispatch(new GetISEInfo(payLoad));

    });
  }

  onSubmit() {
    let data = this.subscriptionForm.value;
    console.log(data);
    data['setting'] = (data['setting']) ? 'enabled' : 'disabled';
    data['proxy'] = (data['proxy']) ? 'enabled' : 'disabled';
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    let progress_data = 'processing';
    progressRef.componentInstance.progress_data = progress_data;
    this.store.dispatch(new AddSubscription({
      data: data,
      ise_id: this.ise_id,
      cb: (data, err) => {
        if (data) {
          progressRef.close();
          this.snackbarService.toastMe('Subscription added Successfully', 2000);
          this.showSubList.emit('cancel');
        }
        else if (err) {
          progressRef.close();
          let err_msg = err.json();
          let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
          alertRef.componentInstance.title = 'Subscriptions';
          alertRef.componentInstance.message = err_msg.result.error.message;
        }
      }
    }));
  }

  /**
   * getMenuContent subscription info for edit
   * @namespace xio.SubscriptionFormComponent
   * @method addSubscription
   * @return {void}
   */
  editSubscription() {
    this.sub.getSubscription(this.id, this.ise_id, this.type).subscribe(
      result => {
        let sub_data = result.subscriptions.subscription;
        if (sub_data['types']['type']) {
          this.subscriptionForm['controls']['id'].setValue(sub_data.id);
          this.subscriptionForm['controls']['setting'].setValue(sub_data.types.type.setting._attr.value !== '0');
          this.subscriptionForm['controls']['interval'].setValue(sub_data.interval);
          this.subscriptionForm['controls']['type'].setValue(sub_data.types.type._attr.name);
          this.subscriptionForm['controls']['type'].disable();
          this.subscriptionForm['controls']['proxy'].setValue(sub_data.types.type.proxy._attr.value !== '0');
          this.subscriptionForm['controls']['proxyaddress'].setValue(sub_data.types.type.proxyaddress);
          this.subscriptionForm['controls']['proxyusername'].setValue(sub_data.types.type.proxyusername);
          this.subscriptionForm['controls']['proxypassword'].setValue(sub_data.types.type.proxypassword);
          if (this.subscriptionForm['controls']['type'].value == 'alert') {
            this.subscriptionForm['controls']['interval'].disable();
          }
          else {
            this.subscriptionForm['controls']['interval'].enable();
          }
        }
        else if (sub_data['types']) {
          console.log(sub_data['types'])
          this.subscriptionForm['controls']['id'].setValue(sub_data.id);
          this.subscriptionForm['controls']['setting'].setValue(sub_data.types.setting._attr.value !== '0');
          this.subscriptionForm['controls']['interval'].setValue(sub_data.interval);
          this.subscriptionForm['controls']['type'].setValue(sub_data.types._attr.name);
          this.subscriptionForm['controls']['type'].disable();
          this.subscriptionForm['controls']['proxy'].setValue(sub_data.types.proxy._attr.value !== '0');
          this.subscriptionForm['controls']['proxyaddress'].setValue(sub_data.types.proxyaddress);
          this.subscriptionForm['controls']['proxyusername'].setValue(sub_data.types.proxyusername);
          this.subscriptionForm['controls']['proxypassword'].setValue(sub_data.types.proxypassword);
          if (this.subscriptionForm['controls']['type'].value == 'alert') {
            this.subscriptionForm['controls']['interval'].disable();
          }
          else {
            this.subscriptionForm['controls']['interval'].enable();
          }
        }
        this.subscriptionForm.markAsPristine();
        this.subscriptionForm.markAsUntouched();
      });
  }
  getDirtyValues(cg) {
    let dirtyValues = {};
    Object.keys(cg['controls']).forEach((c) => {
      let currentControl = cg['controls'][c];
      if (currentControl.dirty) {
        if (currentControl['controls'])
          dirtyValues[c] = this.getDirtyValues(currentControl);
        else
          dirtyValues[c] = currentControl.value;
      }
    });
    return dirtyValues;
  }

  /**
   * update subscription
   * @namespace xio.SubscriptionFormComponent
   * @method onUpdateSubmit
   * @return {void}
   */
  onUpdateSubmit() {

    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Processing';
    let data = this.getDirtyValues(this.subscriptionForm);
    if (data.hasOwnProperty('setting')) {
      data['setting'] = data['setting'] ? 'enabled' : 'disabled';
    }
    if (data.hasOwnProperty('proxy')) {
      data['proxy'] = data['proxy'] ? 'enabled' : 'disabled';
    }
    console.log(this.type);
    let payLoad = {
      'id': this.id,
      'ise_id': this.ise_id,
      'data': data,
      'type': this.type,
    }
    console.log(payLoad);
    this.sub.updateSubscription(payLoad).subscribe(res => {
      progressRef.close();
      this.snackbarService.toastMe('Subscriptions Updated Successfully', 2000);
      this.router.navigate(['/ise/' + this.ise_id + '/settings/']);
    },
      err => {
        progressRef.close();
        let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'Subscriptions';
        alertRef.componentInstance.message = err.json().result.error.message;
      })

  }

  onTypechange() {
    if (this.subscriptionForm['controls']['type'].value == 'alert') {
      this.subscriptionForm['controls']['interval'].setValue(1440);
      this.subscriptionForm['controls']['interval'].disable();

    } else {
      this.subscriptionForm['controls']['interval'].setValue('');
      this.subscriptionForm['controls']['interval'].enable();

    }
  }

  oncancel() {
    this.showSubList.emit('cancel');
  }

  getFormElementVal(element_name: string) {
    const control = this.subscriptionForm['controls'][element_name];
    return control.value;
  }

  proxyChange() {
    if (this.subscriptionForm['controls']['proxy'].value) {
      this.subscriptionForm['controls']['proxyusername'].enable();
      this.subscriptionForm['controls']['proxyaddress'].enable();
      this.subscriptionForm['controls']['proxypassword'].enable();
    }
    else {
      this.subscriptionForm['controls']['proxyusername'].disable();
      this.subscriptionForm['controls']['proxyaddress'].disable();
      this.subscriptionForm['controls']['proxypassword'].disable();
    }
  }
  ngOnDestroy() {
    this.iseInfo$.unsubscribe();
  }
}


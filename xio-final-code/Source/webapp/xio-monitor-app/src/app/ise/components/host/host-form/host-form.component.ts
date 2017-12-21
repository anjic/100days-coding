import {Component, OnInit, Input, Output, EventEmitter, OnDestroy} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router, ActivatedRoute} from '@angular/router';
import {SangroupService} from '../../../../san-group/services/sangroup.service';
import {EndpointsService, StoragevolumeService, HostService} from './../../../services/';
import {MdDialog} from '@angular/material';
import {
  XioProgressComponent,
  XioAlertComponent,
  SnackbarService,
  XioDialogComponent,
  MenuContentService
} from './../../../../theme/';
import {HostComponentUtil} from '../../../../common/utils/host.component';

//REDUX
import {Store} from '@ngrx/store';
import {State, getHost, getSanGroupLst} from '../../../../reducers/';
import {Observable} from 'rxjs/Observable';
import {GetHostAction, HostReset} from "../../../../actions/hosts.actions";
import {GetAllAction} from "../../../../actions/sangroup.action";

@Component({
  selector: 'host-form',
  styleUrls: ['./host-form.component.scss'],
  templateUrl: './host-form.component.html'
})
export class HostFormComponent extends HostComponentUtil implements OnInit, OnDestroy {
  @Input() isVolume: boolean;
  @Input() isSangroup: boolean;
  @Output() isCreated = new EventEmitter();

  public hostsForm: FormGroup;
  public host_details: any;
  public form_title: any;
  public host_obs$;
  public vol_loading_stack: any;
  public selectedLun: object = {};
  public sanGroup$;


  constructor(public fb: FormBuilder,
              public hs: HostService,
              public eps: EndpointsService,
              public svs: StoragevolumeService,
              public sgs: SangroupService,
              public route: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public mcs: MenuContentService,
              public store: Store<State>) {
    super();
  }


  ngOnInit() {
    this.form_title = 'Create WWN Group';
    this.host_details = {
      id: '',
      ise_id: '',
      sg_id: '',
      ise_select_list: [],
      isHost: true,
      current_step: 1,
      active_tab: '',
      selectedIndex: 0,
      loading_stack: {
        endpoint: false,
        endpoint_text: 'Loading......'
      }
    };
    this.vol_loading_stack = {
      vol_list: false,
      vol_list_text: 'Loading.....'
    };

    this.hostsForm = this.fb.group({
      current_wwns: this.fb.array([]),
      available_wwns: this.fb.array([]),
      name: ['', [Validators.required,
        Validators.maxLength(64),
        Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      os: [''],
      comment: ['', [Validators.maxLength(60)]],
      id: [''],
      ise_id: [''],
      volumes: this.fb.array([])
    }, {validator: this.validateEnpoint});

    this.route.parent.params.subscribe(params => {
      if (!this.isSangroup) {
        this.host_details.ise_id = params['ise_id'];
        this.hostsForm['controls']['ise_id'].setValue(this.host_details.ise_id);
        this.getEndpoint();
        this.getVolumes();
      }

      this.route.params.subscribe(params => {
        if (params['host_id']) {
          this.form_title = 'Edit WWN Group';
          this.host_details.id = params['host_id'];
          this.editFormValue();
        }
        if (this.isSangroup && params['sg_id']) {
          this.host_details.sg_id = params['sg_id'];
          this.sanGroup$ = this.store.select(getSanGroupLst).subscribe(
            data => {
              if (data.length > 0) {
                data.forEach((san) => {
                  if(san['sangroup_id'] == this.host_details.sg_id) {
                    this.host_details.ise_select_list = san['ise'];
                  }
                });
              }
            }
          )
          //TODO Sangroup service
          // this.sgs.getSangroup({
          //   ise_id: this.host_details.sg_id
          // }).subscribe(
          //   res => {
          //     this.host_details.ise_select_list = res.ise;
          //   }
          // );
        }
      });
    });


  }

  /**
   * getMenuContent LUN service
   * @namespace xio.HostFormComponent
   * @method getAvailableLUN
   * @return {void}
   */
  getAvailableLUN() {
    for (let i = 1; i < 9999; i++) {
      if (this.host_details.available_lun) {
        this.host_details.available_lun.push(i);
      } else {
        this.host_details.available_lun = [i];
      }
    }
  }

  /**
   * getMenuContent EndPoint service
   * @namespace xio.HostFormComponent
   * @method getEndpoint
   * @return {void}
   */
  getEndpoint() {
    this.host_details.loading_stack.endpoint = true;
    this.eps.getAll(this.host_details.ise_id).subscribe(
      data => {
        this.host_details.loading_stack.endpoint = false;
        let sortWWNArr = [];

        this.host_details.loading_stack.endpoint = false;
        for (let ep of this.eps.endpoint_available_list) {
          sortWWNArr.push(ep.globalid);
        }

        //Sort need to be put
        sortWWNArr.sort();


        for (let ep of sortWWNArr) {
          // sortWWNArr.push(ep.globalid);
          
          this.addWWN(ep, 'available_wwns', false);}
      });
  }

  /**
   * UI - Update Volume info service
   * @namespace xio.HostFormComponent
   * @method getVolumes
   * @return {void}
   */

  getVolumes() {
    this.vol_loading_stack.vol_list = true;
    this.clearVolume();
    // this.getAvailableLUN();
    let payLoad ={
      ise_id :this.host_details.ise_id
    }
    this.svs.getAll(payLoad).subscribe(
      data => {

        let vl = this.svs.volume_list;
        // let lun_no = 1;

        for (let i = 0; i < vl.length; i++) {

          let v = vl[i].name;
          this.addVolume(v, 'volumes', false, 0);
        }
        this.vol_loading_stack.vol_list = false;
      });
  }

  lun(i: number) {
    let value = this.hostsForm['controls']['volumes']['controls'][i]['controls']['volume'].value;
    if (value) {
      let _lun = this.getLun();
      this.hostsForm['controls']['volumes']['controls'][i]['controls']['lun'].setValue(_lun);
      this.selectedLun[_lun] = this.hostsForm['controls']['volumes']['controls'][i]['controls']['lun'];
      console.log(this.hostsForm['controls']['volumes']['controls'][i]['controls']['lun']);
    } else {
      this.resetLunAvailable(this.hostsForm['controls']['volumes']['controls'][i]['controls']['lun'].value);
      this.hostsForm['controls']['volumes']['controls'][i]['controls']['lun'].setValue(0);
    }
  }

  getLun() {
    let maxVal = 9999;
    for (let i = 1; i <= maxVal; i++) {
      if (!this.selectedLun.hasOwnProperty(i)) {
        return i;
      }
    }
  }

  lunFocusIn(e) {
    console.log('focus in settings onChange ->>' + e.currentTarget.value);
    this.selectedLun['changing'] = {
      value: e.currentTarget.value,
      e: this.selectedLun[e.currentTarget.value]
    };
    delete this.selectedLun[e.currentTarget.value];
  }

  lunFocusOut(e) {
    if (this.selectedLun.hasOwnProperty('changing') && this.selectedLun['changing'].value != e.currentTarget.value) {
      console.log('focus out settings new value --> ' + e.currentTarget.value + ' from -->' + this.selectedLun['changing']);
      this.updateSelectedLun(e.currentTarget.value, e.currentTarget);
    }
    else {
      console.log('focus out settings old value itself --> ' + this.selectedLun['changing']);
      this.selectedLun[this.selectedLun['changing'].value] = this.selectedLun['changing'].e;
    }
    delete this.selectedLun['changing'];
  }

  updateSelectedLun(val: number, e = null) {
    if (this.selectedLun.hasOwnProperty(val)) {
      let _nextLun = this.getLun();
      this.selectedLun[_nextLun] = this.selectedLun[val];
      this.selectedLun[_nextLun].setValue(_nextLun);
      this.selectedLun[val] = this.hostsForm['controls'].volumes['controls'][+e.id];
    }
  }

  resetLunAvailable(val: number) {
    console.log('resetLunAvailable --> ' + val);
    delete this.selectedLun[val];
    // let i = 0;
    //
    // while (i < this.host_details.available_lun.length) {
    //   console.log(this.host_details.available_lun[i]);
    //
    //   if (this.host_details.available_lun[i] > val) {
    //
    //     break;
    //   }
    //
    //   i++;
    // }

    // this.host_details.available_lun.splice(i, 0, val);

    // console.log(this.host_details.available_lun);

  }


  /**
   * On ISE selection clear WWN, getMenuContent Endpoint's & volume Info
   * @namespace xio.HostFormComponent
   * @method onISESelectChange
   * @return {void}
   */
  onISESelectChange($event) {
    let ise_id = $event.value;
    this.host_details.ise_id = ise_id;
    if (ise_id) {
      this.clearWWN();
      this.getEndpoint();
      this.getVolumes();
    }
  }

  /**
   * Set Update Host Form values
   * @namespace xio.HostFormComponent
   * @method editFormValue
   * @return {void}
   */
  editFormValue() {

    let payLoad = {
      "ise_id": this.host_details.ise_id,
      "id": this.host_details.id
    }
    this.store.dispatch(new GetHostAction(payLoad));
    this.host_obs$ = this.store.select(getHost).subscribe(data => {
      if (!this.isEmptyObject(data)) {
        let host_data = data['result'].response.data.hosts.host;
        this.hostsForm['controls']['name'].setValue(host_data.name);
        this.hostsForm['controls']['os'].setValue(host_data.os);
        this.hostsForm['controls']['comment'].setValue(host_data.comment);
        this.hostsForm['controls']['id'].setValue(this.host_details.id);
        this.hostsForm['controls']['ise_id'].setValue(this.host_details.ise_id);
        let host_endpoints = [];
        if (host_data.endpoints.hasOwnProperty('endpoint')) {
          host_endpoints = [host_data.endpoints.endpoint];
        }
        if (host_data.endpoints.hasOwnProperty('endpoints')) {
          host_endpoints = host_data.endpoints.endpoints;
        }
        let sort_arr=[];
        for (let i = host_endpoints.length - 1; i >= 0; i--) {
            sort_arr.push(host_endpoints[i].globalid);
           }
          sort_arr.sort();
        for(let v of sort_arr ){  
          this.addWWN(v, 'current_wwns', true);
        }
      }
    }, error => {
      console.log(error);
    }, () => {
      console.log("finished");
    })
  }


  reset() {
    ['name', 'comment'].forEach((k) => {
      this.hostsForm['controls'][k].setValue('');
    });
    this.hostsForm['controls'].current_wwns = this.fb.array([]);
    this.hostsForm['controls'].available_wwns = this.fb.array([]);
    this.getEndpoint();
    this.hostsForm.markAsPristine();
    this.hostsForm.markAsUntouched();
  }

  /**
   * Create a New Host service
   * @namespace xio.HostFormComponent
   * @method onSubmit
   * @return {void}
   */
  onSubmit() {
    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    progressRef.componentInstance.progress_data = 'Processing';

    if (!this.isAvsilableWwn('available_wwns')) {
      let msg = 'Select The endpoint';
    }


    this.hs.addHosts(this.hostsForm.value).subscribe(
      data => {
        progressRef.close();
        if (this.isSangroup) {
          this.router.navigate(['san-group/' + this.host_details.sg_id + '/host/']);
        } else if (!this.isVolume) {
          this.snackbarService.toastMe('WWN Group created Successfully', 2000);

          this.goToHostList();
        } else {
          this.isCreated.emit();
        }
        this.store.dispatch(new GetAllAction({}));
        this.reset();
      },
      err => {
        progressRef.close();
        let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
        alertRef.componentInstance.title = 'WWN Group';
        alertRef.componentInstance.message = err.json().result.error.message;
      }
    );
  }

  /**
   * Host Edit form Update service
   * @namespace xio.HostFormComponent
   * @method onUpdateSubmit
   * @return {void}
   */
  onUpdateSubmit() {
    if (!this.isAvsilableWwn('available_wwns') && !this.isAvsilableWwn('current_wwns')) {
      let msg = 'Select The endpoint';
      return false;
    }
    let host_name = this.hostsForm.value['name']
    if(this.hostsForm['controls'].current_wwns.dirty){
      let dialogRef = this.dialog.open(XioDialogComponent);
      dialogRef.componentInstance.title = host_name;
      dialogRef.componentInstance.message = 'Modifications to the WWN Group will affect the Client Server. Are you sure you want to make these changes?';
      dialogRef.afterClosed().subscribe(result => {
       if (result == 'yes') {

              let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
              progressRef.componentInstance.progress_data = 'Processing';
              this.hs.updateHosts(this.hostsForm.value).subscribe(
              data => {
                progressRef.close();
                this.snackbarService.toastMe('WWN Group Updated Successfully', 2000);
                this.goToHostList();
                this.store.dispatch(new GetAllAction({}));
              },
              err => {
                progressRef.close();
                let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
                alertRef.componentInstance.title = 'WWN Group';
                alertRef.componentInstance.message = err.json().error.message;
              }
            );
          }
   })
}
  else{
        let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    progressRef.componentInstance.progress_data = 'Processing';
    this.hs.updateHosts(this.hostsForm.value).subscribe(
      data => {
        progressRef.close();
        this.snackbarService.toastMe('WWN Group Updated Successfully', 2000);
        this.goToHostList();
        this.store.dispatch(new GetAllAction({}));
      },
      err => {
        progressRef.close();
        let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
        alertRef.componentInstance.title = 'WWN Group';
        alertRef.componentInstance.message = err.json().error.message;
      }
    );

  }
  }

  /**
   * on Volume creation change tabs and getMenuContent volume info's
   * @namespace xio.HostFormComponent
   * @method isVolumeCreated
   * @return {void}
   */
  isVolumeCreated() {
    this.getVolumes();
    this.changeTab();
  }

  //TODO : Generalize for all serices to common
  isEmptyObject(obj) {
    return Object.keys(obj).length === 0;
  }

  ngOnDestroy() {
    this.store.dispatch(new HostReset());
    if (this.host_obs$)
      this.host_obs$.unsubscribe();
    if(this.sanGroup$)
      this.sanGroup$.unsubscribe();
  }
}

import { Component, OnInit, Input, Output, EventEmitter, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { IseService } from '../../../services/ise.service';
import { HostService } from '../../../services/host.service';
import { MdDialog } from '@angular/material';
import { XioProgressComponent, XioAlertComponent, SnackbarService } from './../../../../theme';
import { ISEVolumeUtil } from '../../../../common/utils/ISEVolumeUtil';
import { getAllPoolsState, getVolumeState, State } from '../../../../reducers/index';
import { Store } from '@ngrx/store';
import * as _ from 'lodash';
import { SetISEId } from '../../../../actions/ise-management.actions';

// Redux
import {
  GetVolumeDetailsAction, AddVolumeDetailsAction,
  UpdateVolumeDetailsAction, UpdateVolumeAllocationAction, VolumeReset
} from '../../../../actions/volume.actions';
import {GetAllPoolsAction} from '../../../../actions/pools.actions';

@Component({
  selector: 'app-volume-form',
  templateUrl: './volume-form.component.html',
  styleUrls: ['./volume-form.component.scss'],
})
export class VolumeFormComponent extends ISEVolumeUtil implements OnInit, OnDestroy {
  @Input() isHost: boolean;
  @Input() isHostIse: boolean;
  @Output() isCreated = new EventEmitter();

  public storagevolumeForm: FormGroup;
  public ise_id;
  public pools_list: any;
  public currentLUNArray: any;
  public hostAllocation = {
    allocated_host: [],
    allocated_id: [],
    allocated_lun: [],
    loaded: false,
    _hostLst: null
  };
  public volume_details_observer$;
  public pools_list$;
  public progressRef;
  public loading_stack: any;
  public volume_exceeding_count_msg: Object;


  public volume_details = {
    id: '',
    ise_id: '',
    isAddForm: false,
    isSelectHost: true,
    isSelectHostList: false,
    isAllocateEnable: false,
    isRaidEnable: true,
    wizard_step: 0,
    isVolume: true,
    size_change: false,
    selectedIndex: 0,
    form_title: 'Create Volume',
    loading_stack: {
      pool_data: false,
      pool_data_text: 'loading'
    }
  };

  constructor(public fb: FormBuilder,
              public hostService: HostService,
              public iseService: IseService,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public mdDialog: MdDialog,
              public snackBarService: SnackbarService,
              public store: Store<State>) {
    super();
    this.loading_stack = {
      host_list: false,
      host_list_text: 'Loading.....'
    };
  }

  resetAllocation() {
    this.hostAllocation.allocated_host = [];
    this.hostAllocation.allocated_id = [];
    this.hostAllocation.allocated_lun = [];
    this.hostAllocation.loaded = false;
  }

  ngOnInit() {
    this.resetAllocation();
    this.volume_details.isAddForm = true;
    this.storagevolumeForm = this.initForm();
    this.activatedRoute.parent.params.subscribe(params => {
      this.volume_details.ise_id = params['ise_id'];
      this.ise_id = params['ise_id'];
      if (this.isHostIse) {
          this.ise_id = this.isHostIse;
      }
      this.store.dispatch(new SetISEId(this.ise_id));
      this.activatedRoute.params.subscribe(childParams => {
        if (childParams['id']) {
          this.volume_details.id = childParams['id'];
          this.volume_details.form_title = 'Edit Volume';
          this.editFormValue();
        } else {
          this.isRaid();
          this.isallocatype();
        }
      });
      this.setPoolsDropdown();
      this.watchDisabled();
      this.likevolume();
    });
    this.chageWizard(1);
    this.chageSelectHostWizard(this.volume_details.isSelectHost, true);
    if (!this.volume_details.id) {
      this.setHostList();
    }
  }

  initForm() {
    return this.fb.group({
        size: ['1', this.getSizeValidator()],
        name: ['', this.getNameValidator()],
        writecache: [''],
        pool: [''],
        redundancy: ['5'],
        comment: ['', [Validators.maxLength(60)]],
        affinity: [''],
        alloctype: [true],
        quality_service: [''],
        IOPSmin: [
          {value: 0, disabled: true},
          [this.validatepattern(1, 50000, 'IOPSmin')]
        ],
        IOPSmax: [
          {value: 0, disabled: true},
          [this.validatepattern(10, 500000, 'IOPSmax')]
        ],
        IOPSburst: [
          {value: 0, disabled: true},
          [this.validatepattern(10, 500000, 'IOPSburst')]
        ],
        id: [''],
        host_list: this.fb.array([]),
        allocate_host_list: this.fb.array([]),
        create_like_volumes: [false],
        no_like_volumes: [
          {value: '1', disabled: true},
          [this.checkMultipleVolumes('no_like_volumes')]
        ],
        assign_host: [0],
        dedup: [true],
        host: [true],
      }, {validator: this.validateBurst('IOPSmin', 'IOPSmax', 'IOPSburst')}
    );
  }


  reset() {
    ['writecache', 'comment', 'affinity', 'id'].forEach((property) => {
      this.storagevolumeForm['controls'][property].setValue('');
    });
    this.storagevolumeForm['controls']['name'].setValue(' ');
    this.storagevolumeForm['controls']['size'].setValue('1');
    ['alloctype', 'dedup'].forEach((property) => {
      this.storagevolumeForm['controls'][property].setValue(true);
    });
    ['create_like_volumes', 'quality_service'].forEach((property) => {
      this.storagevolumeForm['controls'][property].setValue(false);
    });
    ['IOPSmin', 'IOPSmax', 'IOPSburst'].forEach((property) => {
      this.storagevolumeForm['controls'][property].setValue(0);
    });
    this.storagevolumeForm.markAsPristine();
    this.storagevolumeForm.markAsUntouched();
  }

  /**
   * Set ISE Host List
   * @namespace VolumeFormComponent
   * @method setHostList
   * @return {void}
   */
  setHostList() {
    this.removeHostItem();
    this.loading_stack.host_list = true;
    let payLoad = {
      ise_id: this.ise_id
    };
    this.hostService.getAll(payLoad).subscribe(data => {
        this.currentLUNArray = [];
        for (let i = this.hostService.host_list.length - 1, j = 0; i >= 0; i--, j++) {
             const v = this.hostService.host_list[i]['id'], lbl = this.hostService.host_list[i]['name'];
                       this.currentLUNArray[j] = _.difference(this.LUNSerial(), _.uniq(this.hostService.host_list[i]['lun']));
             let lunNo = this.currentLUNArray[j][0] === 0 ? this.currentLUNArray[j][1] : this.currentLUNArray[j][0];
                         this.addHostItem(lbl, 'host_list', false, lunNo, this.currentLUNArray[j]);
        }
        this.loading_stack.host_list = false;
    });
  }


  /**
   * Set Pool's List Data
   * @namespace VolumeFormComponent
   * @method setPoolsDropdown
   * @return {void}
   */
  setPoolsDropdown() {
    this.volume_details.loading_stack.pool_data = true;
    this.store.dispatch(new GetAllPoolsAction(this.ise_id));
    this.pools_list$ = this.store.select(getAllPoolsState).subscribe(data => {
      if (data.length > 0) {
          this.volume_details.loading_stack.pool_data = false;
          this.pools_list = data;
          if (!this.volume_details.id) {
            this.storagevolumeForm['controls']['pool'].setValue(this.pools_list[0].id);
          }
      }
    }, error => {
      this.volume_details.loading_stack.pool_data = false;
      console.error(error);
    });
  }

  LUNSerial() {
    return new Array(10000)
      .join().split(',')
      .map(function (item, index) {
        return index;
      });
  }

  /**
   * getMenuContent / set edit form values
   * @namespace xio.VolumeFormComponent
   * @method editFormValue
   * @return {void}
   */
  editFormValue() {

    this.volume_details.size_change = false;
    this.volume_details.isAddForm = false;
    this.progressRef = this.mdDialog.open(XioProgressComponent, {disableClose: true});
    this.progressRef.componentInstance.progress_data = 'Loading....';
    this.store.dispatch(new GetVolumeDetailsAction({
            ise_id: this.ise_id,
            id: this.volume_details.id
    }));
    this.volume_details_observer$ = this.store.select(getVolumeState).subscribe((data: any ) => {
      if (data && data.hasOwnProperty('result')) {
            let volume_data = data.result.response.data.volumes.volume;
            // Need to add one more layer here or do the filling of form in separate service.
            this.storagevolumeForm['controls']['size'].setValue(volume_data.size);
            this.storagevolumeForm['controls']['redundancy'].disable();
            this.storagevolumeForm['controls']['name'].setValue(volume_data.name);
            this.storagevolumeForm['controls']['size'].setValue(volume_data.size);
            this.storagevolumeForm['controls']['comment'].setValue(volume_data.comment);
            this.storagevolumeForm['controls']['alloctype'].setValue((volume_data.alloctype._attr.value !== '0'));

            if (volume_data.type === 'Primary') {
                this.storagevolumeForm['controls']['dedup'].setValue(false);
            } else {
                this.storagevolumeForm['controls']['dedup'].setValue(true);
                this.storagevolumeForm['controls']['quality_service'].disable();
            }

            this.volume_details.isAllocateEnable = volume_data.alloctype._attr.value;
            this.storagevolumeForm['controls']['quality_service'].setValue(volume_data.qosmode._attr.string === 'enabled' ? true : false);
            this.enableIOPS();
            this.storagevolumeForm['controls']['redundancy'].setValue(volume_data.configurationpolicy.redundancy._attr.value);
            this.storagevolumeForm['controls']['pool'].setValue(volume_data.pools.pool.id);
            this.storagevolumeForm['controls']['affinity'].setValue(volume_data.affinity._attr.value);
            this.storagevolumeForm['controls']['IOPSmin'].setValue(volume_data.IOPSmin);
            this.storagevolumeForm['controls']['IOPSmax'].setValue(volume_data.IOPSmax);
            this.storagevolumeForm['controls']['IOPSburst'].setValue(volume_data.IOPSburst);
            this.storagevolumeForm['controls']['id'].setValue(this.volume_details.id);
            if (!this.storagevolumeForm['controls']['alloctype'].value) {
              this.storagevolumeForm['controls']['size'].setValue(volume_data.size);
            }
            this.storagevolumeForm['controls']['size'].enable();
            this.storagevolumeForm.markAsPristine();
            this.storagevolumeForm.markAsUntouched();

            if (volume_data['allocations'].hasOwnProperty('allocations')) {
              let allocate_cnt = volume_data['allocations']['allocations'].length;
              if (allocate_cnt) {
                this.volume_details.size_change = true;
              }
              this.resetAllocation();
              this.setAllocatedHost(allocate_cnt, volume_data, 'allocations');
            }

            if (volume_data['allocations'].hasOwnProperty('allocation')) {
                let allocate_cnt = volume_data['allocations']['allocation']['hostname'].length;
                if (allocate_cnt) {
                  this.volume_details.size_change = true;
                }
                this.setAllocatedHost(1, volume_data, 'allocation');
            }

            this.hostAllocation.loaded = true;
            if (this.hostAllocation._hostLst) {
                this.getAllHostCb(this.hostAllocation._hostLst);
            }

            if (this.progressRef) {
                this.progressRef.close();
                this.progressRef = null;
            }
        }
    }, error => {
      console.log(error);
      this.storagevolumeForm['controls']['size'].disable();
    });
    this.getAllHost();
    this.isRaid();
    this.isallocatype();
    this.watchDisabled();
  }

  setAllocatedHost(allocatedHostCount, volume_data, hostAllocation: string ) {
    for ( let index = 0 ; index < allocatedHostCount ; index++) {
      this.hostAllocation.allocated_host.push(volume_data['allocations'][hostAllocation][index].hostname);
      this.hostAllocation.allocated_id.push(volume_data['allocations'][hostAllocation][index].globalid);
      this.hostAllocation.allocated_lun.push(volume_data['allocations'][hostAllocation][index].lun);
    }
  }

   /**
   * data submit event handler
   * @namespace VolumeFormComponent
   * @method onSubmit
   * @return {void}
   */
  onSubmit() {
    this.progressRef = this.mdDialog.open(XioProgressComponent, {disableClose: true});
    this.progressRef.componentInstance.progress_data = 'Loading....';

    const data = this.storagevolumeForm.value;
          data['name'] = data['name'].trim();
          data['alloctype'] = this.storagevolumeForm['controls']['alloctype'].value ? 1 : 0;
      if (data.hasOwnProperty('dedup') && data['dedup'] === true) {
          data['dedup'] = data['alloctype'] = 1;
          data['redundancy'] = 5;
      } else if (data.hasOwnProperty('dedup') && data['dedup'] === false) {
          data['dedup'] = 0;
          data['redundancy'] = this.storagevolumeForm['controls']['redundancy'].value;
      }

      let payLoad = {
        'volume_data': data,
        'ise_id': this.ise_id,
        'cb': ((success, error) => {
              if (!error) {
                  this.progressRef.close();
                  if (!this.isHost) {
                      this.snackBarService.toastMe('Volume Created Successfully', 2000);
                      this.goToVolumeList();
                  } else {
                      this.isCreated.emit();
                  }
                  this.reset();
              } else {
                  const alertRef = this.mdDialog.open(XioAlertComponent, {disableClose: true});
                        alertRef.componentInstance.title = 'Volume';
                        alertRef.componentInstance.message = error.json().result.error.message;
              }
            if (this.progressRef) {
                this.progressRef.close();
                this.progressRef = null;
            }
        })
      };
      // Add volume details
      this.store.dispatch(new AddVolumeDetailsAction(payLoad));
  }


  /**
   * getMenuContent All Host
   * @namespace VolumeFormComponent
   * @method getAllHost
   * @return {void}
   */
  getAllHost() {
    this.hostAllocation._hostLst = null;
    let payLoad = {
      ise_id: this.ise_id
    };
    this.hostService.getAll(payLoad).subscribe(
      data => {
        if ( this.hostAllocation.loaded) {
            this.getAllHostCb(data);
        }else {
            this.hostAllocation._hostLst = data;
        }
      }, error => {
        console.error(error);
      });
  }

  getAllHostCb(data) {
    let j = 0;
    const lun_array = this.LUNSerial();
    for (let i = data.length - 1; i >= 0; i--) {
      let lun_no = 1, label_id = data[i]['globalid'];
      const v = data[i]['id'], lbl = data[i]['name'], available_lun = _.difference(lun_array, _.uniq(data[i]['lun']));
      if (this.hostAllocation.allocated_host.indexOf(lbl) > -1) {
          j = this.hostAllocation.allocated_host.indexOf(lbl);
          label_id = this.hostAllocation.allocated_id[j];
          lun_no = this.hostAllocation.allocated_lun[j];
          available_lun.push(lun_no);
          j++;
          this.addHostlistItem(lbl, 'allocate_host_list', true, v , label_id, lun_no, available_lun);
      } else {
        let lno = available_lun[0] === 0 ? available_lun[1] : available_lun[0];
        this.addHostlistItem(lbl, 'host_list', false, v , label_id, lno, available_lun);
      }
    }
  }

  onUpdateDetailsCallBack = this.onUpdateDetailsCallBack || ((success, error) => {

    let data = this.getDirtyValues(this.storagevolumeForm), present_list = [], changed_list = [], unpresent_list = [],i = 0;

    if (!this.progressRef) {
        this.progressRef = this.mdDialog.open(XioProgressComponent, {disableClose: true});
        this.progressRef.componentInstance.progress_data = 'Loading....';
    }

    for (let storageVolumeFormData of this.storagevolumeForm.value.host_list) {
      if (storageVolumeFormData.host) {
          present_list.push({host: storageVolumeFormData.label, lun: storageVolumeFormData['lun']});
      }
    }

    for (let storageVolumeAllocatedData of this.storagevolumeForm.value.allocate_host_list) {
      if (!storageVolumeAllocatedData.host) {
          unpresent_list.push({globalid : storageVolumeAllocatedData.globalID,
                               hostid : storageVolumeAllocatedData.host_id });
      }
      if (storageVolumeAllocatedData['lun'] !== this.hostAllocation.allocated_lun[i] && storageVolumeAllocatedData.host) {
          changed_list.push({
                  host: storageVolumeAllocatedData['label'],
                  lun: storageVolumeAllocatedData['lun'],
                  globalID: storageVolumeAllocatedData.globalID
          });
      }
      i++;
    }

    const req_data = {
      unpresent: unpresent_list,
      present: present_list,
      changed: changed_list,
      volume_id: this.storagevolumeForm.value.id,
      volume_name: this.storagevolumeForm.value.name
    };

    if (!error) {
      if (req_data.present.length || req_data.unpresent.length || req_data.changed.length) {
        let payLoad = {
          volume_data: req_data,
          ise_id: this.ise_id,
          cb: ((source, _error) => {
            if (!_error) {
              this.snackBarService.toastMe('Volume Updated Successfully', 2000);
              this.goToVolumeList();
            } else {
              console.error(_error);
              this.router.navigate(['/ise/' + this.ise_id + '/volume']);
            }
            if (this.progressRef) {
                this.progressRef.close();
                this.progressRef = null;
            }
          })
        };
        // Allocate Volume
        this.store.dispatch(new UpdateVolumeAllocationAction(payLoad));
      } else {
        this.snackBarService.toastMe('Volume Updated Successfully', 2000);
        this.goToVolumeList();
        if (this.progressRef) {
            this.progressRef.close();
            this.progressRef = null;
        }
        this.router.navigate(['/ise/' + this.ise_id + '/volume']);
      }
    } else {
      const err_msg = JSON.parse(error._body),
            alertRef = this.mdDialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title = 'Volume';
            alertRef.componentInstance.message = err_msg.result.error.message;
      if (this.progressRef) {
        this.progressRef.close();
        this.progressRef = null;
      }
    }
  });

  /**
   * on update
   * @namespace VolumeFormComponent
   * @method onUpdateSubmit
   * @return {void}
   */
  onUpdateSubmit() {
    let data = this.getDirtyValues(this.storagevolumeForm);
    this.progressRef = this.mdDialog.open(XioProgressComponent, {disableClose: true});
    this.progressRef.componentInstance.progress_data = 'Loading....';
    // Value not assigned ? what's the use
    // this.storagevolumeForm['controls']['quality_service'].value ? 'enabled' : 'disabled';
    if (!this.isEmpty(data)) {
      if (data.hasOwnProperty('dedup') && data['dedup']) {
          data['dedup'] = data['alloctype'] = 1;
          data['redundancy'] = 5;
      } else if (data.hasOwnProperty('dedup') && data['dedup'] === false) {
          data['dedup'] = 0;
          data['redundancy'] = this.storagevolumeForm['controls']['redundancy'].value;
      }

      if (data.hasOwnProperty('alloctype') && data['alloctype'] === 0) {
        delete data['alloctype'];
      } else {
        data['alloctype'] = 1;
      }

    }

    data['id'] = this.storagevolumeForm['controls']['id'].value;
    let payLoad = {
      volume_data: data,
      ise_id: this.ise_id,
      cb: this.onUpdateDetailsCallBack
    };
    // Update Volume details
    this.store.dispatch(new UpdateVolumeDetailsAction(payLoad));
  }


  /**
   *
   * @namespace xio.VolumeFormComponent
   * @method isHostCreated
   * @return {void}
   */
  isHostCreated() {
    this.setHostList();
    this.changeTab();
  }

  /**
   *
   * @namespace xio.VolumeFormComponent
   * @param {String} v
   * @param {boolean} status
   * @param {number} lun_no
   * @param {any} aLUN
   * @method initHostItem
   * @return {void}
   */
  initHostItem(v: string, status: boolean, lun_no: number, aLUN: any) {
    return this.fb.group({host: [status, Validators.required], label: v, lun: [lun_no, [this.isUniqueLUN(aLUN)]]});
  }

  /**
   * add Host Item controller
   * @namespace xio.VolumeFormComponent
   * @param {String} v
   * @param {boolean} status
   * @param {number} lun_no
   * @param {any} aLUN
   * @method addHostItem
   * @return {void}
   */
  addHostItem(v: string, type: string, status: boolean, lun_no: number, aLUN: any) {
    const control = <FormArray>this.storagevolumeForm['controls'][type];
          control.push(this.initHostItem(v, status, lun_no, aLUN));
  }

  /**
   * remove Host Item controller
   * @namespace xio.VolumeFormComponent
   * @method removeHostItem
   * @return {void}
   */
  removeHostItem() {
    let host_cnt = this.storagevolumeForm['controls']['host_list']['controls'].length;
    for (let i = host_cnt - 1; i >= 0; i--) {
      const control = <FormArray>this.storagevolumeForm['controls']['host_list'];
            control.removeAt(i);
    }
  }

  /**
   * getMenuContent Host Label controller
   * @namespace xio.VolumeFormComponent
   * @param {string} type
   * @param {number} i
   * @method getHostLabel
   * @return {void}
   */
  getHostLabel(type: string, i: number) {
    const control = <FormArray>this.storagevolumeForm['controls'][type];
    return control.value[i].label;
  }

  /**
   * getMenuContent Form El values
   * @namespace xio.VolumeFormComponent
   * @param {string} element_name
   * @method getFormElementVal
   * @return {void}
   */
  getFormElementVal(element_name: string) {
    const control = this.storagevolumeForm['controls'][element_name];
    return control.value;
  }

  /**
   *
   * @namespace xio.VolumeFormComponent
   * @method changeSelectHost
   * @return {void}
   */
  changeSelectHost() {
    this.volume_details.isSelectHost = !this.volume_details.isSelectHost;
  }


  /**
   * go to Volume controller
   * @namespace xio.VolumeFormComponent
   * @method goToVolumeList
   * @return {void}
   */
  goToVolumeList() {
    this.router.navigate(['/ise/' + this.ise_id + '/volume']);
  }

  /**
   *
   * @namespace xio.VolumeFormComponent
   * @method isRaid
   * @return {void}
   */
  isRaid() {
    return this.getFormElementVal('redundancy') === 1;
  }

  /**
   *
   * @namespace xio.VolumeFormComponent
   * @method isallocatype
   * @return {void}
   */
  isallocatype() {
    return this.getFormElementVal('dedup') ? true : this.getFormElementVal('alloctype') === true ? true : false;
  }

  /**
   *
   * @namespace VolumeFormComponent
   * @method dedupChange
   * @return {void}
   */
  dedupChange() {
    if (!this.storagevolumeForm['controls']['dedup'].value) {
        this.volume_details.isRaidEnable = this.storagevolumeForm['controls']['redundancy'].value;
        this.storagevolumeForm['controls']['redundancy'].enable();
        this.storagevolumeForm['controls']['alloctype'].enable();
    } else {
        this.volume_details.isRaidEnable = true;
        this.storagevolumeForm['controls']['redundancy'].disable();
        this.storagevolumeForm['controls']['alloctype'].disable();
    }
  }

  /**
   *
   * @namespace xio.VolumeFormComponent
   * @method isdedup
   * @return {void}
   */
  isDedup() {
    if (this.getFormElementVal('dedup')) {
      return 5;
    }
    return this.storagevolumeForm['controls']['redundancy'].value;
  }

  /**
   * change Tab event
   * @namespace xio.VolumeFormComponent
   * @method changeTab
   * @return {void}
   */
  changeTab() {
    this.volume_details.selectedIndex = 0;
  }

  /**
   *
   * @namespace VolumeFormComponent
   * @method checkMultipleVolumes
   * @return {void}
   */
  checkMultipleVolumes(key) {
    return (group: FormGroup) => {
      this.iseService.getCardInfo(this.ise_id).subscribe(data => {
        if (data !== undefined &&
            data !== null &&
            data !== '') {
          let value = parseInt(group.root['controls'][key].value, 10 ),
              count = 239 - data.volumes;
          if (value > count) {
            this.volume_exceeding_count_msg = {
              volume_count_exceed_status: true,
              volume_count: count
            };
          } else {
            this.volume_exceeding_count_msg = {
              volume_count_exceed_status: false,
              volume_count: count
            };
          }
        }
      });
    };
  }

  /**
   * controller to change wizard
   * @namespace xio.VolumeFormComponent
   * @param {number} no
   * @method chageWizard
   * @return {void}
   */
  chageWizard(stepNo: number) {
    this.volume_details.wizard_step = stepNo;
  }

  ngOnDestroy() {
    this.store.dispatch(new VolumeReset());
    if (this.volume_details_observer$) {
      this.volume_details_observer$.unsubscribe();
    }

    if (this.pools_list$) {
      this.pools_list$.unsubscribe();
    }
  }
}

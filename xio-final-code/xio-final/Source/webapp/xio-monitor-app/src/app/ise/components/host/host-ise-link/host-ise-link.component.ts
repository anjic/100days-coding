import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {StoragevolumeService, IseService, HostService} from './../../../services/';
import {MdDialog} from '@angular/material';
import {SnackbarService} from './../../../../theme/';
import {XioProgressComponent, XioAlertComponent} from './../../../../theme/';
import * as _ from 'lodash';
import {HostComponentUtil} from "../../../../common/utils/host.component";
import {SetISEId} from "../../../../actions/ise-management.actions";
import {State} from "../../../../reducers/index";
import {Store} from '@ngrx/store';

@Component({
  selector: 'app-host-ise-link',
  templateUrl: './host-ise-link.component.html',
  styleUrls: ['./host-ise-link.component.scss'],
})

export class HostIseLinkComponent extends HostComponentUtil implements OnInit {
  public host_id: number;
  public ise_id: number;
  public allocated_volume = [];
  public allocated_volume_id: any;
  public allocated_volume_name: any;
  public allocated_volume_lun: any;
  public end_point_wwn: any;
  public available_lun: Array<Number> = [];
  public allocationForm: FormGroup;
  public loading_stack: any;
  public host_name: any;
  public end_point_name: any;
  public selectedLun: object = {};
  public is_volume:Boolean = false;

  constructor(public fb: FormBuilder,
              public hs: HostService,
              public ises: IseService,
              public svs: StoragevolumeService,
              public route: ActivatedRoute,
              public router: Router, public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
    super();

    this.loading_stack = {
      volume_list: false,
      volume_list_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.is_volume=true;
    this.allocated_volume = [];
    this.allocated_volume_id = [];
    this.allocated_volume_name = [];
    this.allocated_volume_lun = [];
    this.end_point_wwn = [];

    this.allocationForm = this.fb.group({
      volume_list: this.fb.array([]),
      allocate_volume_list: this.fb.array([]),
      host_id: [''],
      ise_id: [''],
      host_name: ['']
    }, {validator: this.duplicateLun});

    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];

      this.route.params.subscribe(params => {
        this.host_id = params['host_id'];
        this.allocationForm['controls']['ise_id'].setValue(this.ise_id);
        this.allocationForm['controls']['host_id'].setValue(this.host_id);
        this.store.dispatch(new SetISEId(this.ise_id));
        // this.ises.setCurrentISEId(this.ise_id);
        let payLoad = {
          "id": this.host_id,
          "ise_id": this.ise_id
        }
        this.hs.getHost(payLoad).subscribe(
          res => {
            console.log(res);
            this.host_name = res.result.response.data.hosts.host.name;
            let end_point: any = '';

            if (res.result.response.data.hosts.host.endpoints.hasOwnProperty('endpoint')) {
              end_point = [res.result.response.data.hosts.host.endpoints.endpoint];
            }
            if (res.result.response.data.hosts.host.endpoints.hasOwnProperty('endpoints')) {
              end_point = res.result.response.data.hosts.host.endpoints.endpoints;
            }

            for (let i in end_point) {
              this.end_point_wwn.push(end_point[i].globalid);
            }

            this.end_point_name = this.end_point_wwn;

            this.allocated_volume =[];
            this.allocationForm['controls']['host_name'].setValue(res.result.response.data.hosts.host.name);

            if (res.result.response.data.hosts.host.allocations.hasOwnProperty('allocation')) {
              this.allocated_volume = [res.result.response.data.hosts.host.allocations.allocation];
            }
            if (res.result.response.data.hosts.host.allocations.hasOwnProperty('allocations')) {
              this.allocated_volume = res.result.response.data.hosts.host.allocations.allocations;
            }

            for (let i in this.allocated_volume) {
              this.allocated_volume_name.push(this.allocated_volume[i].volumename);
              this.allocated_volume_id.push(this.allocated_volume[i].globalid);
              this.allocated_volume_lun.push(this.allocated_volume[i].lun);
            }
            this.getAvailableLUN();
            this.volumeList();
          },
          err => {
            console.error(err);
          }
        );
      });
    });
  }

  /**
   * getMenuContent volume list service
   * @namespace xio.HostIseLinkComponent
   * @method volumeList
   * @return {void}
   */
  volumeList() {
    this.loading_stack.volume_list = true;
    let payLoad={
      ise_id:this.ise_id
    }
    this.svs.getAll(payLoad).subscribe(
      res => {
        let lun_cnt = 0;
        this.svs.volume_list = Array.isArray(this.svs.volume_list) ? this.svs.volume_list : (typeof this.svs.volume_list == "object" ? [this.svs.volume_list] : []);
        for (let i in this.svs.volume_list) {
          let vol_name = this.svs.volume_list[i].name;
          let index_no = this.allocated_volume_name.indexOf(vol_name);
          if (index_no > -1) {
            let vol_id = this.allocated_volume_id[index_no];
            this.selectedLun[this.allocated_volume_lun[index_no]] = this.addVolumeItem(vol_name, 'volume_list', true, vol_id, this.allocated_volume_lun[index_no]);
          } else {
            console.log(this.available_lun[lun_cnt]);
            this.selectedLun[this.allocated_volume_lun[index_no]] = this.addVolumeItem(vol_name, 'allocate_volume_list', false, 1, this.available_lun[lun_cnt]);
            lun_cnt++;
          }
        }
        this.loading_stack.volume_list = false;
        if(this.svs.volume_list.length ==0){
          this.is_volume=false;
        }
        else{
          this.is_volume=true;
        }
      }
    );
  }

  volume_listlun(i: number) {
    console.log(i);
    let value = this.allocationForm['controls']['volume_list']['controls'][i]['controls']['volume'].value;
    console.log(value);
    if (value) {
      let _lun = this.getLun();
      console.log(this.allocated_volume_lun);
      this.allocationForm['controls']['volume_list']['controls'][i]['controls']['lun'].setValue(_lun);
      console.log(this.allocationForm['controls']['volume_list']['controls'][i]['controls']['lun'].value);
      this.selectedLun[_lun] = this.allocationForm['controls']['volume_list']['controls'][i]['controls']['lun'];
    }
    else {
      console.log(this.allocationForm['controls']['volume_list']['controls'][i]['controls']['lun'].value)
      this.resetLunAvailable(this.allocationForm['controls']['volume_list']['controls'][i]['controls']['lun'].value);
      this.allocationForm['controls']['volume_list']['controls'][i]['controls']['lun'].setValue(0);
    }
  }

  allocate_volumelun(i: number) {
    let value = this.allocationForm['controls']['allocate_volume_list']['controls'][i]['controls']['volume'].value;
    if (value) {
      let _lun = this.getLun();
      this.allocationForm['controls']['allocate_volume_list']['controls'][i]['controls']['lun'].setValue(_lun);
      this.selectedLun[_lun] = this.allocationForm['controls']['allocate_volume_list']['controls'][i]['controls']['lun'];
    }
    else {
      this.resetLunAvailable(this.allocationForm['controls']['allocate_volume_list']['controls'][i]['controls']['lun'].value);
      this.allocationForm['controls']['allocate_volume_list']['controls'][i]['controls']['lun'].setValue(0);
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
      this.selectedLun[val] = this.allocationForm['controls']['allocate_volume_list']['controls'][+e.id]['controls']['lun'];
    }
  }


  resetLunAvailable(val: number) {
    delete this.selectedLun[val];

    // let i = 0;
    //
    // while (i < this.available_lun.length) {
    //   console.log(this.available_lun[i]);
    //
    //   if (this.available_lun[i] > val) {
    //
    //     break;
    //   }
    //
    //   i++;
    // }
    //
    // this.available_lun.splice(i, 0, val);
    //
    // console.log(this.available_lun);

  }

  /**
   * Util Fn to find duplicate LUN's
   * @namespace xio.HostIseLinkComponent
   * @method duplicateLun
   * @return {Object}
   */
  duplicateLun(fg: FormGroup) {
    let Lun = [],
      return_val: any = null;
    for (let v of fg.value.volume_list) {
      if (v.volume) {
        Lun.push(v.lun);
      }
    }
    for (let v of fg.value.allocate_volume_list) {
      if (v.volume) {
        Lun.push(v.lun);
      }
    }


    let dup = _.filter(Lun, function (value, index, iteratee) {
      return _.includes(iteratee, value, index + 1);
    });

    return_val = dup.length ? ({
      duplicateLun: {
        valid: false
      }
    }) : null;

    let neg_lun = 0;
    _.filter(Lun, function (value) {
      if (value < 0 || value > 9999) {
        neg_lun++;
      }
    });

    if (neg_lun) {
      if (return_val) {
        return_val['invalidLun'] = {valid: false};

      } else {
        return_val = {
          invalidLun: {
            valid: false
          }
        };
      }
    }
    return return_val;
  }

  /**
   * getMenuContent Available LUN
   * @namespace xio.HostIseLinkComponent
   * @method getAvailableLUN
   * @return {void}
   */
  getAvailableLUN() {
    for (let i = 1; i < 9999; i++) {
      if (this.allocated_volume_lun.indexOf(i) <= -1) {
        if (this.available_lun) {
          this.available_lun.push(i);
        } else {
          this.available_lun = [i];
        }
      }
    }
  }

  /**
   * Host ISE link Update service controller
   * @namespace xio.HostIseLinkComponent
   * @method onUpdateSubmit
   * @return {void}
   */
  onUpdateSubmit() {
    let changed_lun = [],
      presentt_list = [],
      unpresentt_list = [];

    if (this.allocationForm.value) {
     let _allocationMap = {};
     this.allocated_volume = Array.isArray(this.allocated_volume) ? this.allocated_volume : [];
      this.allocated_volume.forEach((v) => {
        _allocationMap[v.globalid] = v.lun;
      });
      for (let s in this.allocationForm.value.volume_list) {
        let _vlst = this.allocationForm.value.volume_list[s];
        if (_vlst.volume && _vlst.lun !== _allocationMap[_vlst.globalID]) {
          let lun = {
            lun: this.allocationForm.value.volume_list[s].lun,
            global_id: this.allocationForm.value.volume_list[s].globalID
          };
          changed_lun.push(lun);
        }
      }
    }

    for (let data of this.allocationForm.value.allocate_volume_list) {
      if (data.volume) {
        let present_data = {
          name: data.label,
          lun: data.lun
        };
        presentt_list.push(present_data);
      }
    }

    for (let data of this.allocationForm.value.volume_list) {
      if (!data.volume) {
        unpresentt_list.push(data.globalID);
      }
    }

    let req_data = {
      unpresent: unpresentt_list,
      present: presentt_list,
      changed: changed_lun,
      ise_id: this.allocationForm.value.ise_id,
      host_id: this.allocationForm.value.host_id,
      host_name: this.allocationForm.value.host_name
    };

    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    progressRef.componentInstance.progress_data = 'processing';

    this.hs.updateVolumeAllocation(req_data).subscribe(
      data => {
        progressRef.close();
        this.snackbarService.toastMe('Volume updated Successfully', 2000);
        this.router.navigate(['/ise/' + this.ise_id + '/host']);
      },
      err => {
        progressRef.close();
        let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
        alertRef.componentInstance.title ='Below allocations failed. Try Again';

        alertRef.componentInstance.message = err.json().result.error.message.retry_lun;

        this.router.navigate(['/ise/' + this.ise_id + '/host']);
      }
    );
  }
}

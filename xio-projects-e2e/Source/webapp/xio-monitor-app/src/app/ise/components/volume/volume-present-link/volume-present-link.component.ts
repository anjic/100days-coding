import {Component, OnInit,OnDestroy } from '@angular/core';
import {FormBuilder, FormGroup, FormArray, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {StoragevolumeService} from '../../../services/storagevolume.service';
import {IseService} from '../../../services/ise.service';
import {HostService} from '../../../services/host.service';
import {MdDialog} from '@angular/material';
import {XioProgressComponent, XioAlertComponent} from './../../../../theme/';

//Redux
import {Store} from '@ngrx/store';
import {State, getVolumeState} from "../../../../reducers/";
import {Observable} from "rxjs";
import {GetVolumeDetailsAction, UpdateVolumeAllocationAction} from "../../../../actions/volume.actions";

@Component({
  selector: 'app-volume-present-link',
  templateUrl: './volume-present-link.component.html',
  styleUrls: ['./volume-present-link.component.scss'],
  providers: [StoragevolumeService, HostService]
})
export class VolumePresentLinkComponent implements OnInit, OnDestroy {
  public id: number;
  public ise_id: number;
  public allocationForm: FormGroup;
  public volume_data: any;
  public allocated_host: any;
  public allocated_id: any;
  public allocated_lun: any;
  public isqosmode: number;
  public isAllocateEnable: number;
  public isRaid: number;
  public volume_details_obs$;

  constructor(public fb: FormBuilder,
              public svs: StoragevolumeService,
              public hs: HostService,
              public ises: IseService,
              public route: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public store: Store<State>) {
  }

  isEmpty(obj) {
    return (obj && (Object.keys(obj).length === 0));
  }

  ngOnInit() {
    this.allocated_host = [];
    this.allocated_id = [];
    this.allocated_lun = [];
    this.allocationForm = this.fb.group({
      host_list: this.fb.array([]),
      allocate_host_list: this.fb.array([]),
      id: [''],
      name: ['']
    });


    this.route.parent.params.subscribe(params => {
      console.log(params);
      this.ise_id = params['ise_id'];
      this.route.params.subscribe(params => {
        this.id = params['id'];
        let payLoad = {
          ise_id: this.ise_id,
          id: this.id
        }

        this.store.dispatch(new GetVolumeDetailsAction(payLoad));
        this.volume_details_obs$ = this.store.select(getVolumeState).subscribe(result => {
          if (!this.isEmpty(result)) {

            let data = result['response'].data.volumes.volume;
            this.volume_data = result['response'].data.volumes.volume;
            this.allocationForm['controls']['id'].setValue(this.id);
            this.allocationForm['controls']['name'].setValue(this.volume_data.name);
            this.isqosmode = data.qosmode._attr.value;
            this.isAllocateEnable = data.alloctype._attr.value;
            this.isRaid = data.configurationpolicy.redundancy._attr.value;

            if (this.volume_data['allocations']['allocations']) {
              let allocate_cnt = this.volume_data['allocations']['allocations'].length;
              for (var i = allocate_cnt - 1; i >= 0; i--) {
                this.allocated_host.push(this.volume_data['allocations']['allocations'][i].hostname);
                this.allocated_id.push(this.volume_data['allocations']['allocations'][i].globalid);
                this.allocated_lun.push(this.volume_data['allocations']['allocations'][i].lun);
              }
            }

            if (this.volume_data['allocations']['allocation']) {
              this.allocated_host.push(this.volume_data['allocations']['allocation'].hostname);
              this.allocated_id.push(this.volume_data['allocations']['allocation'].globalid);
              this.allocated_lun.push(this.volume_data['allocations']['allocation'].lun);
            }
          }
        }, error => {
          let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
          alertRef.componentInstance.title = "Volume";
          alertRef.componentInstance.message = error;
        })
        // console.log(this.allocated_id);
        this.getAllHost();

        /*this.svs.getVolumeDetails(payLoad).subscribe(
         result => {
         let data = result.response.data.volumes.volume;
         this.volume_data = result.response.data.volumes.volume;
         this.allocationForm['controls']['id'].setValue(this.id);
         this.allocationForm['controls']['name'].setValue(this.volume_data.name);

         this.isqosmode = data.qosmode._attr.value;
         this.isAllocateEnable = data.alloctype._attr.value;
         this.isRaid = data.configurationpolicy.redundancy._attr.value;
         if (this.volume_data['allocations']['allocations']) {
         let allocate_cnt = this.volume_data['allocations']['allocations'].length;
         for (var i = allocate_cnt - 1; i >= 0; i--) {
         this.allocated_host.push(this.volume_data['allocations']['allocations'][i].hostname);
         this.allocated_id.push(this.volume_data['allocations']['allocations'][i].globalid);
         this.allocated_lun.push(this.volume_data['allocations']['allocations'][i].lun);

         }
         }

         if (this.volume_data['allocations']['allocation']) {

         this.allocated_host.push(this.volume_data['allocations']['allocation'].hostname);
         this.allocated_id.push(this.volume_data['allocations']['allocation'].globalid);
         this.allocated_lun.push(this.volume_data['allocations']['allocation'].lun);

         }

         // console.log(this.allocated_id);
         this.getAllHost();
         },
         err => {
         let err_msg = err.json();
         console.log(err_msg);
         let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
         alertRef.componentInstance.title = "Volume";
         alertRef.componentInstance.message = err_msg.response.data;

         });*/
      });
    });

  }

  /**
   *
   * @param v
   * @param status
   * @param globalID
   * @param lun_no
   * @returns {FormGroup}
   */
  initHostItem(v: string, status: boolean, globalID: any, lun_no: number = 1) {
    return this.fb.group({
      host: [status, Validators.required],
      label: v,
      globalID: globalID,
      lun: [lun_no, [Validators.pattern(/^([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-2][0-9]|23[0-9])$/)]]
    });
  }

  /**
   *
   * @param v
   * @param type
   * @param status
   * @param globalID
   * @param lun_no
   */
  addHostItem(v: string, type: string, status: boolean, globalID: any, lun_no: number = 1) {
    const control = <FormArray>this.allocationForm['controls'][type];
    control.push(this.initHostItem(v, status, globalID, lun_no));
  }

  /**
   *
   * @param type
   * @param i
   */
  getHostLabel(type: string, i: number) {
    const control = <FormArray>this.allocationForm['controls'][type];
    return control.value[i].label;
  }

  getAllHost() {

    this.hs.getAll(this.ise_id).subscribe(
      data => {
        let j = 0;
        for (var i = this.hs.host_list.length - 1; i >= 0; i--) {
          let lun_no = 1;
          let v = this.hs.host_list[i]['id'];
          let lbl = this.hs.host_list[i]['name'];
          let lbl_id = this.hs.host_list[i]['globalid'];
          if (this.allocated_host.indexOf(lbl) > -1) {
            lbl_id = this.allocated_id[j];
            lun_no = this.allocated_lun[j];
            j++;
            this.addHostItem(lbl, 'allocate_host_list', true, lbl_id, lun_no);
          } else {
            this.addHostItem(lbl, 'host_list', false, lbl_id);
          }
        }
      },
      err => {
        console.log(err);
      });
  }

  onUpdateVolumeAllocationAction = this.onUpdateVolumeAllocationAction || ((success,error)=> {
      let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
      progressRef.componentInstance.progress_data = "Loading....";
      if(!error){
        progressRef.close();
        this.router.navigate(['/ise/' + this.ise_id + '/volume']);
      }else{
        progressRef.close();
        let err_msg = JSON.parse(error._body);
        let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
        alertRef.componentInstance.title = "Volume";
        alertRef.componentInstance.message = err_msg.response.data;
      }
  })

  onUpdateSubmit() {
    let presentt_list = [],
      unpresentt_list = [];

    for (let data of this.allocationForm.value.host_list) {
      if (data.host) {
        presentt_list.push({host: data.label, lun: data.lun});
      }
    }
    for (let data of this.allocationForm.value.allocate_host_list) {
      console.log(data.globalID);
      if (!data.host) {
        unpresentt_list.push(data.globalID);
      }
    }

    let req_data = {
      unpresent: unpresentt_list,
      present: presentt_list,
      volume_id: this.allocationForm.value.id,
      id: this.allocationForm.value.id,
      volume_name: this.allocationForm.value.name
    };
    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    progressRef.componentInstance.progress_data = "Loading....";

    let payLoad  = {
      "volume_data" : req_data,
      "ise_id" : this.ise_id,
      "cb":this.onUpdateVolumeAllocationAction
    }

    this.store.dispatch( new UpdateVolumeAllocationAction(payLoad))

    /*this.svs.updateVolumeAllocation(req_data, this.ise_id).subscribe(
      data => {
        progressRef.close();
        this.router.navigate(['/ise/' + this.ise_id + '/volume']);
      },
      err => {
        progressRef.close();
        let err_msg = JSON.parse(err._body);
        let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
        alertRef.componentInstance.title = "Volume";
        alertRef.componentInstance.message = err_msg.response.data;
      });*/
  }
  ngOnDestroy() {
    this.volume_details_obs$.unsubscribe();
  }

}

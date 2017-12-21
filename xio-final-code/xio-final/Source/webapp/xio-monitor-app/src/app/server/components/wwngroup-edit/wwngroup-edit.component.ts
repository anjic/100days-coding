import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { getAllIseLst, State} from '../../../reducers/index';
import { Store } from '@ngrx/store';
import { ServermanagementService } from '../../service/servermanagement.service';
import { SnackbarService } from '../../../theme/';
import { MdDialog } from '@angular/material';
import { GetAllISEList} from '../../../actions/ise-management.actions';
import { XioProgressComponent} from '../../../theme/xio-progress/xio-progress.component';
import * as _ from 'lodash';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import {UpdateWWNAction} from "../../../actions/server.actions";

@Component({
  selector: 'app-wwngroup-edit',
  templateUrl: './wwngroup-edit.component.html',
  styleUrls: ['./wwngroup-edit.component.scss']
})
export class WwngroupEditComponent implements OnInit {

  public editWwnGroupForm: FormGroup;
  public ser_id: any;
  public wwngroup_name: any;
  public ise_list: any[];
  public ise_id;
  public wwngroup_id;
  public current_wwns: any[];
  public over_lappedlist: any[];
  public non_over_lappedlist: any[];
  public iseLst$;
  public selectedIseValue: any;
  public removed_endpoint: any[];
  public endpoint: any[];

  constructor(public router: Router,
              public route: ActivatedRoute,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public servermgmt: ServermanagementService,
              public store: Store<State>,
              public fb: FormBuilder) {

        this.ise_list = [];
        this.current_wwns = [];
        this.over_lappedlist = [];
        this.non_over_lappedlist = [];
        this.removed_endpoint = [];
        this.endpoint = [];
  }

  ngOnInit() {
    this.editWwnGroupForm = this.fb.group({
      wwngroup_name: ['', [Validators.required,
                         Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      comment: [''],
    });

    this.getIse();
    this.route.params.subscribe(params => {
      this.ser_id = params['ser_id'];
      this.ise_id = params['id'];
      this.wwngroup_id = params['wwnid'];

      let PayLoad = {
        'server_id': this.ser_id,
        'ise_id': this.ise_id,
        'wwngroup_id': this.wwngroup_id
      }

      this.servermgmt.getparticularWwnGroup(PayLoad).subscribe(res => {
        this.current_wwns.length = 0;
        this.over_lappedlist.length = 0;
        this.non_over_lappedlist.length = 0;
        this.editWwnGroupForm['controls']['wwngroup_name'].setValue(res.wwn.wwngroup_name);
        this.selectedIseValue = res.ise_details;

        for (let k = 0; k < res.wwn.current_wwn.length; k++) {
          this.current_wwns.push({
            'wwn': res.wwn.current_wwn[k],
            'ise_id': this.ise_id,
            'ise_serial_no': res.ise_details.ise_serialno,
            'ise_name': res.ise_details.ise_name
          })
        }

        for ( let k = 0; k < res.wwn.available_wwn.length; k++) {
          this.over_lappedlist.push({
            'wwn': res.wwn.available_wwn[k],
            'ise_id': this.ise_id,
            'ise_serial_no': res.ise_details.ise_serialno,
            'ise_name': res.ise_details.ise_name
          })
        }
      })
    });
  }

  /**
   * This method is used for getting all ISE Details
   */
  getIse() {
    this.store.dispatch(new GetAllISEList());
    this.iseLst$ = this.store.select(getAllIseLst).subscribe(
      res => {
        this.ise_list.length = 0;
        for ( let k = 0 ; k < res.length ; k++ ) {
          this.ise_list.push({
            'ise_id': res[k]['id'],
            'ise_serial_no': res[k]['serial_no'],
            'ise_name': res[k]['ise_name']
          });
        }
      });
  }


  /**
   * For editing ISE
   * @param $event
   */
  onEditISESelectChange($event){
    let selectedIseIds = [];
    selectedIseIds = $event.value;
    this.over_lappedlist.length = 0;
    this.non_over_lappedlist.length = 0;
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading WWN(s)';
    if (selectedIseIds.length > 0) {
      this.servermgmt.getServerWwn(selectedIseIds).subscribe(res => {
        progressRef.close();

        if (res && res.common && res.common.wwn) {
          if (res.common.wwn.length > 0) {
            this.over_lappedlist = [];
            for (let k = 0; k < res.common.ise_id.length; k++) {
              for (let i = 0; i < res.common.wwn.length; i++) {
                this.over_lappedlist.push({
                  'wwn': res.common.wwn[i]
                });
              }
            }
            this.over_lappedlist = _.uniqBy(this.over_lappedlist, 'wwn');
          }
        }


        if (res && res.un_common && res.un_common.length > 0) {
          this.non_over_lappedlist = [];
          for (let wwnObj = 0; wwnObj < res.un_common.length; wwnObj++) {
            for( let prop in res.un_common[wwnObj]) {
              let ise_id = '', ise_serialno = '', ise_name = '';
              ise_id = res.un_common[wwnObj]['ise_id'];
              ise_serialno = res.un_common[wwnObj]['ise_serialno'];
              ise_name = res.un_common[wwnObj]['ise_name'];
              if (prop == 'wwn') {
                if (res.un_common[wwnObj]['wwn'].length > 0) {
                  for (let m = 0; m < res.un_common[wwnObj]['wwn'].length; m++) {
                    this.non_over_lappedlist.push({
                      'wwn': res.un_common[wwnObj]['wwn'][m],
                      'ise_id': ise_id,
                      'ise_serial_no': ise_serialno,
                      'ise_name': ise_name
                    });
                  }
                }
              }
            }
          }
        }

      });
    } else {
      progressRef.close();
      this.over_lappedlist.length = 0;
      this.non_over_lappedlist.length = 0;
    }
  }

  /**
   * For removing end points
   * @param wwnObj
   * @param e
   */
  assignUnassignWWNGroup(wwnObj, e) {
    if (!e.checked) {
      this.removed_endpoint.push(wwnObj.wwn);
    } else {
      let index = this.removed_endpoint.indexOf(wwnObj.wwn);
      this.removed_endpoint.splice(index, 1);
    }
  }

  /**
   * For adding end points
   * @param overlap_wwn
   * @param event
   */
  assignOverLappedEndPoint(overlap_wwn , event) {
    if (event.checked) {
      this.endpoint.push(overlap_wwn.wwn);
    } else {
      let index = this.endpoint.indexOf(overlap_wwn.wwn);
      this.endpoint.splice(index, 1);
    }
  }

  /**
   * Navigates to particular WWN Group
   */
  onCancel(){
    this.router.navigate(['/server/'+this.ser_id+'/edit'])
  }


  /**
   * For updating WWN
   */
  updateWWNGroup() {
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Processing...';
    let data = this.editWwnGroupForm.value;
    let payLoad = {
      'name': data.wwngroup_name,
      'comment': data.comment,
      'id': this.wwngroup_id,
      'ise_id': this.ise_id,
      'endpoint' : this.endpoint,
      'removed_endpoint': this.removed_endpoint,
      'cb': (success, error) => {
        if (!error) {
          progressRef.close();
          this.snackbarService.toastMe('WWN Group Updated Successfully', 2000);
          this.router.navigate(['/server/' + this.ser_id + '/edit']);
        }else {
          progressRef.close();
          console.log(error);
        }
       }
    };

    this.store.dispatch(new UpdateWWNAction(payLoad));

  }

}

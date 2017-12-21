import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { getISEId, State, getAllIseLst, getISEInfo } from '../../../reducers/index';
import { GetAllISEList } from '../../../actions/ise-management.actions';
import { AddWwnServerAction } from '../../../actions/server.actions';
import { Store } from '@ngrx/store';
import { ServermanagementService } from '../../service/servermanagement.service';
import { MdDialog } from '@angular/material';
import { SnackbarService, XioProgressComponent } from './../../../theme/';
import * as _ from 'lodash';
import {XioAlertComponent} from "../../../theme/xio-alert/xio-alert.component";

@Component({
  selector: 'app-server-wwn-form',
  templateUrl: './server-wwn-form.component.html',
  styleUrls: ['./server-wwn-form.component.scss']
})
export class ServerWwnFormComponent implements OnInit {

  public serverWwnForm: FormGroup;
  public iseId$;
  public iseLst$;
  public ise_list: any[];
  public ise_id;
  public overlapped_wwns_list: any[];
  public non_overlapped_wwns_list: any[];
  public selectedIseIds: any[];
  public selected_wwns: any[];
  public server_id: string = '';
  public counter: number = 0;

  constructor(public fb: FormBuilder,
    public router: Router,
    public route: ActivatedRoute,
    public snackbarService: SnackbarService,
    public dialog: MdDialog,
    public servermgmt: ServermanagementService,
    public store: Store<State>) {

    this.overlapped_wwns_list = [];
    this.non_overlapped_wwns_list = [];
    this.selectedIseIds = [];
    this.selected_wwns = [];
    this.counter = 0;
  }

  ngOnInit() {

    this.serverWwnForm = this.fb.group({
      server_name: ['', [Validators.required,
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      selectedIses: [''],
      comment: [''],

    });
    this.route.params.subscribe(params => {
      this.server_id = params['ser_id'];
    })
    this.getIse();
    this.iseId$ = this.store.select(getISEId).subscribe(
      data => {
        this.ise_id = data;
      }
    );


  }

  getIse() {
    this.store.dispatch(new GetAllISEList());
    this.iseLst$ = this.store.select(getAllIseLst).subscribe(
      res => {
        this.ise_list = res;
      })
  }



  onISESelectChange($event) {
    let selectedIseIds = [];
    selectedIseIds = $event.value;
    this.overlapped_wwns_list.length = 0;
    this.non_overlapped_wwns_list.length = 0;
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading WWN(s)';
    if (selectedIseIds.length > 0) {
      this.servermgmt.getServerWwn(selectedIseIds).subscribe(res => {
        progressRef.close();

        if (res && res.common && res.common.wwn) {
          if (res.common.wwn.length > 0) {
            this.overlapped_wwns_list = [];
            for (let k = 0; k < res.common.ise_id.length; k++) {
              for (let i = 0; i < res.common.wwn.length; i++) {
                this.overlapped_wwns_list.push({
                  'wwn': res.common.wwn[i]
                });
              }
            }
            this.overlapped_wwns_list = _.uniqBy(this.overlapped_wwns_list, 'wwn');
          }
        }


        if (res && res.un_common && res.un_common.length > 0) {
          this.non_overlapped_wwns_list = [];
          for (let wwnObj = 0; wwnObj < res.un_common.length; wwnObj++) {
            for (let prop in res.un_common[wwnObj]) {
              let ise_id = '', ise_serialno = '', ise_name = '';
              ise_id = res.un_common[wwnObj]['ise_id'];
              ise_serialno = res.un_common[wwnObj]['ise_serialno'];
              ise_name = res.un_common[wwnObj]['ise_name'];
              if (prop == 'wwn') {
                if (res.un_common[wwnObj]['wwn'].length > 0) {
                  for (let m = 0; m < res.un_common[wwnObj]['wwn'].length; m++) {
                    this.non_overlapped_wwns_list.push({
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
      this.overlapped_wwns_list.length = 0;
      this.non_overlapped_wwns_list.length = 0;
    }

  }




  wwnCheckBoxChange(wwnObj, e) {
    if (e.checked) {
      this.selected_wwns.push(wwnObj);
    } else {
      let index = this.selected_wwns.indexOf(wwnObj);
      this.selected_wwns.splice(index, 1);
    }
  }

  findObjectByKey(array, key, value) {
    for (var i = 0; i < array.length; i++) {
      if (array[i][key] == value) {
        return array[i];
      }
    }
    return null;
  }


  createWWNGroup($event) {
    let data = this.serverWwnForm.value;
    if(this.selected_wwns.length > 0){
      let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
      progressRef.componentInstance.progress_data = 'Processing';
      let payLoad = {
        wwn_name: '',
        comment: '',
        wwns: [],
        server_id: '',
        cb: ((success, error) => {
          if (!error) {
            progressRef.close();
            this.snackbarService.toastMe('WWN Groups created Successfully', 2000);
            this.router.navigate(['/server/' + this.server_id + '/edit/']);
          } else {
            progressRef.close();
            console.log(error);
            this.serverWwnForm['controls']['server_name'].setErrors({
              remote: true
            });
          }
        })
      }
      payLoad['wwn_name'] = data['server_name'];
      payLoad['comment'] = data['comment'];

      let tempSelIseIdList = [];
      for(let k=0; k < data.selectedIses.length ; k++){
        let searchObj = this.findObjectByKey(this.ise_list,'id',data.selectedIses[k]);
        tempSelIseIdList.push({
          'ise_id':searchObj.id,
          'ise_serial_no':searchObj.serial_no,
          'ise_name':searchObj.ise_name
        })
      }

      for(let n=0; n < this.selected_wwns.length ; n++){
        for(let q=0; q < tempSelIseIdList.length ; q++){
          payLoad['wwns'].push({
            'wwn': this.selected_wwns[n]['wwn'],
            'ise_id': tempSelIseIdList[q]['ise_id'],
            'ise_serial_no': tempSelIseIdList[q]['ise_serial_no'],
            'ise_name': tempSelIseIdList[q]['ise_name']
          });
        }
      }

      payLoad['server_id'] = this.server_id;
      this.store.dispatch(new AddWwnServerAction(payLoad));
    }else{
      const alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
      alertRef.componentInstance.title = 'Create WWN Group';
      alertRef.componentInstance.message = 'Please select atleast 1 WWN to create WWN Group';
    }
  }
}

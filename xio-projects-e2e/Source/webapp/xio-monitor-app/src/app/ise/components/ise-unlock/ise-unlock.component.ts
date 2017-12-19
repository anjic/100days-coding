import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ActivatedRoute, Router} from "@angular/router";
import {MdDialog} from "@angular/material";
import {SnackbarService} from "../../../theme/services/snackbar.service";
import {XioAlertComponent} from "../../../theme";

import {Store} from "@ngrx/store";
import {State} from '../../../reducers/index';
import {ISEEnableEncryption} from "../../../actions/ise-settings.actions";

@Component({
  selector: 'app-ise-unlock',
  templateUrl: './ise-unlock.component.html',
  styleUrls: ['./ise-unlock.component.scss']
})
export class IseUnlockComponent implements OnInit {

  public iseUnlockForm: FormGroup;
  public id;
  public ise_id;


  constructor(public fb: FormBuilder,
              public route: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) { }

  ngOnInit() {
    this.iseUnlockForm = this.fb.group({
      isePassKey: ['', Validators.required],
    });

    this.route.parent.params.subscribe(params => {
      console.log(params);
      this.ise_id = params['ise_id'];
    });
  }

  unlockIse(){
    let iseUnlockFormData = this.iseUnlockForm.value;
    let payLoad= {
      "ise_id": this.ise_id,
      "cb": ((success, error) => {
        if(!error){
          this.snackbarService.toastMe('ISE unlocked Successfully', 2000);
          this.router.navigate(['/ise/' + this.ise_id + '/dashboard']);
        }else{
        const  alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
        alertRef.componentInstance.title = 'ISE UNLOCK';
        alertRef.componentInstance.message = 'ISE unlock failed';
        }
      }),
      "data": {
        "passkey":iseUnlockFormData.isePassKey,
        "locked":"false"
      }
    }
    this.store.dispatch(new ISEEnableEncryption(payLoad));
  }

}

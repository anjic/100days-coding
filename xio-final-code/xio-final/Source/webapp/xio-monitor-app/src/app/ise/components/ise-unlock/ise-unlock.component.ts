import { Component, OnInit, OnDestroy } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {MdDialog} from '@angular/material';
import {SnackbarService} from '../../../theme/services/snackbar.service';
import {XioAlertComponent} from '../../../theme';
import {Store} from '@ngrx/store';
import {State} from '../../../reducers/index';
import {ISEEnableEncryption} from '../../../actions/ise-settings.actions';

@Component({
  selector: 'app-ise-unlock',
  templateUrl: './ise-unlock.component.html',
  styleUrls: ['./ise-unlock.component.scss']
})
export class IseUnlockComponent implements OnInit,OnDestroy {

  public iseUnlockForm: FormGroup;
  public ise_id;


  constructor(public formBuilder: FormBuilder,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) { }

  ngOnInit() {
    this.iseUnlockForm = this.formBuilder.group({
      isePassKey: ['', Validators.required],
    });
    this.activatedRoute.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
    });
  }

   /**
   * To Unlock ISE
   * @namespace xio.IseUnlockComponent 
   * @method unlockIse
   */
  unlockIse() {
    let iseUnlockFormData = this.iseUnlockForm.value;
    let payLoad = {
      'ise_id': this.ise_id,
      'cb': ((success, error) => {
        if (!error) {
          this.snackbarService.toastMe('ISE unlocked Successfully', 2000);
          this.router.navigate(['/ise/' + this.ise_id + '/dashboard']);
        } else {
            const  alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
                   alertRef.componentInstance.title = 'ISE UNLOCK';
                   alertRef.componentInstance.message = 'ISE unlock failed';
        }
      }),
      'data': {
        'passkey': iseUnlockFormData.isePassKey,
        'locked': 'false'
      }
    };
    this.store.dispatch(new ISEEnableEncryption(payLoad));
  }

  ngOnDestroy() {
     // Un Binding Event Listeners
     window.removeEventListener('click', this.unlockIse.bind(this), false);
  }

}

import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { IseService } from './../../../services/ise.service';
import { MdDialog } from '@angular/material';
import { XioAlertComponent, XioProgressComponent, SnackbarService } from './../../../../theme/';
import { getLoginedUser, State } from '../../../../reducers/index';
import { Store } from '@ngrx/store';
import { ChangeISEPWD, SetISEId } from '../../../../actions/ise-management.actions';

@Component({
  selector: 'app-ise-changepwd-form',
  templateUrl: './ise-changepwd-form.component.html',
  styleUrls: ['./ise-changepwd-form.component.scss'],
})
export class IseChangepwdFormComponent implements OnInit,OnDestroy {

  public ISEchangepwdForm: FormGroup;
  public ise_id;
  public username;
  public userInfo$;


  /**
   * 
   * @param {FormBuilder} formBuilder
   * @param {IseService} ises
   * @param {activatedRoute} ActivatedRoute
   * @param {Router} router
   * @param {MdDialog} dialog
   * @param {SnackbarService} snackbarService
   * @param {Store<State>} store
   */

  constructor(public formBuilder: FormBuilder,
              public ises: IseService,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
  }


  ngOnInit() {
    this.userInfo$ = this.store.select(getLoginedUser);
    this.userInfo$.subscribe(
      data => {
        if (data.hasOwnProperty('username')) {
          this.username = data.username;
        }
      }
    )

    this.ISEchangepwdForm = this.formBuilder.group({
      curr_password: ['', Validators.required],
      new_password: ['', Validators.required],
      confirm_password: ['', Validators.required],
      id: ['']
    }, { validator: this.matchingPasswords('new_password', 'confirm_password') });

    this.activatedRoute.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.ISEchangepwdForm['controls']['id'].setValue(this.ise_id);
      this.store.dispatch(new SetISEId(this.ise_id));
    });
  }

  /**
   * Util function to check pwd match
   * @namespace xio.IseChangepwdFormComponent
   * @param {String} new_passwordKey 
   * @param {String} confirm_passwordKey
   * @method matchingPasswords
   * @return {Object}
   */
  matchingPasswords(new_passwordKey, confirm_passwordKey) {
    return (group: FormGroup): { [key: string]: any } => {
      let new_password = group['controls'][new_passwordKey];
      let confirm_password = group['controls'][confirm_passwordKey];
      if (new_password.value !== confirm_password.value) {
        return {
          mismatchedPasswords: true
        };
      }
    };
  }

  /**
   * Submit Form value
   * @namespace xio.IseChangepwdFormComponent
   * @method onSubmit
   * @return {void}
   */
  onSubmit() {
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';
    this.store.dispatch(new ChangeISEPWD({
      data: this.ISEchangepwdForm.value,
      cb: (success, error) => {
        if (success) {
          progressRef.close();
          this.router.navigate(['/ise/']);
          this.snackbarService.toastMe('Password changed Successfully', 2000);
        } else {
          progressRef.close();
          let err_msg = (error.json !== '' || error.json !== undefined
            || error.json !== null) ? error.json() : '';
          let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
          alertRef.componentInstance.title = 'ISE';
          alertRef.componentInstance.message = err_msg !== '' ?
                                               err_msg.result.error.message :
                                               'Bad Request';
          this.ISEchangepwdForm['controls']['curr_password'].setErrors({
            invalidPassword: true
          });
        }
      }
    }))

  }
  ngOnDestroy() {
    window.removeEventListener('click', this.onSubmit.bind(this), false);
  }
}

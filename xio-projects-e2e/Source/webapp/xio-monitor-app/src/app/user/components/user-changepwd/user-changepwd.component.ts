import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../../../user/services/user.service';
import { MdDialog } from '@angular/material';
import { XioProgressComponent, SnackbarService, XioAlertComponent } from './../../../theme/';
import { AuthService } from '../../../auth/services/auth.service';
import { Router } from '@angular/router';
import { ChangeUSERPWD } from '../../../actions/user.actions';
import { Store } from '@ngrx/store';
import { State } from '../../../reducers/';


@Component({
  selector: 'app-user-changepwd',
  templateUrl: './user-changepwd.component.html',
  styleUrls: ['./user-changepwd.component.scss']
})
export class UserChangepwdComponent {

  public userchangepwdForm: FormGroup;

  constructor(public fb: FormBuilder,
              public us: UserService,
              public snackbarService: SnackbarService,
              public dialog: MdDialog,
              public auth: AuthService,
              public router: Router,
              public store: Store<State>) {

    this.userchangepwdForm = this.fb.group({
      curr_password: ['', [Validators.required]],
      new_password: ['', [Validators.required]],
      confirm_password: ['', [Validators.required]]
    },
      { validator: this.matchingPasswords('new_password', 'confirm_password') });
  }

  /**
  * Desc : Util method to match PWD
  * @namespace xio.UserChangepwdComponent
  * @param {string} passwordKey
  * @param {string} confirmpasswordKey
  * @method matchingPasswords
  * @return {void}
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
  * Desc : Button click event to update a userpassword
  * @namespace xio.UserChangepwdComponent
  * @method onSubmit
  * @return {void}
  */

  onSubmit() {
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';


    this.store.dispatch(new ChangeUSERPWD({
      data: this.userchangepwdForm.value,
      cb: (success, error) => {
        if (!error) {
          progressRef.close();
          this.auth.logout();
          this.snackbarService.toastMe('Password changed Successfully', 2000);
          this.router.navigate(['/login']);

        } else {
          progressRef.close();
          let err_msg = (error.json !== '' || error.json !== undefined
            || error.json !== null) ? error.json() : '';

          let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
          alertRef.componentInstance.title = 'User';
          alertRef.componentInstance.message = err_msg !== '' ?
            err_msg.result.error.message :
            'Bad Request';

        }
      }
    }));
  }
}

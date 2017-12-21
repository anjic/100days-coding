import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { MdDialog } from '@angular/material';
import { SnackbarService } from './../../../theme/services/snackbar.service';
import { XioProgressComponent, XioAlertComponent } from './../../../theme/';
import { Store } from '@ngrx/store';
import { State, getUserInfo } from '../../../reducers/';
import { GetUserAction, SaveUserAction, UpdateUserAction } from '../../../actions/user.actions';
import { Observable } from 'rxjs/Observable';
import { User } from './../../models/user';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.scss'],
})

export class UserFormComponent implements OnInit, OnDestroy {

  public userForm: FormGroup;
  public isAddForm: boolean;
  public user_id;
  public user$;

  constructor(public formBuilder: FormBuilder,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
  }

  ngOnInit() {

    this.isAddForm = true;
    this.setFormValidations();
    this.activatedRoute.params.subscribe(params => {
      this.user_id = params['id'];
      if (this.user_id) {
        this.isAddForm = false;
        this.store.dispatch(new GetUserAction(this.user_id));
        this.editFormValue();
      }
    });
  }

  setFormValidations() {

    this.userForm = this.formBuilder.group({
      username: ['', [Validators.required,
      Validators.minLength(4),
      Validators.maxLength(24),
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      first_name: [''],
      last_name: [''],
      email: ['', [Validators.required,
      Validators.pattern(/^(([^<>()\[\]\\.,;:\s@']+(\.[^<>()\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)]
      ],
      password: ['', [Validators.required,
      Validators.minLength(5),
      Validators.maxLength(15)]
      ],
      confirmpassword: ['', Validators.required],
      id: [''],
    }, { validator: this.matchingPasswords('password', 'confirmpassword') });
  }

  /**
   * Desc : Util method to match PWD
   * @namespace xio.UserFormComponent
   * @param {string} passwordKey
   * @param {string} confirmpasswordKey
   * @method matchingPasswords
   * @return {void}
   */
  matchingPasswords(passwordKey, confirmpasswordKey) {
    return (group: FormGroup): { [key: string]: any } => {

      let password = group['controls'][passwordKey],
        confirmpassword = group['controls'][confirmpasswordKey];
      if (password.value !== confirmpassword.value) {

        return {
          mismatchedPasswords: true
        };
      }
    };
  }

  /**
   * Desc : Fetch and set Form data to update
   * @namespace xio.UserFormComponent
   * @method editFormValue
   * @return {void}
   */
  editFormValue() {

    this.user$ = this.store.select(getUserInfo).subscribe(
      (data: User) => {
        if (Object.keys(data).length !== 0) {
          let user_data = data;
          this.userForm['controls']['username'].setValue(user_data['username']);
          this.userForm['controls']['username'].disable();
          this.userForm['controls']['first_name'].setValue(user_data['first_name']);
          this.userForm['controls']['last_name'].setValue(user_data['last_name']);
          this.userForm['controls']['email'].setValue(user_data['email']);
          this.userForm['controls']['password'].setValue(user_data['password']);
          this.userForm['controls']['id'].setValue(user_data['id']);
        }
      });
  }

  /**
   * Desc : Button click event to create a user
   * @namespace xio.UserFormComponent
   * @method onSubmit
   * @return {void}
   */

  onSaveCallBack = this.onSaveCallBack || ((success, error) => {

    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';

    if (success) {
      progressRef.close();
      this.snackbarService.toastMe('User created successfully', 2000);
      this.setFormValidations();
      this.router.navigate(['/user/list']);
    } else {
      progressRef.close();
      this.userForm['controls']['username'].setErrors({
        remote: true
      });

    }
  });

  onSubmit() {
    let data = this.userForm.value;
    data.cb = this.onSaveCallBack;
    this.store.dispatch(new SaveUserAction(data));
  }

  onUpdateCallBack = this.onUpdateCallBack || ((success, error) => {

    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';

    if (success) {
      progressRef.close();
      this.snackbarService.toastMe('User updated successfully', 2000);
      this.router.navigate(['/user/list']);
    } else {
      progressRef.close();
      let err_msg = (error.json !== '' || error.json !== undefined || error.json !== null) ? error.json() : '';
      let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
      alertRef.componentInstance.title = 'User';
      alertRef.componentInstance.message = err_msg !== '' ? err_msg.result.error.message : 'Bad Request';
    }
  });

  /**
   * Desc : Button click event to update a user
   * @namespace xio.UserFormComponent
   * @method onUpdateSubmit
   * @return {void}
   */
  onUpdateSubmit() {
    this.userForm['controls']['username'].enable();
    let data = this.userForm.value;
    data['username'] = this.userForm['controls']['username'].value;
    data.cb = this.onUpdateCallBack;
    this.userForm['controls']['username'].disable();
    this.store.dispatch(new UpdateUserAction(data));
  }

  ngOnDestroy() {
    if (this.user$)
      this.user$.unsubscribe();
  }
}

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { SnackbarService } from './../../../theme/services/snackbar.service';
import { XioProgressComponent, XioAlertComponent} from './../../../theme';
import { MdDialog } from '@angular/material';
import { UpdateISE } from '../../../actions/ise-management.actions';
import { State } from '../../../reducers/index';
import { Store } from '@ngrx/store';

@Component({
  selector: 'app-set-ise-password',
  templateUrl: './set-ise-password.component.html',
  styleUrls: ['./set-ise-password.component.scss']
})
export class SetIsePasswordComponent implements OnInit {

  public setPasswordForm: FormGroup;
  public ise_id;

  /**
   * @param {ActivatedRoute} route
   * @param {FormBuilder} formBuilder
   * @param {Router} router
   * @param {SnackbarService} SnackbarService
   * @param {Store<State>} store
   * @param {MdDialog} dialog
   */

  constructor(public formBuilder: FormBuilder,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public mdDialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
  }

  ngOnInit() {

    this.setPasswordForm = this.formBuilder.group({
                           password: ['', Validators.required],
    });

    this.activatedRoute.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
    });
  }

  /**
   * Desc : set PWD controller method
   * @namespace xio.SetIsePasswordComponent
   * @method onSetPassword
   * @return {void}
   */

  onSetPassword() {

    let progressRef = this.mdDialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'Loading....';

    let data = this.setPasswordForm.value;
        data['id'] = this.ise_id;

    this.store.dispatch(new UpdateISE({
      data: data,
      cb: (success, error) => {
        if (!error) {
          progressRef.close();
          this.snackbarService.toastMe('ISE Updated Successfully', 2000);
          this.router.navigate(['/ise/' + this.ise_id + '/dashboard']);
        } else {
          progressRef.close();
          let err_msg = (error.json !== '' || error.json !== undefined
                || error.json !== null) ? error.json() : '';

          let alertRef = this.mdDialog.open(XioAlertComponent, { disableClose: true });
              alertRef.componentInstance.title = 'ISE';
              alertRef.componentInstance.message = err_msg !== '' ?
                                                   err_msg.result.error.message :
                                                   'Bad Request';  
          if (error && error.status === 401) {  
            let path = '/ise/' + this.ise_id + '/set-password/';
            this.router.navigate([path]);
          }
        }
      }
    }));
  }
}

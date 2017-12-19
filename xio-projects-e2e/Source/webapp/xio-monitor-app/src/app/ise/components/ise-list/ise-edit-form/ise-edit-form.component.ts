import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { MdDialog } from '@angular/material';
import { SnackbarService, MenuContentService, XioProgressComponent, XioDialogComponent, XioAlertComponent } from '../../../../theme/';
import { Store } from '@ngrx/store';
import { getISEId, State, getAllIseLst, getISEInfo } from '../../../../reducers/index';
import { GetAllISEList, GetISEInfo, Reset, SetISEId, UpdateISE } from '../../../../actions/ise-management.actions';
import { GetAllAction } from 'app/actions/sangroup.action';
import { ISE } from '../../../models/ise';
import { CommonUtil } from '../../../../common/utils/CommonUtil';

@Component({
  selector: 'app-ise-edit-form',
  templateUrl: './ise-edit-form.component.html',
  styleUrls: ['./ise-edit-form.component.scss'],
})
export class IseEditFormComponent extends CommonUtil implements OnInit, OnDestroy {

  public ISEEditForm: FormGroup;
  public ise_id;
  public ise_details;
  public loading_stack;
  public iseId$;
  public iseInfo$;


   /**
   * 
   * @param {FormBuilder} formBuilder
   * @param {activatedRoute} ActivatedRoute
   * @param {router} Router
   * @param {MdDialog} dialog
   * @param {SnackbarService} snackbarService
   * @param {Store<State>} store
   */

  constructor(public formBuilder: FormBuilder,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
    super();
    this.loading_stack = {
      ise_details: false,
      ise_details_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.iseId$ = this.store.select(getISEId).subscribe(
      data => {
        this.ise_id = data;
      }
    );

    this.ISEEditForm = this.formBuilder.group({
      name: ['', Validators.required],
      id: [''],
      contactname: ['', [Validators.maxLength(60),
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      address: ['', [Validators.maxLength(60)]],
      location: ['', [Validators.maxLength(32)]],
      contactemail: ['',
        [Validators.pattern(/^(([^<>()\[\]\\.,;:\s@']+(\.[^<>()\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)
        ]],
      contactphone: ['', [Validators.maxLength(16)]],
      prefered_ise: [''],
    });
    this.activatedRoute.params.subscribe(params => {
      this.loading_stack.ise_details = false;
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
    });
    this.iseInfo$ = this.store.select(getISEInfo).subscribe(
      (data: ISE) => {
        if (data) {
          this.loading_stack.ise_details = true;
          this.ise_details = data;
          this.ISEEditForm['controls']['name'].setValue(this.ise_details['ise_name']);
          this.ISEEditForm['controls']['id'].setValue(this.ise_id);
          this.ISEEditForm['controls']['contactname'].setValue(this.ise_details['contactname']);
          this.ISEEditForm['controls']['address'].setValue(this.ise_details['address']);
          this.ISEEditForm['controls']['location'].setValue(this.ise_details['location']);
          this.ISEEditForm['controls']['contactemail'].setValue(this.ise_details['contactemail']);
          this.ISEEditForm['controls']['contactphone'].setValue(this.ise_details['contactphone']);
          this.ISEEditForm['controls']['prefered_ise'].setValue(this.ise_details['prefered']);

          this.ISEEditForm.markAsPristine();
          this.ISEEditForm.markAsUntouched();

        } else if (!data && this.ise_id) {
          let payLoad = {
            ise_id: this.ise_id,
            cb: (success, error) => {
              if (!error) {
              } else {
                this.loading_stack.ise_details = true;
                let err = error.json().result.error.message;
                const alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
                alertRef.componentInstance.title = 'ISE';
                alertRef.componentInstance.message = err;
                alertRef.afterClosed().subscribe(result => {
                  const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
                  progressRef.componentInstance.progress_data = 'processing';
                  if (result === 'Ok') {
                    progressRef.close();
                    this.router.navigate(['/ise/']);
                  }
                });
              }
            }
          };
          this.store.dispatch(new GetISEInfo(payLoad));
        } error => {
            this.catchError(error);
        };
      });
  }

 
  /**
   * Submit Form value
   * @namespace xio.IseEditFormComponent 
   * @method onSubmit
   * @return {void}
   */
  onSubmit() {
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';

    let data = this.getDirtyValues(this.ISEEditForm);
    let payLoad = {
      data: data,
      id: this.ise_id
    };
    this.store.dispatch(new UpdateISE({
      data: payLoad,
      cb: (success, error) => {
        if (success) {
          progressRef.close();
          this.snackbarService.toastMe('ISE Updated Successfully', 2000);
          this.store.dispatch(new GetAllAction({}));
          this.router.navigate(['/ise/']);
        } else {
          progressRef.close();
          this.catchError(error);
        }
      }
    }));
  }


  /**
   * Catching Error
   * @namespace xio.IseEditFormComponent 
   * @method catchError
   */
  catchError(error) {
    let err_msg = (error.json !== '' || error.json !== undefined
                                     || error.json !== null) ? error.json() : '';
    let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'ISE';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             err_msg.result.error.message :
                                             'Bad Request';
  }

  ngOnDestroy() {
    this.store.dispatch(new Reset());
    if (this.iseId$) {
      this.iseId$.unsubscribe();
    }
    if (this.iseInfo$) {
      this.iseInfo$.unsubscribe();
    }
    // unbinding Event Listeners
    window.removeEventListener('click', this.onSubmit.bind(this), false);

  }
}

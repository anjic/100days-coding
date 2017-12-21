import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { MdDialog } from '@angular/material';
import { SnackbarService, XioProgressComponent, XioAlertComponent } from './../../../theme/';
import { getSanGroupState, State } from '../../../reducers';
import { Store } from '@ngrx/store';
import { AddSanGroupAction, GetSanGroupAction, UpdateSanGroupAction } from '../../../actions/sangroup.action';
import { GetMenuAction } from "../../../actions/menu.action";


@Component({
  selector: 'app-sangroup-form',
  templateUrl: './sangroup-form.component.html',
  styleUrls: ['./sangroup-form.component.scss']
})

export class SangroupFormComponent implements OnInit, OnDestroy {

  public sangroupForm: FormGroup;
  public isAddForm: Boolean;
  public loading_stack;
  public sangroup_id;
  public SANGroup$;

  constructor(public formBuilder: FormBuilder,
              public router: Router,
              public activatedRoute: ActivatedRoute,
              public snackbarService: SnackbarService,
              public dialog: MdDialog,
              public store: Store<State>) {

    this.loading_stack = {
      sg_getdata: false,
      sg_getdata_text: 'SAN Group details are loading......'
    };
  }

  ngOnInit() {

    this.isAddForm = true;
    this.sangroupForm = this.formBuilder.group({
      sangroup_name: ['', [Validators.required,
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      comment: [''],
      created_by: '1',
      modified_by: '1',
      sangroup_id: ['']
    });

    this.activatedRoute.params.subscribe(params => {
      this.sangroup_id = params['sg_id'];
      if (this.sangroup_id) {
        this.isAddForm = false;
      }
    });


    /**
  * Desc : Used for getting sangroup details on load when component
  *        gets initialized.
  * Store State Name : getSanGroupState
  */

    this.SANGroup$ = this.store.select(getSanGroupState).subscribe(data => {
      let _data = data.sanGroupLst.filter((s) => {
        if (s['sangroup_id'] == this.sangroup_id) {
          return s;
        }
      });
      if (!this.isAddForm) {

        if (_data.length > 0 || Object.keys(data.SanGroupDetails).length > 0) {

          const sangroup_data: any = _data.length > 0 ? _data[0] :
            data.SanGroupDetails;
          this.sangroupForm['controls']['sangroup_name'].setValue(sangroup_data.sangroup_name);
          this.sangroupForm['controls']['comment'].setValue(sangroup_data.comment);
          this.sangroupForm['controls']['sangroup_id'].setValue(sangroup_data.sangroup_id);
          this.loading_stack.sg_getdata = false;

        } else {

          this.loading_stack.sg_getdata = true;
          this.loading_stack.sangroup_details = true;
          this.store.dispatch(new GetSanGroupAction({
            ise_id: this.sangroup_id,
            cb: (success, error) => {
              if (!error) {
                this.loading_stack.sg_getdata = false;
              } else {
                let err_msg = (error.json !== '' || error.json !== undefined
                  || error.json !== null) ? error.json() : '';

                let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
                alertRef.componentInstance.title = 'SAN Group';
                alertRef.componentInstance.message = err_msg !== '' ?
                  err_msg.result.error.message :
                  'Bad Request';
              }
            }
          }));
        }
      }
    });
  }

  /**
   * Desc : util method to re-direct to particular route
   * @namespace xio.SangroupFormComponent
   * @method navigateTo
   * @param {any} event - event
   * @param {string} path - relative / route path to re-direct to
   * @return {void}
   */
  navigateTo(event: any, path: string) {
    event.stopPropagation();
    this.router.navigate([path]);
  }


  /**
   * Desc : Button click event to create/update a san-group
   * @namespace xio.SangroupFormComponent
   * @method onSubmit
   * @param {Object} e - btn click event
   * @return {void}
   */
  onSubmit(e) {
    const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'processing';
    this.sangroupForm.value.cb = (res, err) => {
      if (res) {
        this.navigateTo(e, '/san-group');
        this.snackbarService.toastMe('SAN Group' + (this.isAddForm ? ' Created' : ' updated') + ' Successfully', 2000);
        progressRef.close();
        this.store.dispatch(new GetMenuAction({}));
      } else if (err) {
        progressRef.close();
        if (this.isAddForm) {
          this.sangroupForm['controls']['sangroup_name'].setErrors({
            remote: true
          });
        }
      }
    };
    this.store.dispatch((this.isAddForm ? (new AddSanGroupAction(this.sangroupForm.value)) : (new UpdateSanGroupAction(this.sangroupForm.value))));
  }

  ngOnDestroy() {
    if (this.SANGroup$) {
      this.SANGroup$.unsubscribe();
    }
  }
}

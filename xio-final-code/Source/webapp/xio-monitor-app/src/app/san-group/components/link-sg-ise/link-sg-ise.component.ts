import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { SnackbarService, XioProgressComponent, XioAlertComponent } from './../../../theme/index';
import { MdDialog } from '@angular/material';
import { getSanGroupISEMap, State } from '../../../reducers';
import { Store } from '@ngrx/store';
import { GetAllAction, GetISEListAction, SanGroupReset, UpdateISEListAction } from '../../../actions/sangroup.action';
import { GetMenuAction } from "../../../actions/menu.action";

@Component({
  selector: 'app-link-sg-ise',
  templateUrl: './link-sg-ise.component.html',
  styleUrls: ['./link-sg-ise.component.scss']
})
export class LinkSgIseComponent implements OnInit, OnDestroy {

  public sg_ise_link_form: FormGroup;
  public manage_ise_list: Array<Object>;
  public no_ise_found: boolean;
  public loading_stack;
  public sangroup_id;
  public SANGrpIseLinkMap$;

  constructor(public formBuilder: FormBuilder,
    public activatedRoute: ActivatedRoute,
    public router: Router,
    public snackbarService: SnackbarService,
    public dialog: MdDialog,
    public store: Store<State>) {

    this.loading_stack = {
      ise_details: false,
      ise_details_text: 'Loading.....'
    };
    this.no_ise_found = false;
    this.manage_ise_list = [];
    this.SANGrpIseLinkMap$ = this.store.select(getSanGroupISEMap)
      .subscribe(data => {
        this.loading_stack.ise_details = false;
        this.manage_ise_list = data;
        this.no_ise_found = !data.length;
        this.sg_ise_link_form = this.formBuilder.group({
          id: [''],
          ise: this.formBuilder.array([])
        });

        for (let i = 0; i < data.length; i++) {
          const v = data[i]['id'],
            lbl = data[i]['ise_name'] + ' - ' + data[i]['ip_primary'],
            checked = data[i]['checked'];
          this.addISE(v, lbl, 'ise', checked);
        }
      }, error => {
        console.error(error);
        this.loading_stack.ise_details = false;
        let err_msg = (error.json !== '' || error.json !== undefined
          || error.json !== null) ? error.json() : '';

        let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
        alertRef.componentInstance.title = 'SAN Group';
        alertRef.componentInstance.message = err_msg !== '' ?
          err_msg.result.error.message : 'Bad Request';
      }
      )
  }

  ngOnInit() {

    this.activatedRoute.params.subscribe(params => {
      this.sangroup_id = params['sg_id'];
      if (this.sangroup_id) {
        this.store.dispatch(new GetISEListAction(this.sangroup_id));
      }
    });
  }

  /**
   * Desc : Initialize ISE
   * @namespace xio.LinkSgIseComponent
   * @param {any} v
   * @param {string} lbl
   * @param {boolean} status
   * @method initISE
   * @return {FormGroup}
   */

  initISE(v: string, lbl: string, status: boolean) {
    return this.formBuilder.group({ ise: [status, Validators.required], label: lbl, ise_id: v, actual_status: status });
  }

  /**
   * Desc : push ISE data into form
   * @namespace xio.LinkSgIseComponent
   * @param {any} v
   * @param {string} lbl
   * @param {boolean} status
   * @method addISE
   * @return {void}
   */

  addISE(v: string, lbl: string, type: string, status: boolean) {
    const control = <FormArray>this.sg_ise_link_form['controls'][type];
    control.push(this.initISE(v, lbl, status));
  }

  /**
   * Desc : get ISE label's
   * @namespace xio.LinkSgIseComponent
   * @param {string} type
   * @param {number} i
   * @method getISELabel
   * @return {FormGroup}
   */

  getISELabel(type: string, i: number) {
    const control = <FormArray>this.sg_ise_link_form['controls'][type];
    return control.value[i].label;
  }

  /**
   * Desc : update's SgISE link with San-group
   * @namespace xio.LinkSgIseComponent
   * @method updateSgISELink
   * @return {void}
   */

  updateSgISELink() {
    const form_data = this.sg_ise_link_form.value,
      data = {
        added: [],
        removed: [],
        san_group_id: this.sangroup_id
      };

    for (let i = 0; i < form_data['ise'].length; i++) {
      if (form_data['ise'][i]['actual_status'] !== form_data['ise'][i]['ise']) {
        if (form_data['ise'][i]['ise']) {
          data.added.push(form_data['ise'][i]['ise_id']);
        } else {
          data.removed.push(form_data['ise'][i]['ise_id']);
        }
      }
    }

    const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'processing';

    data['cb'] = (res, err) => {
      if (res) {

        this.snackbarService.toastMe('ISE Successfully Updated in SAN Group', 2000);
        /*Update ISE in sangroup list*/
        this.store.dispatch(new GetAllAction());
        /*Update ISE in sangroup list in side Menu*/
        this.store.dispatch(new GetMenuAction({}));
        /*Resetting Sangroup list*/
        this.store.dispatch(new SanGroupReset());
        progressRef.close();
        this.router.navigate(['/san-group/' + this.sangroup_id + '/dashboard/']);
      } else if (err) {

        progressRef.close();
      }
    };
    this.store.dispatch(new UpdateISEListAction(data));
  }

  /**
   * Desc : util method to re-direct to particular route
   * @namespace xio.LinkSgIseComponent
   * @method navigateTo
   * @param {any} event - event
   * @return {void}
   */

  navigateTo(event: any) {
    event.stopPropagation();
    this.router.navigate(['/san-group/' + this.sangroup_id + '/dashboard']);
  }

  ngOnDestroy() {
    if (this.SANGrpIseLinkMap$) {
      this.SANGrpIseLinkMap$.unsubscribe();
    }

    this.manage_ise_list.length = 0;
    this.sangroup_id = '';
  }

}

import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { IseService } from '../../../services/ise.service';
import { Store } from '@ngrx/store';
import { State, getISEInfo, getIseDetail } from '../../../../reducers/index';
import { GetISEInfo, SetISEId, ChangeISEIP, GetIseDetail } from '../../../../actions/ise-management.actions';
import { MdDialog } from '@angular/material';
import { XioAlertComponent, XioProgressComponent, SnackbarService } from './../../../../theme/';
import { ISE } from './../../../models/ise';


@Component({
  selector: 'app-ise-modify-form',
  templateUrl: './ise-modify-form.component.html',
  styleUrls: ['./ise-modify-form.component.scss']
})
export class IseModifyFormComponent implements OnInit,OnDestroy{

public IseModifyForm: FormGroup;
public ise_id;
public ise_details;
public loading_stack;


  /**
   * 
   * @param {FormBuilder} formBuilder
   * @param {IseService} ises
   * @param {activatedRoute} ActivatedRoute
   * @param {router} Router
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
    this.loading_stack = {
      ise_details: false,
      ise_details_text: 'Loading.....'
    };
  }

  ngOnInit() {

    this.IseModifyForm = this.formBuilder.group({
      modify_ip: ['', [Validators.required]],
    }, { validator: this.validateIseIP('modify_ip') });

    this.loading_stack.ise_details = true;
    this.activatedRoute.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.store.dispatch(new SetISEId(this.ise_id));
    });
    this.store.dispatch(new GetIseDetail(this.ise_id));
    this.store.select(getIseDetail).subscribe((data: ISE) => {
      this.loading_stack.ise_details = false;
      this.ise_details = data;

    }, error => {
      this.loading_stack.ise_details = false;
      this.catchError(error);
    });
  }

  /**
   * Desc : Button click event to update ise ip address
   * @namespace xio.IseModifyFormComponent
   * @method onSubmit
   * @return {void}
   */

  onSubmit() {

    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';

    this.store.dispatch(new ChangeISEIP({
      data: this.IseModifyForm.value,
      ise_id: this.ise_id,
      cb: (success, error) => {
        if (success) {
          progressRef.close();
          this.router.navigate(['/ise/']);
          this.snackbarService.toastMe('IPAddress changed Successfully', 2000);
        } else {
          progressRef.close();
         this.catchError(error);
        }
      }
    }));
  }

  /**
   * Desc : To validate ise ip address
   * @namespace xio.IseModifyFormComponent
   * @method validateIseIP
   * @return {void}
   */

  validateIseIP(modify_ipkey) {
    return (group: FormGroup): { [key: string]: any } => {
      let ip_domain_value = group.root['controls'][modify_ipkey].value;
      let no = parseInt(ip_domain_value.charAt(0), 10);
      const domainPattern = /^(?!.*[._]{2})[a-zA-Z0-9.-]+[a-zA-Z0-9.-]+$/;
      const regexIP = /^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/;

      if (ip_domain_value.length !== 0) {
        if (no) {
          if (regexIP.test(ip_domain_value)) {
            return null;
          } else {
            return {
              regexIP: {
                valid: false
              }
            };
          }
        } else {
          if (domainPattern.test(ip_domain_value)) {
            return null;
          } else {
            return {
              regexIP: {
                valid: false
              }
            };
          }
        }
      }
    };
  }

    /**
   * Desc : To catch error
   * @namespace xio.IseModifyFormComponent
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
    // Un binding Event Listeners
    window.removeEventListener('click', this.onSubmit.bind(this), false);

   }
}

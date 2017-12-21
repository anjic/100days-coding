import {Component, OnInit, OnDestroy} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {ActivatedRoute} from '@angular/router';
import {MdDialog} from '@angular/material';
import {XioProgressComponent} from './../../../../theme/xio-progress/xio-progress.component';
import {XioAlertComponent} from './../../../../theme/xio-alert/xio-alert.component';
import {SnackbarService} from './../../../../theme/services/snackbar.service';
import {timeZone} from './../../../../../assets/data/timezone';
import {Store} from '@ngrx/store';
import {getChronoTimeZone, State} from '../../../../reducers';
import {GetTimeZone, UpdateTimeZone} from '../../../../actions/ise-settings.actions';
import {DateAndTimeUtil} from '../../../../common/utils/DateAndTimeUtil';
import { TimeSettings } from '../../../models/time_settings';
@Component({
  selector: 'app-time-zone',
  templateUrl: './time-zone.component.html',
  styleUrls: ['./time-zone.component.scss']
})
export class TimeZoneComponent extends DateAndTimeUtil implements OnInit, OnDestroy {

  public timezoneForm: FormGroup;
  public timezone_data;
  public ise_id;
  public timezone_list = [];
  public isForm: boolean;
  public timeZoneLoading: boolean;
  public chronoTimeZone$;
  public picker: string;

   /**
   * 
   * @param {FormBuilder} formBuilder
   * @param {ActivatedRoute} activatedRoute
   * @param {MdDialog} dialog
   * @param {SnackbarService} snackbarService
   * @param {Store<State>} store
   */


  constructor(public formBuilder: FormBuilder,
              public activatedRoute: ActivatedRoute,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
    super();
    this.isForm = false;
    this.timeZoneLoading = false;
    this.timezone_data = <TimeSettings>{};
    this.picker = 'picker';
  }

  ngOnInit() {
    this.initTimeZoneInfo();
    this.activatedRoute.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.timeZoneLoading = true;
      this.store.dispatch(new GetTimeZone({ise_id: this.ise_id}));
      this.setTimeZoneData();
    });
    this.timezone_list = timeZone;    
  }

  /**
   * Getting Data from store and setting it in the Form to edit
   * @namespace xio.TimeZoneComponent 
   * @method setTimeZoneData
   */

  setTimeZoneData() {
    this.chronoTimeZone$ = this.store.select(getChronoTimeZone).subscribe(
      (data: TimeSettings) => {        
        this.timezone_data = data;
        this.timezoneForm['controls']['date'].setValue(new Date(this.timezone_data.date));
        this.timezoneForm['controls']['time'].setValue(new Date(this.timezone_data.date + ' ' + this.timezone_data.time));
        this.timezoneForm['controls']['timezone'].setValue(this.timezone_data.timezone);
        this.timezoneForm['controls']['dst'].setValue((this.timezone_data.dst == 'disabled') ? false : true);
          if (this.timezone_data && this.timezone_data.ntp) {
            this.timezoneForm['controls']['ntpmode'].setValue(this.timezone_data.ntp.ntpmode);
            this.timezoneForm['controls']['ntpserver'].setValue(this.timezone_data.ntp.ntpserver);
          }
        if (this.timeZoneLoading) {
          this.timeZoneLoading = false;
        }
      },
      error => {
        this.catchError(error);
      }
    );
  }

  /**
   * Used to Toggle to the Form and Dispalying Data
   * @namespace xio.TimeZoneComponent 
   * @method toggleForm
   */

  toggleForm() {
    this.setTimeZoneData();
    this.isForm = !this.isForm;
  }

  /**
   * Initialising the Fields for TimeZone form
   * @namespace xio.TimeZoneComponent 
   * @method initTimeZoneInfo
   */

  initTimeZoneInfo() {
    this.timezoneForm = this.formBuilder.group({
      date: [''],
      time: [''],
      timezone: [''],
      dst: [''],
      ntpmode: [''],
      ntpserver: [''],
    });

  }

   /**
   * Updating Time settings
   * @namespace xio.TimeZoneComponent 
   * @method onTimeUpdate
   */

  onTimeUpdate() {
    let data = {chronometer: this.timezoneForm.value};
    data['chronometer']['dst'] = (data['chronometer']['dst']) ? 'enabled' : 'disabled';
    data['chronometer']['date'] = this.getFormattedDate(data['chronometer']['date']);
    data['chronometer']['time'] = this.getFormattedTime(data['chronometer']['time']);
    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    progressRef.componentInstance.progress_data = 'Loading....';
    this.store.dispatch(new UpdateTimeZone({
      ise_id: this.ise_id,
      data: data,
      cb: (response, error) => {
        if (response) {
          progressRef.close();
          this.snackbarService.toastMe('Time updates completed', 2000);
          this.toggleForm();
          this.getTimezone();
        }else if (error) {
          progressRef.close();
          this.catchError(error);
        }
      }
    }));
  }

   /**
   * Getting the Data of DST
   * @namespace xio.TimeZoneComponent 
   * @method getTimezone
   */

  getTimezone() {
    this.chronoTimeZone$ = this.store.select(getChronoTimeZone).subscribe(
      (data: TimeSettings) => {
        this.timezone_data = data;
        this.timezoneForm['controls']['dst'].setValue((this.timezone_data.dst == 'disabled') ? false : true);
        if (this.timeZoneLoading) {
          this.timeZoneLoading = false;
        }
      },
      error => {
        this.catchError(error);
      }
    );
    this.store.dispatch(new GetTimeZone({ise_id: this.ise_id}));
  }
  

   /**
   * On clicking Cancel toggling to Displayed Data
   * @namespace xio.TimeZoneComponent 
   * @method onCancel
   */
  onCancel() {
    this.toggleForm();    
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
        alertRef.componentInstance.title = 'Time Settings';
        alertRef.componentInstance.message = err_msg !== '' ?
                                             err_msg.result.error.message :
                                             'Bad Request';
  }

  ngOnDestroy() {
    if (this.chronoTimeZone$) { 
        this.chronoTimeZone$.unsubscribe();
    }  
    // Un Binding Event Listeners
      window.removeEventListener('click', this.onCancel.bind(this), false);
      window.removeEventListener('click', this.onTimeUpdate.bind(this), false);
      window.removeEventListener('click', this.toggleForm.bind(this), false);
  }
}

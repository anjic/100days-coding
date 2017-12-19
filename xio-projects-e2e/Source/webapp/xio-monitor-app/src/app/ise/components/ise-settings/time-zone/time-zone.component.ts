import {Component, OnInit, OnDestroy} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {ActivatedRoute} from '@angular/router';
import {MdDialog} from '@angular/material';
import {XioProgressComponent} from './../../../../theme/xio-progress/xio-progress.component';
import {SnackbarService} from './../../../../theme/services/snackbar.service';
import {timeZone} from './../../../../../assets/data/timezone'
import {Store} from '@ngrx/store';
import {getChronoTimeZone, State} from '../../../../reducers';
import {GetTimeZone, UpdateTimeZone} from '../../../../actions/ise-settings.actions';
import {DateAndTimeUtil} from "../../../../common/utils/DateAndTimeUtil";

@Component({
  selector: 'app-time-zone',
  templateUrl: './time-zone.component.html',
  styleUrls: ['./time-zone.component.scss']
})
export class TimeZoneComponent extends DateAndTimeUtil implements OnInit, OnDestroy {

  public timezoneForm: FormGroup;
  public timezone_data: any;
  public ise_id: any;
  public timezone_list = [];
  public isForm: boolean = false;
  public date;
  public time;
  public dst;
  public timezone;
  public timeZoneLoading: boolean = false;
  public chronoTimeZone$;
  public picker= 'picker';

  constructor(public fb: FormBuilder,
              public route: ActivatedRoute,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store: Store<State>) {
    super();
    this.isForm = false;
  }

  ngOnInit() {
    this.initTimeZoneInfo();
    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.timeZoneLoading = true;
      this.store.dispatch(new GetTimeZone({ise_id: this.ise_id}));
      this.setTimeZoneData();
    });
    this.timezone_list = timeZone;    
  }

  setTimeZoneData(){
    this.chronoTimeZone$ = this.store.select(getChronoTimeZone).subscribe(
      data => {        
        this.timezone_data = data;
        this.timezoneForm['controls']['date'].setValue(new Date(this.timezone_data.date));
        this.timezoneForm['controls']['time'].setValue(new Date(this.timezone_data.date + ' ' + this.timezone_data.time));
        this.timezoneForm['controls']['timezone'].setValue(this.timezone_data.timezone);
        this.timezoneForm['controls']['dst'].setValue((this.timezone_data.dst == 'disabled') ? false : true);
         if(this.timezone_data && this.timezone_data.ntp){
        this.timezoneForm['controls']['ntpmode'].setValue(this.timezone_data.ntp.ntpmode);
        this.timezoneForm['controls']['ntpserver'].setValue(this.timezone_data.ntp.ntpserver);
        }
        
        if (this.timeZoneLoading) {
          this.timeZoneLoading = false;
        }

      },
      err => {
        console.error(err);
      }
    );
  }

  toggleForm() {
    this.setTimeZoneData();
    this.isForm = !this.isForm;
  }

  initTimeZoneInfo() {
    this.timezoneForm = this.fb.group({
      date: [''],
      time: [''],
      timezone: [''],
      dst: [''],
      ntpmode:[''],
      ntpserver:[''],
    });

  }

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
      cb: (res, err) => {
        if (res) {
          progressRef.close();
          this.snackbarService.toastMe('Time updates completed', 2000);
          this.toggleForm();
          this.getTimezone();
        }
        else if (err) {
          progressRef.close();
        }
      }
    }));
  }

  onCancel() {

    this.toggleForm();    
  }

  getTimezone(){
    this.chronoTimeZone$ = this.store.select(getChronoTimeZone).subscribe(
      data => {
        this.timezone_data = data;
        this.timezoneForm['controls']['dst'].setValue((this.timezone_data.dst == 'disabled') ? false : true);
        if (this.timeZoneLoading) {
          this.timeZoneLoading = false;
        }

      },
      err => {
        console.error(err);
      }
    );
    this.store.dispatch(new GetTimeZone({ise_id: this.ise_id}));
  }

 ngOnDestroy() {
    this.chronoTimeZone$.unsubscribe();
  }
}

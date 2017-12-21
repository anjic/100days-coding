import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {IseService} from './../../services/ise.service';
import {Store} from '@ngrx/store';
import {getISECardInfo, State} from '../../../reducers';
import {GetISECardInfo, SetISEId} from 'app/actions/ise-management.actions';
import {XioAlertComponent} from '../../../theme/xio-alert/xio-alert.component';
import {MdDialog} from '@angular/material';
import {ISECardInfo} from '../../models/ise_card_info';

@Component({
  selector: 'app-ise-landing',
  templateUrl: './ise-landing.component.html',
  styleUrls: ['./ise-landing.component.scss']
})
export class IseLandingComponent implements OnInit, OnDestroy {

  // Initialize variables
  public ise_id: any;
  public selectedIndex: Number = 0;
  public interval_id: any;
  public iseCardInfo$;
  public ise_card_details: ISECardInfo;
  public type: any;
  public alertRef;
  public iseDetails: any;
  public display_time: string;
  public total_time;

  public tabs: any = [
    'dashboard',
    'pools',
    'volume',
    'host',
    'performance',
    'settings',
    'hardwareinfo'
  ];

  /**
   *
   * @param {ActivatedRoute} route
   * @param {Router} router
   * @param {IseService} ises
   * @param {Store<State>} store
   * @param {MdDialog} dialog
   */
  constructor(public route: ActivatedRoute,
              public router: Router,
              public ises: IseService,
              public store: Store<State>,
              public dialog: MdDialog) {
    this.alertRef = null;
    this.ise_card_details = null;
  }


  ngOnInit() {
    this.route.params.subscribe(params => {
      this.selectedIndex = this.tabs.indexOf(this.router.url.split('/')[3]);
      this.ise_id = params['ise_id'];
      if (this.ise_id !== params['ise_id']) {
          this.store.dispatch(new SetISEId(this.ise_id));
      }
      // Get ISE Card details
      this.store.dispatch(new GetISECardInfo(this.ise_id));
      // Subscribe ise card details from store.
      this.iseCardInfo$ = this.store.select(getISECardInfo).subscribe(
        (data: ISECardInfo ) => {
          let isedet = '', detail;
          if (data && data['serial_no']) {
             this.ise_card_details = data;
             this.countdown(this.ise_card_details.time);
             this.type = data['serial_no'].substring(0, 3) === 'USE' ? 'G4' :  'G3';
             if (data['locked'] === true) {
               this.openUnlockDialog(data);
             }
             if (this.ise_card_details.status['details'].hasOwnProperty('details')) {
                detail = this.ise_card_details.status['details']['details'];
                detail.forEach( function (statusObj) {
                     isedet += statusObj + ',  ';
              });
              isedet = isedet.replace(/,\s*$/, '');
              this.iseDetails = isedet;
            } else {
              this.iseDetails = this.ise_card_details.status['details']['detail'];
            }
            this.iseDetails = this.iseDetails.trim();
          }
        }, err => {
          if (err.status === 401) {
            let path = '/ise/' + this.ise_id + '/set-password/';
            this.router.navigate([path]);
          }
        });
        if (this.interval_id) {
          clearInterval(this.interval_id);
        }
        this.interval_id = setInterval(() => {
          if (this.ise_id) {
            this.store.dispatch(new GetISECardInfo(this.ise_id));
          }
        }, 30000);
    });


  }


  /**
   * ISE UnLock
   * @namespace IseLandingComponent
   * @param {Object} data
   * @method openUnlockDialog
   * @return {void}
   */


  openUnlockDialog(data: any) {
    if (this.alertRef == null && this.alertRef === undefined) {
      this.alertRef = 1;
      const alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.message = data.serial_no + '-' + ' ISE is locked and requires encryption passkey';
            alertRef.componentInstance.title = 'ISE Locked';
            alertRef.afterClosed().subscribe(result => {
        if (result === 'Ok' ) {
          this.router.navigate(['/ise/' + this.ise_id + '/ise-unlock']);
          this.alertRef = null;
        }
      });
    }
  }


  /**
   * Get ISE status
   * @namespace IseLandingComponent
   * @method iseStatus
   * @return {void}
   */
  iseStatus() {
    let status, status_detail ;
    status = this.ise_card_details.status._attr.string;
    status_detail = this.ise_card_details.status['details'].hasOwnProperty('details') ?
                    this.ise_card_details.status['details']['details'] :
                    [this.ise_card_details.status['details']['detail']];

    if (status.toLowerCase() === 'uninitialized') {
            let path = '/ise/' + this.ise_id + '/settings/';
            this.selectedIndex = 5;
            this.router.navigate([path]);
    } else if (status.toLowerCase() === 'warning' &&
              ((status_detail.indexOf('Spare capacity could be improved') >= 0) ||
              (status_detail.indexOf('Pending Create') >= 0) || ((status_detail.indexOf('Pending_Delete') >= 0)))) {
              let path = '/ise/' + this.ise_id + '/pools/';
              this.selectedIndex = 1;
              this.router.navigate([path]);
    } else if (status.toLowerCase() === 'warning' &&
              (status_detail.indexOf('Running_out_of_capacity') >= 0)) {
              let path = '/ise/' + this.ise_id + '/pools/';
              this.selectedIndex = 1;
              this.router.navigate([path]);
    } else if (status.toLowerCase() === 'warning' &&
              (status_detail.indexOf('Component Degraded') >= 0) ||
              (status_detail.indexOf('One or more MRCs in degraded state') >= 0)) {
              let path = '/ise/' + this.ise_id + '/hardwareinfo/';
              this.selectedIndex = 6;
              this.router.navigate([path]);
    } else if (status.toLowerCase() === 'critical' &&
              (status_detail.indexOf('Drives need replacement') >= 0)) {
              let path = '/ise/' + this.ise_id + '/pools/';
              this.selectedIndex = 1;
              this.router.navigate([path]);
    } else if (status.toLowerCase() === 'operational' &&
              (status_detail.indexOf('Spare capacity could be improved') >= 0)) {
              let path = '/ise/' + this.ise_id + '/pools/';
              this.selectedIndex = 1;
              this.router.navigate([path]);
    } else if (status.toLowerCase() === 'operational') {
              let path = '/ise/' + this.ise_id + '/hardwareinfo/';
              this.selectedIndex = 6;
              this.router.navigate([path]);
    }

  }

  /**
   * goto util
   * @namespace xio.IseLandingComponent
   * @param {String} m
   * @method goto
   * @return {void}
   */
  goto(m: String, i: number) {
    let path = '/ise/' + this.ise_id + m;
    this.router.navigate([path]);
  }

  /**
   * change tab click event
   * @namespace xio.IseLandingComponent
   * @param {Object} e - event
   * @method changeTab
   * @return {void}
   */
  changeTab(e) {
    if (this.tabs[e.index]) {
      this.router.navigateByUrl('/ise/' + this.ise_id + '/' + this.tabs[e.index]);
    }
  }

  /**
   *  ISE PlatformType
   * @namespace xio.IseLandingComponent
   * @method  getPlatformType
   * @return {void}
   */

  getPlatformType() {
    this.ises.getISE(this.ise_id).subscribe(
      data => {
        this.type = data.serial_no.substring(0, 3) === 'USE' ? 'G4' : 'G3';
      });
  }

  /**
   * Get Banner
   * @namespace xio.IseLandingComponent
   * @param {Object} d
   * @method getBanner
   * @return {String}
   */

  getBanner(d: any) {
    if (d && d['status'] && d['status']['_attr']['string'] === 'Warning') {
      return 'main-bar-warning';
    } else if (d && d['status'] && d['status']['_attr']['string'] === 'Operational') {
      return 'main-bar-operational ';
    } else {
      return 'main-bar-critical';
    }
  }

  /**
   * This method is used for displaying UP Time
   * for ISE
   * @param iseInitTime
   */
  countdown( iseInitTime ) {
    let _iseInitTime = iseInitTime.split(':'),
        hours = _iseInitTime[0],
        mins = _iseInitTime[1],
        sec = _iseInitTime[2],
        days = 0;

        ( sec === 59) ? sec = 0 : sec++ ;
        ( sec === 0 && mins === 59) ? mins = 0 : mins++;
        ( mins === 0 && hours === 23 ) ? hours = 0 : hours++ ;
        ( hours === 0 && mins === 0 && sec === 0) ? days++ : days = 0 ;

        this.display_time = this.pad(hours, 2, 0) + ':' +
                            this.pad(mins, 2, 0) + ':' +
                            this.pad(sec, 2, 0);

        this.total_time = this.pad(days, 1, 0) + ' ' +
                          ' ' + 'Days' + ',' + ' ' + this.pad(hours, 2, 0) + ' ' +
                          ' ' + 'Hours' + ',' + ' ' + this.pad(mins, 2, 0) + ' ' +
                          ' ' + 'Minutes' + ',' + ' ' +
                          ' ' + this.pad(sec, 2, 0) + '  ' + ' Seconds';

    }

  /**
   * It used adding spaces.
   * @param number
   * @param width
   * @param padding
   * @returns {string}
   */
    pad(number, width, padding) {
      let string = number.toString();
      if (!width || string.length >= width) {
        return string;
      }
      return new Array(width - string.length + 1).join(padding || '0') + string;
    }


  ngOnDestroy() {
    this.iseCardInfo$.unsubscribe();
    if (this.interval_id) {
      clearInterval(this.interval_id);
    }
  }
}

import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute,Router} from '@angular/router';
import {IseService, SnmpService} from './../../services/';
import {FormBuilder, FormGroup} from '@angular/forms';
import {MdDialog} from '@angular/material';
import {XioDialogComponent, XioAlertComponent, SnackbarService, XioProgressComponent} from './../../../theme/';
import {Store} from '@ngrx/store';
import {getISECardInfo, getSNMPTraps, State, getButtonStatus} from './../../../reducers';
import {
  GetSMNPList, ISESettingsUpdate, UpdateSMNPList, SNMPAddClient, SNMPDeleteClient,
  DownloadMIBFile, GetAllSNMPData, ISELedUpdate, GetButtonStatus
} from '../../../actions/ise-settings.actions';
import {GetISECardInfo, SetISEId, SetISELEDBlinkStatus} from "../../../actions/ise-management.actions";



@Component({
  selector: 'app-ise-settings',
  templateUrl: './ise-settings.component.html',
  styleUrls: ['./ise-settings.component.scss'],
  providers: [SnmpService]
})

export class IseSettingsComponent implements OnInit, OnDestroy {
  public ise_status: any;
  public ise_id: number;
  public snmpForm: FormGroup;
  public snmp_list: Object;
  public gridOptions;
  public columnDefs: any;
  public is_subs_form: boolean;
  public loading_stack: any;
  public client: string;
  public clients: Array<String> = [];
  public status: any;
  public snmpTraps$;
  public iseCardInfo$;
  public ise_card_details;
  public is_ise_enable:boolean = false;
  public identifyToggleStatus:boolean;
  public multiple = 'multiple';
  public interval_id:any;
  public iseStatusDetail$:any;
  public ise_serialno: any;



  constructor(public ises: IseService,
    public route: ActivatedRoute,
    public router: Router,
    public snackbarService: SnackbarService,
    public fb: FormBuilder,
    public dialog: MdDialog,
    public store: Store<State>) {
    {

      this.loading_stack = {
        available_details: false,
        available_details_text: 'Loading.....'
      },

      this.loading_stack = {
      ise_initialize: false,
      ise_initialize_text: 'Initializing.....'
      };
    }
  }


  ngOnInit() {
    this.is_subs_form = true;
    this.snmpForm = this.fb.group({
      community: [''],
      contact: [''],
      organization: [''],
      description: [''],
      oidname: [''],
      oidnumber: ['']
    });

    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.ise_status = {
        reformat: false,
        initialize: false,
        shutdown: false,
        restart: false,
        identify: false,
        running: true
      };
      this.initCardInfo();
      this.store.dispatch(new SetISEId(this.ise_id));
    });

    if (this.ise_id) {
      this.SnmpFormValue();
      this.iseStatus();
      this.isestatusbutton();
    }

    this.loading_stack.available_details = true;
    this.store.dispatch(new GetAllSNMPData({
      ise_id: this.ise_id,
      cb: (success, error) => {
        if (!error) {

          this.snmpTraps$ = this.store.select(getSNMPTraps).subscribe(
            data => {
              this.loading_stack.available_details = false;
              this.snmp_list = Object.assign({}, data);
              for (let sl of this.snmp_list['selected']) {
                if (typeof sl['trap'] == "object" && sl.hasOwnProperty('trap')) {
                  sl['_attr'] = sl['trap']._attr;
                }
                sl['value'] = true;
              }
              for (let sl of this.snmp_list['available']) {
                if (typeof sl['trap'] == "object" && sl.hasOwnProperty('trap')) {
                  sl['_attr'] = sl['trap']._attr;
                }
                sl['value'] = false;
              }
            })

        } else {
          if (error.status === 401) {
            let path = '/ise/' + this.ise_id + '/set-password/';
            this.router.navigate([path]);
          }

        }
      }

    }));

    this.interval_id = setInterval(() => {
          this.isestatusbutton();
        }, 20000);
   }

  initCardInfo() {
    this.iseCardInfo$ = this.store.select(getISECardInfo).subscribe(
      data => {
        if(data){
        this.ise_card_details = data;
        this.ise_serialno =  this.ise_card_details.serial_no
      }
        if (this.ise_card_details && this.ise_card_details.status) {

          this.status = (this.ise_card_details.status._attr.string == 'Uninitialized') ? this.ise_card_details.status._attr.string : false;
          this.identifyToggleStatus = this.ise_card_details.led._attr.string == "enabled" ? true : false;
          this.is_ise_enable = this.identifyToggleStatus;
          if(this.ise_card_details && 
             this.ise_card_details.status && 
             this.ise_card_details.status._attr && 
             this.ise_card_details.status._attr.string !== 'Uninitialized') {
               clearInterval(this.interval_id);
         }
       }
    });
  }

  /**
   * Get ise Status
   */
  iseStatus() {
    this.store.dispatch(new GetISECardInfo(this.ise_id));
  }

  /**
   * This method is used for setting SNMP form
   * @constructor
   */
  SnmpFormValue() {
    this.store.dispatch(new GetSMNPList({
      ise_id: this.ise_id,
      cb: (data) => {
        if (data) {
          let snmp_data = data;
          this.snmpForm['controls']['community'].setValue(snmp_data.community);
          this.snmpForm['controls']['contact'].setValue(snmp_data.contact);
          this.snmpForm['controls']['organization'].setValue(snmp_data.organization);
          this.snmpForm['controls']['description'].setValue(snmp_data.description);
          this.snmpForm['controls']['oidname'].setValue('1.3.6.1.4.1.' + snmp_data.oidname);
          this.snmpForm['controls']['oidname'].disable();
          this.snmpForm['controls']['oidnumber'].setValue('Ise.org.dod.internet.private.enterprise.' + snmp_data.oidnumber);
          this.snmpForm['controls']['oidnumber'].disable();
          this.clients = snmp_data['clients'].hasOwnProperty('client') ? [snmp_data['clients']['client']] : snmp_data['clients'];
        }

      }
    }));
  }

  /**
   * This method is used for updating SNMP
   */
  onSnmpUpdateSubmit() {
    let data = this.snmpForm.value,
      delete_sl = [],
      add_sl = [];
    for (let sl of this.snmp_list['selected']) {
      if (!sl['value']) {
        delete_sl.push(sl)
      }
    }

    for (let sl of this.snmp_list['available']) {
      if (sl['value']) {
        add_sl.push(sl)
      }
    }  
    
    if (add_sl.length > 0 || delete_sl.length > 0) {
      data['added_list'] = add_sl;
      data['removed_list'] = delete_sl;
    }
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';

    this.store.dispatch(new UpdateSMNPList({
      ise_id: this.ise_id,
      snmp_data: data,
      cb: (data, err) => {
        if (data) {
          progressRef.close();
          this.snackbarService.toastMe('Details updated Successfully', 2000);
        }
        else if (err) {
          progressRef.close();
        }
      }
    }));
  }

  toggleList() {
    this.is_subs_form = false;
  }

  openDialog(btn_name) {
    let setting_data = {
      reformat: false,
      initialize: false,
      shutdown: false,
      restart: false,
      identify: false

    };
   
    setting_data[btn_name] = true;
    let content = "<div class='fs12'><strong class='text-danger'>Note</strong>: Subscriptions to X-IO's proactive monitoring service (Activewatch) are enabled by default. After system initialization, customers who don't want to use this proactive monitoring service can disable Activewatch on the 'Advanced Settings' tab by deleting all subscriptions shown in the 'Subscriptions' section.</div>"
    let dialogRef = this.dialog.open(XioDialogComponent);
    if (btn_name == 'initialize') {
      dialogRef.componentInstance.title = 'Settings';
      //dialogRef.componentInstance.message = 'Do you want to  "' + btn_name + '" ISE ?'  +content ;
      dialogRef.componentInstance.message = 'Do you want to  ' + btn_name + ' ISE ' + this.ise_serialno + '?' + '<br/>' + content;

    }
    else {
      dialogRef.componentInstance.title = 'Settings';
      dialogRef.componentInstance.message = 'Do you want to  ' + btn_name + ' ISE ' + this.ise_serialno +'?';

    }
    dialogRef.afterClosed().subscribe(result => {
      if (result == 'yes') {
        if(btn_name == 'initialize'){
              this.loading_stack.ise_initialize = true;
          }
        // TODO Dominic: ask rohan to test this
        this.store.dispatch(new ISESettingsUpdate({
          setting_data: setting_data,
          ise_id: this.ise_id
        }));
      }
    },
    );
  }

  isestatusbutton() {
  let payLoad = {
      ise_id : this.ise_id
  }
  this.store.dispatch(new GetButtonStatus(payLoad));
  this.iseStatusDetail$ =  this.store.select(getButtonStatus).subscribe(
      data => {
       
       if (data['initialize'] == 'running') {
         
           this.loading_stack.ise_initialize = true;
        }
        else {
           this.loading_stack.ise_initialize = false;
        }
   });
 }

  addClient() {
    let data = {
      client: this.client
    };
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';

    this.store.dispatch(new SNMPAddClient({
      ise_id: this.ise_id,
      snmp_data: data,
      cb: (data, err) => {
        if (data) {
          progressRef.close();
          if (this.clients) {
            this.clients.push(this.client);
          } else {
            this.clients = [this.client];
          }
          this.client = '';
          this.snackbarService.toastMe('Client Added Successfully', 2000);
        }
        else if (err) {
          progressRef.close();
          let err_msg = err.json(),
            alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
          alertRef.componentInstance.title = 'SNMP';
          alertRef.componentInstance.message = err_msg.result.error.message;
        }
      }
    }));
  }

  removeClient(i: number) {
    let data = { client: this.clients[i] },
      dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Delete';
    dialogRef.componentInstance.message = 'Do you want to Delete ?';
    dialogRef.afterClosed().subscribe(result => {
      if (result == 'yes') {
        let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'Loading....';
        this.store.dispatch(new SNMPDeleteClient({
          ise_id: this.ise_id,
          snmp_data: data,
          cb: (data, err) => {
            if (data) {
              progressRef.close();
              this.clients.splice(i, 1);
              this.snackbarService.toastMe('Client Removed Successfully', 2000);
            }
            else if (err) {
              progressRef.close();
            }
          }
        }));
      }
    });

  }

  mibfiledownload() {
    this.store.dispatch(new DownloadMIBFile({
      ise_id: this.ise_id,
      cb: (data, err) => {
        let a = document.createElement('a'),
          blob = new Blob([data.content], { type: 'text/csv;charset=utf-8' }),
          url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = data.ise_name+'-MIB.txt';
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
          document.body.removeChild(a);
          window.URL.revokeObjectURL(url);
        }, 100);
      }
    }));
  }

  enableLed(e: Event) {
    this.is_ise_enable = !this.is_ise_enable;
    let data = { led: 'disabled' };
    this.is_ise_enable ? data.led = 'enabled' : data.led = 'disabled';

    this.store.dispatch(new ISELedUpdate({
      ise_id: this.ise_id,
      data: data,
      cb: (data, error) => {
        if (!error) {
          if (data.length > 0 && data[0].result.response.data == 'Array Activity LED has been enabled') {
            this.store.dispatch(new SetISELEDBlinkStatus(true));
          } else {
            this.store.dispatch(new SetISELEDBlinkStatus(false));
          }
        } else {
          console.error(error);
        }
      }
    }));
  }


  ngOnDestroy() {
    if(this.snmpTraps$){
      
    this.snmpTraps$.unsubscribe();
    }
    this.iseCardInfo$.unsubscribe();
    this.iseStatusDetail$.unsubscribe();
  }
}

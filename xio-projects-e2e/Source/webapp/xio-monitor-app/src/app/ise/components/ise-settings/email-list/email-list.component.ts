import {Component, OnInit, OnDestroy} from '@angular/core';
import {FormBuilder, FormGroup,Validators} from '@angular/forms';
import {ActivatedRoute} from '@angular/router';
import {EmailService} from './../../../../ise/services/email.service';
import {MdDialog} from '@angular/material';
import {XioAlertComponent, XioProgressComponent, SnackbarService} from './../../../../theme/';
import {Store} from '@ngrx/store';
import {State, getEmailState} from '../../../../reducers/';
import {listConfig} from './email-list-options';
import {XioDialogComponent} from "../../../../theme/xio-dialog/xio-dialog.component";
import {
  GetEmailAction,
  CreateSMPTAction, GetTestEmail
} from '../../../../actions/email.actions';

@Component({
  selector: 'app-email-list',
  templateUrl: './email-list.component.html',
  styleUrls: ['./email-list.component.scss']
})
export class EmailListComponent implements OnInit, OnDestroy {

  public gridOptions;
  public columnDefs: any;
  public ise_id: number;
  public is_email_list: Boolean = true;
  public smtpForm: FormGroup;
  public test_email = {email: ''};
  public emails$;
  public progressRef: any;
  public toastMeMess = '';
  public isLoading = false;
  public doEdit = false;
  public userInfo = {};
  public smtp_details:any;
  public btnLabel : any;
  public testEmailForm:FormGroup;

  constructor(public es: EmailService,
              public route: ActivatedRoute,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public fb: FormBuilder,
              public store: Store<State>) {

  }

   buildGridOptions() {
    this.emails$ = this.store.select(getEmailState)
    this.gridOptions = listConfig;
    this.gridOptions['deleteCb'] = this.bindEmailDeleteCb.bind(this);
  }

  ngOnInit() {
    this.smtpForm = this.fb.group({
      email_host: ['',Validators.required],
      email_port: ['',[Validators.required,Validators.maxLength(5),
      Validators.pattern(/^[0-9]+$/)]],
      from_mail: ["",
        [Validators.required,
          Validators.pattern(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/),
        ]],
      email_host_user: [''],
      email_host_password: [''],
      enable_authentication: [''],
      use_ssl_tl: ['']
    });
    this.initTestEmailForm();
    this.buildGridOptions();
      this.emails$ = this.store.select(getEmailState).subscribe(
      data => {
        this.gridOptions.rowData = data.emailLst;
      });
      this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.getUserList();
    });

    this.SmtpFormValue();
  }

  initTestEmailForm(){
    this.testEmailForm = this.fb.group({
      test_email: ["",
        [Validators.required,
          Validators.pattern(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/),
        ]],
    })
  }

  openProgressDialog() {
    this.progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    this.progressRef.componentInstance.progress_data = 'processing';
  }

  closeProgressDialog(res, err) {
    if (res) {
      this.snackbarService.toastMe(this.toastMeMess, 2000);
      this.progressRef.close();
    } else if (err) {
      console.error(err);
      this.progressRef.close();
    }
  }

  bindEmailDeleteCb(data) {
    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = "Delete";
    dialogRef.componentInstance.message = "Do you want to Delete ?";
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
      if (result == 'yes') {
        let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
        progressRef.componentInstance.progress_data = "Loading....";
        this.es.deleteEmail(this.ise_id, data.id).subscribe(
          data => {
            progressRef.close();
            this.getUserList();
            this.snackbarService.toastMe('User Deleted Successfully', 2000);
          },
          err => {
            progressRef.close();
            let err_msg = err.json();
            console.log(err_msg);
            let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title = "Email";
            alertRef.componentInstance.message = err_msg.result.response.data;
          });
      }

    });
  }


  /**
   * This method is used for getting user list
   */
  getUserList() {
    this.store.dispatch(new GetEmailAction(this.ise_id));
  }

  /**
   * This method is used for setting smpt form values
   * @constructor
   */
  SmtpFormValue() {
    this.es.getsmtpDetails().subscribe(
      data => {
         this.btnLabel = data &&
                         data.result &&
                         data.result.response &&
                         data.result.response.data  &&
                         !this.isEmpty(data.result.response.data) ? 'Update' : 'Save';
         console.log("btnLabel...:",data.result.response.data);
         if( data && data.result && data.result.response ){
           this.smtp_details=data.result.response.data;
           this.smtpForm['controls']['email_host'].setValue(this.smtp_details.email_host);
           this.smtpForm['controls']['email_port'].setValue(this.smtp_details.email_port);
           this.smtpForm['controls']['from_mail'].setValue(this.smtp_details.from_mail);
           this.smtpForm['controls']['email_host_user'].setValue(this.smtp_details.email_host_user);
           this.smtpForm['controls']['email_host_password'].setValue(this.smtp_details.email_host_password);
           this.smtpForm['controls']['enable_authentication'].setValue(this.smtp_details.enable_authentication);
           this.smtpForm['controls']['use_ssl_tl'].setValue(this.smtp_details.use_ssl_tl);
         }
      });
  }

  /**
   * This method is used for returning value
   * of form element
   * @param element_name
   */
 getFormElementVal(element_name: string) {
    const control =  this.smtpForm['controls'][element_name];
    return control.value;
  }

  /**
   * This method ise used to change the port
   */
 portChange(){
  if(this.smtpForm['controls']['enable_authentication'].value){
    this.smtpForm['controls']['email_port'].setValue('587');
    this.smtpForm['controls']['email_host_user'].enable();
    this.smtpForm['controls']['email_host_password'].enable();
  }else{
     this.smtpForm['controls']['email_port'].setValue('25');
     this.smtpForm['controls']['email_host_user'].disable();
     this.smtpForm['controls']['email_host_password'].disable();
  }
}

 onSubmit() {
    this.openProgressDialog();
    this.isLoading = true;
    this.toastMeMess = 'SMTP Configuration Updated ';
    this.smtpForm.value['cb'] = this.closeProgressDialog.bind(this);
    this.btnLabel = 'Update';
    this.store.dispatch(new CreateSMPTAction(this.smtpForm.value));
  }

  onTestMail() {
    this.es.getsmtpDetails().subscribe(
      data => {          
         if( data && data.result && 
             data.result.response.data && 
             !this.isEmpty(data.result.response.data)){
           this.openProgressDialog();
           let testEmailFormData = this.testEmailForm.value;
           this.store.dispatch(new GetTestEmail({
             'email':testEmailFormData.test_email,
             'cb' : (res,err) =>{
                if(res){
                  this.snackbarService.toastMe('SMTP Test Email Configuration Updated ', 2000);  
                } else {
                  let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
                  alertRef.componentInstance.title = 'SMTP Test Email Configuration';
                  alertRef.componentInstance.message = err.json().result.error.message;
                }  
                this.progressRef.close();                     
            }}));
          
         } else {
            if(this.progressRef)
              this.progressRef.close();
            const alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title = 'SMTP Email Configuration';
            alertRef.componentInstance.message = 'Please set SMTP Email Configuration';

         }
      });
  }

  toogleEmailList() {
    this.is_email_list = !this.is_email_list;
    if (this.is_email_list) {
      this.getUserList();
    }
  }

  userEditCb(e) {
      this.doEdit = true;
      this.userInfo = e.data;
      this.toogleEmailList();
  }

  ngOnDestroy() {
    if(this.emails$)
      this.emails$.unsubscribe();
  }

  /**
   * This method is used for checking is
   * empty object or not
   * @param obj
   * @returns {boolean}
   */
  isEmpty(obj) {
    for(var prop in obj) {
      if(obj.hasOwnProperty(prop))
        return false;
    }
    return JSON.stringify(obj) === JSON.stringify({});
  }

}

import {Component, OnInit, Output, EventEmitter, Input, OnDestroy} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router, ActivatedRoute} from '@angular/router';
import {EmailService} from './../../../../ise/services/email.service';
import {SnackbarService} from './../../../../theme/services/snackbar.service';
import {Md2Toast} from 'md2/toast/toast';
import {MdDialog} from '@angular/material';
import {MdProgressSpinnerModule} from '@angular/material';
import {XioDialogComponent} from './../../../../theme/xio-dialog/xio-dialog.component';
import {XioProgressComponent} from './../../../../theme/xio-progress/xio-progress.component';
import {Observable} from 'rxjs/Observable';
import {Store} from '@ngrx/store';
import {State, getEmailState, getISEId} from '../../../../reducers/';
import {XioAlertComponent} from '../../../../theme/xio-alert/xio-alert.component';


@Component({
  selector: 'app-email-form',
  templateUrl: './email-form.component.html',
  styleUrls: ['./email-form.component.scss']
})
export class EmailFormComponent implements OnInit, OnDestroy {

  @Output() showEmailList = new EventEmitter();
  @Input() isAddForm: boolean = true;
  @Input() userInfo: object;

  public emailForm: FormGroup;
  public ise_id: Number;
  public alert_severity = {critical: false,
      severe: false,
      error: false,
      warning: false,
      informational: false,
      normal: false};
  public ise_id_obs$;
  public id;
  public isEdit = false;
  public form_title:any;


  constructor(public fb: FormBuilder,
              public router: Router,
              public route: ActivatedRoute,
              public es: EmailService,
              public snackbarService: SnackbarService,
              public toast: Md2Toast,
              public dialog: MdDialog,
              public store: Store<State>) {
  }

  ngOnInit() {
    this.form_title="Add Email User"
    this.emailForm = this.fb.group({
      name: ["", [Validators.required]],
      email: ["",
        [Validators.required,
          Validators.pattern(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/),
        ]]
    });

    this.ise_id_obs$ = this.store.select(getISEId).subscribe(data => {
      this.ise_id = +data;
    });
    // this.getEmail();

    this.subEmailState();
    this.route.parent.params.subscribe(params => {
      console.log(params);
        this.ise_id = params['ise_id'];
        console.log( this.ise_id)
        })
    this.route.params.subscribe(params => {
          this.id = params['id'];
         if (this.id) {
            this.isEdit = true;
            this.form_title = 'Edit Email User';
            this.editFormValue();
          } else {
            this.isEdit = false;
          }
     
   
        });
  }
  subEmailState() {
    this.alert_severity = {
      critical: false,
      severe: false,
      error: false,
      warning: false,
      informational: false,
      normal: false
    };
    // this.editFormValue();
  }

  editFormValue() {
   this.es.getUser(this.ise_id,this.id).subscribe(
       result => {
        this.alert_severity = Object.assign(this.alert_severity);
      this.emailForm['controls']['name'].setValue(result.name);
      this.emailForm['controls']['email'].setValue(result.email);
      this.alert_severity.critical = result.critical;
      this.alert_severity.severe = result.severe;
      this.alert_severity.error = result.error;
      this.alert_severity.warning = result.warning;
      this.alert_severity.informational = result.informational;
      this.alert_severity.normal = result.normal;

    }) 
  }

  
 

  onsubmit() {
    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    progressRef.componentInstance.progress_data = 'processing';
   this.es[(!this.id ? 'addEmail' : 'updateEmail')](
      Object.assign(this.emailForm.value, {
        ise_id: this.ise_id,
        id: this.id,
        critical: this.alert_severity['critical'],
        severe: this.alert_severity['severe'],
        error: this.alert_severity['error'],
        warning: this.alert_severity['warning'],
        informational: this.alert_severity['informational'],
        normal: this.alert_severity['normal']
      })
    ).subscribe(
      data => {
        this.snackbarService.toastMe('User ' + (!this.id ? ' Added ' : ' Updated ') + ' Successfully', 2000);
        progressRef.close();
        if(this.id){
          this.router.navigate(['/ise/' + this.ise_id + '/settings']);
          this.showEmailList.emit('cancel');
        }
        this.showEmailList.emit('cancel');
      },
      err => {
         progressRef.close();
         setTimeout(()=> {
            let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title = 'Email';
            alertRef.componentInstance.message = err.json().result.error.message;

          },500)
      });
  }

  oncancel() {
    this.showEmailList.emit('cancel');
     if(this.id){
          this.router.navigate(['/ise/' + this.ise_id + '/settings']);
          
        }
  }

  ngOnDestroy() {
    this.ise_id_obs$.unsubscribe();
  }

}
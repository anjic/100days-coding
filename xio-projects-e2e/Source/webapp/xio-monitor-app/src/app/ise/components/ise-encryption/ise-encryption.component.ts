import { Component, OnInit } from '@angular/core';
import {State, getISEId, getISECardInfo} from '../../../reducers';
import {Store} from "@ngrx/store";
import {GetISECardInfo} from "../../../actions/ise-management.actions";
import {ActivatedRoute} from "@angular/router";
import {FormGroup, FormBuilder, Validators} from "@angular/forms";
import {ISEEnableEncryption} from "../../../actions/ise-settings.actions";
import {SnackbarService} from "../../../theme/services/snackbar.service";
import {Md2Dialog} from "md2";
import {XioAlertComponent} from "../../../theme/xio-alert/xio-alert.component";
import {MdDialog} from "@angular/material";
import {XioDialogComponent} from "../../../theme/xio-dialog/xio-dialog.component";

@Component({
  selector: 'app-ise-encryption',
  templateUrl: './ise-encryption.component.html',
  styleUrls: ['./ise-encryption.component.scss']
})
export class IseEncryptionComponent implements OnInit {

  public encryptionForm: FormGroup;
  public decryptionForm:FormGroup;
  public changePassKeyForm:FormGroup;

  public ise_id$:any;
  public ise_id:string;
  public iseCardInfo$;
  public ise_card_details;
  public enryptionEnable:string;
  public disableEncryptionFlag:boolean = false;
  public enableEncryptionFlag:boolean = false;
  public changePassKeyFlag:boolean = false;
  public enableEncryptionBtnContainers:boolean;
  public disableEncyptionBtnContainers:boolean;
  public encryptionOpened:boolean = false;
  public decryptionOpened:boolean = false;
  public changePassKeyOpened:boolean = false;

  constructor(public route: ActivatedRoute,
              public store:Store<State>,
              public formBuilder: FormBuilder,
              public snackbarService: SnackbarService,
              public dialog: MdDialog) {

  }

  ngOnInit() {

    this.ise_id$ = this.store.select(getISEId).subscribe(
      data => {
        this.ise_id = data;
        this.store.dispatch(new GetISECardInfo(this.ise_id));
      });

    this.initEncryptionForm();
    this.initDecryptForm();
    this.initChangePassKeyForm();

    //Subscribing for ise card details
    this.iseCardInfo$ = this.store.select(getISECardInfo).subscribe(
      data => {
        if(data && data['serial_no']){
          this.ise_card_details = data;
          this.enryptionEnable = this.ise_card_details['encrpytion_enabled'] != false ? 'enabled' : 'disabled' ;
          if(this.enryptionEnable == 'disabled'){
            if(!this.encryptionOpened)
              this.toggleContainers(false,false,false,true,false);
          }else if(!this.decryptionOpened){
              if(this.changePassKeyOpened)
                this.toggleContainers(false,false,true,false,false);
              else
                this.toggleContainers(false,false,false,false,true);
          }
        }
      },error => {
        console.log(error);
      });
  }

  /**
   * Setting encryption form
   */
  initEncryptionForm(){
    this.encryptionForm = this.formBuilder.group({
      passKey : ['',Validators.required],
      confirmPassKey : ['',Validators.required]
    });
  }

  /**
   * Setting Decrypt form
   */
  initDecryptForm(){
    this.decryptionForm = this.formBuilder.group({
      passKey : ['',Validators.required]
    });
  }

  /**
   * Setting ise change pass key form
   */
  initChangePassKeyForm(){
    this.changePassKeyForm = this.formBuilder.group({
      oldPassKey : ['',Validators.required],
      newPassKey : ['',Validators.required],
      confirmPassKey : ['',Validators.required]
    }, {validator: this.iseChangePWDmatchingPasswords('newPassKey', 'confirmPassKey')});
  }

  iseChangePWDmatchingPasswords(new_passKey: string, confirm_passKey: string) {
    return (group: FormGroup): { [key: string]: any } => {
      let new_passkey = group['controls'][new_passKey];
      let confirm_passkey = group['controls'][confirm_passKey];
      if (new_passkey.value !== confirm_passkey.value) {
        return {
          mismatchedISEEncryptionPasswords: true
        };
      }
    };
  }

  /**
   * Enable ise encryption
   */
  enableEncryption(){
    let content="<div class='fs14'>By enabling Encryption, you acknowledge that you are required to provide a password in order to encrypt your data. You also acknowledge that you will not be able to recover the encrypted information if you lose or forget the password</div>"
    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Enable Encryption';
    dialogRef.componentInstance.message = content;
    dialogRef.afterClosed().subscribe(result => {
      if (result === 'yes') {
        let encryptionFormData = this.encryptionForm.value;
        let payLoad= {
          "ise_id": this.ise_id,
          "cb":((success, error) => {
            if(!error){
              this.initEncryptionForm();
              this.snackbarService.toastMe('Encrypted Successfully', 2000);
              this.store.dispatch(new GetISECardInfo(this.ise_id));
              this.toggleContainers(false,false,false,false,true);
            }else{
              let err =error.json().result.error.message;
              let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
              alertRef.componentInstance.title ='Enable Encryption';
              alertRef.componentInstance.message = err;
            }
          }),
          "data": {
            "passkey":encryptionFormData.passKey,
            "enabled":"true",
            "accepteula":"true"
          }
        }
        this.store.dispatch(new ISEEnableEncryption(payLoad));
      }
    });
  }

  /**
   * Disable encryption
   */
  disableEncryption(){
    let decyptionFormData = this.decryptionForm.value;
    let payLoad= {
      "ise_id": this.ise_id,
      "cb": ((success, error) => {
        if(!error){
          this.initDecryptForm();
          this.snackbarService.toastMe('Decrypted Successfully', 2000);
          this.store.dispatch(new GetISECardInfo(this.ise_id));
          this.toggleContainers(false,false,false,true,false);
        }else{
          //this.snackbarService.toastMe('Decryption failed', 1000);
          let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
          alertRef.componentInstance.title ='Disable Encryption';
          let message = 'Please pass valid passkey';
          alertRef.componentInstance.message = message;
        }
      }),
      "data": {
        "passkey":decyptionFormData.passKey,
        "enabled":"false"
      }
    }
    this.store.dispatch(new ISEEnableEncryption(payLoad));
  }

  /**
   * Change ise pass key
   */
  changePassKey(){
    let changePassKeyForm = this.changePassKeyForm.value;
    let payLoad= {
      "ise_id": this.ise_id,
      "cb": ((success, error) => {
        if(!error){
          this.initChangePassKeyForm();
          this.snackbarService.toastMe('Passkey changed Successfully', 2000);
          this.store.dispatch(new GetISECardInfo(this.ise_id));
          this.changePassKeyOpened = false;
          this.toggleContainers(false,false,false,false,true);
        }else{
          console.log(error);
          if(error.json() && error.json().result){
            let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
            alertRef.componentInstance.title ='Change PassKey';
            // let message = error.json().result.response.data == 'Unknown Error' ? 'Old Password not matched' : '';
            alertRef.componentInstance.message =  error.json().result.error.message;
          }

        }
      }),
      "data": {
        "passkey":changePassKeyForm.oldPassKey,
        "newpasskey":changePassKeyForm.newPassKey
      }
    }
    this.store.dispatch(new ISEEnableEncryption(payLoad));
  }

  /**
   * Enable encryption
   */
  public goToEnableEncryption(){
    this.encryptionOpened = true;
    this.toggleContainers(false,true,false,false,false);
  }

  /**
   * Disable encryption
   */
  public goToDisableEncryption(){
    this.decryptionOpened = true;
    this.toggleContainers(true,false,false,false,false);
  }

  /**
   * Change pass key
   * @param status
   */
  public goToChangePassKey(status:string){
    this.changePassKeyOpened = true;
    this.toggleContainers(false,false,true,false,false);
  }

  /**
   * Close decryption
   */
  public cancelDisableEncryption(){
    this.initDecryptForm();
    this.toggleContainers(false,false,false,false,true);
  }

  /**
   * Close encryption
   */
  public cancelEnableEncryption(){
    this.initEncryptionForm();
    this.toggleContainers(false,false,false,true,false);
  }

  /**
   * Close change pass key
   */
  public cancelUpdatePassKey(){
    this.initChangePassKeyForm();
    if(this.enryptionEnable == 'disabled') {
      this.toggleContainers(false, false, false, true, false);
    }else{
      this.toggleContainers(false, false, false, false, true);
    }
  }

  /**
   * Generic method to toggle containers based on the status
   * @param _disableEncryptionFlag
   * @param _enableEncryptionFlag
   * @param _changePassKey
   * @param _enableEncryptionBtnContainers
   * @param _disableEncyptionBtnContainers
   */
  public toggleContainers(_disableEncryptionFlag:boolean,
                          _enableEncryptionFlag:boolean,
                          _changePassKey:boolean,
                          _enableEncryptionBtnContainers:boolean,
                          _disableEncyptionBtnContainers:boolean){
    this.disableEncryptionFlag = _disableEncryptionFlag;
    this.enableEncryptionFlag = _enableEncryptionFlag;
    this.changePassKeyFlag = _changePassKey;
    this.enableEncryptionBtnContainers = _enableEncryptionBtnContainers;
    this.disableEncyptionBtnContainers = _disableEncyptionBtnContainers;


  }
}

import { Component, OnInit, OnDestroy } from '@angular/core';
import {State, getISEId, getISECardInfo} from '../../../reducers';
import {Store} from '@ngrx/store';
import {GetISECardInfo} from '../../../actions/ise-management.actions';
import {FormGroup, FormBuilder, Validators} from '@angular/forms';
import {ISEEnableEncryption} from '../../../actions/ise-settings.actions';
import {SnackbarService} from '../../../theme/services/snackbar.service';
import {Md2Dialog} from 'md2';
import {XioAlertComponent} from '../../../theme/xio-alert/xio-alert.component';
import {MdDialog} from '@angular/material';
import {XioDialogComponent} from '../../../theme/xio-dialog/xio-dialog.component';
import { ISECardInfo } from '../../models/ise_card_info';
@Component({
  selector: 'app-ise-encryption',
  templateUrl: './ise-encryption.component.html',
  styleUrls: ['./ise-encryption.component.scss']
})
export class IseEncryptionComponent implements OnInit, OnDestroy  {

  public encryptionForm: FormGroup;
  public decryptionForm: FormGroup;
  public changePassKeyForm: FormGroup;

  public ise_id$;
  public ise_id;
  public iseCardInfo$;
  public ise_card_details;
  public enryptionEnable;
  public disableEncryptionFlag;
  public enableEncryptionFlag: boolean;
  public changePassKeyFlag: boolean;
  public enableEncryptionBtnContainers: boolean;
  public disableEncyptionBtnContainers: boolean;
  public encryptionOpened: boolean;
  public decryptionOpened: boolean;
  public changePassKeyOpened: boolean;

  constructor(public store: Store<State>,
              public formBuilder: FormBuilder,
              public snackbarService: SnackbarService,
              public dialog: MdDialog) {

       this.disableEncryptionFlag = false;         
       this.enableEncryptionFlag = false;         
       this.changePassKeyFlag = false;         
       this.encryptionOpened = false;         
       this.decryptionOpened = false;         
       this.changePassKeyOpened = false;   
       this.iseCardInfo$ = <ISECardInfo> {};   

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

    // Subscribing for ise card details
    this.iseCardInfo$ = this.store.select(getISECardInfo).subscribe(
      (data: ISECardInfo) => {
        if (data && data['serial_no']) {
          this.ise_card_details = data;
          this.enryptionEnable = this.ise_card_details['encrpytion_enabled'] != false ? 'enabled' : 'disabled' ;
          if (this.enryptionEnable == 'disabled') {
            if (!this.encryptionOpened) {
              this.toggleContainers(false, false, false, true, false);
            }  
          }else if (!this.decryptionOpened) {
              if (this.changePassKeyOpened) {
                this.toggleContainers(false, false, true, false, false);
              } else {
                this.toggleContainers(false, false, false, false, true);
              }  
          }
        }
      }, error => {
        if (error.json() && error.json().result) {
          let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
              alertRef.componentInstance.title = 'Ise CardInfo';
              alertRef.componentInstance.message =  error.json().result.error.message;
        }

      });
  }

   /**
   * Setting Encryption Form
   * @namespace xio.IseEncryptionComponent 
   * @method initEncryptionForm
   */
  initEncryptionForm() {
    this.encryptionForm = this.formBuilder.group({
      passKey : ['', Validators.required],
      confirmPassKey : ['', Validators.required]
    });
  }

   /**
   * Setting Decryption Form
   * @namespace xio.IseEncryptionComponent 
   * @method initDecryptForm
   */
  initDecryptForm() {
    this.decryptionForm = this.formBuilder.group({
      passKey : ['', Validators.required]
    });
  }
  /**
   * SettingChangePasskey Form
   * @namespace xio.IseEncryptionComponent 
   * @method initChangePassKeyForm
   */
  initChangePassKeyForm() {
    this.changePassKeyForm = this.formBuilder.group({
      oldPassKey : ['', Validators.required],
      newPassKey : ['', Validators.required],
      confirmPassKey : ['', Validators.required]
    }, {validator: this.iseChangePWDmatchingPasswords('newPassKey', 'confirmPassKey')});
  }

  /**
   * Passkey Matching
   * @namespace xio.IseEncryptionComponent 
   * @method iseChangePWDmatchingPasswords
   */

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
   * Enable ISE Encryption
   * @namespace xio.IseEncryptionComponent 
   * @method iseChangePWDmatchingPasswords
   */
  enableEncryption() {
    let content = "<div class='fs14'>By enabling Encryption, you acknowledge that you are required to provide a password in order to encrypt your data. You also acknowledge that you will not be able to recover the encrypted information if you lose or forget the password</div>"
    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.title = 'Enable Encryption';
    dialogRef.componentInstance.message = content;
    dialogRef.afterClosed().subscribe(result => {
      if (result === 'yes') {
        let encryptionFormData = this.encryptionForm.value;
        let payLoad = {
          'ise_id': this.ise_id,
          'cb': ((success, error) => {
            if (!error) {
              this.initEncryptionForm();
              this.snackbarService.toastMe('Encrypted Successfully', 2000);
              this.store.dispatch(new GetISECardInfo(this.ise_id));
              this.toggleContainers(false, false, false, false, true);
            }else {
              let err = error.json().result.error.message;
              let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
              alertRef.componentInstance.title = 'Enable Encryption';
              alertRef.componentInstance.message = err;
            }
          }),
          'data': {
            'passkey': encryptionFormData.passKey,
            'enabled': 'true',
            'accepteula': 'true'
          }
        };
        this.store.dispatch(new ISEEnableEncryption(payLoad));
      }
    });
  }

  /**
   * Disable ISE Encryption
   * @namespace xio.IseEncryptionComponent 
   * @method iseChangePWDmatchingPasswords
   */
  disableEncryption(){
    let decyptionFormData = this.decryptionForm.value;
    let payLoad = {
      'ise_id': this.ise_id,
      'cb': ((success, error) => {
        if (!error) {
          this.initDecryptForm();
          this.snackbarService.toastMe('Decrypted Successfully', 2000);
          this.store.dispatch(new GetISECardInfo(this.ise_id));
          this.toggleContainers(false, false, false, true, false);
        } else {
          let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
          alertRef.componentInstance.title = 'Disable Encryption';
          let message = 'Please pass valid passkey';
          alertRef.componentInstance.message = message;
        }
      }),
      'data': {
        'passkey': decyptionFormData.passKey,
        'enabled': 'false'
      }
    };
    this.store.dispatch(new ISEEnableEncryption(payLoad));
  }

  /**
   * Change ISE Passkey
   * @namespace xio.IseEncryptionComponent 
   * @method changePassKey
   */
  changePassKey() {
    let changePassKeyForm = this.changePassKeyForm.value;
    let payLoad = {
      'ise_id': this.ise_id,
      'cb': ((success, error) => {
        if (!error) {
          this.initChangePassKeyForm();
          this.snackbarService.toastMe('Passkey changed Successfully', 2000);
          this.store.dispatch(new GetISECardInfo(this.ise_id));
          this.changePassKeyOpened = false;
          this.toggleContainers(false, false, false, false, true);
        } else {
          if (error.json() && error.json().result) {
            let alertRef = this.dialog.open(XioAlertComponent, {disableClose: true});
                alertRef.componentInstance.title = 'Change PassKey';
                alertRef.componentInstance.message =  error.json().result.error.message;
          }

        }
      }),
      'data': {
        'passkey': changePassKeyForm.oldPassKey,
        'newpasskey': changePassKeyForm.newPassKey
      }
    };
    this.store.dispatch(new ISEEnableEncryption(payLoad));
  }

  /**
   * For Enabling Encryption
   * @namespace xio.IseEncryptionComponent 
   * @method changePassKey
   */
  public goToEnableEncryption() {
    this.encryptionOpened = true;
    this.toggleContainers(false, true, false, false, false);
  }

  /**
   * For Disabling Encryption
   * @namespace xio.IseEncryptionComponent 
   * @method changePassKey
   */
  public goToDisableEncryption() {
    this.decryptionOpened = true;
    this.toggleContainers(true, false, false, false, false);
  }

  /**
   * Change pass key
   * @param status
   */
  public goToChangePassKey(status: string) {
    this.changePassKeyOpened = true;
    this.toggleContainers(false, false, true, false, false);
  }

  /**
   * Close decryption
   */
  public cancelDisableEncryption() {
    this.initDecryptForm();
    this.toggleContainers(false, false, false, false, true);
  }

  /**
   * Close encryption
   */
  public cancelEnableEncryption() {
    this.initEncryptionForm();
    this.toggleContainers(false, false, false, true, false);
  }

  /**
   * Close change pass key
   */
  public cancelUpdatePassKey() {
    this.initChangePassKeyForm();
    if (this.enryptionEnable == 'disabled') {
      this.toggleContainers(false, false, false, true, false);
    } else {
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
  public toggleContainers(_disableEncryptionFlag: boolean,
                          _enableEncryptionFlag: boolean,
                          _changePassKey: boolean,
                          _enableEncryptionBtnContainers: boolean,
                          _disableEncyptionBtnContainers: boolean) {
    this.disableEncryptionFlag = _disableEncryptionFlag;
    this.enableEncryptionFlag = _enableEncryptionFlag;
    this.changePassKeyFlag = _changePassKey;
    this.enableEncryptionBtnContainers = _enableEncryptionBtnContainers;
    this.disableEncyptionBtnContainers = _disableEncyptionBtnContainers;
  }

  ngOnDestroy() {
    if (this.iseCardInfo$) {
      this.iseCardInfo$.unsubscribe();
    }
    // Un Binding Event Listeners
    window.removeEventListener('click', this.cancelUpdatePassKey.bind(this), false);
    window.removeEventListener('click', this.cancelEnableEncryption.bind(this), false);
    window.removeEventListener('click', this.cancelDisableEncryption.bind(this), false);
    window.removeEventListener('click', this.goToChangePassKey.bind(this), false);
    window.removeEventListener('click', this.goToDisableEncryption.bind(this), false);
    window.removeEventListener('click', this.goToChangePassKey.bind(this), false);
    window.removeEventListener('click', this.goToEnableEncryption.bind(this), false);

  }

}

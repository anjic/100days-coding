/**
 * Created by Dominic on 7/19/2017.
 */
import {Injectable} from '@angular/core';
import {Effect, Actions, toPayload} from '@ngrx/effects';
import {Observable} from 'rxjs';
import {Action} from '@ngrx/store';
import * as settingAction from '../actions/ise-settings.actions';
import {EffectSwitchMapCb} from '../common/utils/EffectsSwitchMapCb';
import {IseSettingService} from '../ise/services/ise-setting.service';

@Injectable()
export class ISESettingsEffects {

  constructor(public actions: Actions,
              public iseSettingService: IseSettingService) {
  }

  @Effect()
  getAll: Observable<Action> = this.actions
    .ofType(settingAction.GET_ALL_SNMP)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'getAll', query, settingAction['GetAllSNMPDataSuccess'], null);
    });

  @Effect()
  ISESettingUpdate$: Observable<Action> = this.actions
    .ofType(settingAction.ISE_SETTING_UPDATE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'doSetting', query, settingAction['ISESettingsUpdateSuccess'], null);
    });

  @Effect()
  ISELedUpdate$: Observable<Action> = this.actions
    .ofType(settingAction.ISE_LED_UPDATE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'updateLed', query, settingAction['ISELedUpdateSuccess'], null);
    });

  @Effect()
  getTimeZone$: Observable<Action> = this.actions
    .ofType(settingAction.GET_TIMEZONE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'getTimeZone', query, settingAction['GetTimeZoneSuccess'], null);
    })

  @Effect()
  updateTimeZone$: Observable<Action> = this.actions
    .ofType(settingAction.UPDATE_TIMEZONE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'updateTimezone', query, settingAction['UpdateTimeZoneSuccess'], null);
    })

  @Effect()
  getSNMP$: Observable<Action> = this.actions
    .ofType(settingAction.GET_SNMP_LIST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'getsnmp_list', query, settingAction['GetSMNPListSuccess'], null);
    })

  @Effect()
  updateSNMP$: Observable<Action> = this.actions
    .ofType(settingAction.UPDATE_SNMP_LIST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'updatesnmp', query, settingAction['UpdateSMNPListSuccess'], null);
    })

  @Effect()
  addSNMP$: Observable<Action> = this.actions
    .ofType(settingAction.ADD_SNMP_CLIENT)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'addClient', query, settingAction['SNMPAddClientSuccess'], null);
    })

  @Effect()
  deleteSNMP$: Observable<Action> = this.actions
    .ofType(settingAction.DELETE_SNMP_CLIENT)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'deleteClient', query, settingAction['SNMPDeleteClientSuccess'], null);
    })

  @Effect()
  mibFileDownload: Observable<Action> = this.actions
    .ofType(settingAction.DOWNLOAD_MIB_FILE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'downloadfile', query, settingAction['DownloadMIBFileSuccess'], null);
    })

  @Effect()
  iseGetAllSubscription: Observable<Action> = this.actions
    .ofType(settingAction.GET_ISE_SUBSCRIPTION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'getAllSubscription', query, settingAction['GetAllSubscriptionSuccess'], null);
    })

  @Effect()
  addISESubscription: Observable<Action> = this.actions
    .ofType(settingAction.ADD_ISE_SUBSCRIPTION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'addSubscription', query, settingAction['AddSubscriptionSuccess'], null);
    })

  @Effect()
  updateISESubscription: Observable<Action> = this.actions
    .ofType(settingAction.UPDATE_ISE_SUBSCRIPTION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'updateSubscription', query, settingAction['UpdateSubscriptionSuccess'], null);
    })

  @Effect()
  deleteISESubscription: Observable<Action> = this.actions
    .ofType(settingAction.DELETE_ISE_SUBSCRIPTION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'deleteSubscription', query, settingAction['DeleteSubscriptionSuccess'], null);
    })

  @Effect()
  enableEnryption: Observable<Action> = this.actions
    .ofType(settingAction.ENABLE_ENCRYPTION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'enableEncryption', query, settingAction['ISEEnableEncryptionSuccess'], null);
    })

  @Effect()
  GetButtonStatus: Observable<Action> = this.actions
    .ofType(settingAction.ISE_STATUS_BUTTON)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.iseSettingService, 'isebuttonstatus', query, settingAction['GetButtonStatusSuccess'], null);
    })  
}

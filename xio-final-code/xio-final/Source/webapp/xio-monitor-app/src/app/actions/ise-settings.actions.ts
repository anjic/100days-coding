/**
 * Created by Dominic on 7/19/2017.
 */

import {Action} from '@ngrx/store';
import * as iseMetaData from '../common/Metadata/ise.metadata';

export const GET_ALL_SNMP = '[SNMP] getMenuContent';
export const GET_ALL_SNMP_SUCCESS = '[SNMP] getMenuContent success';

export const ISE_SETTING_UPDATE = '[ISE Settings] update';
export const ISE_SETTING_UPDATE_SUCCESS = '[ISE Settings] update success';

export const ISE_LED_UPDATE = '[ISE Led] update';
export const ISE_LED_UPDATE_SUCCESS = '[ISE Led] update success';

export const GET_TIMEZONE = '[ISE TimeZone] getMenuContent';
export const GET_TIMEZONE_SUCCESS = '[ISE TimeZone] getMenuContent success';

export const UPDATE_TIMEZONE = '[ISE TimeZone] update';
export const UPDATE_TIMEZONE_SUCCESS = '[ISE TimeZone] update success';

export const GET_SNMP_LIST = '[ISE SNMP List] getSnmpList';
export const GET_SNMP_LIST_SUCCESS = '[ISE SNMP List] getSnmpList success';

export const UPDATE_SNMP_LIST = '[ISE SNMP List] update';
export const UPDATE_SNMP_LIST_SUCCESS = '[ISE SNMP List] update success';

export const ADD_SNMP_CLIENT = '[ISE SNMP Client] add';
export const ADD_SNMP_CLIENT_SUCCESS = '[ISE SNMP Client] add success';

export const DELETE_SNMP_CLIENT = '[ISE SNMP Client] delete';
export const DELETE_SNMP_CLIENT_SUCCESS = '[ISE SNMP Client] delete success';

export const DOWNLOAD_MIB_FILE = '[ISE MIB File] dowload';
export const DOWNLOAD_MIB_FILE_SUCCESS = '[ISE MIB File] dowload success';

export const GET_ISE_SUBSCRIPTION = '[ISE Subcription] getAll';
export const GET_ISE_SUBSCRIPTION_SUCCESS = '[ISE Subcription] getAll success';

export const ADD_ISE_SUBSCRIPTION = '[ISE Subcription] add';
export const ADD_ISE_SUBSCRIPTION_SUCCESS = '[ISE Subcription] add success';

export const UPDATE_ISE_SUBSCRIPTION = '[ISE Subcription] update';
export const UPDATE_ISE_SUBSCRIPTION_SUCCESS = '[ISE Subcription] update success';

export const DELETE_ISE_SUBSCRIPTION = '[ISE Subcription] delete';
export const DELETE_ISE_SUBSCRIPTION_SUCCESS = '[ISE Subcription] delete success';

export const ENABLE_ENCRYPTION = '[ISE Enable Encryption] enableEncryption';
export const ENABLE_ENCRYPTION_SUCCESS = '[ISE Enable Encryption] enableEncryption success';

export const ISE_STATUS_BUTTON = '[ISE Status Button] getStausButton';
export const ISE_STATUS_BUTTON_SUCCESS = '[ISE Status Button] getStausButton success'; 

export class ISEEnableEncryption implements Action {
  readonly type = ENABLE_ENCRYPTION;

  constructor(public payload: any) {
  }
}
export class ISEEnableEncryptionSuccess implements Action {
  readonly type = ENABLE_ENCRYPTION_SUCCESS;

  constructor(public payload: any) {
  }
}

export class GetAllSNMPData implements Action {
  readonly type = GET_ALL_SNMP;

  constructor(public payload: any) {
  }
}
export class GetAllSNMPDataSuccess implements Action {
  readonly type = GET_ALL_SNMP_SUCCESS;

  constructor(public payload: any) {
  }
}

export class ISESettingsUpdate implements Action {
  readonly type = ISE_SETTING_UPDATE;

  constructor(public payload: iseMetaData.ISEUpdateReqPayload) {
  }
}
export class ISESettingsUpdateSuccess implements Action {
  readonly type = ISE_SETTING_UPDATE_SUCCESS;

  constructor(public payload: any) {
  }
}

export class ISELedUpdate implements Action {
  readonly type = ISE_LED_UPDATE;
  constructor(public payload:any) {
  }
}

export class ISELedUpdateSuccess implements Action {
  readonly type = ISE_LED_UPDATE_SUCCESS;
  constructor(public payload:any) {
  }
}

export class GetTimeZone implements Action {
  readonly type = GET_TIMEZONE;

  constructor(public payload: any) {
  }
}
export class GetTimeZoneSuccess implements Action {
  readonly type = GET_TIMEZONE_SUCCESS;

  constructor(public payload: any) {
  }
}

export class UpdateTimeZone implements Action {
  readonly type = UPDATE_TIMEZONE;

  constructor(public payload: any) {
  }
}
export class UpdateTimeZoneSuccess implements Action {
  readonly type = UPDATE_TIMEZONE_SUCCESS;

  constructor(public payload: any) {
  }
}

export class GetSMNPList implements Action {
  readonly type = GET_SNMP_LIST;

  constructor(public payload: any) {
  }
}
export class GetSMNPListSuccess implements Action {
  readonly type = GET_SNMP_LIST_SUCCESS;

  constructor(public payload: any) {
  }
}

export class UpdateSMNPList implements Action {
  readonly type = UPDATE_SNMP_LIST;

  constructor(public payload: iseMetaData.snmpReqPayload) {
  }
}
export class UpdateSMNPListSuccess implements Action {
  readonly type = UPDATE_SNMP_LIST_SUCCESS;

  constructor(public payload: any) {
  }
}

export class SNMPAddClient implements Action {
  readonly type = ADD_SNMP_CLIENT;

  constructor(public payload: iseMetaData.snmpReqPayload) {
  }
}
export class SNMPAddClientSuccess implements Action {
  readonly type = ADD_SNMP_CLIENT_SUCCESS;

  constructor(public payload: any) {
  }
}

export class SNMPDeleteClient implements Action {
  readonly type = DELETE_SNMP_CLIENT;

  constructor(public payload: iseMetaData.snmpReqPayload) {
  }
}
export class SNMPDeleteClientSuccess implements Action {
  readonly type = DELETE_SNMP_CLIENT_SUCCESS;

  constructor(public payload: any) {
  }
}

export class DownloadMIBFile implements Action {
  readonly type = DOWNLOAD_MIB_FILE;

  constructor(public payload: iseMetaData.mibFileDownload) {
  }
}
export class DownloadMIBFileSuccess implements Action {
  readonly type = DOWNLOAD_MIB_FILE_SUCCESS;

  constructor(public payload: any) {
  }
}

export class GetAllSubscription implements Action {
  readonly type = GET_ISE_SUBSCRIPTION;

  constructor(public payload: iseMetaData.mibFileDownload) {
  }
}
export class GetAllSubscriptionSuccess implements Action {
  readonly type = GET_ISE_SUBSCRIPTION_SUCCESS;

  constructor(public payload: any) {
  }
}

export class AddSubscription implements Action {
  readonly type = ADD_ISE_SUBSCRIPTION;

  constructor(public payload: any) {
  }
}
export class AddSubscriptionSuccess implements Action {
  readonly type = ADD_ISE_SUBSCRIPTION_SUCCESS;

  constructor(public payload: any) {
  }
}

export class UpdateSubscription implements Action {
  readonly type = UPDATE_ISE_SUBSCRIPTION;

  constructor(public payload: any) {
  }
}
export class UpdateSubscriptionSuccess implements Action {
  readonly type = UPDATE_ISE_SUBSCRIPTION_SUCCESS;

  constructor(public payload: any) {
  }
}

export class DeleteSubscription implements Action {
  readonly type = DELETE_ISE_SUBSCRIPTION;

  constructor(public payload: any) {
  }
}
export class DeleteSubscriptionSuccess implements Action {
  readonly type = DELETE_SNMP_CLIENT_SUCCESS;

  constructor(public payload: any) {
  }
}

export class GetButtonStatus implements Action {
  readonly type =  ISE_STATUS_BUTTON;

  constructor(public payload: any) {
  }
}
export class GetButtonStatusSuccess implements Action {
  readonly type =  ISE_STATUS_BUTTON_SUCCESS;

  constructor(public payload: any) {
  }
}

export type Actions
  = GetAllSNMPData
  | GetAllSNMPDataSuccess
  | ISESettingsUpdate
  | ISESettingsUpdateSuccess
  | ISELedUpdate
  | ISELedUpdateSuccess
  | GetTimeZone
  | GetTimeZoneSuccess
  | UpdateTimeZone
  | UpdateTimeZoneSuccess
  | GetSMNPList
  | GetSMNPListSuccess
  | UpdateSMNPList
  | UpdateSMNPListSuccess
  | SNMPAddClient
  | SNMPAddClientSuccess
  | SNMPDeleteClient
  | SNMPDeleteClientSuccess
  | DownloadMIBFile
  | DownloadMIBFileSuccess
  | GetAllSubscription
  | GetAllSubscriptionSuccess
  | AddSubscription
  | AddSubscriptionSuccess
  | UpdateSubscription
  | UpdateSubscriptionSuccess
  | DeleteSubscription
  | DeleteSubscriptionSuccess
  | ISEEnableEncryption
  | ISEEnableEncryptionSuccess
  | GetButtonStatus
  | GetButtonStatusSuccess;



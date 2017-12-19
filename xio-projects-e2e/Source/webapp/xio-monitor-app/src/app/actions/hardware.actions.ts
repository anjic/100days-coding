/**
 * Created by Venkatesh on 7/19/2017.
 */

import {Action} from '@ngrx/store';

//MRC
export const GET_CONTROLLERS = "[MRC] getControllers";
export const GET_CONTROLLERS_SUCCESS = '[MRC] getControllers success';
export const UPDATE_MRC = "[MRC] updateMrc";
export const UPDATE_MRC_SUCCESS = '[MRC] updateMrc success';
export const UPDATE_DATA_PAC = "[MRC] updateDataPac";
export const UPDATE_DATA_PAC_SUCCESS = '[MRC] updateDataPac success';
export const UPDATE_SPEED = "[MRC] updateSpeed";
export const UPDATE_SPEED_SUCCESS = '[MRC] updateSpeed success';
export const UPDATE_SPEED_FCPORT = "[MRC] updateFcPortSpeed";
export const UPDATE_SPEED_FCPORT_SUCCESS = '[MRC] updateFcPortSpeed success';

export const GET_NETWORK = '[Network] getNetwork';
export const GET_NETWORK_SUCCESS = '[Network] getNetwork success';
export const UPDATE_NETWORK = '[Network] updateNetwork';
export const UPDATE_NETWORK_SUCCESS = '[Network] updateNetwork success';

export const GET_DATA_PAC = '[DataPac] getDataPac';
export const GET_DATA_PAC_SUCCESS = '[DataPac] getDataPac success';
export const UPDATE_PAC = '[DataPac] updatePac';
export const UPDATE_PAC_SUCCESS = '[DataPac] updatePac success';

export const GET_POWER_SUPPLY = '[PowerSupply] getPowerSupply';
export const GET_POWER_SUPPLY_SUCCESS = '[PowerSupply] getPowerSupply success';
export const UPDATE_POWER_SUPPLY = '[PowerSupply] updatePowerSupply';
export const UPDATE_POWER_SUPPLY_SUCCESS = '[PowerSupply] updatePowerSupply success';

export const GET_FANS = '[Fans] getFans';
export const GET_FANS_SUCCESS = '[Fans] getFans success';
export const UPDATE_FANS= '[Fans] updateFans';
export const UPDATE_FANS_SUCCESS = '[Fans] updateFans success';

export class GetPowerSupplyAction implements Action {
  readonly type = GET_POWER_SUPPLY;
  constructor(public payload:any) {
  }
}

export class GetPowerSupplyActionSuccess implements Action {
  readonly type = GET_POWER_SUPPLY_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdateDataPACAction implements Action {
  readonly type = UPDATE_PAC;
  constructor(public payload:any) {
  }
}

export class UpdateDataPACActionSuccess implements Action {
  readonly type = UPDATE_PAC_SUCCESS;
  constructor(public payload:any) {
  }
}

export class GetDataPACAction implements Action {
  readonly type = GET_DATA_PAC;
  constructor(public payload:any) {
  }
}

export class GetDataPACActionSuccess implements Action {
  readonly type = GET_DATA_PAC_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdateNetworkAction implements Action {
  readonly type = UPDATE_NETWORK;
  constructor(public payload:any) {
  }
}

export class UpdateNetworkActionSuccess implements Action {
  readonly type = UPDATE_NETWORK_SUCCESS;
  constructor(public payload:any) {
  }
}

export class GetNetworkAction implements Action {
  readonly type = GET_NETWORK;
  constructor(public payload:any) {
  }
}

export class GetNetworkActionSuccess implements Action {
  readonly type = GET_NETWORK_SUCCESS;
  constructor(public payload:any) {
  }
}

export class GetAllControllersAction implements Action {
  readonly type = GET_CONTROLLERS;
  constructor(public payload:any) {
  }
}

export class GetAllControllersActionSuccess implements Action {
  readonly type = GET_CONTROLLERS_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdateMRCAction implements Action {
  readonly type = UPDATE_MRC;
  constructor(public payload:any) {
  }
}

export class UpdateMRCActionSuccess implements Action {
  readonly type = UPDATE_MRC_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdateDataPacAction implements Action {
  readonly type = UPDATE_DATA_PAC;
  constructor(public payload:any) {
  }
}

export class UpdateDataPacActionSuccess implements Action {
  readonly type = UPDATE_DATA_PAC_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdateSpeedAction implements Action {
  readonly type = UPDATE_SPEED;
  constructor(public payload:any) {
  }
}

export class UpdateSpeedActionSuccess implements Action {
  readonly type = UPDATE_SPEED_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdatePowerSupplyAction implements Action {
  readonly type = UPDATE_POWER_SUPPLY;
  constructor(public payload:any) {
  }
}

export class UpdatePowerSupplyActionSuccess implements Action {
  readonly type = UPDATE_POWER_SUPPLY_SUCCESS;
  constructor(public payload:any) {
  }
}

export class GetFansAction implements Action {
  readonly type = GET_FANS;
  constructor(public payload:any) {
  }
}

export class GetFansActionSuccess implements Action {
  readonly type = GET_FANS_SUCCESS;
  constructor(public payload:any) {
  }
}

export class UpdateFansAction implements Action {
  readonly type = UPDATE_FANS;
  constructor(public payload:any) {
  }
}

export class UpdateFansActionSuccess implements Action {
  readonly type = UPDATE_FANS_SUCCESS;
  constructor(public payload:any) {
  }
}


export class UpdateFcPortSpeedAction implements Action {
  readonly type = UPDATE_SPEED_FCPORT;
  constructor(public payload:any) {
  }
}

export class UpdateFcPortSpeedActionSuccess implements Action {
  readonly type = UPDATE_SPEED_FCPORT_SUCCESS;
  constructor(public payload:any) {
  }
}

export type Actions
  = GetAllControllersAction
  | GetAllControllersActionSuccess
  | UpdateMRCAction
  | UpdateMRCActionSuccess
  | UpdateDataPacAction
  | UpdateDataPacActionSuccess
  | UpdateSpeedAction
  | UpdateSpeedActionSuccess
  | GetPowerSupplyAction
  | GetPowerSupplyActionSuccess
  | UpdateDataPACAction
  | UpdateDataPACActionSuccess
  | GetDataPACAction
  | GetDataPACActionSuccess
  | UpdateNetworkAction
  | UpdateNetworkActionSuccess
  | GetNetworkAction
  | GetNetworkActionSuccess
  | UpdatePowerSupplyAction
  | UpdatePowerSupplyActionSuccess
  | GetFansAction
  | GetFansActionSuccess
  | UpdateFansAction
  | UpdateFansActionSuccess
  | UpdateFcPortSpeedAction
  | UpdateFcPortSpeedActionSuccess;


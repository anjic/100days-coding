/**
 * Created by Venkatesh on 7/28/2017.
 */

import { Action } from '@ngrx/store';
import { Pools } from '../ise/models/pools';
import { Drives } from '../ise/models/drives';


export const GET_ALL_POOLS = '[Pool] getAll';
export const GET_ALL_POOLS_SUCCESS = '[Pool] getAll success';
export const GET_DRIVES = '[Pool] getDrives';
export const GET_DRIVES_SUCCESS = '[Pool] getDrives success';
export const GET_MEDIUM = '[Pool] getMedium';
export const GET_MEDIUM_SUCCESS = '[Pool] getMedium success';
export const CREATE_POOL = '[Pool] createPool';
export const CREATE_POOL_SUCCESS = '[Pool] createPool success';
export const EXPAND_POOL = '[Pool] expandPool';
export const EXPAND_POOL_SUCCESS = '[Pool] expandPool success';
export const DELETE_POOL = '[Pool] deletePool';
export const DELETE_POOL_SUCCESS = '[Pool] deletePool success';
export const GET_CHART = '[Pool] getchart';
export const GET_CHART_SUCCESS = '[Pool] getchart success';
export const GET_RATIO = '[Pool] getRatio';
export const GET_RATIO_SUCCESS = '[Pool] getRatio success';

export const ISE_ERROR = '[Pool] ISE_ERROR';
export const ISE_STATE_RESET = '[Pool] ISE_STATE_RESET';

export const UPDATE__DRIVES_IDENTIFY= '[Pool] updateDrivesIdentify';
export const UPDATE_DRIVES_IDENTIFY_SUCCESS = '[Pool] updateDrivesIdentify success';

export class IseError implements Action {
  readonly type = ISE_ERROR;
  constructor(public payload) {
  }
}

export class Reset implements Action {
  readonly type = ISE_STATE_RESET;
  constructor() {
  }
}

export class GetRatioAction implements Action {
  readonly type = GET_RATIO;
  constructor(public payload) {
  }
}

export class GetRatioSuccessAction implements Action {
  readonly type = GET_RATIO_SUCCESS;
  constructor(public payload) {
  }
}

export class GetChartAction implements Action {
  readonly type = GET_CHART;
  constructor(public payload) {
  }
}

export class GetChartSuccessAction implements Action {
  readonly type = GET_CHART_SUCCESS;
  constructor(public payload) {
  }
}

export class DeletePoolAction implements Action {
  readonly type = DELETE_POOL;
  constructor(public payload) {
  }
}

export class DeletePoolSuccessAction implements Action {
  readonly type = DELETE_POOL_SUCCESS;
  constructor(public payload) {
  }
}

export class ExpandPoolAction implements Action {
  readonly type = EXPAND_POOL;
  constructor(public payload) {
  }
}

export class ExpandPoolSuccessAction implements Action {
  readonly type = EXPAND_POOL_SUCCESS;
  constructor(public payload) {
  }
}


export class CreatePoolAction implements Action {
  readonly type = CREATE_POOL;
  constructor(public payload) {
  }
}

export class CreatePoolSuccessAction implements Action {
  readonly type = CREATE_POOL_SUCCESS;
  constructor(public payload) {
  }
}

export class GetAllPoolsAction implements Action {
  readonly type = GET_ALL_POOLS;
  constructor(public payload) {
  }
}

export class GetAllPoolsSuccessAction implements Action {
  readonly type = GET_ALL_POOLS_SUCCESS;
  constructor(public payload: Array<Pools>) {
  }
}

export class GetDrivesAction implements Action {
  readonly type = GET_DRIVES;
  constructor(public payload) {
  }
}

export class GetDrivesSuccessAction implements Action {
  readonly type = GET_DRIVES_SUCCESS;
  constructor(public payload) {
  }
}

export class GetMediumAction implements Action {
  readonly type = GET_MEDIUM;
  constructor(public payload) {
  }
}

export class GetMediumActionSuccess implements Action {
  readonly type = GET_MEDIUM_SUCCESS;
  constructor(public payload: Array<Pools>) {
  }
}

export class UpdateDrivesIdentifyAction implements Action {
  readonly type = UPDATE__DRIVES_IDENTIFY;
  constructor(public payload) {
  }
}

export class UpdateDrivesIdentifyActionSuccess implements Action {
  readonly type = UPDATE_DRIVES_IDENTIFY_SUCCESS;
  constructor(public payload) {
  }
}
export type Actions
  = GetAllPoolsAction
  | GetAllPoolsSuccessAction
  | GetDrivesAction
  | GetDrivesSuccessAction
  | GetMediumAction
  | GetMediumActionSuccess
  | CreatePoolAction
  | CreatePoolSuccessAction
  | ExpandPoolAction
  | ExpandPoolSuccessAction
  | DeletePoolAction
  | DeletePoolSuccessAction
  | GetChartAction
  | GetChartSuccessAction
  | GetRatioAction
  | GetRatioSuccessAction
  | IseError
  | Reset
  | UpdateDrivesIdentifyAction
  | UpdateDrivesIdentifyActionSuccess;

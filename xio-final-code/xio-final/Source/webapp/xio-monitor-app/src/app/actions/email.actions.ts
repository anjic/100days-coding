/**
 * Created by Dominic on 7/10/2017.
 */

import {Action} from '@ngrx/store';

export const GET_ALL_EMAIL = '[Email] getMenuContent';
export const GET_ALL_EMAIL_SUCCESS = '[Email] getMenuContent success';

export const ADD_EMAIL = '[Email] add';

export const DELETE_EMAIL = '[Email] delete';

export const ALERT_GET_DATA = '[Email] alertGet';
export const ALERT_GET_DATA_SUCCESS = '[Email] alertGet success';

export const ALERT_UPDATE_DATA = '[Email] alertUpdate';
export const ALERT_UPDATE_DATA_SUCCESS = '[Email] alertUpdate success';

export const GET_SMPT = '[Email] getSMPT';

export const CREATE_SMPT = '[Email] createSMPT';
export const CREATE_SMPT_SUCCESS = '[Email] createSMPT success';

export const GET_TEST_EMAIL = '[Email] getTest';
export const GET_TEST_EMAIL_SUCCESS = '[Email] getTest success';

export const UPDATE_EMAIL = '[Email] update';
export const UPDATE_EMAIL_SUCCESS = '[Email] update success';

/**
 * Every action is comprised of at least a type and an optional
 * payload. Expressing actions as classes enables powerful
 * type checking in reducer functions.
 *
 * See Discriminated Unions: https://www.typescriptlang.org/docs/handbook/advanced-types.html#discriminated-unions
 */

export class GetEmailAction implements Action {
  readonly type = GET_ALL_EMAIL;

  constructor(public payload: number) {
  }
}

export class GetEmailActionSuccess implements Action {
  readonly type = GET_ALL_EMAIL_SUCCESS;

  constructor(public payload) {
  }
}

export class AddEmailAction implements Action {
  readonly type = ADD_EMAIL;
  constructor(public payload) {}
}

export class DeleteEmailAction implements Action {
  readonly type = DELETE_EMAIL;
}

export class AlertGetDataAction implements Action {
  readonly type = ALERT_GET_DATA;
  constructor(public payload) {}
}
export class AlertGetDataActionSuccess implements Action {
  readonly type = ALERT_GET_DATA_SUCCESS;

  constructor(public payload) {}
}

export class AlertUpdateDataAction implements Action {
  readonly type = ALERT_UPDATE_DATA;

  constructor(public payload) {
  }
}

export class AlertUpdateDataActionSuccess implements Action {
  readonly type = ALERT_UPDATE_DATA_SUCCESS;

  constructor(public payload) {}
}


export class GetSMPTAction implements Action {
  readonly type = GET_SMPT;
  constructor(public payload) {}
}

export class CreateSMPTAction implements Action {
  readonly type = CREATE_SMPT;
  constructor(public payload) {
  }
}
export class CreateSMPTActionSuccess implements Action {
  readonly type = CREATE_SMPT_SUCCESS;

  constructor(public payload) {
  }
}

export class GetTestEmail implements Action {
  readonly type = GET_TEST_EMAIL;
  constructor(public payload) {}
}
export class GetTestEmailSuccess implements Action {
  readonly type = GET_TEST_EMAIL_SUCCESS;
  constructor(public payload) {}
}
export class UpdateEmailAction implements Action {
  readonly type = UPDATE_EMAIL;
  constructor(public payload) {}
}

export class  UpdateEmailActionSuccess implements Action {
  readonly type = UPDATE_EMAIL_SUCCESS;
  constructor(public payload) {}
}
/**
 * Export a type alias of all actions in this action group
 * so that reducers can easily compose action types
 */
export type Actions
  = GetEmailAction
  | GetEmailActionSuccess
  | AddEmailAction
  | DeleteEmailAction
  | AlertGetDataAction
  | AlertGetDataActionSuccess
  | AlertUpdateDataAction
  | AlertUpdateDataActionSuccess
  | GetSMPTAction
  | CreateSMPTActionSuccess
  | CreateSMPTAction
  | GetTestEmail
  | GetTestEmailSuccess
  | UpdateEmailAction
  | UpdateEmailActionSuccess;

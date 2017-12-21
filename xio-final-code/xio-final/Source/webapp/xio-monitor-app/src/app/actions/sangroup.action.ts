
/**
 * Created by Dominic on 7/15/2017.
 */

import { Action } from '@ngrx/store';
import { SANGroup } from '../san-group/models/san-group';

export const GET_ALL = '[SanGroup] getAll';
export const GET_ALL_SUCCESS = '[SanGroup] getAll success';

export const ADD_SANGROUP = '[SanGroup] add';
export const ADD_SANGROUP_SUCCESS = '[SanGroup] add success';

export const GET_SANGROUP = '[SanGroup] getMenuContent';
export const GET_SANGROUP_SUCCESS = '[SanGroup] getMenuContent success';

export const UPDATE_SANGROUP = '[SanGroup] update';
export const UPDATE_SANGROUP_SUCCESS = '[SanGroup] update success';

export const DELETE_SANGROUP = '[SanGroup] delete';
export const DELETE_SANGROUP_SUCCESS = '[SanGroup] delete success';

export const GET_ISELIST = '[SanGroup] getISEList';
export const GET_ISELIST_SUCCESS = '[SanGroup] getISEList success';

export const UPDATE_ISELIST = '[SanGroup] updateISEList';
export const UPDATE_ISELIST_SUCCESS = '[SanGroup] updateISEList success';

export const GET_SANGROUP_HOST = '[SanGroup] getSanGroupHost';
export const GET_SANGROUP_HOST_SUCCESS = '[SanGroup] getSanGroupHost success';

export const SAN_RESET = '[SanGroup] reset';
export const SAN_ISE_INFO_RESET = '[SanGroup] ISE Info reset';

/**
 * Every action is comprised of at least a type and an optional
 * payload. Expressing actions as classes enables powerful
 * type checking in reducer functions.
 *
 * See Discriminated Unions: https://www.typescriptlang.org/docs/handbook/advanced-types.html#discriminated-unions
 */

export class GetAllAction implements Action {
  readonly type = GET_ALL;

  constructor(public payload: Object = {}) {
  }
}

export class GetAllSuccessAction implements Action {
  readonly type = GET_ALL_SUCCESS;

  constructor(public payload: Array<SANGroup>) {
  }
}

export class AddSanGroupAction implements Action {
  readonly type = ADD_SANGROUP;

  constructor(public payload) {
  }
}

export class AddSanGroupActionSuccess implements Action {
  readonly type = ADD_SANGROUP_SUCCESS;

  constructor(public payload) {
  }
}

export class GetSanGroupAction implements Action {
  readonly type = GET_SANGROUP;

  constructor(public payload) {
  }
}

export class GetSanGroupActionSuccess implements Action {
  readonly type = GET_SANGROUP_SUCCESS;

  constructor(public payload) {
  }
}

export class UpdateSanGroupAction implements Action {
  readonly type = UPDATE_SANGROUP;

  constructor(public payload) {
  }
}

export class UpdateSanGroupActionSuccess implements Action {
  readonly type = UPDATE_SANGROUP_SUCCESS;

  constructor(public payload) {
  }
}

export class DeleteSanGroupAction implements Action {
  readonly type = DELETE_SANGROUP;

  constructor(public payload) {
  }
}

export class DeleteSanGroupActionSuccess implements Action {
  readonly type = DELETE_SANGROUP_SUCCESS;

  constructor(public payload) {
  }
}

export class GetISEListAction implements Action {
  readonly type = GET_ISELIST;

  constructor(public payload) {
  }
}

export class GetISEListActionSuccess implements Action {
  readonly type = GET_ISELIST_SUCCESS;

  constructor(public payload) {
  }
}

export class UpdateISEListAction implements Action {
  readonly type = UPDATE_ISELIST;

  constructor(public payload) {
  }
}

export class UpdateISEListActionSuccess implements Action {
  readonly type = UPDATE_ISELIST_SUCCESS;

  constructor(public payload) {
  }
}

export class GetSanGroupHostAction implements Action {
  readonly type = GET_SANGROUP_HOST;

  constructor(public payload) {
  }
}

export class GetSanGroupHostActionSuccess implements Action {
  readonly type = GET_SANGROUP_HOST_SUCCESS;

  constructor(public payload) {
  }
}

export class SanGroupReset implements Action {
  readonly type = SAN_RESET;
}

export class SanGroupISEInfoReset implements Action {
  readonly type = SAN_ISE_INFO_RESET;
}

/**
 * Export a type alias of all actions in this action group
 * so that reducers can easily compose action types
 */
export type Actions
  = GetAllAction
  | GetAllSuccessAction
  | AddSanGroupAction
  | AddSanGroupActionSuccess
  | GetSanGroupAction
  | GetSanGroupActionSuccess
  | UpdateSanGroupAction
  | UpdateSanGroupActionSuccess
  | DeleteSanGroupAction
  | DeleteSanGroupActionSuccess
  | GetISEListAction
  | GetISEListActionSuccess
  | UpdateISEListAction
  | UpdateISEListActionSuccess
  | GetSanGroupHostAction
  | GetSanGroupHostActionSuccess
  | SanGroupReset
  | SanGroupISEInfoReset;

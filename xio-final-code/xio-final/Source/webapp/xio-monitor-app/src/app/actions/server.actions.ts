
import {Action} from '@ngrx/store';

export const GET_ALL = '[Server] getAll';
export const GET_ALL_SUCCESS = '[Server] getAll success';

export const GET_WWN = '[Server] getWwn';
export const GET_WWN_SUCCESS = '[Server] getWwn success';


export const GET_SERVER_WWNGROUPS = '[Server] getServerWwnGroups';
export const GET_SERVER_WWNGROUPS_SUCCESS = '[Server] getServerWwnGroups success';

export const GET_ALL_WWN_GROUPS = '[Server] getAllWwnGroup';
export const GET_ALL_WWN_GROUPS_SUCCESS = '[Server] getAllWwnGroup success';

export const GET_SERVERSIDE_WWN_GROUPS = '[Server] getServerSideWwnGroup';
export const GET_SERVERSIDE_WWN_GROUPS_SUCCESS = '[Server] getServerSideWwnGroup success';

export const ADD_SERVER = '[Server] add';
export const ADD_SERVER_SUCCESS = '[Server] add success';

export const ADD_WWN_SERVER = '[Server] addwwn';
export const ADD_WWN_SERVER_SUCCESS = '[Server] addwwn success';

export const GET_SERVER = '[Server] getMenuContent';
export const GET_SERVER_SUCCESS = '[Server] getMenuContent success';

export const UPDATE_SERVER = '[Server] update';
export const UPDATE_SERVER_SUCCESS = '[Server] update success';

export const DELETE_SERVER = '[Server] delete';
export const DELETE_SERVER_SUCCESS = '[Server] delete success';

export const GET_SERVER_SAN = '[Server SAN] getMenuContent';
export const GET_SERVER_SAN_SUCCESS = '[Server SAN] getMenuContent success';

export const GET_SERVER_SAN_LINK = '[Server SAN] link';
export const GET_SERVER_SAN_LINK_SUCCESS = '[Server SAN] link success';

export const UPDATE_WWN_GROUP = '[Server Update_WWN] link';
export const UPDATE_WWN_GROUP_SUCCESS = '[Server Update_WWN] link success';


/**
 * Every action is comprised of at least a type and an optional
 * payload. Expressing actions as classes enables powerful
 * type checking in reducer functions.
 *
 * See Discriminated Unions: https://www.typescriptlang.org/docs/handbook/advanced-types.html#discriminated-unions
 */

export class UpdateWWNAction implements Action {
  readonly type = UPDATE_WWN_GROUP;

  constructor(public payload: Object = {}) {
  }
}

export class UpdateWWNSuccessAction implements Action {
  readonly type = UPDATE_WWN_GROUP_SUCCESS;

  constructor(public payload: Object = {}) {
  }
}

export class GetAllAction implements Action {
  readonly type = GET_ALL;

  constructor(public payload: Object = {}) {
  }
}
export class GetAllSuccessAction implements Action {
  readonly type = GET_ALL_SUCCESS;

  constructor(public payload: Array<Object>) {
  }
}

export class GetWwnAction implements Action {
  readonly type = GET_WWN;

  constructor(public payload: Object = {}) {
  }
}
export class GetWwnSuccessAction implements Action {
  readonly type = GET_WWN_SUCCESS;

  constructor(public payload: Array<Object>) {
  }
}

export class GetServerWwnGroupAction implements Action {
  readonly type = GET_SERVER_WWNGROUPS;

  constructor(public payload: Object = {}) {
  }
}
export class GetServerWwnGroupSuccessAction implements Action {
  readonly type = GET_SERVER_WWNGROUPS_SUCCESS;

  constructor(public payload: Array<Object>) {
  }
}

export class GetAllWwnGroupAction implements Action {
  readonly type = GET_ALL_WWN_GROUPS;

  constructor(public payload: Object = {}) {
  }
}
export class GetAllWwnGroupSuccessAction implements Action {
  readonly type = GET_ALL_WWN_GROUPS_SUCCESS;

  constructor(public payload: Array<Object>) {
  }
}

export class GetServerSideWwnGroupAction implements Action {
  readonly type = GET_SERVERSIDE_WWN_GROUPS;

  constructor(public payload: Object = {}) {
  }
}
export class GetServerSideWwnGroupSuccessAction implements Action {
  readonly type = GET_SERVERSIDE_WWN_GROUPS_SUCCESS;

  constructor(public payload: Array<Object>) {
  }
}

export class AddServerAction implements Action {
  readonly type = ADD_SERVER;

  constructor(public payload) {
  }
}
export class AddServerActionSuccess implements Action {
  readonly type = ADD_SERVER_SUCCESS;

  constructor(public payload) {
  }
}

export class AddWwnServerAction implements Action {
  readonly type = ADD_WWN_SERVER;

  constructor(public payload) {
  }
}
export class AddWwnServerActionSuccess implements Action {
  readonly type = ADD_WWN_SERVER_SUCCESS;

  constructor(public payload) {
  }
}

export class GetServerAction implements Action {
  readonly type = GET_SERVER;

  constructor(public payload) {
  }
}
export class GetServerActionSuccess implements Action {
  readonly type = GET_SERVER_SUCCESS;

  constructor(public payload) {
  }
}


export class UpdateServerAction implements Action {
  readonly type = UPDATE_SERVER;

  constructor(public payload) {
  }
}
export class UpdateServerActionSuccess implements Action {
  readonly type = UPDATE_SERVER_SUCCESS;

  constructor(public payload) {
  }
}


export class DeleteServerAction implements Action {
  readonly type = DELETE_SERVER;

  constructor(public payload) {
  }
}
export class DeleteServerActionSuccess implements Action {
  readonly type = DELETE_SERVER_SUCCESS;

  constructor(public payload) {
  }
}

export class GetServerSanGroup implements Action {
  readonly type = GET_SERVER_SAN;

  constructor(public payload) {
  }
}
export class GetServerSanGroupSuccess implements Action {
  readonly type = GET_SERVER_SAN_SUCCESS;

  constructor(public payload) {
  }
}

export class ChangeServerLink implements Action {
  readonly type = GET_SERVER_SAN_LINK;

  constructor(public payload) {
  }
}
export class ChangeServerLinkSuccess implements Action {
  readonly type = GET_SERVER_SAN_LINK_SUCCESS;

  constructor(public payload) {
  }
}


/**
 * Export a type alias of all actions in this action group
 * so that reducers can easily compose action types
 */
export type Actions
  = GetAllAction
  | GetAllSuccessAction
  | GetWwnAction
  | GetWwnSuccessAction
  | GetServerWwnGroupAction
  | GetServerWwnGroupSuccessAction
  | GetAllWwnGroupAction
  | GetAllWwnGroupSuccessAction
  | GetServerSideWwnGroupAction
  | GetServerSideWwnGroupSuccessAction
  | AddServerAction
  | AddServerActionSuccess
  | AddWwnServerAction
  | AddWwnServerActionSuccess
  | GetServerAction
  | GetServerActionSuccess
  | UpdateServerAction
  | UpdateServerActionSuccess
  | DeleteServerAction
  | DeleteServerActionSuccess
  | GetServerSanGroup
  | GetServerSanGroupSuccess
  | ChangeServerLink
  | ChangeServerLinkSuccess
  | UpdateWWNAction
  | UpdateWWNSuccessAction;

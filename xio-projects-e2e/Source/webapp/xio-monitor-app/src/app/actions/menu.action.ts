/**
 * Created by Dominic on 8/21/2017.
 */

import {Action} from '@ngrx/store';

export const GET_MENU = '[Menu] get ';
export const GET_MENU_SUCCESS = '[Menu] get success';

export const GET_HOST = '[Menu] get host';
export const GET_HOST_SUCCESS = '[Menu] get host success';

export const ADD_MENU_SAN = '[Menu] add SanGroup ';
export const ADD_MENU_SAN_SUCCESS = '[Menu] add SanGroup success';

export const DELETE_MENU_SAN = '[Menu] delete SanGroup ';
export const DELETE_MENU_SAN_SUCCESS = '[Menu] delete SanGroup success';

export class GetMenuAction implements Action {
  readonly type = GET_MENU;
  constructor(public payload) {
  }
}

export class GetMenuActionSuccess implements Action {
  readonly type = GET_MENU_SUCCESS;

  constructor(public payload) {
  }
}

export class GetMenuHostAction implements Action {
  readonly type = GET_HOST;
  constructor(public payload) {
  }
}

export class GetMenuHostActionSuccess implements Action {
  readonly type = GET_HOST_SUCCESS;

  constructor(public payload) {
  }
}

export class AddMenuSanGroup implements Action {
  readonly type = ADD_MENU_SAN;
  constructor(public payload) {
  }
}

export class AddMenuSanGroupSuccess implements Action {
  readonly type = ADD_MENU_SAN_SUCCESS;

  constructor(public payload) {
  }
}

export class DeleteMenuSanGroup implements Action {
  readonly type = DELETE_MENU_SAN;
  constructor(public payload) {
  }
}

export class DeleteMenuSanGroupSuccess implements Action {
  readonly type = DELETE_MENU_SAN_SUCCESS;

  constructor(public payload) {
  }
}


export type Actions
  = GetMenuAction
  | GetMenuActionSuccess
  | GetMenuHostAction
  | GetMenuHostActionSuccess
  | AddMenuSanGroup
  | DeleteMenuSanGroup;


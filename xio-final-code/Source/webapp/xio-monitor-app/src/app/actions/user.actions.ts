
import { Action } from '@ngrx/store';
import { User } from "../user/models/user";

export const GET_ALL_USERS = "[User] getAll";
export const GET_ALL_USERS_SUCCESS = '[User] getAll success';
export const SAVE_USER = "[User] createUser";
export const SAVE_USER_SUCCESS = "[User] createUser success";
export const UPDATE_USER = "[User] editUser";
export const UPDATE_USER_SUCCESS = "[User] editUser success";
export const DELETE_USER = "[User] deleteUser";
export const DELETE_USER_SUCCESS = "[User] deleteUser success";
export const GET_USER = "[User] getUser";
export const GET_USER_SUCCESS = "[User] getUser success";
export const CHANGE_USER_PWD = '[USER PWD] change';
export const CHANGE_USER_PWD_SUCCESS = '[USER PWD] change success';

export class GetAllUsersAction implements Action {
  readonly type = GET_ALL_USERS;

    constructor(public payload: Object = {}) {
  }
}

export class GetAllUsersActionSuccess implements Action {
  readonly type = GET_ALL_USERS_SUCCESS;

  constructor(public payload: Array<User>) {
  }
}

export class GetUserAction implements Action {
  readonly type = GET_USER;
  constructor(public payload) {
  }
}

export class GetUserActionSuccess implements Action {
  readonly type = GET_USER_SUCCESS;
  constructor(public payload) {
  }
}

export class SaveUserAction implements Action {
  readonly type = SAVE_USER;

  constructor(public payload) {
  }
}

export class SaveUserActionSuccess implements Action {
  readonly type = SAVE_USER_SUCCESS;

  constructor(public payload) {
  }
}

export class UpdateUserAction implements Action {
  readonly type = UPDATE_USER;

  constructor(public payload) {
  }
}

export class UpdateUserActionSuccess implements Action {
  readonly type = UPDATE_USER_SUCCESS;

  constructor(public payload) {
  }
}

export class DeleteUserAction implements Action {
  readonly type = DELETE_USER;

  constructor(public payload) {
  }
}

export class DeleteUserActionSuccess implements Action {
  readonly type = DELETE_USER_SUCCESS;

  constructor(public payload) {
  }
}

export class ChangeUSERPWD implements Action {
  readonly type = CHANGE_USER_PWD;

  constructor(public payload) {
  }
}
export class ChangeUSERPWDSuccess implements Action {
  readonly type = CHANGE_USER_PWD_SUCCESS;

  constructor(public payload) {
  }
}

/**
 * Export a type alias of all actions in this action group
 * so that reducers can easily compose action types
 */
export type Actions
  = GetAllUsersAction
  | GetAllUsersActionSuccess
  | GetUserAction
  | GetUserActionSuccess
  | SaveUserAction
  | SaveUserActionSuccess
  | UpdateUserAction
  | UpdateUserActionSuccess
  | DeleteUserAction
  | DeleteUserActionSuccess
  | ChangeUSERPWD
  | ChangeUSERPWDSuccess;

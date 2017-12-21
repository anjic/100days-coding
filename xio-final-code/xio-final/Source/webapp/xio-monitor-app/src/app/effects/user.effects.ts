/**
 * Created by Venkatesh on 7/13/2017.
 */
import { Injectable } from "@angular/core";
import { Effect, Actions, toPayload } from '@ngrx/effects';
import { Observable } from "rxjs";
import { Action } from '@ngrx/store';
import * as userActions from '../actions/user.actions';
import { UserService } from "../user/services/user.service";
import { EffectSwitchMapCb } from "../common/utils/EffectsSwitchMapCb";

@Injectable()
export class UserEffects {

  constructor(public actions: Actions,
    public userService: UserService) {
  }

  @Effect()
  getAll$: Observable<Action> = this.actions
    .ofType(userActions.GET_ALL_USERS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.userService, 'getAll', query, userActions['GetAllUsersActionSuccess'], null);
    }).share();

  @Effect()
  getUser$: Observable<Action> = this.actions
    .ofType(userActions.GET_USER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.userService, 'getUser', query, userActions['GetUserActionSuccess'], null);
    }).share();

  @Effect()
  createUser$: Observable<Action> = this.actions
    .ofType(userActions.SAVE_USER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.userService, 'createUser', query, userActions['SaveUserActionSuccess'], null);
    }).share();

  @Effect()
  updateUser$: Observable<Action> = this.actions
    .ofType(userActions.UPDATE_USER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.userService, 'updateUser', query, userActions['UpdateUserActionSuccess'], null);
    }).share();

  @Effect()
  deleteUser$: Observable<Action> = this.actions
    .ofType(userActions.DELETE_USER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.userService, 'deleteUser', query, userActions['DeleteUserActionSuccess'], null);
    }).share();


    @Effect()
  changeUSERPassword$: Observable<Action> = this.actions
    .ofType(userActions.CHANGE_USER_PWD)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.userService, 'changeUserPassword', query, userActions['ChangeUSERPWDSuccess'], null);
    }).share();
}

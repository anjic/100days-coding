
import 'rxjs/add/operator/switchMap';
import {Injectable} from '@angular/core';
import {Effect, Actions, toPayload} from '@ngrx/effects';
import {Action} from '@ngrx/store';
import {Observable} from 'rxjs/Observable';

import {ServermanagementService} from '../server/service/servermanagement.service';
import * as ServerActions from '../actions/server.actions';
import {EffectSwitchMapCb} from '../common/utils/EffectsSwitchMapCb';


/**
 * Effects offer a way to isolate and easily test side-effects within your
 * application.
 * The `toPayload` helper function returns just
 * the payload of the currently dispatched action, useful in
 * instances where the current state is not necessary.
 *
 * Documentation on `toPayload` can be found here:
 * https://github.com/ngrx/effects/blob/master/docs/api.md#topayload
 *
 * If you are unfamiliar with the operators being used in these examples, please
 * check out the sources below:
 *
 * Official Docs: http://reactivex.io/rxjs/manual/overview.html#categories-of-operators
 * RxJS 5 Operators By Example: https://gist.github.com/btroncone/d6cf141d6f2c00dc6b35
 */

@Injectable()
export class ServerEffects {

  @Effect()
  getAll$: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_ALL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getAll', query, ServerActions['GetAllSuccessAction'], null);
    }).share();

  @Effect()
  getAllWwnGroupsgetAllWwnGroups: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_ALL_WWN_GROUPS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getAllWwnGroups', query, ServerActions['GetAllWwnGroupSuccessAction'], null);
    }).share();


  @Effect()
  getServerSideWwnGroups: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_SERVERSIDE_WWN_GROUPS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getserverside', query, ServerActions['GetServerSideWwnGroupSuccessAction'], null);
    }).share();


  @Effect()
  getAddServerAction$: Observable<Action> = this.actions$
    .ofType(ServerActions.ADD_SERVER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'addServer', query, ServerActions['AddServerActionSuccess'], null);
    }).share();

  @Effect()
  getServerAction$: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_SERVER)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getServer', query, ServerActions['GetServerActionSuccess'], null);
    }).share();

  @Effect()
  getUpdateServerAction$: Observable<Action> = this.actions$
    .ofType(ServerActions.UPDATE_SERVER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'updateServer', query, ServerActions['UpdateServerActionSuccess'], null);
    }).share();

  @Effect()
  getDeleteServerAction$: Observable<Action> = this.actions$
    .ofType(ServerActions.DELETE_SERVER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'deleteServer', query, ServerActions['DeleteServerActionSuccess'], null);
    }).share();

  @Effect()
  getServerSangroup$: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_SERVER_SAN)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getServerSangroup', query, ServerActions['GetServerSanGroupSuccess'], null);
    });

  @Effect()
  updateServerSangroupLink$: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_SERVER_SAN_LINK)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'updateServerSglink', query, ServerActions['ChangeServerLinkSuccess'], null);
    });

  @Effect()
  getWwn$: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_WWN)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getServerWwn', query, ServerActions['GetWwnSuccessAction'], null);
    }).share();


  @Effect()
  getServerWwnGroups$: Observable<Action> = this.actions$
    .ofType(ServerActions.GET_SERVER_WWNGROUPS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'getServerWwnGroups', query, ServerActions['GetServerWwnGroupSuccessAction'], null);
    }).share();


  @Effect()
  getAddWwnServerAction$: Observable<Action> = this.actions$
    .ofType(ServerActions.ADD_WWN_SERVER)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'addWwnServer', query, ServerActions['AddWwnServerActionSuccess'], null);
    }).share();


  @Effect()
  updateISEWWNGroupAction$: Observable<Action> = this.actions$
    .ofType(ServerActions.UPDATE_WWN_GROUP)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.ServermanagementService, 'updateWWNGroup', query, ServerActions['UpdateWWNSuccessAction'], null);
    }).share();


    constructor(public actions$: Actions, public ServermanagementService: ServermanagementService) {
  }

}

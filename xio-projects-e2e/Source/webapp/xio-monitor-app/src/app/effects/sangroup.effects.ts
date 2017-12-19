/**
 * Created by Dominic on 7/15/2017.
 */


import 'rxjs/add/operator/switchMap';
import { Injectable } from '@angular/core';
import { Effect, Actions, toPayload } from '@ngrx/effects';
import { Action } from '@ngrx/store';
import { Observable } from 'rxjs/Observable';

import { SangroupService } from '../san-group/services/sangroup.service';
import * as SanGroupActions from '../actions/sangroup.action';
import { EffectSwitchMapCb } from '../common/utils/EffectsSwitchMapCb';

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
export class SanGroupEffects {

  @Effect()
  getAll$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.GET_ALL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'getAll', query, SanGroupActions['GetAllSuccessAction'], null);
    }).share();

  @Effect()
  getAddSanGroupAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.ADD_SANGROUP)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'addSangroup', query, SanGroupActions['AddSanGroupActionSuccess'], null);
    }).share();

  @Effect()
  getSanGroupAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.GET_SANGROUP)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'getSangroup', query, SanGroupActions['GetSanGroupActionSuccess'], null);
    }).share();

  @Effect()
  getUpdateSanGroupAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.UPDATE_SANGROUP)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'updateSangroup', query, SanGroupActions['UpdateSanGroupActionSuccess'], null);
    }).share();

  @Effect()
  getDeleteSanGroupAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.DELETE_SANGROUP)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'deleteSangroup', query, SanGroupActions['DeleteSanGroupActionSuccess'], null);
    }).share();

  @Effect()
  getGetISEAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.GET_ISELIST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'getIseList', query, SanGroupActions['GetISEListActionSuccess'], null);
    }).share();

  @Effect()
  getUpdateISEAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.UPDATE_ISELIST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'updateSgISElink', query, SanGroupActions['UpdateISEListActionSuccess'], null);
    }).share();

  @Effect()
  getSanGroupHostAction$: Observable<Action> = this.actions$
    .ofType(SanGroupActions.GET_SANGROUP_HOST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.sanGroupService, 'getSangroupHost', query, SanGroupActions['GetSanGroupHostActionSuccess'], null);
    }).share();

  constructor(public actions$: Actions, public sanGroupService: SangroupService) {
  }
}

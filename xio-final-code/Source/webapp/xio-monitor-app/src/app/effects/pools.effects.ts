/**
 * Created by Venkatesh on 7/28/2017.
 */
import {Injectable} from "@angular/core";
import {PoolsService} from "../ise/services/pools.service";
import {Effect,Actions, toPayload} from "@ngrx/effects";
import {Observable} from "rxjs";
import {Action} from '@ngrx/store';
import * as poolsActions from '../actions/pools.actions';
import {EffectSwitchMapCb} from "../common/utils/EffectsSwitchMapCb";

@Injectable()
export class PoolsEffects {
    constructor(public actions: Actions,
                public poolsService: PoolsService ) {

    }

  @Effect()
  getAll$: Observable<Action> = this.actions
    .ofType(poolsActions.GET_ALL_POOLS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'getAll', query, poolsActions['GetAllPoolsSuccessAction'], null);
    });

  @Effect()
  getDrives$: Observable<Action> = this.actions
    .ofType(poolsActions.GET_DRIVES)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'getDrives', query, poolsActions['GetDrivesSuccessAction'], null);
    });

  @Effect()
  getMedium$: Observable<Action> = this.actions
    .ofType(poolsActions.GET_MEDIUM)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'getMedium', query, poolsActions['GetMediumActionSuccess'], null);
    });

  @Effect()
  createPool$: Observable<Action> = this.actions
    .ofType(poolsActions.CREATE_POOL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'createPool', query, poolsActions['CreatePoolSuccessAction'], null);
    });

  @Effect()
  expandPool$: Observable<Action> = this.actions
    .ofType(poolsActions.EXPAND_POOL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'expandPool', query, poolsActions['ExpandPoolSuccessAction'], null);
    });

  @Effect()
  deletePool$: Observable<Action> = this.actions
    .ofType(poolsActions.DELETE_POOL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'deletePool', query, poolsActions['DeletePoolSuccessAction'], null);
    });

  @Effect()
  getRatio$: Observable<Action> = this.actions
    .ofType(poolsActions.GET_RATIO)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'getRatio', query, poolsActions['GetRatioSuccessAction'], null);
    });


  @Effect()
  getChart$: Observable<Action> = this.actions
    .ofType(poolsActions.GET_CHART)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'getChart', query, poolsActions['GetChartSuccessAction'], null);
    });

  @Effect()
  updateDrivesIdentify$: Observable<Action> = this.actions
    .ofType(poolsActions.UPDATE__DRIVES_IDENTIFY)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.poolsService, 'updateDrivesIdentify', query, poolsActions['UpdateDrivesIdentifyActionSuccess'], null);
    });

}

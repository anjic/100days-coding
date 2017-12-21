/**
 * Created by Venkatesh on 7/19/2017.
 */
import { Injectable } from "@angular/core";
import { Effect, Actions, toPayload } from '@ngrx/effects';
import { MrcService } from "../ise/services/mrc.service";
import { Observable } from "rxjs/Observable";
import { Action } from '@ngrx/store';
import * as hardwareActions from '../actions/hardware.actions';
import { EffectSwitchMapCb } from "../common/utils/EffectsSwitchMapCb";


@Injectable()
export class HardWareEffects {

  constructor(public actions: Actions,
    public mrcService: MrcService) {
  }

  @Effect()
  getControllers$: Observable<Action> = this.actions
    .ofType(hardwareActions.GET_CONTROLLERS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'getControllers', query, hardwareActions['GetAllControllersActionSuccess'], null);
    }).share();


  @Effect()
  updateMrc$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_MRC)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'updateMrc', query, hardwareActions['UpdateMRCActionSuccess'], null);
    }).share();

  @Effect()
  updateDataPac$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_DATA_PAC)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'updateDataPac', query, hardwareActions['UpdateDataPacActionSuccess'], null);
    }).share();

  @Effect()
  UpdateSpeed$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_SPEED)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'UpdateSpeed', query, hardwareActions['UpdateSpeedActionSuccess'], null);
    }).share();

  @Effect()
  getNetwork$: Observable<Action> = this.actions
    .ofType(hardwareActions.GET_NETWORK)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'getNetwork', query, hardwareActions['GetNetworkActionSuccess'], null);
    }).share();

  @Effect()
  updateNetwork$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_NETWORK)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'updateNetwork', query, hardwareActions['UpdateNetworkActionSuccess'], null);
    }).share();

  @Effect()
  getPowerSupply$: Observable<Action> = this.actions
    .ofType(hardwareActions.GET_POWER_SUPPLY)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'getPowerSupply', query, hardwareActions['GetPowerSupplyActionSuccess'], null);
    }).share();

  @Effect()
  getDataPac$: Observable<Action> = this.actions
    .ofType(hardwareActions.GET_DATA_PAC)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'getDataPac', query, hardwareActions['GetDataPACActionSuccess'], null);
    }).share();

  @Effect()
  updatePowerSupply$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_POWER_SUPPLY)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'updatePowerSupply', query, hardwareActions['UpdatePowerSupplyActionSuccess'], null);
    }).share();

  @Effect()
  getFans$: Observable<Action> = this.actions
    .ofType(hardwareActions.GET_FANS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'getFans', query, hardwareActions['GetFansActionSuccess'], null);
    }).share();

  @Effect()
  updateFans$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_FANS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'updateFans', query, hardwareActions['UpdateFansActionSuccess'], null);
    }).share();


  @Effect()
  UpdateFcportSpeed$: Observable<Action> = this.actions
    .ofType(hardwareActions.UPDATE_SPEED_FCPORT)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.mrcService, 'updateFcport', query, hardwareActions['UpdateFcPortSpeedActionSuccess'], null);
    }).share();


}





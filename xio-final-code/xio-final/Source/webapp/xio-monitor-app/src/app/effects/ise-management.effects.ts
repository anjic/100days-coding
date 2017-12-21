/**
 * Created by Dominic on 7/27/2017.
 */

import 'rxjs/add/operator/switchMap';
import { Injectable } from '@angular/core';
import { Effect, Actions, toPayload } from '@ngrx/effects';
import { Action } from '@ngrx/store';
import { Observable } from 'rxjs/Observable';

import { IseService } from '../ise/services/ise.service';
import * as iseManagement from '../actions/ise-management.actions';
import { EffectSwitchMapCb } from '../common/utils/EffectsSwitchMapCb';

@Injectable()
export class ISEManagementEffects {

  @Effect()
  getAll$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_ALL_ISE_LIST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getAll', query, iseManagement['GetAllISEListSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getISE$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_ISE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getISE', query, iseManagement['GetISEInfoSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getDiscovery$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_DISCOVERY)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getDiscovery', query, iseManagement['GetDiscoverySuccess'], iseManagement['IseError']);
    });  
  
  
  @Effect()
    getISEDetail$: Observable<Action> = this.actions$
      .ofType(iseManagement.GET_ISE_DETAIL)
      .map(toPayload)
      .switchMap(query => {
        return EffectSwitchMapCb(this.IseService, 'getISEInfo', query, iseManagement['GetIseDetailSuccess'], iseManagement['IseError']);
      });  
    
  @Effect()
  addISE$: Observable<Action> = this.actions$
    .ofType(iseManagement.ADD_ISE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'addIse', query, iseManagement['AddISESuccess'], iseManagement['IseError']);
    });

  @Effect()
  deleteISE$: Observable<Action> = this.actions$
    .ofType(iseManagement.DELETE_ISE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'deleteISE', query, iseManagement['DeleteISESuccess'], iseManagement['IseError']);
    });

  @Effect()
  updateISE$: Observable<Action> = this.actions$
    .ofType(iseManagement.UPDATE_ISE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'updateISE', query, iseManagement['UpdateISESuccess'], iseManagement['IseError']);
    });

  @Effect()
  changeISEPassword$: Observable<Action> = this.actions$
    .ofType(iseManagement.CHANGE_ISE_PWD)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'changeISEPassword', query, iseManagement['ChangeISEPWDSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getISESangroup$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_ISE_SAN)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getISESangroup', query, iseManagement['GetISESanGroupSuccess'], iseManagement['IseError']);
    });

  @Effect()
  updateISESangroupLink$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_ISE_SAN_LINK)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'updateISESangroupLink', query, iseManagement['ChangeISELinkSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getCardInfo$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_ISE_CARD_INFO)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getCardInfo', query, iseManagement['GetISECardInfoSuccess'], iseManagement['IseError']);
    });

  // @Effect()
  // getStorageInfo$: Observable<Action> = this.actions$
  //   .ofType(iseManagement.GET_STORAGE_INFO)
  //   .map(toPayload)
  //   .switchMap(query => {
  //     return EffectSwitchMapCb(this.IseService, 'getStorageInfo', query, iseManagement['GetStorageInfoSuccess'], iseManagement['IseError']);
  //   });

  @Effect()
  getchartdata$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_IOPS_CHART_DATA)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getchartdata', query, iseManagement['GetIOPSChartDataSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getLatencychartdata$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_LATENCY_CHART_DATA)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getchartdata', query, iseManagement['GetLatencyChartDataSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getDataratechartdata$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_DataRate_CHART_DATA)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getchartdata', query, iseManagement['GetDataRateChartDataSuccess'], iseManagement['IseError']);
    });

  @Effect()
  getqDepthchartdata$: Observable<Action> = this.actions$
    .ofType(iseManagement.GET_QDepth_CHART_DATA)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.IseService, 'getchartdata', query, iseManagement['GetQDepthChartDataSuccess'], iseManagement['IseError']);
    });

  @Effect()
  changeISEIP$: Observable<Action> = this.actions$
    .ofType(iseManagement.CHANGE_ISE_IP)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.IseService, 'changeISEIPAddress', query, iseManagement['ChangeISEIPSuccess'], iseManagement['IseError']);
    });

  constructor(public actions$: Actions, public IseService: IseService) {
  }
}

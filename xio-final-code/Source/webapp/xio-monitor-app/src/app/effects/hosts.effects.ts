/**
 * Created by Venkatesh on 7/31/2017.
 */
import {Injectable} from "@angular/core";
import {Effect, Actions, toPayload} from '@ngrx/effects';
import {Observable} from "rxjs";
import {Action} from '@ngrx/store';
import * as hostsActions from '../actions/hosts.actions';
import {EffectSwitchMapCb} from "../common/utils/EffectsSwitchMapCb";
import {HostService} from "../ise/services/host.service";

@Injectable()
export class HostEffects{

  constructor(public actions: Actions,
              public hostService:HostService){

  }

  @Effect()
  getAll$: Observable<Action> = this.actions
    .ofType(hostsActions.GET_ALL_HOSTS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.hostService, 'getAll', query, hostsActions['GetAllHostsActionSuccess'], null);
    }).share()

  @Effect()
  getHost$: Observable<Action> = this.actions
    .ofType(hostsActions.GET_HOST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.hostService, 'getHost', query, hostsActions['GetHostActionSuccess'], null);
    }).share()

  @Effect()
  deleteHost$: Observable<Action> = this.actions
    .ofType(hostsActions.DELETE_HOST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.hostService, 'deleteHost', query, hostsActions['DeleteHostActionSuccess'], null);
    }).share()

  @Effect()
  updateHosts$: Observable<Action> = this.actions
    .ofType(hostsActions.UPDATE_HOST)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.hostService, 'updateHosts', query, hostsActions['UpdateHostActionSuccess'], null);
    }).share()

  @Effect()
  updateVolumeAllocation$: Observable<Action> = this.actions
    .ofType(hostsActions.UPDATE_VOLUME_ALLOCATION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.hostService, 'updateVolumeAllocation', query, hostsActions['UpdateVolumeAllocationActionSuccess'], null);
    }).share()

  @Effect()
  getHostVolume$: Observable<Action> = this.actions
    .ofType(hostsActions.GET_HOST_VOLUME)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.hostService, 'getHostVolume', query, hostsActions['GetHostVolumeActionSuccess'], null);
    }).share()
}




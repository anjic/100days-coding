/**
 * Created by Venkatesh on 7/28/2017.
 */
import {Injectable} from "@angular/core";
import {StoragevolumeService} from "../ise/services/storagevolume.service";
import {Effect,Actions, toPayload} from "@ngrx/effects";
import {Observable} from "rxjs";
import {Action} from '@ngrx/store';
import * as volumeActions from '../actions/volume.actions';
import {EffectSwitchMapCb} from "../common/utils/EffectsSwitchMapCb";


@Injectable()
export class VolumeEffects{

  constructor(public actions: Actions,
              public storagevolumeService: StoragevolumeService) {
  }

  @Effect()
  getAll$: Observable<Action> = this.actions
    .ofType(volumeActions.GET_ALL_VOLUMES)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'getAll', query, volumeActions['GetAllVolumesSuccessAction'], null);
    }).share();

  @Effect()
  addVolumesdetails$: Observable<Action> = this.actions
    .ofType(volumeActions.ADD_VOLUME_DETAILS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'addVolumesdetails', query, volumeActions['AddVolumeDetailsSuccessAction'], null);
    }).share();

  @Effect()
  getVolumeDetails$: Observable<Action> = this.actions
    .ofType(volumeActions.GET_VOLUME_DETAILS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'getVolumeDetails', query, volumeActions['GetVolumeDetailsSuccessAction'], null);
    }).share();

  @Effect()
  updateVolumeDetails$: Observable<Action> = this.actions
    .ofType(volumeActions.UPDATE_VOLUME_DETAILS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'updateVolumeDetails', query, volumeActions['UpdateVolumeDetailsSuccessAction'], null);
    }).share();

  @Effect()
  deleteVolumeDetails$: Observable<Action> = this.actions
    .ofType(volumeActions.DELETE_VOLUME_DETAILS)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'deleteVolumeDetails', query, volumeActions['DeleteVolumeDeleteSuccessAction'], null);
    }).share();

  @Effect()
  updateVolumeAllocation$: Observable<Action> = this.actions
    .ofType(volumeActions.UPDATE_VOLUME_ALLOCATION)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'updateVolumeAllocation', query, volumeActions['UpdateVolumeAllocationSuccessAction'], null);
    }).share();

  @Effect()
  getTotalSize$: Observable<Action> = this.actions
    .ofType(volumeActions.GET_TOTAL_SIZE)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.storagevolumeService, 'getTotalSize', query, volumeActions['GetTotalSizeSuccessAction'], null);
    }).share();
}

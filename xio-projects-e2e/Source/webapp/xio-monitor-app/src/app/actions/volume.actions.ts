/**
 * Created by Venkatesh on 7/28/2017.
 */

import {Action} from '@ngrx/store';

export const GET_ALL_VOLUMES = '[Volume] getAll';
export const GET_ALL_VOLUMES_SUCCESS = '[Volume] getAll success';
export const ADD_VOLUME_DETAILS = '[Volume] addVolumesdetails';
export const ADD_VOLUME_DETAILS_SUCCESS = '[Volume] addVolumesdetails success';
export const GET_VOLUME_DETAILS = '[Volume] getVolumeDetails';
export const GET_VOLUME_DETAILS_SUCCESS = '[Volume] getVolumeDetails success';
export const UPDATE_VOLUME_DETAILS = '[Volume] updateVolumeDetails';
export const UPDATE_VOLUME_DETAILS_SUCCESS = '[Volume] updateVolumeDetails success';
export const DELETE_VOLUME_DETAILS = '[Volume] deleteVolumeDetails';
export const DELETE_VOLUME_DETAILS_SUCCESS = '[Volume] deleteVolumeDetails success';


export const UPDATE_VOLUME_ALLOCATION = '[Volume] updateVolumeAllocation';
export const UPDATE_VOLUME_HOST_ALLOCATION_SUCCESS = '[Volume] updateVolumeAllocation success';
export const GET_TOTAL_SIZE = '[Volume] getTotalSize';
export const GET_TOTAL_SIZE_SUCCESS = '[Volume] getTotalSize success';
export const VOL_RESET = '[Volume] Reset';


export class GetAllVolumesAction implements Action {
  readonly type = GET_ALL_VOLUMES;
  constructor(public payload: any) {
  }
}

export class GetAllVolumesSuccessAction implements Action {
  readonly type = GET_ALL_VOLUMES_SUCCESS;
  constructor(public payload) {
  }
}

export class AddVolumeDetailsAction implements Action {
  readonly type = ADD_VOLUME_DETAILS;
  constructor(public payload: any) {
  }
}

export class AddVolumeDetailsSuccessAction implements Action {
  readonly type = ADD_VOLUME_DETAILS_SUCCESS;
  constructor(public payload) {
  }
}

export class GetVolumeDetailsAction implements Action {
  readonly type = GET_VOLUME_DETAILS;
  constructor(public payload: any) {
  }
}

export class GetVolumeDetailsSuccessAction implements Action {
  readonly type = GET_VOLUME_DETAILS_SUCCESS;
  constructor(public payload) {
  }
}

export class UpdateVolumeDetailsAction implements Action {
  readonly type = UPDATE_VOLUME_DETAILS;
  constructor(public payload: any) {
  }
}

export class UpdateVolumeDetailsSuccessAction implements Action {
  readonly type = UPDATE_VOLUME_DETAILS_SUCCESS;
  constructor(public payload) {
  }
}

export class UpdateVolumeAllocationAction implements Action {
  readonly type = UPDATE_VOLUME_ALLOCATION;
  constructor(public payload: any) {
  }
}

export class UpdateVolumeAllocationSuccessAction implements Action {
  readonly type = UPDATE_VOLUME_HOST_ALLOCATION_SUCCESS;
  constructor(public payload) {
  }
}

export class DeleteVolumeAction implements Action {
  readonly type = DELETE_VOLUME_DETAILS;
  constructor(public payload: any) {
  }
}

export class DeleteVolumeDeleteSuccessAction implements Action {
  readonly type = DELETE_VOLUME_DETAILS_SUCCESS;
  constructor(public payload) {
  }
}

export class GetTotalSizeAction implements Action {
  readonly type = GET_TOTAL_SIZE;
  constructor(public payload: any) {
  }
}

export class GetTotalSizeSuccessAction implements Action {
  readonly type = GET_TOTAL_SIZE_SUCCESS;
  constructor(public payload) {
  }
}

export class VolumeReset implements Action {
  readonly type = VOL_RESET;
}

export type Actions
  = GetAllVolumesAction
  | GetAllVolumesSuccessAction
  | AddVolumeDetailsAction
  | AddVolumeDetailsSuccessAction
  | GetVolumeDetailsAction
  | GetVolumeDetailsSuccessAction
  | UpdateVolumeDetailsAction
  | UpdateVolumeDetailsSuccessAction
  | UpdateVolumeAllocationAction
  | UpdateVolumeAllocationSuccessAction
  | DeleteVolumeAction
  | DeleteVolumeDeleteSuccessAction
  | GetTotalSizeAction
  | GetTotalSizeSuccessAction
  | VolumeReset;

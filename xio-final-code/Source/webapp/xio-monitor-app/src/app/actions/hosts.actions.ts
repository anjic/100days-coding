/**
 * Created by Venkatesh on 7/31/2017.
 */
import { Action } from '@ngrx/store';

export const GET_ALL_HOSTS = "[Hosts] addHosts";
export const GET_ALL_HOSTS_SUCCESS = '[Hosts] addHosts success';
export const UPDATE_HOST = "[Hosts] updateHosts";
export const UPDATE_HOST_SUCCESS = '[Hosts] updateHosts success';
export const DELETE_HOST = "[Hosts] deleteHost";
export const DELETE_HOST_SUCCESS = '[Hosts] deleteHost success';
export const GET_HOST = "[Hosts] getHost";
export const GET_HOST_SUCCESS = '[Hosts] getHost success';
export const UPDATE_VOLUME_ALLOCATION = "[Hosts] updateVolumeAllocation";
export const UPDATE_VOLUME_ALLOCATION_SUCCESS = '[Hosts] updateVolumeAllocation success';
export const GET_HOST_VOLUME = "[Hosts] getHostVolume";
export const GET_HOST_VOLUME_SUCCESS = '[Hosts] getHostVolume success';
export const HOST_RESET = '[Volume] Reset';

export class GetAllHostsAction implements Action {
  readonly type = GET_ALL_HOSTS;
  constructor(public payload: any) {
  }
}

export class GetAllHostsActionSuccess implements Action {
  readonly type = GET_ALL_HOSTS_SUCCESS;
  constructor(public payload: any) {
  }
}

export class UpdateHostAction implements Action {
  readonly type = UPDATE_HOST;
  constructor(public payload: any) {
  }
}

export class UpdateHostActionSuccess implements Action {
  readonly type = UPDATE_HOST_SUCCESS;
  constructor(public payload: any) {
  }
}

export class DeleteHostAction implements Action {
  readonly type = DELETE_HOST;
  constructor(public payload: any) {
  }
}

export class DeleteHostActionSuccess implements Action {
  readonly type = DELETE_HOST_SUCCESS;
  constructor(public payload: any) {
  }
}

export class GetHostAction implements Action {
  readonly type = GET_HOST;
  constructor(public payload: any) {
  }
}

export class GetHostActionSuccess implements Action {
  readonly type = GET_HOST_SUCCESS;
  constructor(public payload: any) {
  }
}

export class UpdateVolumeAllocationAction implements Action {
  readonly type = UPDATE_VOLUME_ALLOCATION;
  constructor(public payload: any) {
  }
}

export class UpdateVolumeAllocationActionSuccess implements Action {
  readonly type = UPDATE_VOLUME_ALLOCATION_SUCCESS;
  constructor(public payload: any) {
  }
}

export class GetHostVolumeAction implements Action {
  readonly type = GET_HOST_VOLUME;
  constructor(public payload: any) {
  }
}

export class GetHostVolumeActionSuccess implements Action {
  readonly type = GET_HOST_VOLUME_SUCCESS;
  constructor(public payload: any) {
  }
}

export class HostReset implements Action {
  readonly type = HOST_RESET;
}

export type Actions = GetAllHostsAction
  | GetAllHostsActionSuccess
  | UpdateHostAction
  | UpdateHostActionSuccess
  | DeleteHostAction
  | DeleteHostActionSuccess
  | GetHostAction
  | GetHostActionSuccess
  | UpdateVolumeAllocationAction
  | UpdateVolumeAllocationActionSuccess
  | GetHostVolumeAction
  | GetHostVolumeActionSuccess
  | HostReset;



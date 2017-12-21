/**
 * Created by Venkatesh on 7/28/2017.
 */

import * as volume from '../actions/volume.actions';

export interface State {
  volume_list: Array<Object>,
  volume: Array<Object>,
  total_size: Object
}

export const initialState: State = {
  volume_list: [],
  volume: [],
  total_size: {}
};

export function reducer(state = initialState, action: volume.Actions): State {
  switch (action.type) {
    case volume.GET_ALL_VOLUMES_SUCCESS: {
      return {
        volume_list: Array.isArray(action.payload) ? action.payload : (typeof  action.payload == "object" ? [action.payload] : []),
        volume: state.volume,
        total_size: state.total_size
      }
    }

    case volume.GET_TOTAL_SIZE_SUCCESS: {
      return {
        volume_list: state.volume_list,
        volume: state.volume,
        total_size: action.payload
      }
    }

    case volume.GET_VOLUME_DETAILS_SUCCESS: {
      return {
        volume_list: state.volume_list,
        volume: action.payload,
        total_size: state.total_size
      }
    }

    case volume.ADD_VOLUME_DETAILS_SUCCESS: {
      return {
        volume_list: state.volume_list,
        volume: state.volume,
        total_size: state.total_size
      }
    }

    case volume.UPDATE_VOLUME_DETAILS_SUCCESS: {
      return {
        volume_list: state.volume_list,
        volume: state.volume,
        total_size: state.total_size
      }
    }

    case volume.DELETE_VOLUME_DETAILS_SUCCESS: {
      return {
        volume_list: state.volume_list,
        volume: state.volume,
        total_size: state.total_size
      }
    }

    case volume.UPDATE_VOLUME_HOST_ALLOCATION_SUCCESS: {
      return {
        volume_list: state.volume_list,
        volume: action.payload,
        total_size: state.total_size
      }
    }

    case volume.VOL_RESET: {
      return initialState;
    }

    default: {
      return state
    }
  }
}

export const getAllVolumesList = (state: State) => state.volume_list;
export const getVolume = (state: State) => state.volume;
export const totalSize = (state: State) => state.total_size;

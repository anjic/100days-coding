/**
 * Created by Venkatesh on 7/31/2017.
 */

import * as hosts from '../actions/hosts.actions';

export interface State{
  all_hosts:Array<Object>,
  host:Object
};

export const initialState: State = {
  all_hosts:[],
  host:{}
};

export function reducer(state = initialState, action:  hosts.Actions) : State {
  switch(action.type) {
    case hosts.GET_ALL_HOSTS_SUCCESS: {
      return {
        all_hosts:action.payload,
        host:state.host
      }
    }

    case hosts.GET_HOST_SUCCESS: {
      return {
        all_hosts:state.all_hosts,
        host:action.payload
      }
    }

    case hosts.UPDATE_HOST_SUCCESS: {
      return {
        all_hosts:state.all_hosts,
        host:state.host
      }
    }

    case hosts.DELETE_HOST_SUCCESS: {
      return {
        all_hosts:state.all_hosts,
        host:state.host
      }
    }

    case hosts.UPDATE_VOLUME_ALLOCATION_SUCCESS: {
      return {
        all_hosts:state.all_hosts,
        host:state.host
      }
    }

    case hosts.GET_HOST_VOLUME_SUCCESS: {
      return {
        all_hosts:state.all_hosts,
        host:state.host
      }
    }

    case hosts.HOST_RESET: {
      return initialState;
    }

    default:{
      return state;
    }
  }
}


export const getAllHosts = (state : State) => state.all_hosts;
export const getHost = (state : State) => state.host;

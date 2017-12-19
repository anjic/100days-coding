/**
 * Created by Dominic on 8/21/2017.
 */

import * as menu from '../actions/menu.action';

export interface State {
  menuContent: Array<object>;
  iseHostMap: object;
}

export const initialState: State = {
  menuContent: [],
  iseHostMap: {}
};

export function reducer(state = initialState, action: menu.Actions): State {
  switch (action.type) {
    case menu.GET_MENU_SUCCESS: {
      return {
        menuContent: action.payload,
        iseHostMap: state.iseHostMap
      }
    }

    case menu.GET_HOST_SUCCESS: {
      return {
        menuContent: state.menuContent,
        iseHostMap: (function() {
          state.iseHostMap[action.payload['ise_id']] = action.payload.data;
          return Object.assign({}, state.iseHostMap);
        })()
      }
    }

    default: {
      return state;
    }
  }
}

export const getMenuList = (state: State) => state.menuContent || [];
export const getHostList = (state: State) => state.iseHostMap || [];

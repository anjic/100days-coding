/**
 * Created by Dominic on 7/15/2017.
 */

import * as sanGroup from '../actions/sangroup.action';
import { SANGroup } from '../san-group/models/san-group';

export interface State {
  sanGroupLst: Array<SANGroup>;
  SanGroupDetails: Object;
  SanGroupISELinkMap: Array<Object>;
  SanGroupHostList: Array<Object>;
  SanGroupIseListInfo: Array<Object>;
};

export const initialState: State = {
  sanGroupLst: [{
    'sangroup_id': 0,
    'sangroup_name': '',
    'comment': '',
    'created_date': '',
    'updated_date': '',
    'created_by': '',
    'modified_by': '',
    'is_delete': false,
    'ise': [],
  }],
  SanGroupDetails: {},
  SanGroupISELinkMap: [],
  SanGroupHostList: [],
  SanGroupIseListInfo: []
};

export function reducer(state = initialState, action: sanGroup.Actions): State {
  switch (action.type) {

    case sanGroup.GET_ALL_SUCCESS: {
      return {
        sanGroupLst: action.payload,
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: state.SanGroupIseListInfo
      };
    }

    case sanGroup.ADD_SANGROUP_SUCCESS: {
      return {
        sanGroupLst: [...state.sanGroupLst, action.payload[0] || {}],
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: state.SanGroupIseListInfo
      };
    }

    case sanGroup.UPDATE_SANGROUP_SUCCESS: {
      return {
        sanGroupLst: [...state.sanGroupLst.map((sg) => {
          if (sg['sangroup_id'] === action.payload[0].sangroup_id) {
            return action.payload[0];
          } else {
            return sg;
          }
        })],
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: state.SanGroupIseListInfo
      };
    }

    case sanGroup.GET_ISELIST_SUCCESS: {
      return {
        sanGroupLst: state.sanGroupLst,
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: action.payload,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: state.SanGroupIseListInfo
      };
    }

    case sanGroup.GET_SANGROUP_HOST_SUCCESS: {
      return {
        sanGroupLst: state.sanGroupLst,
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: action.payload,
        SanGroupIseListInfo: state.SanGroupIseListInfo
      };
    }

    case sanGroup.DELETE_SANGROUP_SUCCESS: {
      return {
        sanGroupLst: action.payload,
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: state.SanGroupIseListInfo
      };
    }

    case sanGroup.GET_SANGROUP_SUCCESS: {
      return {
        sanGroupLst: state.sanGroupLst,
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: [...state.SanGroupIseListInfo, ...action.payload]
      };
    }

    case sanGroup.SAN_RESET: {
      return initialState;
    }

    case sanGroup.SAN_ISE_INFO_RESET: {
      return {
        sanGroupLst: state.sanGroupLst,
        SanGroupDetails: state.SanGroupDetails,
        SanGroupISELinkMap: state.SanGroupISELinkMap,
        SanGroupHostList: state.SanGroupHostList,
        SanGroupIseListInfo: []
      };
    }

    default: {
      return state;
    }
  }
}

export const getSanGroupLst = (state: State) => state.sanGroupLst || [];

export const getSanGroupISELstMap = (state: State) => state.SanGroupISELinkMap || [];

export const getSanGroupHostLst = (state: State) => state.SanGroupHostList || [];

export const getSanGroupISELstInfo = (state: State) => state.SanGroupIseListInfo || [];

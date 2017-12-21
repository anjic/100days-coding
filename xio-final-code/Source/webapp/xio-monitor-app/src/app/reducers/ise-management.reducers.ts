/**
 * Created by Dominic on 7/27/2017.
 */

import * as iseManagement from '../actions/ise-management.actions';
import { ISE } from '../ise/models/ise';
import { SANGroup } from '../san-group/models/san-group';

export interface State {
  iseLst: Array<ISE>;
  iseInfo: Object;
  iseID: string;
  iseCardInfo: Object;
  IOPsChartData: Array<Object>;
  LatencyChartData: Array<Object>;
  DataRateChartData: Array<Object>;
  qDepthChartData: Array<Object>;
  error: Object;
  iseLedBlinkStatus: boolean;
  iseDiscovery: Object;
  iseLocal: Object;
};

export const initialState: State = {
  iseLst: [{
    id: '',
    root_node_id: '',
    ise_name: '',
    serial_no: '',
    ip_primary: '',
    ip_secondary: '',
    mrc1_status: false,
    mrc2_status: false,
    username: '',
    password: '',
    time_stamp: '',
    status: '',
    initialize: '',
    contactphone: '',
    contactemail: '',
    contactname: '',
    location: '',
    address: '',
    prefered: false,
    sangroup: [{
      sangroup_id: 0,
      sangroup_name: '',
      comment: '',
      created_date: '',
      updated_date: '',
      created_by: '',
      modified_by: '',
      is_delete: false,
      ise: []
    }],
    controllers: {
      controllers: [
        {
          macaddress: '',
          fwversion: '',
          ipaddress: '',
        }
      ]
    },
    contact: {
      phone: '',
      email: '',
      location: '',
      name: '',
      address: '',
    },
    model: '',
  }],
  iseInfo: null,
  iseCardInfo: {
    status: {
      _attr: {
          string: '',
          value: '',
      },
      details: {
          _attr: {
              value: '',
          },
          detail: '',
      }
  },
  mrc2_status: '',
  eula: 'By enabling Encryption, you acknowledge that you are required to provide a\npassword in order to encrypt your data. You also acknowledge that you will\nnot be able to recover the encrypted information if you lose or forget the\npassword.',
  ipaddress1: '',
  name: '',
  ipaddress2: '',
  locked: false,
  serial_no: '',
  encrpytion_enabled: false,
  mrc2_fwversion: '',
  hosts: 0,
  volumes: 0,
  time: '',
  date: '',
  led: {
      _attr: {
          string: '',
          value: '',
      },
      led: '',
  },
  endpoints: 0,
  mrc1_status: '',
  pool: 0,
  mrc1_fwversion: '',

  },
  iseID: '',
  IOPsChartData: null,
  LatencyChartData: null,
  DataRateChartData: null,
  qDepthChartData: null,
  error: null,
  iseLedBlinkStatus: false,
  iseDiscovery: null,
  iseLocal: null,
};

export function reducer(state = initialState, action: iseManagement.Actions): State {
  switch (action.type) {

    case iseManagement.SET_ISE_ID: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: action.payload,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: state.error,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
      };
    }

    case iseManagement.GET_ALL_ISE_LIST_SUCCESS: {
      return {
        iseLst: action.payload,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: state.error,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_ISE_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: action.payload,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: state.error,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.ISE_ERROR: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_ISE_CARD_INFO_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: action.payload,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_IOPS_CHART_DATA_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: action.payload,
        LatencyChartData: state.LatencyChartData,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_LATENCY_CHART_DATA_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: action.payload,
        DataRateChartData: state.DataRateChartData,
        qDepthChartData: state.qDepthChartData,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_DataRate_CHART_DATA_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        qDepthChartData: state.qDepthChartData,
        DataRateChartData: action.payload,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_QDepth_CHART_DATA_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        qDepthChartData: action.payload,
        DataRateChartData: state.DataRateChartData,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_QDepth_CHART_DATA_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        qDepthChartData: action.payload,
        DataRateChartData: state.DataRateChartData,
        error: action.payload,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.SET_ISE_BLINK_STATUS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        qDepthChartData: state.qDepthChartData,
        DataRateChartData: state.DataRateChartData,
        error: state.error,
        iseLedBlinkStatus: action.payload,
        iseDiscovery: state.iseDiscovery,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_DISCOVERY_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        qDepthChartData: state.qDepthChartData,
        DataRateChartData: state.DataRateChartData,
        error: state.error,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: action.payload,
        iseLocal: state.iseLocal
        
      };
    }

    case iseManagement.GET_ISE_DETAIL_SUCCESS: {
      return {
        iseLst: state.iseLst,
        iseInfo: state.iseInfo,
        iseCardInfo: state.iseCardInfo,
        iseID: state.iseID,
        IOPsChartData: state.IOPsChartData,
        LatencyChartData: state.LatencyChartData,
        qDepthChartData: state.qDepthChartData,
        DataRateChartData: state.DataRateChartData,
        error: state.error,
        iseLedBlinkStatus: state.iseLedBlinkStatus,
        iseDiscovery: state.iseDiscovery,
        iseLocal: action.payload
        
      };
    }


    case iseManagement.ISE_STATE_RESET: {
      return initialState;
    }

    default: {
      return state;
    }
  }
}

export const getISELst = (state: State) => state.iseLst;
export const getISEID = (state: State) => state.iseID;
export const getISEInfo = (state: State) => state.iseInfo;
export const getCardInfo = (state: State) => state.iseCardInfo;
export const getIOPChartData = (state: State) => state.IOPsChartData;
export const getLantencyChartData = (state: State) => state.LatencyChartData;
export const getDataRateChartData = (state: State) => state.DataRateChartData;
export const getqDepthChartData = (state: State) => state.qDepthChartData;
export const getISEBlinkStatus = (state: State) => state.iseLedBlinkStatus;
export const getISEDiscovery = (state: State) => state.iseDiscovery;
export const getISEDetail = (state: State) => state.iseLocal;

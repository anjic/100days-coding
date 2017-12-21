/**
 * Created by Dominic on 7/19/2017.
 */


import * as settings from '../actions/ise-settings.actions';
import {snmp} from '../common/Metadata/ise.metadata';

export interface State {
  chronometer: Object;
  snmpLst: snmp,
  traps: {
    available: Array<Object>;
    selected: Array<Object>;
  },
  subscriptionLst: Array<Object>;
  ledStatus:Object;
  initialize:Object;
};

export const initialState = {
  chronometer: {
    'uptime': {
      'hours': 0,
      'seconds': 0,
      '_attr': {
          'duration': ''
      },
      'minutes': 0,
      'days': 0
  },
  'scale': '',
  'ntp': {
      'ntpmode': '',
      'ntpserver': '' 
  },
  'dst': '',
  '_attr': {
      'self': ''
  },
  'time': '',
  'date': '',
  'timezone': '',
  'timezonesetting': '',
  },
  snmpLst: {
    email_host: '',
    email_host_password: '',
    email_host_user: '',
    email_port: '',
    enable_authentication: '',
    from_mail: '',
    use_ssl_tl: ''
  },
  traps: {
    available: [],
    selected: []
  },
  subscriptionLst: [],
  ledStatus: {},
  initialize: {}
};

export function reducer(state = initialState, action: settings.Actions): State {
  switch (action.type) {
    case settings.GET_TIMEZONE_SUCCESS: {
      return {
        chronometer: action.payload,
        snmpLst: state.snmpLst,
        traps: state.traps,
        subscriptionLst: state.subscriptionLst,
        ledStatus:state.ledStatus,
        initialize:state.initialize
      }
    }

    case settings.GET_ISE_SUBSCRIPTION_SUCCESS: {
      return {
        chronometer: state.chronometer,
        snmpLst: state.snmpLst,
        traps: state.traps,
        subscriptionLst: action.payload,
        ledStatus:state.ledStatus,
        initialize:state.initialize
      }
    }

    case settings.GET_ALL_SNMP_SUCCESS: {
      return {
        chronometer: state.chronometer,
        snmpLst: state.snmpLst,
        traps: {
          available: Array.isArray(action.payload['available']) ? action.payload['available'] : (typeof  action.payload['available'] == "object" ? [action.payload['available']] : []),
          selected: Array.isArray(action.payload['selected']) ? action.payload['selected'] : (typeof  action.payload['selected'] == "object" ? [action.payload['selected']] : [])
        },
        subscriptionLst: state.subscriptionLst,
        ledStatus:state.ledStatus,
        initialize:state.initialize
      }
    }

    case settings.ISE_LED_UPDATE_SUCCESS : {
      return {
        chronometer: state.chronometer,
        snmpLst: state.snmpLst,
        traps: state.traps,
        subscriptionLst: state.subscriptionLst,
        ledStatus:action.payload,
        initialize:state.initialize
      }
    }

    case settings.ENABLE_ENCRYPTION_SUCCESS : {
      return {
        chronometer: state.chronometer,
        snmpLst: state.snmpLst,
        traps: state.traps,
        subscriptionLst: state.subscriptionLst,
        ledStatus:state.ledStatus,
        initialize:state.initialize
      }
    }

    case settings.ISE_STATUS_BUTTON_SUCCESS : {
      return {
        chronometer: state.chronometer,
        snmpLst: state.snmpLst,
        traps: state.traps,
        subscriptionLst: state.subscriptionLst,
        ledStatus:state.ledStatus,
        initialize:action.payload
      }
    }

    default: {
      return state;
    }
  }
}

export const getTraps = (state: State) => state.traps;
export const getChronometer = (state: State) => state.chronometer || [];
export const getSnmpLst = (state: State) => state.snmpLst || [];
export const getSubcriptionLst = (state: State) => state.subscriptionLst || [];
export const getLedStatus = (state: State) => state.ledStatus || [];
export const getIsebuttonstatus = (state: State) => state.initialize ;

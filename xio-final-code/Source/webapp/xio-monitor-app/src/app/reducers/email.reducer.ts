/**
 * Created by Dominic on 7/10/2017.
 */
import * as email from '../actions/email.actions';

export interface State {
  id: number;
  emailLst: Array<Object>;
  defaultAlertSevirity: Object;
}
;

export const initialState: State = {
  id: 0,
  emailLst: [],
  defaultAlertSevirity: {
    critical: false,
    severe: false,
    error: false,
    warning: false,
    informational: false,
    normal: false
  }
};


export function reducer(state = initialState, action: email.Actions): State {
  switch (action.type) {
    case email.GET_ALL_EMAIL: {
      return {
        id: action.payload,
        emailLst: state.emailLst,
        defaultAlertSevirity: state.defaultAlertSevirity
      };
    }
    case email.GET_ALL_EMAIL_SUCCESS: {
      return {
        id: state.id,
        emailLst: action.payload,
        defaultAlertSevirity: state.defaultAlertSevirity
      };
    }

    case email.ALERT_GET_DATA_SUCCESS: {
      return {
        id: state.id,
        emailLst: state.emailLst,
        defaultAlertSevirity: Object.assign({}, state.defaultAlertSevirity, action.payload)
      };
    }

    case email.ALERT_UPDATE_DATA_SUCCESS: {
      return {
        id: state.id,
        emailLst: state.emailLst,
        defaultAlertSevirity: Object.assign({}, state.defaultAlertSevirity, action.payload)
      };
    }

    case email.GET_TEST_EMAIL_SUCCESS: {
      return state;
    }

    default: {
      return state;
    }
  }
}

export const getEmailLst = (state: State) => state.emailLst || [];

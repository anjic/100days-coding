/**
 * Created by Dominic on 7/27/2017.
 */

import { Action } from '@ngrx/store';
import { ISE } from '../ise/models/ise';

export const SET_ISE_ID = '[ISE ID] set';

export const GET_ALL_ISE_LIST = '[ISE] getAll';
export const GET_ALL_ISE_LIST_SUCCESS = '[ISE] getAll success';

export const GET_ISE = '[ISE] getISE';
export const GET_ISE_SUCCESS = '[ISE] getISE success';

export const GET_ISE_DETAIL = '[ISE] getISEDetail';
export const GET_ISE_DETAIL_SUCCESS = '[ISE] getISEDetail success';

export const GET_DISCOVERY = '[ISE] getDiscovery';
export const GET_DISCOVERY_SUCCESS = '[ISE] getDiscovery success';

export const ADD_ISE = '[ISE] addISE';
export const ADD_ISE_SUCCESS = '[ISE] addISE success';

export const DELETE_ISE = '[ISE] deleteISE';
export const DELETE_ISE_SUCCESS = '[ISE] deleteISE success';

export const UPDATE_ISE = '[ISE] updateISE';
export const UPDATE_ISE_SUCCESS = '[ISE] updateISE success';

export const CHANGE_ISE_PWD = '[ISE PWD] change';
export const CHANGE_ISE_PWD_SUCCESS = '[ISE PWD] change success';

export const GET_ISE_SAN = '[ISE SAN] getMenuContent';
export const GET_ISE_SAN_SUCCESS = '[ISE SAN] getMenuContent success';

export const GET_ISE_SAN_LINK = '[ISE SAN] link';
export const GET_ISE_SAN_LINK_SUCCESS = '[ISE SAN] link success';

export const GET_ISE_CARD_INFO = '[ISE CARD] getInfo';
export const GET_ISE_CARD_INFO_SUCCESS = '[ISE CARD] getInfo success';

export const GET_IOPS_CHART_DATA = '[ISE CHART] getInfo';
export const GET_IOPS_CHART_DATA_SUCCESS = '[ISE CHART] getInfo success';

export const GET_LATENCY_CHART_DATA = '[ISE CHART] latency getInfo';
export const GET_LATENCY_CHART_DATA_SUCCESS = '[ISE CHART] latency getInfo success';

export const GET_DataRate_CHART_DATA = '[ISE CHART] datarate getInfo';
export const GET_DataRate_CHART_DATA_SUCCESS = '[ISE CHART] datarate getInfo success';

export const GET_QDepth_CHART_DATA = '[ISE CHART] qDepth getInfo';
export const GET_QDepth_CHART_DATA_SUCCESS = '[ISE CHART] qDepth getInfo success';

export const ISE_ERROR = '[ISE IseError]';
export const ISE_STATE_RESET = '[ISE reset]';

export const SET_ISE_BLINK_STATUS = '[ISE Blink] blink status';

export const CHANGE_ISE_IP = '[ISE IP] change';
export const CHANGE_ISE_IP_SUCCESS = '[ISE IP] change success';

export class SetISEId implements Action {
  readonly type = SET_ISE_ID;

  constructor(public payload) {
  }
}

export class GetAllISEList implements Action {
  readonly type = GET_ALL_ISE_LIST;

  constructor(public payload: Object = {}) {
  }
}
export class GetAllISEListSuccess implements Action {
  readonly type = GET_ALL_ISE_LIST_SUCCESS;

  constructor(public payload: Array<ISE>) {
  }
}

export class GetISEInfo implements Action {
  readonly type = GET_ISE;

  constructor(public payload) {
  }
}
export class GetISEInfoSuccess implements Action {
  readonly type = GET_ISE_SUCCESS;

  constructor(public payload) {
  }
}



export class GetIseDetail implements Action {
  readonly type = GET_ISE_DETAIL;

  constructor(public payload) {
  }
}
export class GetIseDetailSuccess implements Action {
  readonly type = GET_ISE_DETAIL_SUCCESS;

  constructor(public payload) {
  }
}


export class GetDiscovery implements Action {
  readonly type = GET_DISCOVERY;

  constructor(public payload) {
  }
}
export class GetDiscoverySuccess implements Action {
  readonly type = GET_DISCOVERY_SUCCESS;

  constructor(public payload) {
  }
}

export class AddISE implements Action {
  readonly type = ADD_ISE;

  constructor(public payload) {
  }
}
export class AddISESuccess implements Action {
  readonly type = ADD_ISE_SUCCESS;

  constructor(public payload) {
  }
}

export class DeleteISE implements Action {
  readonly type = DELETE_ISE;

  constructor(public payload) {
  }
}
export class DeleteISESuccess implements Action {
  readonly type = DELETE_ISE_SUCCESS;

  constructor(public payload) {
  }
}

export class UpdateISE implements Action {
  readonly type = UPDATE_ISE;

  constructor(public payload) {
  }
}
export class UpdateISESuccess implements Action {
  readonly type = UPDATE_ISE_SUCCESS;

  constructor(public payload) {
  }
}

export class ChangeISEPWD implements Action {
  readonly type = CHANGE_ISE_PWD;

  constructor(public payload) {
  }
}
export class ChangeISEPWDSuccess implements Action {
  readonly type = CHANGE_ISE_PWD_SUCCESS;

  constructor(public payload) {
  }
}

export class GetISESanGroup implements Action {
  readonly type = GET_ISE_SAN;

  constructor(public payload) {
  }
}
export class GetISESanGroupSuccess implements Action {
  readonly type = GET_ISE_SAN_SUCCESS;

  constructor(public payload) {
  }
}

export class ChangeISELink implements Action {
  readonly type = GET_ISE_SAN_LINK;

  constructor(public payload) {
  }
}
export class ChangeISELinkSuccess implements Action {
  readonly type = GET_ISE_SAN_LINK_SUCCESS;

  constructor(public payload) {
  }
}

export class GetISECardInfo implements Action {
  readonly type = GET_ISE_CARD_INFO;

  constructor(public payload) {
  }
}
export class GetISECardInfoSuccess implements Action {
  readonly type = GET_ISE_CARD_INFO_SUCCESS;

  constructor(public payload) {
  }
}

export class GetIOPSChartData implements Action {
  readonly type = GET_IOPS_CHART_DATA;

  constructor(public payload) {
  }
}
export class GetIOPSChartDataSuccess implements Action {
  readonly type = GET_IOPS_CHART_DATA_SUCCESS;

  constructor(public payload) {
  }
}

export class GetLatencyChartData implements Action {
  readonly type = GET_LATENCY_CHART_DATA;

  constructor(public payload) {
  }
}
export class GetLatencyChartDataSuccess implements Action {
  readonly type = GET_LATENCY_CHART_DATA_SUCCESS;

  constructor(public payload) {
  }
}

export class GetDataRateChartData implements Action {
  readonly type = GET_DataRate_CHART_DATA;

  constructor(public payload) {
  }
}
export class GetDataRateChartDataSuccess implements Action {
  readonly type = GET_DataRate_CHART_DATA_SUCCESS;

  constructor(public payload) {
  }
}

export class GetQDepthChartData implements Action {
  readonly type = GET_QDepth_CHART_DATA;

  constructor(public payload) {
  }
}
export class GetQDepthChartDataSuccess implements Action {
  readonly type = GET_QDepth_CHART_DATA_SUCCESS;

  constructor(public payload) {
  }
}

export class IseError implements Action {
  readonly type = ISE_ERROR;

  constructor(public payload) {
  }
}

export class Reset implements Action {
  readonly type = ISE_STATE_RESET;

  constructor() {
  }
}

export class SetISELEDBlinkStatus implements Action {
  readonly type = SET_ISE_BLINK_STATUS;

  constructor(public payload) {
  }
}

export class ChangeISEIP implements Action {
  readonly type = CHANGE_ISE_IP;

  constructor(public payload) {
  }
}
export class ChangeISEIPSuccess implements Action {
  readonly type = CHANGE_ISE_IP_SUCCESS;

  constructor(public payload) {
  }
}


/**
 * Export a type alias of all actions in this action group
 * so that reducers can easily compose action types
 */
export type Actions
  = SetISEId
  | GetAllISEList
  | GetAllISEListSuccess
  | GetISEInfo
  | GetISEInfoSuccess
  | GetIseDetail
  | GetIseDetailSuccess
  | GetDiscovery
  | GetDiscoverySuccess
  | AddISE
  | AddISESuccess
  | DeleteISE
  | DeleteISESuccess
  | UpdateISE
  | UpdateISESuccess
  | ChangeISEPWD
  | ChangeISEPWDSuccess
  | GetISESanGroup
  | GetISESanGroupSuccess
  | ChangeISELink
  | ChangeISELinkSuccess
  | GetISECardInfo
  | GetISECardInfoSuccess
  | GetIOPSChartData
  | GetIOPSChartDataSuccess
  | GetLatencyChartData
  | GetLatencyChartDataSuccess
  | GetDataRateChartData
  | GetDataRateChartDataSuccess
  | GetQDepthChartData
  | GetQDepthChartDataSuccess
  | IseError
  | Reset
  | SetISELEDBlinkStatus
  | ChangeISEIP
  | ChangeISEIPSuccess;

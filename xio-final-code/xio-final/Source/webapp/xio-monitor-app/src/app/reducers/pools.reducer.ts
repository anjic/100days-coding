/**
 * Created by Venkatesh on 7/28/2017.
 */

import * as pools from '../actions/pools.actions';
import { Pools } from '../ise/models/pools';
import { Drives } from '../ise/models/drives';

export interface State {
  pools_list: Array<Pools>;
  drives_list: Array<Drives>;
  drives_performance_list: Array<Object>;
  medium_list: Array<Object>;
  ratio: number;
  error: any;
}

export const initialState: State = {
  pools_list: [{
      status: {
              _attr: {
                string: '',
                value: 0
              },
              details: {
                _attr: {
                   value: '',
                },
              detail: '',
          }
      },
      available: {
        _attr: {
          total: '',
        },
      byredundancy: {
        'raid-1': 0,
        'raid-0': 0,
        'raid-5': 0
      }
  },
  used: {
    _attr: {
      total: '',
    },
    byredundancy: {
      'raid-1': 0,
      'raid-0': 0,
      'raid-5': 0
    }
  },
  name: '',
  globalid: '',
  provisioned: {
    _attr: {
      total: ''
    },
    byredundancy: {
      'raid-1': 0,
      'raid-0': 0,
      'raid-5': 0
    }
  },
  SlowSheettotal: 0,
  media: {
    medium: {
      tier: {
        tier: '',
        _attr: {
          string: '',
          value: 0
        }
      },
      _attr: {
        self: '',
      },
      health: 0
    },
    _attr: {
      self: '',
    }
  },
  _attr: {
    self: ''
  },
  Flashavailable: {
    _attr: {
      total: ''
    },
    byredundancy: {
      'raid-1': 0,
      'raid-0': 0,
      'raid-5': 0
    }
  },
  FastSheettotal: 0,
  Flashcapacity: 0,
  FastSheetallocated: 0,
  Flashused: {
    _attr: {
      total: '',
    },
    byredundancy: {
      'raid-1': 0,
      'raid-0': 0,
      'raid-5': 0
    }
  },
  volumes: {
    _attr: {
      self: '',
    },
    volumes: [
      {
        _attr: {
          self: '',
        },
        globalid: '',
      }

    ]
  },
  ThinThreshold: 0,
  SlowSheetallocated: 0,
  Flashprovisioned: {
    _attr: {
      total: '',
    },
    byredundancy: {
      'raid-1': 0,
      'raid-0': 0,
      'raid-5': 0
    }
  },
  id: 0,
  Flashquota: 0,
  size: 0,

  }],
  drives_list: [{
     status: {
      _attr: {
        string: '',
      },
      details: {
        _attr: {
          value: '',
        },
        detail: '',
        details: [{}],
      }
    },
    medium: {
      medium: '',
      _attr: {
        self: '',
      }
    },
    capacity: 0,
    temperature: {
      scale: '',
      _attr: {
        value: '',
      }
    },
    reducedcapacity: 0,
    serialnumber: '',
    fwversion: '',
    voltage: {},
    _attr: {},
    position: 0,
    wwn: '',
    servoversion: '',
    pool: {},
    productid: '',
  }
  ],
  drives_performance_list: [],
  medium_list: [],
  ratio: 0,
  error: {},

};


export function reducer(state = initialState, action: pools.Actions): State {
  switch (action.type) {
    case pools.GET_ALL_POOLS_SUCCESS: {
      return {
        pools_list: action.payload,
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: state.ratio,
        error: state.error
      }
    }

    case pools.GET_DRIVES_SUCCESS: {
      return {
        pools_list: state.pools_list,
        drives_list: action.payload,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: state.ratio,
        error: state.error
      }
    }


    case pools.GET_MEDIUM_SUCCESS: {
      return {
        pools_list: state.pools_list,
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: action.payload,
        ratio: state.ratio,
        error: state.error
      }
    }

    case pools.CREATE_POOL_SUCCESS: {
      return {
        pools_list: state.pools_list,
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: state.ratio,
        error: state.error
      }
    }

    case pools.EXPAND_POOL_SUCCESS: {
      return {
        pools_list: state.pools_list,
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: state.ratio,
        error: state.error
      }
    }

    case pools.DELETE_POOL_SUCCESS: {
      return {
        pools_list: state.pools_list.filter((ps) => {
          if (ps['globalid'] != action.payload['deleted_pool']) {
            return ps;
          }
        }),
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: state.ratio,
        error: state.error
      }
    }

    case pools.GET_RATIO_SUCCESS: {
      return {
        pools_list: state.pools_list,
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: action.payload,
        error: state.error
      }
    }

    case pools.ISE_STATE_RESET: {
      return initialState;
    }

    case pools.ISE_ERROR: {
      return {
        pools_list: state.pools_list,
        drives_list: state.drives_list,
        drives_performance_list: state.drives_performance_list,
        medium_list: state.medium_list,
        ratio: state.ratio,
        error: action.payload
      }
    }


    default: {
      return state;
    }
  }
}

export const getAllPoolsList = (state: State) => state.pools_list;
export const getDrivesList = (state: State) => state.drives_list;
export const getDrivesPerformaceList = (state: State) => state.drives_performance_list;
export const getMediumList = (state: State) => state.medium_list;
export const getRatio = (state: State) => state.ratio;


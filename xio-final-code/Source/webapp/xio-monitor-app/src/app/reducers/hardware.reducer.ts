/**
 * Created by Venkatesh on 7/19/2017.
 */
import * as hardware from '../actions/hardware.actions';
import { Datapac } from '../ise/models/datapac';
import { Powersupply } from '../ise/models/powersupply';
import { Network } from '../ise//models/network';
import { Controller } from '../ise/models/controllers';


export interface State {
  controllers_list: Array<Controller>,
  DNS_list: Array<Network>,
  PowerSupply_list: Array<Powersupply>,
  DataPac_list: Array<Datapac>,
  Fans_list: Array<any>
};

export const initialState: State = {
  controllers_list: [{
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
      },
    },

    model: '',
    serialnumber: '',
    led: {
      _attr: {
        string: '',
        value: '',
      },
      led: '',
    },

    temperature: {
      low: 0,
      scale: '',
      warning: 0,
      critical: 0,
      _attr: {
        value: '',
      },
    },

    fcports: {
      fcports: [
        {
          status: {
            status: '',
            _attr: {
              string: '',
              value: '',
            },
          },
          bytesreceived: 0,
          lipcount: 0,
          speedsetting: 0,
          type: {
            _attr: {
              string: '',
              value: '',
            },
            type: '',
          },
          _attr: {
            self: '',
          },
          noscount: 0,
          bytestransmitted: 0,
          wwn: '',
          speed: 0,
          id: 0,
          editFlag : false
        }
      ],
      _attr: {
        self: '',
      },
    },

    _attr: {
      self: '',
    },

    rank: {
      _attr: {
        string: '',
        value: '',
      },
      rank: '',
    },

    taskstatus: {
      progress: 0,
      _attr: {
        string: '',
        value: '',
      },
      type: '',
    },

    sfps: {
      sfps: [
        {
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
            },
          },
          serialnumber: '',
          hectxfault: '',
          _attr: {
            self: '',
          },
          numlosevents: 0,
          hecportsignalloss: '',
          manufacturingdate: '',
          partnumber: '',
          hwversion: '',
          id: 0,
          numtxfltevents: 0,
        }
      ],

      _attr: {
        self: '',
      },
    },

    fwversion: '',
    manufacturingdate: '',
    position: 0,
    partnumber: '',
    hwversion: '',
    id: 0,
  }],

  DNS_list: [{
    dhcp: {
      dhcp: '',
      _attr: {
        string: '',
        value: '',
      },
    },
    _attr: {
      self: '',
    },
    wakeonlan: {
      _attr: {
        string: '',
        value: '',
      },
      wakeonlan: '',
    },
    dns: {
      nameservers: [''],
      domainserver: '',
    },
    ports: {
      _attr: {
        self: '',
      },
      ports: [
        {
          macaddress: '',
          linkstatus: '',
          _attr: {
            self: '',
          },
          dnsname: '',
          ipmask: '',
          ipaddress: '',
          gateway: '',
        }
      ],
      port: {
        macaddress: '',
        linkstatus: '',
        _attr: {
          self: '',
        },
        dnsname: '',
        ipmask: '',
        ipaddress: '',
        gateway: '',
      },
    }
  }],

  PowerSupply_list: [{

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
      },
    },
    model: '',
    serialnumber: '',
    led: {
      _attr: {
        string: '',
        value: '',
      },
      led: '',
    },
    temperature: {
      low: 0,
      scale: '',
      warning: 0,
      critical: 0,
      _attr: {
        value: '',
      },
    },
    _attr: {
      self: '',
    },
    fans: '',
    manufacturingdate: '',
    position: 0,
    partnumber: '',
    hwversion: '',
    id: 0,
  }],

  DataPac_list: [{

    status: {
      _attr: {
        string: '',
        value: ''
      },
      details: {
        _attr: {
          value: ''
        },
        detail: ''
      }
    },
    model: '',
    serialnumber: '',
    led: {
      _attr: {
        string: '',
        value: ''
      },
      led: ''
    },
    temperature: {
      low: 0,
      scale: '',
      warning: 0,
      critical: 0,
      _attr: {
        peak: '',
        value: ''
      }
    },
    capacity: 0,
    _attr: {
      self: ''
    },
    taskstatus: {
      progress: 0,
      _attr: {
        string: '',
        value: ''
      },
      type: ''
    },
    fwversion: '',
    manufacturingdate: '',
    health: {
      warning: 0,
      critical: 0,
      _attr: {
        value: ''
      }
    },
    tier: {
      tier: '',
      _attr: {
        string: '',
        value: ''
      }
    },
    position: 0,
    partnumber: '',
    sparelevel: 0,
    hwversion: '',
    id: 0,
    pool: {
      _attr: {
        self: ''
      },
      globalid: ''
    },
    redundancyhealth: {
      healthstring: '',
      _attr: {
        value: ''
      },
      inselfhealing: ''
    }
  }],

  Fans_list: []

}

export function reducer(state = initialState, action: hardware.Actions): State {
  switch (action.type) {

    case hardware.GET_CONTROLLERS_SUCCESS: {
      return {
        controllers_list: action.payload,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.UPDATE_DATA_PAC_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.UPDATE_MRC_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.UPDATE_SPEED_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.GET_NETWORK_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: action.payload,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.UPDATE_NETWORK_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.GET_POWER_SUPPLY_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: action.payload,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.GET_DATA_PAC_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: action.payload,
        Fans_list: state.Fans_list
      }
    }

    case hardware.UPDATE_POWER_SUPPLY_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    case hardware.GET_FANS_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: action.payload
      }
    }

    case hardware.UPDATE_FANS_SUCCESS: {
      return {
        controllers_list: state.controllers_list,
        DNS_list: state.DNS_list,
        PowerSupply_list: state.PowerSupply_list,
        DataPac_list: state.DataPac_list,
        Fans_list: state.Fans_list
      }
    }

    default: {
      return state;
    }

  }
}

export const getControllerList = (state: State) => state.controllers_list || [];
export const getNetworkList = (state: State) => state.DNS_list || [];
export const getPowerSupplyList = (state: State) => state.PowerSupply_list || [];
export const getDataPacList = (state: State) => state.DataPac_list || [];
export const getFansList = (state: State) => state.Fans_list || [];

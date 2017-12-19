export interface ISECardInfo {

    status: {
      _attr: {
        string: string;
        value: string;
      };
      details: {
        _attr: {
          value: string;
        };
        detail: string;
      }
    };
    mrc2_status: string;
    eula: string;
    ipaddress1: string;
    name: string;
    ipaddress2: string;
    locked: boolean;
    serial_no: string;
    encrpytion_enabled: boolean;
    mrc2_fwversion: string;
    hosts: number;
    volumes: number;
    time: string;
    date: string;
    led: {
      _attr: {
        string: string;
        value: string;
      };
      led: string;
    };
    endpoints: number;
    mrc1_status: string;
    pool: number;
    mrc1_fwversion: string;

}


export interface Drives {
    status: {
      _attr: {
        string: string;
      };
      details: {
        _attr: {
          value: string;
        },
        detail: string;
        details: [{}];
      }
    };
    medium: {
      medium: string;
      _attr: {
        self: string;
      }
    };
    capacity: number;
    temperature: {
      scale: string;
      _attr: {
        value: string;
      }
    };
    reducedcapacity: number;
    serialnumber: string;
    fwversion: string;
    voltage: {};
    _attr: {};
    position: number;
    wwn: string;
    servoversion: string;
    pool: {};
    productid: string;
}

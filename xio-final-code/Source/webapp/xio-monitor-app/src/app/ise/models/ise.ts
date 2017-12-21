import { SANGroup } from '../../san-group/models/san-group';

export interface ISE {
  id: string;
  root_node_id: string;
  ise_name: string;
  serial_no: string;
  ip_primary: string;
  ip_secondary: string;
  mrc1_status: boolean;
  mrc2_status: boolean;
  username: string;
  password: string;
  time_stamp: string;
  status: string;
  initialize: string;
  contactphone: string;
  contactemail: string;
  contactname: string;
  location: string;
  address: string;
  prefered: boolean;
  sangroup: SANGroup[];
  controllers: {
    controllers: [
      {
        macaddress: string;
        fwversion: string;
        ipaddress: string;
      }
    ]
  },
  contact: {
    phone: string;
    email: string;
    location: string;
    name: string;
    address: string;
  },
  model: string;
}

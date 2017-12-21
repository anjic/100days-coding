/**
 * Created by Dominic on 7/24/2017.
 */

export interface snmp {
  email_host: string;
  email_host_password: string;
  email_host_user: string;
  email_port: string;
  enable_authentication: string;
  from_mail: string;
  use_ssl_tl: string;
};

export interface snmpReqPayload {
  ise_id: number;
  snmp_data?: Object;
  cb?: Function
}

export interface ISEUpdateReqPayload {
  ise_id: number;
  setting_data?: Object;
  cb?: Function
}

export interface mibFileDownload {
  ise_id: number;
  cb?: Function
}


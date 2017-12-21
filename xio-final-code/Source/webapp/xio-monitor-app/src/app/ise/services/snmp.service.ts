import {Injectable} from '@angular/core';
import {Http, Response, Headers} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from './../../app-setting';
import {log} from '../../common/utils/logger';
import {XhrService} from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class SnmpService extends XhrService {
  public actionUrl: string;
  public headers: Headers;
  public snmp_list: Array<Object>;
  public ise_id;

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'ise/';
  }

  // getsnmp_list(ise_id: any) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/snmp/';
  //   return this.getMenuContent(url)
  //     .map((res: Response) => {
  //       return res.json().response.data.snmp;
  //     })
  //     .catch((IseError: any) => Observable.throw(IseError || 'Server IseError'));
  // }

  // getAll(ise_id: any) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/snmp/';
  //   return this.getMenuContent(url)
  //     .map((res: Response) => {
  //       this.snmp_list = res.json().response.data.snmp.traps;
  //       // console.log(this.snmp_list);
  //     })
  //     .catch((IseError: any) => Observable.throw(IseError.json().IseError || 'Server IseError'));
  // }

  // updatesnmp(ise_id: number, snmp_data: any) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/snmp-update/';
  //   return this.put(url, snmp_data)
  //     .map((res: Response) => res.json());
  // }

  // addClient(ise_id: number, snmp_data: any) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/snmp-client/';
  //   return this.post(url, snmp_data)
  //     .map((res: Response) => res.json());
  // }
  //
  // deleteClient(ise_id: any, snmp_data: any) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/snmp-delete/';
  //   return this.post(url, snmp_data)
  //     .map((res: Response) => res.json())
  //     .catch((IseError: any) => Observable.throw(IseError));
  //   //Observable.throw(IseError.json().IseError || 'Server IseError')
  // }

  // downloadfile(ise_id: number) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/files/mib';
  //   return this.getMenuContent(url)
  //     .map((res: Response) => {
  //       let data = res.json().result.response.data;
  //       return data;
  //     })
  //     .catch((IseError: any) => Observable.throw(IseError.json().IseError || 'Server IseError'));
  // }
}

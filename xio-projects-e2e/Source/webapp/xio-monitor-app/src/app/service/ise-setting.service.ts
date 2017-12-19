import {Injectable} from '@angular/core';
import {Http, Response, Headers} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from '../app-setting';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';


@Injectable()
export class IseSettingService {
  public actionUrl: string;
  public headers: Headers;
  public data: any;
  public ise_id;


  constructor(public _http: Http) {
    this.actionUrl = AppSettings.API_ENDPOINT + 'ise/';
    this.headers = new Headers();
    this.headers.set('content-type', 'application/json');
    this.headers.set('Accept', 'application/json');
  }

  /**
   * getMenuContent all snmp data
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method getAll
   * @return {void}
   */
  getAll(ise_id: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/snmp/';
    return this._http.get(url)
      .map((res: Response) => {
        return res.json().result.response.data.snmp.traps;
      })
      .catch((error: any) => Observable.throw(error|| 'Server error'));
  }

  /**
   * getMenuContent all snmp Subscription data list
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method getAllSubscription
   * @return {void}
   */
  getAllSubscription(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/subscriptions/';
    return this._http.get(url)
      .map((res: Response) => {
        let data = res.json().result.response.data.subscriptions;
        return (data && data.hasOwnProperty('subscription') ? [data.subscription] : data.subscriptions);
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }

  /**
   * getMenuContent advance settings data
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method doSetting
   * @return {void}
   */
  doSetting(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/advance-settings/';
    return Observable.forkJoin(
      this._http.put(url, payload['setting_data'], this.headers)
        .map((res: Response) => res.json())
    );
  }

  /**
   * getMenuContent chronometer TimeZone
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method getTimeZone
   * @return {void}
   */
  getTimeZone(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/chronometer/';
    return this._http.get(url)
      .map((res: Response) => {
        return res.json().result.response.data.chronometer;
      })
  }

  /**
   * update time zone
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method updateTimezone
   * @return {void}
   */
  updateTimezone(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/chronometer/';
    return Observable.forkJoin(
      this._http.put(url, payload['data'], this.headers)
        .map((res: Response) => res.json())
    );
  }

  /**
   * getMenuContent SNMP list of corresponding ISE
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method getsnmp_list
   * @return {void}
   */
  getsnmp_list(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/snmp/';
    return this._http.get(url)
      .map((res: Response) => {
        return res.json().result.response.data.snmp;
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }

  /**
   * update SNMP
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @param {object} snmp_data
   * @method updatesnmp
   * @return {void}
   */
  updatesnmp(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/snmp-update/';
    return this._http.put(url, payload['snmp_data'])
      .map((res: Response) => res.json());
  }

  /**
   * add SNMP client
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @param {object} snmp_data
   * @method addClient
   * @return {void}
   */
  addClient(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id']+ '/snmp-client/';
    return this._http.post(url, payload['snmp_data'])
      .map((res: Response) => res.json());
  }

  /**
   * delete SNMP client
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @param {object} snmp_data
   * @method addClient
   * @return {void}
   */
  deleteClient(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id']+ '/snmp-delete/';
    return this._http.post(url, payload['snmp_data'])
      .map((res: Response) => res.json())
      .catch((error: any) => Observable.throw(error));
  }

  /**
   * delete SNMP client
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @param {object} snmp_data
   * @method addClient
   * @return {void}
   */
  downloadfile(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/files/mib';
    return this._http.get(url)
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server error'));
  }
  /**
   * add subscription
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @param {object} data
   * @method addSubscription
   * @return {void}
   */
  addSubscription(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/subscriptions/';
    return this._http.post(url, payload['data'])
      .map((res: Response) => res.json());
  }

  /**
   * update subscription
   * @namespace xio.IseSettingService
   * @param {number} id
   * @param {number} ise_id
   * @param {number} data
   * @method addSubscription
   * @return {void}
   */
  updateSubscription(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id']+ '/subscriptions/' + payload['id']+ '/';
    return this._http.put(url, payload['data'])
      .map((res: Response) => res.json());

  }

  /**
   * update subscription
   * @namespace xio.IseSettingService
   * @param {number} id
   * @param {number} ise_id
   * @method addSubscription
   * @return {void}
   */
  deleteSubscription(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id']+ '/subscriptions/' + payload['id']+ '/';
    return this._http.delete(url)
      .map((res: Response) => res.json())
      .catch((error: any) => Observable.throw(error));
  }
}

import {Injectable} from '@angular/core';
import {Http, Response, Headers} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from '../../app-setting';
import {log} from '../../common/utils/logger';
import {XhrService} from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';


@Injectable()
export class IseSettingService extends XhrService {
  public actionUrl: string;
  public data: any;
  public ise_id;
  public subscription_list: any;


  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'ise/';
  }

  /**
   * getMenuContent all snmp data
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method getAll
   * @return {void}
   */
  getAll(payload : any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/snmp/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data.snmp.traps;
      })
      .catch((error: any) => Observable.throw(error|| 'Server IseError'));
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
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.subscriptions;
         this.subscription_list = [];

            if(data && data.hasOwnProperty('subscriptions')){
              this.subscription_list = data.subscriptions;
            }

            if(data && data.hasOwnProperty('subscription')){
             
              this.subscription_list = [data.subscription];
            }

          return this.subscription_list
        // return (data.hasOwnProperty('subscription') ? [data.subscription] : data.subscriptions);
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
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
      this.put(url, payload['setting_data'])
        .map((res: Response) => log(res.json(), null, url))
    );
  }

  isebuttonstatus(payload : any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/initialize/';
    return this.get(url)
      .map((res: Response) => {

        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error|| 'Server IseError'));
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
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data.chronometer;
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
      this.put(url, payload['data'])
        .map((res: Response) => log(res.json(), null, url))
    );
  }

  /**
   * getMenuContent SNMP list of corresponding ISE
   * @namespace xio.IseSettingService
   * @param {number} ise_id
   * @method getsnmp_list
   * @return {void}
   */
  getsnmp_list(payload : any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/snmp/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data.snmp;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
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
    return this.put(url, payload['snmp_data'])
      .map((res: Response) => log(res.json(), null, url));
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
    return this.post(url, payload['snmp_data'])
      .map((res: Response) => log(res.json(), null, url));
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
    return this.post(url, payload['snmp_data'])
      .map((res: Response) => log(res.json(), null, url))
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
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
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
    return this.post(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url));
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
    return this.put(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url));

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
    return this.delete(url)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }

  /**
   *
   * @param payload
   * @returns {any}
   */
  updateLed(payload){
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/led/';
    return Observable.forkJoin(
      this.put(url, payload['data'])
        .map((res: Response) => log(res.json(), null, url))
    );
  }

  /**
   *
   * @param payload
   * @returns {Observable<R>}
   */
  enableEncryption(payload){
    console.log("EnableEncryption..:",payload);
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id']+ '/encryption/';
    return this.put(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url));
  }
}

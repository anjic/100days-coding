import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppSettings } from '../../app-setting';
import { log } from '../../common/utils/logger';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/Rx';

@Injectable()
export class IseService extends XhrService {

  public ise_sangroup_list;
  public ise_list;
  public ise_details;
  public ise_dashboard_details;
  public ise_card_details;
  public free_space_card;
  public ise_storage_details;
  public actionUrl;
  public data;
  public current_ise_id;


   /**
   * 
   * @param {Http} _http
   */

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'ise/';
    this.ise_details = {
      ise_name: '',
      ip_primary: '',
      ip_secondary: '',
      serial_no: ''
    };
  }

  /**
  * Desc :set current Ise Id
  * @namespace xio.IseService
  * @method setCurrentISEId
  */
  setCurrentISEId(id) {
    this.current_ise_id = id;
  }
  /**
     * Desc :Get current Ise Id
     * @namespace xio.IseService
     * @method getCurrentISEId
     */
  getCurrentISEId() {
    return this.current_ise_id;
  }

  /**
  * Desc :get discovery data of ISE
  * Method type : Post
  * URL : api/discovery/ 
  * @namespace xio.IseService
  * @method getDiscovery
  * @return {Observable} http
  */

  getDiscovery(payload) {
    let url = AppSettings.API_ENDPOINT + 'discovery/';
    return this.post(url, payload.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }
  /**
   * Desc :get data of All ISE
   * Method type : Get
   * URL : api/ise-list/ 
   * @namespace xio.IseService
   * @method getAll
   * @return {Observable} http
   */

  getAll() {
    let url = AppSettings.API_ENDPOINT + 'ise-list/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }
  /**
   * Desc :get data of ISE
   * Method type : Get
   * URL : api/ise-details/ise_id/ 
   * @namespace xio.IseService
   * @method getISE
   * @return {Observable} http
   */

  getISE(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise-details/' + payLoad.ise_id + '/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * Desc :Adding Ise 
   * Method type : Post
   * URL : api/ise-list/
   * @namespace xio.IseService
   * @method addIse
   * @return {Observable} http
   */


  addIse(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise-list/';
    return this.post(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }


  /**
 * Desc : delete Ise
 * Method type : delete
 * URL : api/ise/ise_id/management/
 * @namespace xio.IseService
 * @method deleteISE
 * @return {Observable} http
 */

  deleteISE(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/management/';
    return this.delete(url)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }

  /**
 * Desc : Updating Ise
 * Method type : put
 * URL : api/ise/ise_id/management/
 * @namespace xio.IseService
 * @method updateISE
 * @return {Observable} http
 */
  updateISE(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload.data.id + '/management/';
    return this.put(url, payload.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }

  /**
 * Desc : Change Ise Password
 * Method type : put
 * URL : api/ise/ise_id/management/
 * @namespace xio.IseService
 * @method changeISEPassword
 * @return {Observable} http
 */
  changeISEPassword(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload.data.id + '/management/';
    return this.put(url, payload.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }
  /**
  * Desc : getting sangroup details which is mapped with ISE
  * Method type : get
  * URL : api/ise/ise_id/sangroup_map/
  * @namespace xio.IseService
  * @method getISESangroup
  * @return {Observable} http
  */
  getISESangroup(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/sangroup_map/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }
  /**
  * Desc : updating sangroup details which is mapped with ISE
  * Method type : put
  * URL : api/ise/ise_id/sangroup_map/
  * @namespace xio.IseService
  * @method updateISESangroupLink
  * @return {Observable} http
  */
  updateISESangroupLink(payload) {
    let added = [],
      ise_sangroup_data = payload['ise_sangroup_data'];
    for (let i in ise_sangroup_data.available_sg) {
      if (ise_sangroup_data.available_sg[i].sg) {
        added.push(ise_sangroup_data.available_sg[i].sangroup_id);
      }
    }

    let removed = [];
    for (let i in ise_sangroup_data.current_sg) {
      if (!ise_sangroup_data.current_sg[i].sg) {
        removed.push(ise_sangroup_data.current_sg[i].sangroup_id);
      }
    }

    delete ise_sangroup_data['available_sg'];
    delete ise_sangroup_data['current_sg'];
    ise_sangroup_data['added'] = added;
    ise_sangroup_data['removed'] = removed;
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_sangroup_data['ise_id'] + '/sangroup_map/';
    return this.put(url, ise_sangroup_data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }

  /**
  * Desc : Getting card-info details for ISE
  * Method type : Get
  * URL : api/ise/ise_id/card-info/
  * @namespace xio.IseService
  * @method getCardInfo
  * @return {Observable} http
  */
  getCardInfo(ise_id: number) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/card-info/';
    return this.get(url).map((res: Response) => {
      let res_data = log(res.json(), null, url);
      return res_data.result.response.data;
    })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * getMenuContent ISE storage Info
   * @namespace xio.IseService
   * @method getStorageInfo
   */
  // getStorageInfo(ise_id: number) {
  //   this.free_space_card = '';
  //   return this.getMenuContent(AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/storage-info/').map((res: Response) => {
  //     this.free_space_card = log(res.json(), null, url).result.response.data;
  //   })
  //     .catch((error: any) => Observable.throw(error || 'Server IseError'));
  // }

  /**
   * Desc : Getting chart data details for ISE
   * Method type : Get
   * URL : api/ise/ise_id/payload['url']/
   * @namespace xio.IseService
   * @method getchartdata
   * @return {Observable} http
   */
  getchartdata(payload) {

    return this.get(AppSettings.API_ENDPOINT + payload['url'])
      .map((res: Response) => {
        let _data = log(res.json(), null, payload['url']).result.response.data,
          _type = res.url.split('/');
        if (_data && _data.hasOwnProperty('type'))
          _data['type'] = _type[_type.length - 2];
        return _data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc : Changing ISE IP Address
  * Method type : Put
  * URL : api/ise/ise_id/ip-update/
  * @namespace xio.IseService
  * @method changeISEIPAddress
  * @return {Observable} http
  */

  changeISEIPAddress(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/ip-update/';
    return this.put(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }

  /**
* Desc : Getting ISE IP Address
* Method type : get
* URL : api/ise/ise_id/ip-update/
* @namespace xio.IseService
* @method getISEInfo
* @return {Observable} http
*/

  getISEInfo(ise_id: number) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/ip-update/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }


}

import { Injectable } from '@angular/core';
import { Http, Response, Jsonp } from '@angular/http';
import { AppSettings } from '../../app-setting';
import { Observable } from 'rxjs/Observable';
import { log } from '../../common/utils/logger';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class PoolsService extends XhrService {

  public drives_list: Array<Object>;
  public actionUrl;
  public pools_list: Array<Object>;


  /**
   *
   * @param {Http} _http
   * @param {Jsonp} _jsonp
   */

  constructor(public _http: Http, public _jsonp: Jsonp) {
    super(_http);
    this.pools_list = [];
    this.actionUrl = AppSettings.API_ENDPOINT;
  }

  /**
   * Desc :getAll pool's data
   * Method type : Get
   * URL : api/ise/ise_id/pools/
   * @namespace xio.PoolsService
   * @method getAll
   * @return {Observable} http
   */

  getAll(ise_id) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/pools/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data;
        if (data.pools.hasOwnProperty('pools')) {
          this.pools_list = data.pools.pools
        }
        else if (data.pools.hasOwnProperty('pool')) {
          this.pools_list = [data.pools.pool]
        }

        return data.pools.hasOwnProperty('pools') ? data.pools.pools : (data.pools.hasOwnProperty('pool') ? [data.pools.pool] : data.pools);
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
 * Desc : get drive data
 * Method type : Get
 * URL : api/ise/ise_id/drives/
 * @namespace xio.PoolsService
 * @method getDrives
 * @return {void}
 */


  getDrives(ise_id) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id.ise_id + '/drives/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.drives.drives;
        this.drives_list = data;
        return this.drives_list;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }



  /**
   * Desc : get medium data
   * Method type : Get
   * URL : api/ise/ise_id/media/
   * @namespace xio.PoolsService
   * @method getMedium
   * @return {void}
   */

  getMedium(ise_id) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/media/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data.media.media;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }


  /**
   * Desc : create Pool service
   * Method type : post
   * URL : api/ise/ise_id/pools/
   * @namespace xio.PoolsService
   * @method createPool
   * @return {void}
   */

  createPool(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/pools/';
    return this.post(url, payLoad.media)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc : Expand Pool service
  * Method type : put
  * URL : api/ise/ise_id/pools/pool_id/
  * @namespace xio.PoolsService
  * @method expandPool
  * @return {void}
  */


  expandPool(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/pools/' + payLoad.pool_id + '/';
    return this.put(url, payLoad.media)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
 * Desc : delete pool service
 * Method type : delete
 * URL : api/ise/ise_id/pools/pool_id/
 * @namespace xio.PoolsService
 * @method deletePool
 * @return {void}
 */

  deletePool(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/pools/' + payLoad.pool_id + '/';
    return this.delete(url).map((res: Response) => {
      return log(res.json(), null, url).result.response.data;
    })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * Desc : get pools data which is using Storage Utilisation chart
   * Method type : Get
   * URL : api/ise/ise_id/pools-chart/
   * @namespace xio.PoolsService
   * @method getchart
   * @return {void}
   */

  getChart(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload.ise_id + '/pools-chart/';
    return this.get(url)
      .map((res: Response) => {
        return log(res.json(), null, url).result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc : get Ratio which is using Storage Utilisation chart
  * Method type : Get
  * URL : api/ise/ise_id/datareduction/
  * @namespace xio.PoolsService
  * @method getRatio
  * @return {void}
  */

  getRatio(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload.ise_id + '/datareduction/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data;
        return data;
      })
       .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * Desc : update drives identify
   * Method type : put
   * URL : api/ise/ise_id/drives/drive_id/
   * @namespace xio.PoolsService
   * @method UpdateDrivesIdentify
   * @return {void}
   */

  updateDrivesIdentify(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/drives/' + payload['drive_id'] + '/';
    return Observable.forkJoin(
      this.put(url, payload['data'])
        .map((res: Response) => log(res.json(), null, url))
        .catch((error: any) => Observable.throw(error || 'Server IseError')));

  }
}

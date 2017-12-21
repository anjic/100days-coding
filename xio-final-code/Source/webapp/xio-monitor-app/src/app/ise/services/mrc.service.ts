import { Injectable } from '@angular/core';
import { Http, Response, Jsonp } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppSettings } from '../../app-setting';
import { log } from '../../common/utils/logger';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { Controller } from '../../ise/models/controllers';

@Injectable()
export class MrcService extends XhrService {

  /**
  * @param {Http} _http
  */

  constructor(public _http: Http) {
    super(_http);
  }

  /**
  * Desc :Getting particular ise mrc details
  * Method type : Get
  * URL : api/ise/ise_id/controllers/ 
  * @namespace xio.MrcService
  * @method getControllers
  * @return {Observable} http
  */

  getControllers(payLoad) {

    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad['ise_id'] + '/controllers/';
    return this.get(url)
      .map((res: Response) => {

        let data = log(res.json(), null, url),
            ise_hardinfo_details: Array<Controller>;

        if (data.result.response.data.controllers.hasOwnProperty('controllers')) {
          ise_hardinfo_details = data.result.response.data.controllers.controllers;
        } else {
          ise_hardinfo_details = [data.result.response.data.controllers.controller];
        }

        return ise_hardinfo_details;

      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc :updating particular ise mrc details
  * Method type : put
  * URL : api/ise/ise_id/controllers/mrc_id/ 
  * @namespace xio.MrcService
  * @method updateMrc
  * @return {Observable} http
  */

  updateMrc(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/controllers/' + payLoad.id + '/';
    return this.put(url, payLoad.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;
  }

  /**
  * Desc :Getting particular ise datapac details
  * Method type : Get
  * URL : api/ise/ise_id/media/ 
  * @namespace xio.MrcService
  * @method getDataPac
  * @return {Observable} http
  */

  getDataPac(ise_id) {

    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/media/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.media.media;
        return data;

      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc :updating particular ise datapac details
  * Method type : put
  * URL : api/ise/ise_id/media/datapac_id 
  * @namespace xio.MrcService
  * @method updateDataPac
  * @return {Observable} http
  */

  updateDataPac(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/media/' + payLoad.id + '/';
    return this.put(url, payLoad.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;
  }


  /**
  * Desc :Getting particular ise powersupply details
  * Method type : Get
  * URL : api/ise/ise_id/powersupplies/ 
  * @namespace xio.MrcService
  * @method getPowerSupply
  * @return {Observable} http
  */

  getPowerSupply(ise_id) {

    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/powersupplies/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.powersupplies.powersupplies;
        return data;

      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc :Getting particular ise powersupply details
  * Method type : Get
  * URL : api/ise/ise_id/powersupplies/ 
  * @namespace xio.MrcService
  * @method getNetwork
  * @return {Observable} http
  */

  getNetwork(ise_id) {

    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/network/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.network;
        return data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc :updating particular ise network details
  * Method type : put
  * URL : api/ise/ise_id/network/network_id 
  * @namespace xio.MrcService
  * @method updateNetwork
  * @return {Observable} http
  */

  updateNetwork(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/network/';
    return this.put(url, payLoad.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;
  }

  /**
  * Desc :update Fcport speed 
  * Method type : put
  * URL : api/ise/ise_id/controllers/mrc_id 
  * @namespace xio.MrcService
  * @method UpdateSpeed
  * @return {Observable} http
  */

  UpdateSpeed(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/controllers/1/';
    return this.put(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;

  }

  /**
  * Desc :updating particular ise powersupply details
  * Method type : put
  * URL : api/ise/ise_id/powersupplies/id 
  * @namespace xio.MrcService
  * @method updatePowerSupply
  * @return {Observable} http
  */

  updatePowerSupply(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/powersupplies/' + payLoad.id + '/';
    return this.put(url, payLoad.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;
  }

  /**
  * Desc :Getting particular ise fans details
  * Method type : Get
  * URL : api/ise/ise_id/fans/ 
  * @namespace xio.MrcService
  * @method getFans
  * @return {Observable} http
  */

  getFans(ise_id) {

    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/fans/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.fans.fans;
        return data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
  * Desc :updating particular ise fans details
  * Method type : put
  * URL : api/ise/ise_id/fans/fans_id 
  * @namespace xio.MrcService
  * @method updateFans
  * @return {Observable} http
  */

  updateFans(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/fans/' + payLoad.id + '/';
    return this.put(url, payLoad.data)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;
  }

  /**
  * Desc :update particular fcportspeed
  * Method type : put
  * URL : api/ise/ise_id/fcports/port_id/ 
  * @namespace xio.MrcService
  * @method updateFcport
  * @return {Observable} http
  */

  updateFcport(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/fcports/' + payload.data['id'] + '/';
    return this.put(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));;

  }

}

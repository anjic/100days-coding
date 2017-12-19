import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppSettings } from '../../app-setting';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class ServermanagementService extends XhrService {

  public actionUrl: string;

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'servermgmt/';
  }

  /**
   * getMenuContent All server's data
   * @namespace xio.ServerService
   * @method getAll
   * @return {Observable} http
   */
  getAll() {
    return this.get(this.actionUrl)
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }


  /**
   * add server
   * @namespace xio.ServerService
   * @param {any} server_data
   * @method addServer
   * @return {Observable} http
   */
  addServer(payLoad: any) {
    console.log(payLoad)
    let url = AppSettings.API_ENDPOINT + 'servermgmt/';
    return this.post(url, payLoad)
      .map((res: Response) => console.log(res));
  }

  getAllWwnGroups(ser_id) {

    let url = AppSettings.API_ENDPOINT + 'servermgmt/' + ser_id + '/wwngroups/';
    return this.get(url)
      .map((res: Response) => {

        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  addWwnServer(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'servermgmt/' + payLoad['server_id'] + '/wwngroups/';
    return this.post(url, payLoad)
      .map((res: Response) => console.log(res));
  }
  /**
   * getMenuContent server Info with ISE and Server details
   * @namespace xio.ServerService
   * @param {any} id - server ID
   * @method getServer
   * @return {Observable} http
   */
  getServer(payload: any) {
    return this.get(AppSettings.API_ENDPOINT + 'server-ise/' + payload['server_id'] + '/')
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  getserverside(payload: any){
     return this.get(AppSettings.API_ENDPOINT + 'sangroup/' + payload['sangroup_id'] + '/wwnserver/' + payload['server_id'])
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  getServerWwn(payLoad) {
    console.log(payLoad)
    let ise_id = payLoad.join();
    return this.get(AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/wwngroups/')
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  getServerWwnGroups(payLoad){
    return this.get(AppSettings.API_ENDPOINT + 'servermgmt/'+  payLoad['server_id'] + '/wwnserver/')
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  getparticularWwnGroup(payLoad){
     return this.get(AppSettings.API_ENDPOINT + 'ise/' + payLoad['ise_id'] + '/wwngroups/'+ payLoad['wwngroup_id'])
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }


  /**
  * update server Info service
  * @namespace xio.ServerService
  * @param {any} server_data - server info
  * @method updateServer
  * @return {Observable}
  */
  updateServer(payload: any) {
    return Observable.forkJoin(
      this.put(this.actionUrl + payload['server_id'] + '/wwnserver-map/', payload)
        .map((res: Response) => res.json().result.response.data)
    );
  }


  /**
   * getMenuContent ISE list for group number {n}
   * @namespace xio.ServerService
   * @param {number} n - group number
   * @method getSanGroupList
   * @return {Observable} http
   */
  getServerSangroup(data: any) {
    const url = this.actionUrl + data['server_id'] + '/sanserver-map/';
    return this.get(url)
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * update San-group Info
   * @namespace xio.SangroupService
   * @param {any} data - san-group info
   * @method updateServerSglink
   * @return {Observable} http
   */

  updateServerSglink(payload: any) {
    let added = [],
      server_sangroup_data = payload['server_sangroup_data'];
    for (let i in server_sangroup_data.available_sg) {
      if (server_sangroup_data.available_sg[i].sg) {
        added.push(server_sangroup_data.available_sg[i].sangroup_id);
      }
    }

    let removed = [];
    for (let i in server_sangroup_data.current_sg) {
      if (!server_sangroup_data.current_sg[i].sg) {
        removed.push(server_sangroup_data.current_sg[i].sangroup_id);
      }
    }

    delete server_sangroup_data['available_sg'];
    delete server_sangroup_data['current_sg'];
    server_sangroup_data['added'] = added;
    server_sangroup_data['removed'] = removed;
    let url = this.actionUrl + server_sangroup_data['ser_id'] + '/sanserver-map/';
    return this.put(url, server_sangroup_data)
      .map((res: Response) => console.log(res.json(), null, url));
  }

  /**
   * delete server service
   * @namespace xio.ServerService
   * @param {any} id - server ID to be deleted
   * @method deleteSangroup
   * @return {Observable} http
   */
  deleteServer(payload: Object) {
    return this.delete(this.actionUrl + payload['server_id'] + '/')
      .map((res: Response) => res.json().result.response.data)
      .catch((error: any) => Observable.throw(error));
  }

  updateWWNGroup(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad['ise_id'] + '/wwngroups/' + payLoad['id'] + '/' ;
    return this.put(url, payLoad)
      .map((res: Response) => console.log(res));
  }

}

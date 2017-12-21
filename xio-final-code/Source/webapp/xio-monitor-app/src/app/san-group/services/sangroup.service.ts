import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { ErrorObservable } from 'rxjs/observable/ErrorObservable';
import { AppSettings } from '../../app-setting';
import { XhrService } from '../../common/utils/xhr.service.util';
import { GetSanIseData } from '../models/san-group';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class SangroupService extends XhrService {

  public actionUrl: string;

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'sangroup/';
  }

  /**
   * Desc :getMenuContent All san's data
   * Method type : Get
   * URL : api/sangroup/ 
   * @namespace xio.SangroupService
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
   * Desc : add san-group
   * Method type : post
   * URL : api/sangroup/ 
   * @namespace xio.SangroupService
   * @param {any} sangroup_data
   * @method addSangroup
   * @return {Observable} http
   */
  addSangroup(sangroup_data: Object) {
    return Observable.forkJoin(
      this.post(this.actionUrl, sangroup_data)
        .map((res: Response) => res.json().result.response.data)
    );
  }

  
  /**
   * Desc : getMenuContent san-group Info with ISE and Sans details
   * Method type : Get
   * URL : api/san-ise/ise_id/ 
   * @namespace xio.SangroupService
   * @param {any} id - san-group ID
   * @method getSangroup
   * @return {Observable} http
   */
  getSangroup(payload):Observable<GetSanIseData[] | ErrorObservable> {
    return this.get(AppSettings.API_ENDPOINT + 'san-ise/' + payload['ise_id'] + '/')
      .map((res: Response):GetSanIseData[] => {
        return res.json().result.response.data;
      })
      .catch((error: any):ErrorObservable => Observable.throw(error || 'Server IseError'));
  }

  /**
   * Desc : update san-group Info service
   * Method type : put
   * URL : api/sangroup/sangroup_id/
   * @namespace xio.SangroupService
   * @param {any} sangroup_data - san-group info
   * @method updateSangroup
   * @return {Observable}
   */
  updateSangroup(sangroup_data: Object) {
    return Observable.forkJoin(
      this.put(this.actionUrl + sangroup_data['sangroup_id'] + '/', sangroup_data)
        .map((res: Response) => res.json().result.response.data)
    );
  }

  /**
   * Desc : delete san-group service
   * Method Type : delete
   * Back End URL : api/sangroup/sangroup_id/
   * @namespace xio.SangroupService
   * @param {any} id - san-group ID to be deleted
   * @method deleteSangroup
   * @return {Observable} http
   */
  deleteSangroup(payload) {
    return this.delete(this.actionUrl + payload['sangroup_id'] + '/')
      .map((res: Response) => res.json().result.response.data['san_list'])
      .catch((error: any) => Observable.throw(error));
  }

  /**
   * getMenuContent ISE list for group number {n}
   * Method Type : get
   * Back End URL : api/sangroup/ise_id/ise-map/
   * @namespace xio.SangroupService
   * @param {number} n - group number
   * @method getIseList
   * @return {Observable} http
   */
  getIseList(ise_id) {
    const url = this.actionUrl + ise_id + '/ise-map/';
    return this.get(url)
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * update San-group Info
   * Method Type : put
   * Back End URL : api/sangroup/sangroup_id/ise-map/
   * @namespace xio.SangroupService
   * @param {any} data - san-group info
   * @method updateSgISElink
   * @return {Observable} http
   */
  updateSgISElink(data) {
    const url = this.actionUrl + data.san_group_id + '/ise-map/';
    return Observable.forkJoin(
      this.put(url, data)
        .map((res: Response) => res.json())
    );
  }

  /**
   * getMenuContent San-group host by Id
   * Method Type : put
   * Back End URL : api/sangroup/sangroup_id/hosts/
   * @namespace xio.SangroupService
   * @param {number} sg_id - san-group id
   * @method getSangroupHost
   * @return {Observable} http
   */
  getSangroupHost(sangroup_id) {
    const url = AppSettings.API_ENDPOINT + 'sangroup/' + sangroup_id + '/hosts/';
    return this.get(url)
      .map((res: Response) => {
        return res.json().result.response.data;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }
}


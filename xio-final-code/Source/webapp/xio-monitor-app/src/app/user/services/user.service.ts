import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppSettings } from '../../app-setting';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/Rx';

@Injectable()
export class UserService extends XhrService {

  public actionUrl: string;

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'user/';
  }

  /**
  * Desc :getMenuContent All user's data
  * Method type : Get
  * URL : api/user/ 
  * @namespace xio.UserService
  * @method getAll
  * @return {Observable} http
  */
  getAll() {
    return this.get(this.actionUrl)
      .map((res: Response) => res.json().result.response.data)
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * Desc : get user data
   * Method type : Get
   * URL : api/user/user_id 
   * @namespace xio.UserService
   * @method getUser
   * @return {void}
   */

  getUser(id) {
    return this.get(this.actionUrl + id + '/')
      .map((res: Response) => res.json().result.response.data)
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  /**
   * Desc : create user service
   * Method type : post
   * URL : api/user/
   * @namespace xio.UserService
   * @method createUser
   * @return {void}
   */
  createUser(user_data: Object) {
    return this.post(this.actionUrl, user_data)
      .map((res: Response) => res.json());
  }

  /**
  * Desc : update user service
  * Method type : put
  * URL : api/user/user_id/
  * @namespace xio.UserService
  * @method updateUser
  * @return {void}
  */
  updateUser(user_data: Object) {
    return this.put(this.actionUrl + user_data['id'] + '/', user_data)
      .map((res: Response) => res.json());
  }

  /**
  * Desc : delete user service
  * Method type : delete
  * URL : api/user/user_id/
  * @namespace xio.UserService
  * @method deleteUser
  * @return {void}
  */
  deleteUser(payLoad) {
    return this.delete(this.actionUrl + payLoad.id + '/')
      .map((res: Response) => res.json())
      .catch((error: any) => Observable.throw(error));
  }

  /**
  * Desc : change user PWD service
  * Method type : put
  * URL : api/user-password/
  * @namespace xio.UserService
  * @method changeUserPassword
  * @return {void}
  */
  changeUserPassword(payLoad) {
    let url = AppSettings.API_ENDPOINT + 'user-password/';
    return this.put(url, payLoad.data)
      .map((res: Response) => res.json()
      );
  }

}

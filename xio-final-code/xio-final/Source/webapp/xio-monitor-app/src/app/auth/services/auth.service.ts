/**
 * User Authentication Service to manage user login session using JWT authentication
 * */

import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { AppSettings } from '../../app-setting';
import { Observable } from 'rxjs/Observable';
import {XhrService} from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';

@Injectable()
export class AuthService extends XhrService {
  public actionUrl: string;
  public token = '';
  public is_login: Boolean = false;

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'login/';
    this.is_login = false;
    this.getToken();
  }

  /**
   * Returns User Session token
   * @namespace xio.AuthService
   * @method getToken
   * @return {String} token
   */
  getToken() {
    const currentUser = JSON.parse(sessionStorage.getItem('currentUser'));
    this.is_login = !!currentUser;
    this.token = (currentUser && currentUser.token) || '';
    return this.token;
  }


  /**
   * User Authentication Service - Login
   * Successful login will return a jwt token in the response
   * Store username and jwt token in sessionStorage to keep user logged in over the current session
   * @namespace xio.AuthService
   * @param {String} username - user name to authenticate with
   * @param {String} password - pwd string
   * @method login
   * @return {Observable}
   */
  login(username: string, password: string) {
    return this.post(this.actionUrl, { username: username, password: password })
      .map((response: Response) => {
        const res = response.json().result.response.data;
        res['username'] =  username;
        this.token = res.token ? res : false;
        return this.token;
      }).catch((error: any) =>
          Observable.throw(error)
          );
  }

  /**
   * User Authentication Service - Logout
   * clear token remove user from session storage to log user out
   * @namespace xio.AuthService
   * @method logout
   * @return {void}
   */
  logout(): void {
    sessionStorage.removeItem('currentUser');
    this.token = null;
    this.is_login = false;
  }
}

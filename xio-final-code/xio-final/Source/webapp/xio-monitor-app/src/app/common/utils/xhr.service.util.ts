/**
 * Created by Dominic on 8/23/2017.
 */

import {Http, Headers} from '@angular/http';
import * as uuid from 'uuid/v1';
import {Router} from "@angular/router";

export class XhrService {
  public current_user = null;
  public headers = null;

  constructor(public http: Http) {
  }

  getHeader() {
    this.current_user = JSON.parse(sessionStorage.getItem('currentUser'));
    this.headers = new Headers();
    this.headers.set('content-type', 'application/json');
    this.headers.set('Accept', 'application/json');
    if (this.current_user)
      this.headers.append('Authorization', 'JWT ' + this.current_user.token);
    this.headers.append('X-Request-ID', uuid());
    return this.headers;
  }

  get (url) {
    return this.http.get(url, {
      headers: this.getHeader()
    });
  }

  post(url, payload) {
    return this.http.post(url, payload, {
      headers: this.getHeader()
    });
  }

  put(url, payload) {
    return this.http.put(url, payload, {
      headers: this.getHeader()
    });
  }

  delete(url) {
    return this.http.delete(url, {
      headers: this.getHeader()
    });
  }
}

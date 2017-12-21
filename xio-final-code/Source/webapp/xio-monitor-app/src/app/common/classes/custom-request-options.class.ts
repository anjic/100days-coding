import {BaseRequestOptions} from '@angular/http';
import * as uuid from 'uuid/v1';
export class CustomRequestOptions extends BaseRequestOptions {
  constructor() {
    super();
    let current_user = JSON.parse(sessionStorage.getItem('currentUser'));
    if (current_user) {
      // this.headers.append('Authorization', 'JWT ' + current_user.token);
      // this.headers.append('X-Request-ID', uuid());
    }
  }

  getToken(token: any) {
    this.headers.append('Authorization', 'JWT ' + token);
  }
}




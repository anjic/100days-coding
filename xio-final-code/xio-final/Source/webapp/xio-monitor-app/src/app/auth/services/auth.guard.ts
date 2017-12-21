import {Injectable} from '@angular/core';
import {CanActivate, Router} from '@angular/router';
import {XhrService} from '../../common/utils/xhr.service.util';

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(public router: Router) {
  }

  /**
   * Auth-guard returns 'true' if login else 'false'
   * @namespace xio.AuthGuard
   * @method canActivate
   * @return {boolean}
   */
  canActivate(): boolean {
    if (sessionStorage.getItem('currentUser')) {
      return true;
    }
    this.router.navigate(['/login']);
    return false;
  }
}

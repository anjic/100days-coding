import {Injectable} from '@angular/core';
import {Http, Response, Headers} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {BehaviorSubject} from 'rxjs/Rx';
import {AppSettings} from '../../app-setting';
import {log} from '../../common/utils/logger'
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class MenuContentService {
  public san_grp_init_state: any = {
    'message': '',
    'result': {
      'status_code': '',
      'response': {
        'data': []
      }
    }
  };

  public _obs_menu_list: BehaviorSubject<any> = new BehaviorSubject(this.san_grp_init_state);
  public readonly obs_menu_list: Observable<any>;

  constructor(public _http: Http) {
    this.obs_menu_list = this._obs_menu_list.asObservable();
  }

  getMenuContent() {
    let url = AppSettings.API_ENDPOINT + 'menu-content/';
    return this._http.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data || [];
        return data;
      })
      .catch((error: any) => {
        return Observable.throw(error || 'Server IseError');
      });
  }

  getHostLst(payload) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/ise-hosts/';
    let headers = new Headers({'Content-Type': 'application/json'});
    return this._http.get(url, {
      headers: headers
    })
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data.hosts.hosts || [];
        return {'ise_id': payload['ise_id'], data : data};
      })
      .catch((error: any) => {
        return Observable.throw(error || 'Server IseError');
      });
  }
}

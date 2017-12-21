import {Injectable} from '@angular/core';
import {Http, Response, Headers, Jsonp} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from '../../app-setting';
import {log} from '../../common/utils/logger';
import {XhrService} from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';


@Injectable()
export class EndpointsService extends XhrService{

  public endpoint_list: any;
  public endpoint_available_list: any;
  public endpoint_available_cnt: number;
  public actionUrl: string;
  public headers: Headers;

  constructor(public _http: Http, public _jsonp: Jsonp) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'endpoints/';
    this.headers = new Headers();
    this.endpoint_available_cnt = 0;
    this.headers.set('content-type', "application/json");
    this.headers.set('Accept', 'application/json');


  }

  getAll(ise_id: number) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/endpoints/'
    return this.get(url)
      .map((res: Response) => {

        let data = log(res.json(), null, url);

        this.endpoint_list = [];
        this.endpoint_available_list = [];
        this.endpoint_available_cnt = 0;
        if(data.result.response.data.endpoints.endpoints)
        for (let ep of data.result.response.data.endpoints.endpoints) {
          if (ep.array == '') {
            this.endpoint_list.push(ep);
          }

          if (ep.host == '' && ep.array == '') {
            this.endpoint_available_list.push(ep);
            this.endpoint_available_cnt++;
          }
        }

        this.endpoint_available_list = Array.isArray(this.endpoint_available_list) ? this.endpoint_available_list : (typeof  this.endpoint_available_list == "object" ? [this.endpoint_available_list] : [] );
        return this.endpoint_available_list;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));

  }


}

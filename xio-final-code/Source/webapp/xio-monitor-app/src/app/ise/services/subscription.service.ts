import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppSettings } from './../../app-setting';
import { log } from '../../common/utils/logger';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class SubscriptionService extends XhrService {
  public actionUrl: string;
  public data: any;
  public ise_id;
  public type;
  public subscription_list: any;
  public subscription_details: any;

  constructor(public _http: Http) {
    super(_http);
    this.actionUrl = AppSettings.API_ENDPOINT + 'ise/';

    this.subscription_details = {
      id: '',
      name: '',
      ssl: '',
      proxy: '',
      proxyaddress: '',
      proxyusername: '',
      proxypassword: ''
    }

  }

  // getAll(payload) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/subscriptions/';
  //   return this.getMenuContent(url)
  //     .map((res: Response) => {
  //       let data = log(res.json(), null, url).response.data.subscriptions;
  //       return (data.hasOwnProperty('subscription') ? [data.subscription] : data.subscriptions);
  //     })
  //     .catch((IseError: any) => Observable.throw(IseError || 'Server IseError'));
  // }

  // TODO Dominic remove this service -> use the data fetched from list
  getSubscription(id: any, ise_id, type) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/subscriptions/' + id + '/' + type;
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url);

        this.subscription_details = data.result.response.data;
        return this.subscription_details;
      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  // addSubscription(payload) {
  //   let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/subscriptions/';
  //   return this.post(url, payload['data'])
  //     .map((res: Response) => log(res.json(), null, url));
  // }

  deleteSubscription(ise_id: number, id: any, type) {
   let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/subscriptions/' + id + '/' + type;
    return this.delete(url)
      .map((res: Response) => log(res.json(), null, url))
      .catch((IseError: any) => Observable.throw(IseError));
  }

  updateSubscription(payload: any) {
    console.log(payload);
    let url = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/subscriptions/' + payload['id'] + '/' + payload['type'];
    return this.put(url, payload['data'])
      .map((res: Response) => log(res.json(), null, url));

  }
}

import {Injectable} from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from '../../app-setting';
import {log} from '../../common/utils/logger';
import {XhrService} from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class EmailService extends XhrService {
  public email_list: Array<Object>;
  public _http: any;
  public emailuser:any;

  constructor(_http: Http) {
    super(_http);
    this._http = _http;
  }

  getAll(ise_id: Number) {
    let url: string = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/settings/mailuser/';
    return this.get(url)
      .map((res: Response) =>
        log(res.json(), null, url).result.response.data
      )
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  addEmail(payload) {
    let url: string = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/settings/mailuser/';
    return this.post(url, payload)
      .map((res: Response) => log(res.json(), null, url));
  }

  updateEmail(payload){
    let url: string = AppSettings.API_ENDPOINT + 'ise/' + payload['ise_id'] + '/settings/mailuser/';
    return this.put(url + payload.id + '/', payload).map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));

  }

  deleteEmail(ise_id: Number, user_id: Number) {
    let url: string = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/settings/mailuser/' + user_id + '/';
    return this.delete(url).map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error));
  }
   getUser(ise_id: Number,id:Number){
     let url: string = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/settings/mailuser/'+ id + '/';
     return this.get(url).map((res: Response) => {
      let data = log(res.json(), null, url);

      this.emailuser = data.result.response.data;
      return this.emailuser;
    })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }


  // alertGetData(ise_id: number) {
  //   let url: string = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/settings/ise-alert/';
  //   return this.getMenuContent(url)
  //     .map((res: Response) => {
  //       let data = log(res.json(), null, url).result.response.data;
  //       return data;
  //     })
  //     .catch((error: any) => Observable.throw(error || 'Server IseError'));
  // }

  // alertUpdate(payload) {
  //   let ise_id: number = payload.ise_id, alert_data = payload.alert_data,
  //     url: string = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/settings/ise-alert/';
  //   return this.put(url, alert_data)
  //     .map((res: Response) => log(res.json(), null, url));
  // }

  getsmtpDetails() {
    let url: string = AppSettings.API_ENDPOINT + 'settings/smtp/';
    return this.get(url)
      .map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  getsmtpCreate(email_data) {
    let url: string = AppSettings.API_ENDPOINT + 'settings/smtp/';
    return this.post(url, email_data)
      .map((res: Response) => log(res.json(), null, url));
  }

  getTestmail(test_data) {
    let url: string = AppSettings.API_ENDPOINT + 'mail/';
    return this.post(url, test_data)
      .map((res: Response) => log(res.json(), null, url));
  }
}



import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppSettings } from '../../app-setting';
import { log } from '../../common/utils/logger';
import { XhrService } from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/Rx';


@Injectable()
export class StoragevolumeService extends XhrService {

  public volume_list: any;
  public actionUrl: string;

  constructor(public _http: Http) {
    super(_http);
    this.volume_list = [];
    this.actionUrl = AppSettings.API_ENDPOINT + 'volumes/';
  }

  getAll(payLoad: any) {
    this.volume_list = [];
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad['ise_id'] + '/volumes/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url);
        if (data.result.response.data.volumes.hasOwnProperty('volumes')) {

          // this.volume_list = data.response.data.volumes.volumes;
          this.volume_list = Array.isArray(data.result.response.data.volumes.volumes) ? data.result.response.data.volumes.volumes :
            (typeof data.result.response.data.volumes.volumes == "object" ?
              [data.result.response.data.volumes.volumes] : [])

        } else if (data.result.response.data.volumes.hasOwnProperty('volume')) {
          this.volume_list = [data.result.response.data.volumes.volume];
        }


        for (let v of this.volume_list) {
          v['lun'] = new Array();
          v['hostname'] = new Array();
          if (v.allocations.hasOwnProperty('allocation')) {
            v['lun'] = [v.allocations.allocation.lun];
            v['hostname'] = [v.allocations.allocation.hostname];
          }

          if (v.allocations.hasOwnProperty('allocations') && v.allocations.allocations != '') {
            for (let a of v.allocations.allocations) {
              if (v['hostname'].indexOf(a.hostname) < 0) {
                v['lun'].push(a.lun);
                v['hostname'].push(a.hostname);
              }
            }
          }
        }
        this.volume_list = Array.isArray(this.volume_list) ? this.volume_list : (typeof this.volume_list == "object" ? [this.volume_list] : [])
        return this.volume_list;

      })
      .catch((error: any) => Observable.throw(error || 'Server IseError'));

  }

  addVolumesdetails(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/volumes/';
    return Observable.forkJoin(
      this.post(url, payLoad.volume_data)
        .map((res: Response) => log(res.json(), null, url))
    );
  }

  getVolumeDetails(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/volumes/' + payLoad.id + '/';
    return this.get(url).map((res: Response) => log(res.json(), null, url))
      .catch((error: any) => Observable.throw(error || 'Server IseError'));
  }

  updateVolumeDetails(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/volumes/' + payLoad.volume_data.id + '/';
    return Observable.forkJoin(
      this.put(url, payLoad.volume_data)
        .map((res: Response) => log(res.json(), null, url))
    );

  }

  updateVolumeAllocation(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/volumes/allocation/';
    return Observable.forkJoin(
      this.put(url, payLoad.volume_data)
        .map((res: Response) => log(res.json(), null, url))
    );

  }

  deleteVolumeDetails(payLoad: any) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + payLoad.ise_id + '/volumes/' + payLoad.id + '/';
    return this.delete(url).map((res: Response) => {
      // this.getAll();
      return log(res.json(), null, url);
    })
      .catch((error: any) => Observable.throw(error));
  }

  getTotalSize(ise_id: number) {
    let url = AppSettings.API_ENDPOINT + 'ise/' + ise_id + '/volumes-chart/';
    return this.get(url)
      .map((res: Response) => {
        let data = log(res.json(), null, url).result.response.data;
        return data;
      });
  }

}

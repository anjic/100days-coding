import { Injectable } from '@angular/core';
import { Http, Response, Headers, Jsonp } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { AppSettings } from '../../app-setting';
import {log} from '../../common/utils/logger';
import {XhrService} from '../../common/utils/xhr.service.util';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/Rx';

@Injectable()
export class HostService extends XhrService {

  public host_list:any;
  public actionUrl:string;

  constructor(public _http: Http, public _jsonp: Jsonp) {
    super(_http);
    this.host_list = [];
	  this.actionUrl = AppSettings.API_ENDPOINT+'hosts/';
  }

  addHosts(host_data) {
  	let new_wwn = [];
     for (var i = host_data.available_wwns.length - 1; i >= 0; i--) {
       if(host_data.available_wwns[i].wwn){
         new_wwn.push(host_data.available_wwns[i].label);
       }
     }

    host_data['endpoint'] = new_wwn;

    delete host_data['current_wwns'];
    delete host_data['available_wwns'];

   let url = AppSettings.API_ENDPOINT+'ise/'+host_data['ise_id']+'/hosts/';
    return Observable.forkJoin(
       this.post(url, host_data)
       .map((res: Response) => log(res.json(), null, url))
       );

  }

  updateHosts(host_data){
     console.log(host_data);
     let removed_wwn = [];
     let new_wwn = [];
     if(host_data.available_wwns){     
     for (var i = host_data.available_wwns.length - 1; i >= 0; i--) {
       if(host_data.available_wwns[i].wwn){
         new_wwn.push(host_data.available_wwns[i].label);
       }
     }
     host_data['endpoint'] = new_wwn;
    }
    if(host_data.current_wwns){     
     for (var i = host_data.current_wwns.length - 1; i >= 0; i--) {
       if(!host_data.current_wwns[i].wwn){
         removed_wwn.push(host_data.current_wwns[i].label);
       }
     }
     host_data['removed_endpoint'] = removed_wwn;

    delete host_data['current_wwns'];
    delete host_data['available_wwns'];
  }

    let url = AppSettings.API_ENDPOINT+'ise/'+host_data['ise_id']+'/hosts/'+host_data.id+'/';

    return Observable.forkJoin(
       this.put(url, host_data)
       .map((res: Response) => log(res.json(), null, url))
       );
  }

  deleteHost(id:any, ise_id:number){
    let url =  AppSettings.API_ENDPOINT+'ise/'+ise_id+'/hosts/'+id+"/";
    return this.delete(url).map((res:Response)=>  log(res.json(), null, url))
        .catch((error:any) =>  Observable.throw(error));
        //Observable.throw(IseError.json().IseError || 'Server IseError')
  }

  getHost(payload: any){
     let url =  AppSettings.API_ENDPOINT+'ise/'+ payload['ise_id']+'/hosts/'+payload['id']+"/";

    return this.get(url).map((res:Response)=>  log(res.json(), null, url))
        .catch((error:any) => Observable.throw(error || 'Server IseError'));
  }

  getAll(payload: any){

    let url:string;

    if(payload['ise_id']){
      url =  AppSettings.API_ENDPOINT+'ise/'+payload['ise_id']+'/hosts/';
    }

   this.host_list = []; //To Empty the Hostlist
   return this.get(url)
        .map((res:Response)=> {
            let data = log(res.json(), null, url);
            this.host_list = [];

            if(data.result.response.data.hosts.hasOwnProperty('hosts')){
              this.host_list = data.result.response.data.hosts.hosts;
            }

            if(data.result.response.data.hosts.hasOwnProperty('host')){
              // this.host_list = [];
              this.host_list.push(data.result.response.data.hosts.host);
            }

            for(let h of this.host_list){
              h['lun'] = new Array();
              if(h.allocations.hasOwnProperty('allocation')){
                h['lun'] = [h.allocations.allocation.lun];
              }

              if(h.allocations.hasOwnProperty('allocations') && h.allocations.allocations != ''){
                for(let a of h.allocations.allocations){
                   h['lun'].push(a.lun);
                }
              }
            }
           return this.host_list;
        })
        .catch((error:any) => Observable.throw(error || 'Server IseError'));
  	}




  updateVolumeAllocation(allocation_data){
    let url = AppSettings.API_ENDPOINT+'ise/'+allocation_data.ise_id+'/hosts/'+allocation_data.host_id+'/allocation/';
    return this.put(url, allocation_data)
       .map((res: Response) => log(res.json(), null, url));

  }


   getHostVolume(id:any, ise_id:number){
      let unique_volume = [];

      let obs =  new BehaviorSubject({});

        this.getHost({
          id: id, ise_id: ise_id
        }).subscribe(
            res => {
            // console.log(res)
            let data:any = '';
            if(res.result.response.data.hosts.host.allocations.hasOwnProperty('allocations')){
               data = res.result.response.data.hosts.host.allocations.allocations;
            }

            if(res.result.response.data.hosts.host.allocations.hasOwnProperty('allocation')){
               data = [res.result.response.data.hosts.host.allocations.allocation];
            }

            let unique_volume_name = [];

            if(data){
              unique_volume = data.filter((item, i, data) => {
                  if(unique_volume_name.indexOf(item.volumename) < 0){
                    unique_volume_name.push(item.volumename);
                    return item;
                  }
              });
            }


             let endpoints_data:any = '';
            if(res.result.response.data.hosts.host.endpoints.hasOwnProperty('endpoints')){
               endpoints_data = res.result.response.data.hosts.host.endpoints.endpoints;
            }

            if(res.result.response.data.hosts.host.endpoints.hasOwnProperty('endpoint')){
               endpoints_data = [res.result.response.data.hosts.host.endpoints.endpoint];
            }

            let host_data = {
              host_name : res.result.response.data.hosts.host.name,
              volumes : unique_volume,
              endpoints : endpoints_data

            }
          return obs.next(host_data);
        },
            err => { console.log(err);}
        );

        return obs.asObservable();
    }
}

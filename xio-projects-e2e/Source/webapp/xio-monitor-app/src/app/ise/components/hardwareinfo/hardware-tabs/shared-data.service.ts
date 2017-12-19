import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable()
export class SharedDataService {

  _data: BehaviorSubject<any>;
  _notifyEvent:BehaviorSubject<any>;
  _volume_info:BehaviorSubject<any>;
  _host_info:BehaviorSubject<any>;

  constructor() {
    this._data = <BehaviorSubject<any[]>>new BehaviorSubject([]);
    this._notifyEvent = <BehaviorSubject<any>>new BehaviorSubject('');
    this._volume_info = <BehaviorSubject<any>>new BehaviorSubject({});
    this._host_info = <BehaviorSubject<any>>new BehaviorSubject({});
  }

  /**
   * 
   */
  getData(): Observable<any> {
       return this._data.asObservable();
  }


  /**
   * @returns {Observable<T>}
   */
  notify(): Observable<any> {
       return this._notifyEvent.asObservable();
  }

  /**
   * Interchanging volume data
   */
  getVolumeInfo() : Observable<any>{
    return this._volume_info.asObservable();
  }

  /**
   * Interchanging host data
   */
  getHostInfo() : Observable<any>{
    return this._host_info.asObservable();
  }

}

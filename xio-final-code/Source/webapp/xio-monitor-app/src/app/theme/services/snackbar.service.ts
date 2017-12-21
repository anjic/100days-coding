import {Injectable} from '@angular/core';
import {Md2Toast} from 'md2/toast/toast';

@Injectable()
export class SnackbarService {

  constructor(public toast: Md2Toast) {
  }

  /**
   * @param msg
   * @param duration
   */
  toastMe(msg: string, duration?: number) {
    this.toast.show(msg, duration);
   
  }

}

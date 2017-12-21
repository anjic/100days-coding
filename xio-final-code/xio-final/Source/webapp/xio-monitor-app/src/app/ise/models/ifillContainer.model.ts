import {IBar} from './ibar.model';
import {IRGB} from './irgb.model';

export interface IFillContainer {
  storageSize: number;
  bars: IBar[];
  color: IRGB;
}

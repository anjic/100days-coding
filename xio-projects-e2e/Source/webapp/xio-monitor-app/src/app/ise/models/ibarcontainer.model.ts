import {IRGB} from './irgb.model';
import {IBar} from './ibar.model';

export interface IBarContainer {
  storageSize: number; // in TB
  storageType: string;
  capacityLabel: string;
  labelOffset: string;
  width: string;
  color: IRGB;
  bars: IBar[];
}

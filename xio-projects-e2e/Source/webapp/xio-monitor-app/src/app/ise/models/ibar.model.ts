import {IRGB} from './irgb.model';

export interface IBar {
  data: { value: number, label: string, labelOffset: string };
  color: IRGB;
  gradient: string;
}

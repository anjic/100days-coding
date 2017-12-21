import {IBarData} from './ibardata.model';

export interface IFillBar {
  data: IBarData;
  offset: string;
  width: string;
  fillColor: string;
  ovalFill: string;
}

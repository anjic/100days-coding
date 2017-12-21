export interface IVolume {
  type: string;
  size: number;
  allocpercent: number;
  configurationpolicy: {
    redundancy: {
      '_attr': {
        'string': string
      }
    }
  };
}

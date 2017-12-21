import {environment} from '../../../environments/environment'


export const log = (data: any, filter: string = 'time_taken', url: string = null,) => {
  if (!environment.production) {
    if (data && data.hasOwnProperty(filter) && filter == 'time_taken') {
      console.log("##################################################################\n");
      if (url)
        console.log(url);
      console.log(data[filter]);
      console.log("##################################################################\n");
    }
    else if(filter == 'error') {
      console.error(data);
    }
  }
  return data;
};

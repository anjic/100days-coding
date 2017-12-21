/**
 * Created by Dominic on 7/12/2017.
 */

import {Observable} from 'rxjs/Observable';

export function EffectSwitchMapCb(service, serviceFn, query, actionSucess, actionFailure) {
  return service[serviceFn](query)
    .map(data => {
      if (query && query.cb) {
        query.cb(data, null);
      }
      return new actionSucess(data);
    })
    .catch((err) => {
      console.error(err);
      if (query && query.cb) {
        query.cb(null, err);
      }
      return Observable.of(actionFailure ? new actionFailure(err) : new actionSucess(err));
    });
}

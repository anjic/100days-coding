/**
 * Created by Dominic on 7/10/2017.
 */

import 'rxjs/add/operator/switchMap';
import {Injectable} from '@angular/core';
import {Effect, Actions, toPayload} from '@ngrx/effects';
import {Action} from '@ngrx/store';
import {Observable} from 'rxjs/Observable';

import {EmailService} from '../ise/services/email.service';
import * as emailActions from '../actions/email.actions';
import {EffectSwitchMapCb} from '../common/utils/EffectsSwitchMapCb';

/**
 * Effects offer a way to isolate and easily test side-effects within your
 * application.
 * The `toPayload` helper function returns just
 * the payload of the currently dispatched action, useful in
 * instances where the current state is not necessary.
 *
 * Documentation on `toPayload` can be found here:
 * https://github.com/ngrx/effects/blob/master/docs/api.md#topayload
 *
 * If you are unfamiliar with the operators being used in these examples, please
 * check out the sources below:
 *
 * Official Docs: http://reactivex.io/rxjs/manual/overview.html#categories-of-operators
 * RxJS 5 Operators By Example: https://gist.github.com/btroncone/d6cf141d6f2c00dc6b35
 */

@Injectable()
export class EmailEffects {

  @Effect()
  getAll$: Observable<Action> = this.actions$
    .ofType(emailActions.GET_ALL_EMAIL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.emailService, 'getAll', query, emailActions['GetEmailActionSuccess'], null);
    }).share();

  @Effect()
  alertGet$: Observable<Action> = this.actions$
    .ofType(emailActions.ALERT_GET_DATA)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.emailService, 'alertGetData', query, emailActions['AlertGetDataActionSuccess'], null);
    }).share();

  @Effect()
  alertUpdate$: Observable<Action> = this.actions$
    .ofType(emailActions.ALERT_UPDATE_DATA)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.emailService, 'alertUpdate', query, emailActions['AlertUpdateDataActionSuccess'], null);
    }).share();

  @Effect()
  createSMPT: Observable<Action> = this.actions$
    .ofType(emailActions.CREATE_SMPT)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.emailService, 'getsmtpCreate', query, emailActions['CreateSMPTActionSuccess'], null);
    }).share();

  @Effect()
  getTestEmail: Observable<Action> = this.actions$
    .ofType(emailActions.GET_TEST_EMAIL)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.emailService, 'getTestmail', query, emailActions['GetTestEmailSuccess'], null);
    }).share();

  constructor(public actions$: Actions, public emailService: EmailService) {
  }
}

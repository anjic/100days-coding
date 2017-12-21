/**
 * Created by Dominic on 8/21/2017.
 */

import 'rxjs/add/operator/switchMap';
import {Injectable} from '@angular/core';
import {Effect, Actions, toPayload} from '@ngrx/effects';
import {Action} from '@ngrx/store';
import {Observable} from 'rxjs/Observable';
import {MenuContentService} from '../theme/services/menu-content.service';
import * as menuActions  from '../actions/menu.action';
import {EffectSwitchMapCb} from '../common/utils/EffectsSwitchMapCb';


@Injectable()
export class MenuEffects {
  @Effect()
  getMenu$: Observable<Action> = this.actions$
    .ofType(menuActions.GET_MENU)
    .map(toPayload)
    .switchMap(query => {
      return EffectSwitchMapCb(this.menuService, 'getMenuContent', query, menuActions['GetMenuActionSuccess'], null);
    });

  @Effect()
  getHost$: Observable<Action> = this.actions$
    .ofType(menuActions.GET_HOST)
    .map(toPayload)
    .flatMap(query => {
      return EffectSwitchMapCb(this.menuService, 'getHostLst', query, menuActions['GetMenuHostActionSuccess'], null);
    });

  constructor(public actions$: Actions, public menuService: MenuContentService) {
  }
}

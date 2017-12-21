import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HttpModule, JsonpModule, RequestOptions } from '@angular/http';
import { NgModule } from '@angular/core';

import { MaterialModule } from './material/material.module';
import { AppRoutingModule } from './app-routing.module';
import { ThemeModule } from './theme/theme.module';
import { AuthModule } from './auth/auth.module';
import { AppComponent } from './app.component';
import { Md2Module } from 'md2';
import { CoreModule } from './core/core.module';
import { SharedModule } from './shared/shared.module';

import { CustomRequestOptions } from './common/classes/custom-request-options.class';
import 'hammerjs';
import { EffectsModule } from '@ngrx/effects';
import { EmailEffects } from './effects/email.effects';
import { StoreModule } from '@ngrx/store';
import { reducer } from './reducers';
import { SanGroupEffects } from './effects/sangroup.effects';
import { UserEffects } from './effects/user.effects';
import { HardWareEffects } from './effects/hardware.effects';
import { ISESettingsEffects } from './effects/ise-settings.effects';
import { HostEffects } from './effects/hosts.effects';
import { ISEManagementEffects } from './effects/ise-management.effects';
import { VolumeEffects } from './effects/volume.effects';
import { PoolsEffects } from './effects/pools.effects';
import { MenuEffects } from './effects/menu.effects';
import { ServerEffects } from './effects/server.effects';

const appRoutingProviders: any[] = [];

@NgModule({
  declarations: [
    AppComponent,
      
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpModule,
    AppRoutingModule,
    ThemeModule,
    AuthModule,
    SharedModule,
    MaterialModule,
    Md2Module.forRoot(),
    CoreModule.forRoot(),

    /**
     * EffectsModule.run() sets up the effects class to be initialized
     * immediately when the application starts.
     *
     * See: https://github.com/ngrx/effects/blob/master/docs/api.md#run
     */
    EffectsModule.run(EmailEffects),
    EffectsModule.run(UserEffects),
    EffectsModule.run(SanGroupEffects),
    EffectsModule.run(ISESettingsEffects),
    EffectsModule.run(HardWareEffects),
    EffectsModule.run(HostEffects),
    EffectsModule.run(ISEManagementEffects),
    EffectsModule.run(VolumeEffects),
    EffectsModule.run(PoolsEffects),
    EffectsModule.run(MenuEffects),
    EffectsModule.run(ServerEffects),



    /**
     * StoreModule.provideStore is imported once in the root module, accepting a reducer
     * function or object map of reducer functions. If passed an object of
     * reducers, combineReducers will be run creating your application
     * meta-reducer. This returns all providers for an @ngrx/store
     * based application.
     */
    StoreModule.provideStore(reducer),
    /**
     * `provideDB` sets up @ngrx/db with the provided schema and makes the Database
     * service available.
     */
    // DBModule.provideDB(schema)

  ],
  providers: [appRoutingProviders, {provide: RequestOptions, useClass: CustomRequestOptions}],
  bootstrap: [AppComponent]
})
export class XioAppModule { }

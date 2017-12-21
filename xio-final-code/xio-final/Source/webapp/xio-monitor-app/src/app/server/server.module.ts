import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SharedModule} from './../shared/shared.module';
import {CoreModule} from './../core/core.module';
import {ThemeModule} from './../theme/theme.module';
import {IseModule} from './../ise/ise.module';
import {ServerRoutingModule} from './server-routing.module';
import {SERVER_COMPONENTS} from './components';


@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    ServerRoutingModule,
    CoreModule,
    ThemeModule,
    IseModule
  ],
  declarations: [...SERVER_COMPONENTS],
 })
export class ServerModule { }

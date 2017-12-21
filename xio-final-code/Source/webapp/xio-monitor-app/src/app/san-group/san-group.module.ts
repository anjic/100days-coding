import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from './../shared/shared.module';
import { CoreModule } from './../core/core.module';
import { ThemeModule } from './../theme/theme.module';
import { IseModule } from './../ise/ise.module';
import { SanGroupRoutingModule } from './san-group-routing.module';
import { SANGROUP_COMPONENTS, SANGROUP_ENTRY_COMPONENTS } from './components';

@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    SanGroupRoutingModule,
    CoreModule,
    ThemeModule,
    IseModule
  ],
  declarations: [...SANGROUP_COMPONENTS, ...SANGROUP_ENTRY_COMPONENTS],
  entryComponents: [...SANGROUP_ENTRY_COMPONENTS]
})
export class SanGroupModule {
}

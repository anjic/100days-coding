import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from './../shared/shared.module';
import { MaterialModule } from './../material/material.module';
import { CoreModule } from './../core/core.module';
import { ThemeModule } from './../theme/theme.module';
import { IseRoutingModule } from './ise-routing.module';
import { ISE_COMPONENTS, ISE_ENTRY_COMPONENTS, ISE_EXPORT_COMPONENTS } from './components';
import { nvD3 } from '../common/utils/ng2-nvd3';
import { CustomRequestOptions } from '../common/classes/custom-request-options.class';
import { RequestOptions } from '@angular/http';
import { EqualValidatorDirective } from './directives/equal-validator.directive';
import { IsePerformanceChartComponent } from './components/ise-performance-chart/ise-performance-chart.component';
import { SharedDataService } from '../ise/components/hardwareinfo/hardware-tabs/shared-data.service';


@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    MaterialModule,
    IseRoutingModule,
    CoreModule,
    ThemeModule
  ],
  declarations: [
    ...ISE_COMPONENTS,
    ...ISE_ENTRY_COMPONENTS,
    nvD3,
    EqualValidatorDirective,
    IsePerformanceChartComponent,
   ],
  providers: [ SharedDataService , {provide: RequestOptions, useClass: CustomRequestOptions}],
  entryComponents: [...ISE_ENTRY_COMPONENTS],
  exports: [...ISE_EXPORT_COMPONENTS]
})

export class IseModule { }

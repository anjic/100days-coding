import { NgModule, ModuleWithProviders } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ALL_SERVICES} from './services.collection';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: []
})
export class CoreModule {

	static forRoot(): ModuleWithProviders {
	    return {
	      ngModule: CoreModule,
	      providers: [ALL_SERVICES]
	    };
  	}
}

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from './../shared/shared.module';
import { CoreModule } from './../core/core.module';
import { UserRoutingModule } from './user-routing.module';
import { USER_COMPONENTS } from './components';
import { ThemeModule } from './../theme/theme.module';

@NgModule({
	imports: [
		CommonModule,
		SharedModule,
		UserRoutingModule,
		ThemeModule,
		CoreModule
	],
	declarations: [...USER_COMPONENTS]
})
export class UserModule {
}

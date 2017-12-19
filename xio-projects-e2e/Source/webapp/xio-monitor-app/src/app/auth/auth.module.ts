import { NgModule } from '@angular/core';
import { SharedModule } from './../shared/shared.module';
import { LoginComponent } from './login/login.component';
import { ContactUsComponent } from './contact-us/contact-us.component';
@NgModule({
  imports: [  SharedModule ],
  declarations: [ LoginComponent,ContactUsComponent ],
  exports: [ LoginComponent,ContactUsComponent ]
})
export class AuthModule { }

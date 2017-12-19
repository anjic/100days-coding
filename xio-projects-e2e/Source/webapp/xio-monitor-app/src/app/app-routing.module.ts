import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { ContactUsComponent } from './auth/contact-us/contact-us.component';
import { AuthGuard } from './auth/services/auth.guard';

export const routes: Routes = [
 	  { path: 'login', component: LoginComponent},
 	  { path: 'contact-us', component : ContactUsComponent},
    { path: '', redirectTo: 'ise', pathMatch: 'full', canActivate: [AuthGuard] },
	  { path: 'user', loadChildren: '../app/user/user.module#UserModule', canActivate: [AuthGuard] },
	  { path: 'ise', loadChildren: '../app/ise/ise.module#IseModule', canActivate: [AuthGuard] },
	  { path: 'san-group', loadChildren: '../app/san-group/san-group.module#SanGroupModule', canActivate: [AuthGuard] },
	  { path: 'server', loadChildren: '../app/server/server.module#ServerModule', canActivate: [AuthGuard] }

];


@NgModule({
	imports: [RouterModule.forRoot(routes)],
	exports: [RouterModule]
})
export class AppRoutingModule { }

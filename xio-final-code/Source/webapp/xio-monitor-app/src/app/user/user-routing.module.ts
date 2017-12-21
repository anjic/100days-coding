import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { USERS_ROUTES } from './components';

const usersRoutes: Routes = [...USERS_ROUTES];

@NgModule({
	imports: [RouterModule.forChild(usersRoutes)],
	exports: [RouterModule]
})
export class UserRoutingModule {
}

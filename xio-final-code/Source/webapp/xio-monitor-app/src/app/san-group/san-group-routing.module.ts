import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SANGROUP_ROUTES } from './components';

const sangroupRoutes: Routes = [...SANGROUP_ROUTES];

@NgModule({
	imports: [RouterModule.forChild(sangroupRoutes)],
	exports: [RouterModule]
})
export class SanGroupRoutingModule { }

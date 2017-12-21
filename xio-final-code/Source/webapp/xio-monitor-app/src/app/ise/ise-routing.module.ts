import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ISE_ROUTES } from './components';

const iseRoutes: Routes = [...ISE_ROUTES];

@NgModule({
  imports: [RouterModule.forChild(iseRoutes)],
  exports: [RouterModule]
})
export class IseRoutingModule { }
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SERVER_ROUTES } from './components';

const serverRoutes: Routes = [...SERVER_ROUTES];

@NgModule({
  imports: [RouterModule.forChild(serverRoutes)],
  exports: [RouterModule]
})
export class ServerRoutingModule { }
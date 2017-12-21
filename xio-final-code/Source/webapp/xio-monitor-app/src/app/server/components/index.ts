import { ServerComponent } from './server/server.component';
import { ServerListComponent } from './server-list/server-list.component';
import { ServerFormComponent } from './server-form/server-form.component';
import { ServerSangroupLinkComponent } from './server-sangroup-link/server-sangroup-link.component';
import { ServerWwnFormComponent } from './server-wwn-form/server-wwn-form.component';
import { ServerEditFormComponent } from './server-edit-form/server-edit-form.component';
import { WwngroupEditComponent } from './wwngroup-edit/wwngroup-edit.component';
import { ServerWwngroupComponent } from './server-wwngroup/server-wwngroup.component';



export const SERVER_COMPONENTS = [
	  ServerComponent,
	  ServerListComponent,
	  ServerFormComponent,
    ServerSangroupLinkComponent,
    ServerWwnFormComponent,
    ServerEditFormComponent,
    WwngroupEditComponent,
    ServerWwngroupComponent
];



export const SERVER_ROUTES = [
  {
    path: '', component: ServerComponent,
    children: [
      {path: '', redirectTo: 'list', pathMatch: 'full'},
      {path: 'list', component: ServerListComponent},
      {path: 'create', component: ServerFormComponent},
      {path: ':ser_id/edit', component: ServerEditFormComponent},
      {path: ':ser_id/edit/serverwwn/:sangroup_id', component: ServerWwngroupComponent},
      {path: ':ser_id/edit/wwn', component: ServerWwnFormComponent},
      {path: ':ser_id/edit/wwngroup/:id/:wwnid', component: WwngroupEditComponent},
      {path: ':ser_id/san-group/link', component: ServerSangroupLinkComponent},
    ]
  },
];

export * from './server/server.component';
export * from './server-list/server-list.component';
export * from './server-form/server-form.component';
export * from './server-sangroup-link/server-sangroup-link.component';
export * from './server-wwn-form/server-wwn-form.component';
export * from './server-edit-form/server-edit-form.component';
export * from './wwngroup-edit/wwngroup-edit.component';
export * from './server-wwngroup/server-wwngroup.component';





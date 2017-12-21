import { SanGroupComponent } from './san-group/san-group.component';
import { SanGroupListComponent } from './san-group-list/san-group-list.component';
import { SangroupDashboardComponent } from './sangroup-dashboard/sangroup-dashboard.component';
import { SangroupFormComponent } from './sangroup-form/sangroup-form.component';
import { SangroupHostComponent } from './sangroup-host/sangroup-host.component';
import { SangroupHostFormComponent } from './sangroup-host/sangroup-host-form/sangroup-host-form.component';
import { LinkSgIseComponent } from './link-sg-ise/link-sg-ise.component';
import { HostLandingPageComponent } from './../../ise/components/host/host-landing-page/host-landing-page.component';

export const SANGROUP_COMPONENTS = [
  SanGroupComponent,
  SanGroupListComponent,
  SangroupDashboardComponent,
  SangroupFormComponent,
  SangroupHostComponent,
  SangroupHostFormComponent,
  LinkSgIseComponent
];

export const SANGROUP_ENTRY_COMPONENTS = [
];

export const SANGROUP_ROUTES = [
  {
    path: '', component: SanGroupComponent,
    children: [
      { path: '', redirectTo: 'list', pathMatch: 'full' },
      { path: 'list', component: SanGroupListComponent },
      { path: 'create', component: SangroupFormComponent },
      { path: 'edit/:sg_id', component: SangroupFormComponent },
      { path: ':sg_id/dashboard', component: SangroupDashboardComponent },
      { path: ':sg_id/ise/link', component: LinkSgIseComponent },
      { path: ':sg_id/host', component: SangroupHostComponent },
      { path: ':sg_id/host/add', component: SangroupHostFormComponent }
    ]
  },
  { path: ':sg_id/ise/:ise_id/host/:host_id', component: HostLandingPageComponent },
];

export * from './san-group/san-group.component';
export * from './san-group-list/san-group-list.component';
export * from './sangroup-dashboard/sangroup-dashboard.component';
export * from './sangroup-form/sangroup-form.component';
export * from './sangroup-host/sangroup-host.component';
export * from './sangroup-host/sangroup-host-form/sangroup-host-form.component';
export * from './link-sg-ise/link-sg-ise.component';
export * from './../../ise/components/host/host-landing-page/host-landing-page.component';


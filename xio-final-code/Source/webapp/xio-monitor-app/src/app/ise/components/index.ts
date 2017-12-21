import { IseComponent } from './ise/ise.component';
import { IseListComponent } from './ise-list/ise-list.component';
import { IseDashboardComponent } from './ise-dashboard/ise-dashboard.component';
import { IseInfoCardComponent } from './ise-info-card/ise-info-card.component';
import { IseDiscoverComponent } from './ise-discover/ise-discover.component';
import { IseLandingComponent } from './ise-landing/ise-landing.component';
import { IsePerformanceComponent } from './ise-performance/ise-performance.component';
import { IseSangroupLinkComponent } from './ise-sangroup-link/ise-sangroup-link.component';
import { IseSettingsComponent } from './ise-settings/ise-settings.component';
import { IseEditFormComponent } from './ise-list/ise-edit-form/ise-edit-form.component';
import { IseChangepwdFormComponent } from './ise-list/ise-changepwd-form/ise-changepwd-form.component';
import { HostComponent } from './host/host.component';
import { HostPresentButtonComponent } from './host/host-present-button/host-present-button.component';
import { HostLandingPageComponent } from './host/host-landing-page/host-landing-page.component';
import { HostIseLinkComponent } from './host/host-ise-link/host-ise-link.component';
import { HostFormComponent } from './host/host-form/host-form.component';
import { HostEditButtonComponent } from './host/host-edit-button/host-edit-button.component';
import { HostDeleteButtonComponent } from './host/host-delete-button/host-delete-button.component';
import { VolumeComponent } from './volume/volume.component';
import { VolumeFormComponent } from './volume/volume-form/volume-form.component';
import { VolumeEditButtonComponent } from './volume/volume-edit-button/volume-edit-button.component';
import { VolumeDeleteButtonComponent } from './volume/volume-delete-button/volume-delete-button.component';
import { VolumePresentButtonComponent } from './volume/volume-present-button/volume-present-button.component';
import { VolumePresentLinkComponent } from './volume/volume-present-link/volume-present-link.component';

import { PoolsListComponent } from './pools/pools-list/pools-list.component';
import { PoolsFormComponent } from './pools/pools-form/pools-form.component';

import { IopsComponent } from './charts/iops/iops.component';
import { LatencyComponent } from './charts/latency/latency.component';
import { DataRateComponent } from './charts/data-rate/data-rate.component';
import { QueueDepthComponent } from './charts/queue-depth/queue-depth.component';
import { PerformanceVolumeComponent } from './ise-performance-volume/ise-performance-volume.component';
import { PerformanceHostComponent } from './ise-performance-host/ise-performance-host.component';
import { EndpointListComponent } from './endpoints/endpoint-list/endpoint-list.component';
import { SubscriptionListComponent } from './ise-settings/subscription-list/subscription-list.component';
import { SubscriptionFormComponent } from './ise-settings/subscription-form/subscription-form.component';
import { SubscriptionEditComponent } from './ise-settings/subscription-list/subscription-edit/subscription-edit.component';
import { SubscriptionDeleteComponent } from './ise-settings/subscription-list/subscription-delete/subscription-delete.component';
import { EmailListComponent } from './ise-settings/email-list/email-list.component';
import { EmailFormComponent } from './ise-settings/email-form/email-form.component';
import { TimeZoneComponent } from './ise-settings/time-zone/time-zone.component';
import { HardwareinfoComponent } from './hardwareinfo/hardwareinfo.component';
import { SetIsePasswordComponent } from './set-ise-password/set-ise-password.component';
import { MrcComponent } from './hardwareinfo/hardware-tabs/mrc/mrc.component';
import { NetworkComponent } from './hardwareinfo/hardware-tabs/network/network.component';
import { OpendatapacComponent } from './hardwareinfo/hardware-tabs/opendatapac/opendatapac.component';
import { PowersupplyComponent } from './hardwareinfo/hardware-tabs/powersupply/powersupply.component';
import { UserEditButtonComponent } from './ise-settings/user-edit-button/user-edit-button.component';
import { FansComponent } from './hardwareinfo/hardware-tabs/fans/fans.component';
import { FillContainerComponent } from '../../shared/fill-bars/fill-container.component';
import { BarFillComponent } from '../../shared/fill-bars/bar-fill.component';
import { NonEmptyContainersPipe } from './ise-dashboard/ise-dashboard.component';
import { IseEncryptionComponent } from './ise-encryption/ise-encryption.component';
import { EqualValidatorDirective } from '../directives/equal-validator.directive';
import { IseUnlockComponent } from './ise-unlock/ise-unlock.component';
import { IseModifyFormComponent } from './ise-list/ise-modify-form/ise-modify-form.component';
import { IsePerformanceChartComponent } from './ise-performance-chart/ise-performance-chart.component';

export const ISE_COMPONENTS = [
  IseComponent,
  IseListComponent,
  IseDiscoverComponent,
  IseDashboardComponent,
  IseSettingsComponent,
  IsePerformanceComponent,
  IseLandingComponent,
  IseEditFormComponent,
  IseInfoCardComponent,
  IseChangepwdFormComponent,
  IseSangroupLinkComponent,
  HostComponent,
  HostFormComponent,
  HostLandingPageComponent,
  HostIseLinkComponent,
  VolumeComponent,
  VolumeFormComponent,
  PoolsListComponent,
  PoolsFormComponent,
  IopsComponent,
  LatencyComponent,
  DataRateComponent,
  QueueDepthComponent,
  PerformanceVolumeComponent,
  PerformanceHostComponent,
  EndpointListComponent,
  SubscriptionListComponent,
  SubscriptionFormComponent,
  EmailListComponent,
  EmailFormComponent,
  TimeZoneComponent,
  HardwareinfoComponent,
  SetIsePasswordComponent,
  MrcComponent,
  NetworkComponent,
  OpendatapacComponent,
  PowersupplyComponent,
  UserEditButtonComponent,
  FansComponent,
  FillContainerComponent,
  BarFillComponent,
  NonEmptyContainersPipe,
  EqualValidatorDirective,
  IseUnlockComponent,
  IseModifyFormComponent,
];

export const ISE_EXPORT_COMPONENTS = [
  HostLandingPageComponent,
  HostFormComponent,
  IseInfoCardComponent,
  VolumeFormComponent
];

export const ISE_ENTRY_COMPONENTS = [
  HostEditButtonComponent,
  HostDeleteButtonComponent,
  HostPresentButtonComponent,
  VolumeEditButtonComponent,
  VolumeDeleteButtonComponent,
  VolumePresentButtonComponent,
  VolumePresentLinkComponent,
  SubscriptionEditComponent,
  SubscriptionDeleteComponent,
  UserEditButtonComponent,
  IseEncryptionComponent
];

export const ISE_ROUTES = [
  {
    path: '', component: IseComponent,
    children: [
      { path: '', redirectTo: 'list', pathMatch: 'full' },
      { path: 'list', component: IseListComponent },
      { path: 'discover', component: IseDiscoverComponent },
      { path: ':ise_id/change-pwd', component: IseChangepwdFormComponent },
      { path: ':ise_id/san-group/link', component: IseSangroupLinkComponent },
      { path: ':ise_id/edit', component: IseEditFormComponent },
      { path: ':ise_id/ip-update', component: IseModifyFormComponent },

      {
        path: ':ise_id', component: IseLandingComponent,
        children: [
          { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
          { path: 'dashboard', component: IseDashboardComponent },
          { path: 'host', component: HostComponent },
          { path: 'host/add', component: HostFormComponent },
          { path: 'host/edit/:host_id', component: HostFormComponent },
          { path: 'host/:host_id/present', component: HostIseLinkComponent },
          { path: 'volume', component: VolumeComponent },
          { path: 'volume/create', component: VolumeFormComponent },
          { path: 'volume/edit/:id', component: VolumeFormComponent },
          { path: 'volume/present/:id', component: VolumePresentLinkComponent },
          { path: 'settings', component: IseSettingsComponent },
          { path: 'settings/edit/:id/:type', component: SubscriptionFormComponent },
          { path: 'email/edit/:id', component: EmailFormComponent },
          { path: 'pools', component: PoolsListComponent },
          { path: 'pools/add', component: PoolsFormComponent },
          { path: 'pools/expand/:pool_id/:pool_name', component: PoolsFormComponent },
          { path: 'endpoints', component: EndpointListComponent },
          {
            path: 'hardwareinfo', component: HardwareinfoComponent,
            children: [
              { path: '', redirectTo: 'mrc', pathMatch: 'full' },
              { path: 'mrc', component: MrcComponent },
              { path: 'opendatapac', component: OpendatapacComponent },
              { path: 'powersupply', component: PowersupplyComponent },
              { path: 'network', component: NetworkComponent },
              { path: 'fans', component: FansComponent }
            ]
          },
          { path: 'set-password', component: SetIsePasswordComponent },
          { path: 'ise-unlock', component: IseUnlockComponent },
          {
            path: 'performance', component:IsePerformanceChartComponent,
            children: [
              { path: '', redirectTo: 'ise', pathMatch: 'full' },
              { path: 'ise', component: IsePerformanceComponent },
              { path: 'volume', component: PerformanceVolumeComponent },
              { path: 'wwngroup', component: PerformanceHostComponent },
            ]
          }
        ]
      }
    ]
  }
];

import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SharedModule} from './../shared/shared.module';
import {XioSidebarComponent, XioAlertComponent, XioDialogComponent, XioProgressComponent, XioLoaderComponent} from './';


@NgModule({
  imports: [
    CommonModule,
    SharedModule
  ],
  declarations: [
    XioSidebarComponent,
    XioDialogComponent,
    XioProgressComponent,
    XioLoaderComponent,
    XioAlertComponent
  ],
  exports: [
    XioSidebarComponent,
    XioLoaderComponent,

  ],
  entryComponents: [
    XioDialogComponent,
    XioProgressComponent,
    XioLoaderComponent,
    XioAlertComponent
  ]
})
export class ThemeModule {
}

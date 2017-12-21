import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MaterialModule } from './../material/material.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import { Md2Module } from 'md2';
import { XioMdDataTableModule } from './Component/xio-md-dataTable/xio-md-dataTable.module';
import { RefreshButtonComponent } from './Component/refresh-button/refresh-button.component';
import { FooterComponent } from '../layout/footer/footer.component';

const MODULE_COLLECTION = [
  CommonModule,
  RouterModule,
  FormsModule,
  ReactiveFormsModule,
  HttpModule,
  JsonpModule,
  MaterialModule,
  Md2Module,
  XioMdDataTableModule
];

@NgModule({
  imports: [
    ...MODULE_COLLECTION
  ],
  declarations: [RefreshButtonComponent, FooterComponent],
  exports: [
    ...MODULE_COLLECTION,
    RefreshButtonComponent,
    FooterComponent
    
    
  ]
})
export class SharedModule {
}

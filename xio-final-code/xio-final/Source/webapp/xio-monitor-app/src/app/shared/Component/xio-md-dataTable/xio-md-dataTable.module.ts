/**
 * Created by Dominic on 06-09-2017.
 */
import {NgModule} from '@angular/core';
import {XioMdRowContainerComponent} from './xio-md-rowContainer/xio-md-rowContainer.component';
import {XioMdDataTableComponent} from './xio-md-dataTable.component';
import {EditButtonComponent} from './edit-button/edit-button.component';
import {DeleteButtonComponent} from './delete-button/delete-button.component';
import {ChangepwdComponent} from './changepwd-button/changepwd.component';
import {PresentButtonComponent} from './present-button/present-button.component';
import {Md2CollapseModule} from 'md2/collapse'
import {FormsModule} from "@angular/forms";
import {CommonModule} from "@angular/common";
import {Md2Module} from 'md2';
import {MaterialModule} from './../../../material/material.module';
import { ModifyButtonComponent } from './modify-button/modify-button.component';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    Md2CollapseModule,
    Md2Module,
    MaterialModule

  ],
  exports: [
    XioMdDataTableComponent, XioMdRowContainerComponent, EditButtonComponent, DeleteButtonComponent, ChangepwdComponent, PresentButtonComponent
  ],
  declarations: [XioMdDataTableComponent, XioMdRowContainerComponent, EditButtonComponent, DeleteButtonComponent, ChangepwdComponent, PresentButtonComponent, ModifyButtonComponent],
  bootstrap: []
})
export class XioMdDataTableModule {
}

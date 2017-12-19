/**
 * Created by dominic on 3/7/17.
 */

import {FormArray, Validators} from '@angular/forms';
import {XioAlertComponent} from '../../theme/';

export abstract class SanGroupUtil {
  abstract fb;

  initSG(v: number, lbl: string, status: boolean) {
    return this.fb.group({sg: [status, Validators.required], label: lbl, sangroup_id: v});
  }

  addSG(v: number, lbl: string, type: string, status: boolean) {
    const control = <FormArray>this['discoveryForm']['controls'][type];
    control.push(this.initSG(v, lbl, status));
  }

  addServerSG(v: number, lbl: string, type: string, status: boolean) {
    const control = <FormArray>this['serverForm']['controls'][type];
    control.push(this.initSG(v, lbl, status));
  }

  getSGLabel(type: string, i: number) {
    const control = <FormArray>this['discoveryForm']['controls'][type];
    return control.value[i].label;
  }
  
  isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }
}

/**
 * Created by dominic on 3/7/17.
 */

import {FormGroup, FormArray, Validators} from '@angular/forms';

export abstract class HostComponentUtil {

  abstract router: any;
  abstract fb: any;

  /**
   * initWwn prop
   * @namespace xio.HostComponentUtil
   * @param {String} v
   * @method initWwn
   * @return {FormGroup}
   */
  initWwn(v: string, status: boolean) {
    let isAdd = this['host_details'].id;
    return this.fb.group({wwn: [status, Validators.required], label: v, isAdd: isAdd});
  }

  /**
   * Add WWN
   * @namespace xio.HostComponentUtil
   * @param {String} v
   * @param {String} type
   * @param {boolean} status
   * @method addWWN
   * @return {void}
   */
  addWWN(v: string, type: string, status: boolean) {
    const control = <FormArray>this['hostsForm']['controls'][type];
    control.push(this.initWwn(v, status));
  }

  /**
   * remove WWN
   * @namespace xio.HostComponentUtil
   * @method removeWWN
   * @return {void}
   */
  removeWWN(i: number) {
    const control = <FormArray>this['hostsForm']['controls']['available_wwns'];
    control.removeAt(i);
  }

  /**
   * clear WWN UI
   * @namespace xio.HostComponentUtil
   * @method clearWWN
   * @return {void}
   */
  clearWWN() {
    let n = this['hostsForm']['controls']['available_wwns']['controls'].length;
    for (let i = 0; i < n; i++) {
      this.removeWWN(i);
    }
  }

  /**
   * get WWN Label val
   * @namespace xio.HostComponentUtil
   * @method getWWNLabel
   * @return {void}
   */
  getWWNLabel(type: string, i: number, w: any) {
    const control = <FormArray>this['hostsForm']['controls'][type];
    return control.value[i].label;
  }

  /**
   * init Volume's
   * @namespace xio.HostComponentUtil
   * @method initVolume
   * @return {FormGroup}
   */
  initVolume(v: string, status: boolean, lun_no: Number) {
    return this.fb.group({volume: [status, Validators.required], label: v, lun: lun_no});
  }

  /**
   * add volume
   * @namespace xio.HostComponentUtil
   * @param {String} v
   * @param {String} type
   * @param {boolean} status
   * @method addVolume
   * @return {void}
   */
  addVolume(v: string, type: string, status: boolean, lun_no: Number) {
    const control = <FormArray>this['hostsForm']['controls'][type];
    control.push(this.initVolume(v, status, lun_no ));
  }

  /**
   * remove Volume
   * @namespace xio.HostComponentUtil
   * @param {number} i
   * @method removeVolume
   * @return {void}
   */
  removeVolume(i: number) {
    const control = <FormArray>this['hostsForm']['controls']['volumes'];
    control.removeAt(i);
  }

  /**
   * clear Volume
   * @namespace xio.HostComponentUtil
   * @method clearVolume
   * @return {void}
   */
  clearVolume() {
    while (this['hostsForm']['controls']['volumes']['controls'].length) {
      this.removeVolume(this['hostsForm']['controls']['volumes']['controls'].length - 1);
    }
  }

  /**
   * get Volume Lbl
   * @namespace xio.HostComponentUtil
   * @param {string} string
   * @param {number} i
   * @method getVolumeLabel
   * @return {FormArray}
   */
  getVolumeLabel(type: string, i: number, formGroup: string) {
    const control = <FormArray>this[formGroup]['controls'][type];
    return control.value[i].label;
  }

  /**
   * get Host Lst
   * @namespace xio.HostComponentUtil
   * @method goToHostList
   * @return {void}
   */
  goToHostList() {
    this.router.navigate(['/ise/' + this['host_details'].ise_id + '/host']);
  }

  /**
   * add validation to FormGroup
   * @namespace xio.HostComponentUtil
   * @method validateEnpoint
   * @return {void}
   */
  validateEnpoint(formGroup: FormGroup) {
    let form_value = formGroup.root.value;
    let current_wwn = 0;
    let new_wwn = 0;
    let return_val: any = '';
    for (let control in form_value['available_wwns']) {
      if (form_value['available_wwns'][control]['wwn']) {
        new_wwn++;
        break;
      }
    }
    if (!form_value['id'] && new_wwn) {
      return_val = null;

    } else {
      if (form_value['id']) {
        for (let control of form_value['current_wwns']) {
          if (control.wwn) {
            current_wwn++;
            break;
          }
        }

        if (current_wwn || new_wwn) {
          return_val = null;
        } else {
          return_val = {
            validateEnpoint: {
              valid: false
            }
          };
        }
      }
    }

    let LUN = [];
    for (let v of form_value.volumes) {
      if (v.volume) {
        if (v.lun < 0 || v.lun > 9999) {
          if (!return_val) {
            return_val = {};
          }
          return_val['invalidLUN'] = {
            valid: false
          };
          break;
        }
        if (LUN.indexOf(v.lun) > -1) {
          if (!return_val) {
            return_val = {};
          }
          return_val['validateLUN'] = {
            valid: false
          };
          break;
        }
        LUN.push(v.lun);
      }
    }
    return return_val;
  }

  /**
   * Util Fn to check isAvsilableWwn
   * @namespace xio.HostComponentUtil
   * @method isAvsilableWwn
   * @return {number}
   */
  isAvsilableWwn(type: string) {
    let cnt = 0;
    let ele = this['hostsForm'].value[type];
    for (let i = ele.length - 1; i >= 0; i--) {
      if (this['hostsForm'].value[type][i].wwn) {
        cnt++;
      }
    }
    return cnt;
  }

  /**
   * change Step
   * @namespace xio.HostComponentUtil
   * @method changeStep
   * @return {void}
   */
  changeStep(n: number) {
    this['host_details'].current_step = n;
  }

  /**
   * Change tab
   * @namespace xio.HostComponentUtil
   * @method validateEnpoint
   * @return {void}
   */
  changeTab() {
    this['host_details'].selectedIndex = 0;
  }

  /**
   * init volumetem
   * @namespace xio.HostComponentUtil
   * @param {String} v
   * @param {boolean} status
   * @param {any} globalID
   * @param {number} lun_no
   * @method initVolumetem
   * @return {FormGroup}
   */
  initVolumetem(v: string, status: boolean, globalID: any, lun_no: number) {
    return this.fb.group({
      volume: [status, Validators.required],
      label: v,
      globalID: globalID,
      lun: [lun_no]
    });
  }

  /**
   * add volumetem
   * @namespace xio.HostComponentUtil
   * @param {String} v
   * @param {string} type
   * @param {boolean} status
   * @param {any} globalID
   * @param {number} lun_no
   * @method addVolumeItem
   * @return {FormGroup}
   */
  addVolumeItem(v: string, type: string, status: boolean, globalID: any, lun_no: any) {
    const control = <FormArray>this['allocationForm']['controls'][type];
    let _c = this.initVolumetem(v, status, globalID, lun_no);
    control.push(_c);
    return _c;
  }
}

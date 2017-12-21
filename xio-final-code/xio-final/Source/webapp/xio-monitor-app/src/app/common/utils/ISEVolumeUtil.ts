/**
 * Created by Dominic on 7/20/2017.
 */


import {Validators, FormControl, FormGroup, FormArray} from '@angular/forms';

export abstract class ISEVolumeUtil {

  abstract storagevolumeForm;

  getSizeValidator() {
    return [Validators.required,
      // Validators.pattern(/^([1-9]|[1-8][0-9]|9[0-9]|[1-8][0-9]{2}|9[0-8][0-9]|99[0-9]|[1-7][0-9]{3}|80[0-9]{2}|81[0-8][0-9]|819[01])$/)
      ];
  }

  getNameValidator() {
    return [Validators.required,
      Validators.maxLength(256),
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)];
  }

  removeDuplicates(arrayList, prop) {
    return arrayList.filter((obj, pos, arr) => {
      return arr.map(mapObj => mapObj[prop]).indexOf(obj[prop]) === pos;
    });
  }


  likevolume() {
    if (this.storagevolumeForm['controls']['create_like_volumes'].value) {
      this.storagevolumeForm['controls']['no_like_volumes'].enable();

    } else {
      this.storagevolumeForm['controls']['no_like_volumes'].disable();
    }
  }

  enableIOPS() {
    this.storagevolumeForm['controls']['IOPSmin'].enable();
    this.storagevolumeForm['controls']['IOPSmax'].enable();
    this.storagevolumeForm['controls']['IOPSburst'].enable();
  }

  disableIOPS() {
    this.storagevolumeForm['controls']['IOPSmin'].disable();
    this.storagevolumeForm['controls']['IOPSmax'].disable();
    this.storagevolumeForm['controls']['IOPSburst'].disable();
  }

  watchDisabled() {
    this.storagevolumeForm['controls']['quality_service'].value ? this.enableIOPS() : this.disableIOPS();
  }

  validateBurst(IOPSminkey: string, IOPSmaxkey: string, IOPSburstkey: string) {
    return (group: FormGroup): { [key: string]: any } => {
      if (group.root['controls']['quality_service'].value) {
        const IOPSmin = group.root['controls'][IOPSminkey].value,
              IOPSmax = group.root['controls'][IOPSmaxkey].value,
              IOPSburst = group.root['controls'][IOPSburstkey].value;

        if (IOPSmin === 0 || IOPSmax === 0 || IOPSburst === 0) {
          return null;
        } else if ((IOPSmin >= IOPSmax)) {
          return {
            validateMax: {
              valid: false
            }
          };
        } else if (IOPSmax > IOPSburst) {
          return {
            validateBurst: {
              valid: false
            }
          };

        }
      }
      return null;
    };
  }

  isUniqueLUN(aLUN: any) {
    return (c: FormControl): { [key: string]: any } => {
      // console.log(c.value);
      return (c.value < 0 || c.value > 9999) ? {
        invalidLUN: {
          valid: false
        }
      } : ((aLUN.indexOf(c.value) > -1) ? null : {
        duplicateLUN: {
          valid: false
        }
      });
    };
  }

  /**
   * Initialize  Host List Items
   * @namespace xio.VolumeFormComponent
   * @method initHostlistItem
   * @return {void}
   */
  initHostlistItem(name: string, status: boolean, host_id: any, globalID: any, lun_no: number, aLUN: any) {
    return this['fb'].group({
      host: [status, Validators.required],
      label: name,
      host_id : host_id,
      globalID: globalID,
      lun: [lun_no, [this.isUniqueLUN(aLUN)]]
    });
  }

  /**
   * Add Host List Items
   * @namespace xio.VolumeFormComponent
   * @method addHostlistItem
   * @return {void}
   */
  addHostlistItem(name: string, type: string, status: boolean, host_id: any , globalID: any, lun_no: any, aLUN: any) {
    const control = <FormArray>this.storagevolumeForm['controls'][type];
    control.push(this.initHostlistItem(name, status, host_id, globalID, lun_no, aLUN));
  }

  validatepattern(min, max, key) {
    return (group: FormGroup): { [key: string]: any } => {
      if (group.root['controls']['quality_service'].value) {
        let value = group.root['controls'][key].value;
         if ( group.root['controls']['id']['value'] &&
              group.root['controls']['IOPSburst']['value'] === 0 &&
              group.root['controls']['IOPSmax']['value'] === 0 &&
              group.root['controls']['IOPSmin']['value'] === 0) {
              return null;
        }
        value = parseInt(value, 10);
        if (min > value || max < value) {
          return {
            validatepattern: {
              valid: false
            }
          };
        }
      }
      return null;
    };
  }

  isEmpty(obj) {
    return  Object.keys(obj).length === 0;
  }

  /**
   * getMenuContent dirty form values
   * @namespace xio.VolumeFormComponent
   * @method getDirtyValues
   * @return {void}
   */
  getDirtyValues(controlGroup) {
    let dirtyValues = {};
    Object.keys(controlGroup['controls']).forEach((control) => {
      let currentControl = controlGroup['controls'][control];
      if (controlGroup['controls'][control].dirty) {
        dirtyValues[control] = currentControl['controls'] ? this.getDirtyValues(currentControl) : currentControl.value;
      }
    });
    return dirtyValues;
  }

  /**
   * on ISE Discover getMenuContent all ise and sgs data
   * @namespace xio.VolumeFormComponent
   * @param {boolean} t
   * @method chageSelectHostWizard
   * @return {void}
   */
  chageSelectHostWizard(isSelectHostList , hostWizard: boolean) {
    isSelectHostList = hostWizard;
  }




}

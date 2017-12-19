/**
 * Created by Venkatesh on 4/12/2017.
 */
import {Validators, FormControl, FormGroup, FormArray} from '@angular/forms';

export abstract class PoolsUtil {
	    abstract poolform;
      abstract router: any;
      abstract formBuilder: any;


  /**
   * This method is used for checking object empty or not
   */	
  isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }

    /**
   * add Medium Control
   * @namespace xio.PoolsFormComponent
   * @param {Object} dp_obj
   * @method addMedia
   * @return {FormGroup}
   */
  addMedia(dp_obj: any) {
    const control = <FormArray>this.poolform['controls'][dp_obj['type_media']];
    control.push(this.initMedia(dp_obj));
  }

    /**
   * init Medium Control
   * @namespace xio.PoolsFormComponent
   * @param {Object} dp_obj
   * @method initMedia
   * @return {FormGroup}
   */
  initMedia(dp_obj) {
    return this.formBuilder.group({
      dp: [dp_obj['status'], Validators.required],
      label: dp_obj['dp_label'],
      id: dp_obj['media_id'],
      dp_status: dp_obj['dp_status'],
      dp_redundancyhealth: dp_obj['dp_redundancyhealth']
    });
  }

 
 
  /**
   * get Pool Lbl's
   * @namespace xio.PoolsFormComponent
   * @param {number} i
   * @param {any} type_media
   * @param {string} lbl_type
   * @method getPoolLabel
   * @return {String}
   */
  getPoolLabel(i: number, type_media: any, lbl_type: string) {
    const control = <FormArray>this.poolform['controls'][type_media];
    return control.value[i][lbl_type];
  }


}
/**
 * Created by Venkatesh on 4/12/2017.
 */
export abstract class CommonUtil {

  /**
   * This method is used for checking object empty or not
   */
  isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }

  /**
   * Util method to remove duplicates from array
   * @param arrayList
   * @param propertyName
   */
  removeDuplicates(arrayList, propertyName) {
    return arrayList.filter((obj, pos, arr) => {
      return arr.map(mapObj => mapObj[propertyName]).indexOf(obj[propertyName]) === pos;
    });
  }

  /**
   * This method is used for getting only dirty values
   */

  getDirtyValues(controlGroup) {
    let dirtyValues = {};
    Object.keys(controlGroup['controls']).forEach((c) => {
      let currentControl = controlGroup['controls'][c];
      if (currentControl.dirty) {
        if (currentControl['controls']) {
          dirtyValues[c] = this.getDirtyValues(currentControl);
        } else {
          dirtyValues[c] = currentControl.value;
        }
      }
    });
    return dirtyValues;
  }
}

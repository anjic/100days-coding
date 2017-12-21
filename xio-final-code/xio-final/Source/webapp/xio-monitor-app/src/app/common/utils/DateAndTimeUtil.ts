/**
 * Created by Venkatesh on 10/10/2017.
 */

export abstract class DateAndTimeUtil {

  /**
   * Accepts date and format as DD:MMM:YYYY
   * @param date
   * @returns {string}
   */
  getFormattedDate(date) {
    date = new Date(date);
    let dd = date.getDate(),
      months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return (dd < 10 ? '0' + dd : dd) + '-' + months[date.getMonth()] + '-' + date.getFullYear();
  }

  /**
   * Accepts date and format as HH:mm:ss
   * @param date
   * @returns {string}
   */

  getFormattedTime(date) {
    let _data =  new Date(date),
      hh = date.getHours(),
      mm = date.getMinutes(),
      ss = date.getSeconds();

    return (hh < 10 ? '0' + hh : hh) + ':' + (mm < 10 ? '0' + mm : mm) + ':' + (ss < 10 ? '0' + ss : ss);
  }

}

import { XioLogin } from './../po/xio_login.po';
import { Uds_dash } from './../po/uds_dashboard.po';
// import {HtmlReporter} from './HtmlReporter'
describe('XIO monitor sidebar navigation', function(){
    let udsdash: Uds_dash;
    beforeEach(function(){
        udsdash = new Uds_dash();
      });
    /*afterEach(() => {
     // browser.executeScript('window.sessionStorage.clear();');
     // browser.executeScript('window.localStorage.clear();');
  });*/
    
    it('should Click on Dashboard', function(){
        udsdash.uds_dashboard_nav();
    });
  
});
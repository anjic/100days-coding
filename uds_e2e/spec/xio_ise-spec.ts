import { Xio_ise } from './../po/xio_ise.po';
import { XioLogin } from './../po/xio_login.po';

describe('XIO monitor sidebar navigation', function(){
    let ise_sider: Xio_ise;
    beforeEach(() => {
        ise_sider = new Xio_ise();
      });
    /*afterEach(() => {
     // browser.executeScript('window.sessionStorage.clear();');
     // browser.executeScript('window.localStorage.clear();');
  });*/
  
    it('should Click on ISE Management', function(){
        ise_sider.click_ise_sider();
    });
  
});
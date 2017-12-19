import { Xio_san_sider } from './../po/xio_san.po';
import { XioLogin } from './../po/login.po';

describe('XIO monitor SAN sidebar navigation', function(){
    let san_sider: Xio_san_sider;
    beforeEach(() => {
        san_sider = new Xio_san_sider();
      });
    /*afterEach(() => {
     // browser.executeScript('window.sessionStorage.clear();');
     // browser.executeScript('window.localStorage.clear();');
  });*/
  
    it('should Click on SAN groups', function(){
        san_sider.click_san_sider();
    });
  
  });
import { Xio_User_sider } from './../po/xio_user.po';
import { XioLogin } from './../po/login.po';

describe('XIO monitor sidebar navigation', function(){
    let user_sider: Xio_User_sider;
    beforeEach(() => {
      user_sider = new Xio_User_sider();
      });
    /*afterEach(() => {
     // browser.executeScript('window.sessionStorage.clear();');
     // browser.executeScript('window.localStorage.clear();');
  });*/
  
    it('Should click on User Management', function(){
      user_sider.click_user_sider();
    });
  
  });
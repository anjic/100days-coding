import { XioLogin } from './../po/login.po';

let xio = new XioLogin;
//xio.user_login();

describe('XIO monitor App', function(){
    let login: XioLogin;
    
    beforeEach(() => {
      login = new XioLogin();
    });
  
    /*afterEach(() => {
     // browser.executeScript('window.sessionStorage.clear();');
     // browser.executeScript('window.localStorage.clear();');
  });*/
  
    it('XIO login page should Launch', function(){
      login.user_login();
    });
    
  
  });
import { Xio_sidemenu } from './../po/xio_sidebar.po';
import { XioLogin } from './../po/xio_login.po';

describe('XIO monitor sidemenu of san group...', function(){
    let xio_side_san: Xio_sidemenu;
    beforeEach(() => {
        xio_side_san = new Xio_sidemenu(); 
      });
   
  
    it('should Click sidemenu of san group...', function(){
        xio_side_san.click_sidemenu();
    });


    /*it('should Click Storage Tab.....', function(){
      xio_side_san.clickTab();
    });*/
    
  
});
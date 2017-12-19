import{Xio_side_server} from './../po/xio_server.po';
import{XioLogin} from './../po/login.po';

describe("XIO server management",function(){
    let xio_server : Xio_side_server;
    /*beforeEach(() => {
        xio_server = new Xio_side_server();
      });*/

    it('Should Click sidemenu of Server management...', function(){
        xio_server.click_side_server();
    });

});
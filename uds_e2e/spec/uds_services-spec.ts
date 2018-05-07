import { XioLogin } from './../po/xio_login.po';
// import { Uds_dash } from './../po/uds_dashboard.po';
import{UDSservices} from './../po/uds_services.po';


describe("UDS Service page",function(){
    let udsserives : UDSservices;

    beforeEach(() =>{
        udsserives = new UDSservices();
    });

    it('UDS service window should open',function(){
        udsserives.uds_service();

    });

    it('UDS service should create',function(){
        udsserives.new_uds_service();
    });



});
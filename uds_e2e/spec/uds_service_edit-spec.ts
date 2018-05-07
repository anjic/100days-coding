import { XioLogin } from './../po/xio_login.po';
import {UDSservices} from './../po/uds_services.po';
import{UDS_Service_edit} from './../po/uds_service_edit.po';

describe("UDS Service Edit",function(){
    let udsserivesedit : UDS_Service_edit;
    //let udsservice : UDSservices

    beforeEach(()=>{
        udsserivesedit = new UDS_Service_edit();
       // udsservice = new UDSservices();
    })

    it('UDS service edit page open',function(){
        //udsservice.uds_service();
        udsserivesedit.udsservice_edit();

    });
});
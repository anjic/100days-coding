import { OvirtEngine } from '../po/ovirt.po';

// console.log("####################################");

describe('Ovirt-engine Test with Protractor',function(){
    let ovirt;

    beforeEach(()=> {
        ovirt = new OvirtEngine();
    });

    it('UDS service window should open',function(){
        ovirt.ovirt_home();
    
    });


});
import { browser, element, by } from 'protractor';

browser.driver.manage().window().maximize();
console.log("####################################");

export default class OvirtEngine {
    constructor() {
        this.navigateTo();
    }
    navigateTo(){
        browser.get('https://udstest.udsdomain.com/ovirt-engine/')
    }

    ovirt_home() {
        expect(browser.getTitle()).toEqual('oVirt Engine');
        console.log('********************************')
        console.log(browser.getTitle())
        console.log('********************************')
        const adminportal = element(by.id("WelcomePage_webadmin"));
        browser.sleep(2000);
        adminportal.click();

    }

}
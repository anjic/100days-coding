import{browser, element, by } from 'protractor';

export class UDSservices{
    uds_service(){
        const over_service = element(by.xpath("//li[2]/*[@class='lnk-service_providers']"));
        
        over_service.click();
        browser.sleep(1000);    
        // browser.actions().mouseMove(over_service).click().perform();
        over_service.click();
        //browser.sleep(2000);

        const close_btn = element(by.xpath("//div/button[@class='close']"));
        close_btn.click();
        browser.sleep(2000);

        const new_btn = element(by.xpath("//div/button/span[@class='label-tbl-button' and text()='New']"));
        new_btn.click();
        browser.sleep(2000);

        const ovirt = element(by.xpath("//li/a[@data-type='oVirtPlatform']"));
        ovirt.click();
        // const service = element(by.css("a.lnk-service_providers"));
        // service.click();
        browser.sleep(2000);

    }
    new_uds_service(){

        const name = element(by.id("name_field"));
        name.clear();
        name.click();
        name.sendKeys("Protractor1");
        browser.sleep(1000);

        const comment = element(by.id("comments_field"));
        comment.clear();
        comment.click();
        comment.sendKeys("Portractor testing");
        browser.sleep(1000);

        const ovirt_ver= element(by.xpath("//select[@name='ovirtVersion']/option[@value='4']"));
        ovirt_ver.click();
        browser.sleep(1000);

        const ovirt_host = element(by.id("host_field"));
        ovirt_host.click();
        ovirt_host.clear();
        ovirt_host.sendKeys("172.30.56.72");
        browser.sleep(1000);

        const ovirt_user = element(by.id("username_field"));
        ovirt_user.click();
        ovirt_user.clear();
        ovirt_user.sendKeys("admin@internal");
        browser.sleep(1000);

        const ovirt_pwd = element(by.id("password_field"));
        ovirt_pwd.click();
        ovirt_pwd.clear();
        ovirt_pwd.sendKeys("ovirt123");
        browser.sleep(1000);

        const ovirt_test = element(by.css(".pull-left.btn.btn-info"));
        ovirt_test.click();
        browser.sleep(2000);

        const ovirt_test_ok = element(by.xpath("//button[@class='btn btn-default' and text()='Ok'] "));
        ovirt_test_ok.click();
        browser.sleep(2000);
        
        const ovirt_save = element(by.css(".btn.btn-primary.button-accept"));
        ovirt_save.click();
        browser.sleep(2000);

        // const ovirt_close = element(by.css(".btn.btn-default"));
        // ovirt_close.click();
        // browser.sleep(2000);



    }
}
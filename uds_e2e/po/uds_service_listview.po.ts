import{browser,element,by} from'protractor';

export class UDSserviceList{
    uds_service_list(){
        const over_service = element(by.xpath("//li[2]/*[@class='lnk-service_providers']"));
        
        over_service.click();
        browser.sleep(1000);    
        // browser.actions().mouseMove(over_service).click().perform();
        over_service.click();
        //browser.sleep(2000);

        const close_btn = element(by.xpath("//div/button[@class='close']"));
        close_btn.click();
        browser.sleep(2000);
    };


};
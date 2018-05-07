import{ element,browser,by} from 'protractor';

export class UDS_Service_edit{
    udsservice_edit(){
        const service = element(by.xpath("//tr[@class='row-maintenance-false even']/td[1]"));
        service.click();
        browser.sleep(1000);

        // const service_edit = element(by.xpath("//button[@class='btn btn-action btn-tables']/span[@class='label-tbl-button' and text()='Edit']"));
        // service_edit.click();
        // browser.sleep(1000);
    }
};
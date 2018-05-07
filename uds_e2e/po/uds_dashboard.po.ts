import { browser, element, by } from 'protractor';

export class Uds_dash{
    uds_dashboard_nav() {

        const admin = element(by.xpath("//*[@class='dropdown'][2]"))
        const dashboard=element(by.xpath("//*[@href='/adm/']"));
        admin.click();
        // browser.sleep(1000);
        dashboard.click();
        // browser.sleep(2000);

    }
    
}
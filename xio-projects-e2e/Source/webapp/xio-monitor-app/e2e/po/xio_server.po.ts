import{ ElementFinder, browser, by, element} from 'protractor';
import { XioLogin } from './../po/login.po';

export class Xio_side_server{

    click_side_server(){

        const server_mgmt= element(by.xpath("//a[@id='userId-2']"));
        server_mgmt.click();
        browser.sleep(2000);


        const server_btn = element(by.xpath("//button[@class='toolbar-btn mat-raised-button']"));
        server_btn.click();
        browser.sleep(2000);

        const server_name = element(by.xpath("//input[@placeholder='Server Name']"));
        server_name.click();
        //console.log(server_name.getText);
        server_name.sendKeys("Test_server");
        browser.sleep(2000);

        const server_cmnt = element(by.xpath("//textarea[@placeholder='Comment']"));
        server_cmnt.click();
        server_cmnt.sendKeys("Test server comment");
        browser.sleep(2000);


    }

}
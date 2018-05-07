import { ElementFinder, browser, by, element } from 'protractor';


export class Xio_User_sider{

    click_user_sider() {
        //var ise_sider= element(by.xpath("//@id='userId'[2]"));
        //var ise_sider= element(by.xpath("//div[contains(text(),'SAN Groups')]"));
        //var ise_sider= element(by.css("a#userId[2]"));
        var user_sidebar= element(by.xpath("//a[@id='userId-0']"));
         //input[@id='email']
         user_sidebar.click();
        browser.sleep(2000);

    }

}

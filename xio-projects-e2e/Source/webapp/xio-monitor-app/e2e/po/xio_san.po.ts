import { ElementFinder, browser, by, element } from 'protractor';


export class Xio_san_sider{

    click_san_sider() {
        //var ise_sider= element(by.xpath("//@id='userId'[2]"));
        //var ise_sider= element(by.xpath("//div[contains(text(),'SAN Groups')]"));
        //var ise_sider= element(by.css("a#userId[2]"));
        const san_sidebar= element(by.xpath("//a[@id='userId-3']"));
         //input[@id='email']

        san_sidebar.click();
        //browser.sleep(2000);

    }

}


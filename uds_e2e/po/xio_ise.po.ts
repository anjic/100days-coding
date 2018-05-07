import { ElementFinder, browser, by, element } from 'protractor';


export class Xio_ise{

    click_ise_sider() {
        //var ise_sider= element(by.xpath("//@id='userId'[2]"));
        //var ise_sider= element(by.xpath("//div[contains(text(),'SAN Groups')]"));
        //var ise_sider= element(by.css("a#userId[2]"));
        const ise_sidebar= element(by.xpath("//a[@id='userId-1']"));
         //input[@id='email']
        ise_sidebar.click();
        //browser.sleep(2000);
        //using ID of the element
        const ise_add=element(by.css("button#add_ise"));
        ise_add.click();
        //browser.sleep(2000);
        //Using attribute of the element
        const ise_ip=element(by.css("input[placeholder='IP']"));
        ise_ip.click();
        ise_ip.sendKeys("10.20.238.4")
        //browser.sleep(2000);
        //using 'formcontrolname' attribute as element
        const ise_user=element(by.css("input[formcontrolname='user_name']"));
        ise_user.clear();
        ise_user.sendKeys("administrator");
        //browser.sleep(2000);
        const ise_pwd=element(by.css("input[formcontrolname='user_password']"));
        ise_pwd.clear();
        ise_pwd.sendKeys("administrator");
        //browser.sleep(2000);
        const ise_btn=element(by.css("button[type='submit']"));
        ise_btn.click();
        //browser.sleep(2000);
        //using id="name"
        const name=element(by.css("input#name"));
        name.clear();
        name.sendKeys("Msys Tech Pvt Ltd");
        //browser.sleep(2000);
        //using 'input-prefered_ise' as id
        const pre_ise=element(by.css("#input-prefered_ise"))
        name.click();
        //browser.sleep(2000);
        //sending SAN name
        const san_name=element(by.css("input[formcontrolname='sangroup_name']"));
        san_name.click();
        san_name.sendKeys("Msys");
        //browser.sleep(2000);
        //Click save button
        const btn_save=element(by.css("button[type='submit']"));
        btn_save.click();
        //browser.sleep(2000);
    }

}

import { browser, element, by } from 'protractor';

export class XioLogin {

  constructor() {
        this.navigateTo();
    }
    
  navigateTo() {
    return browser.get('http://localhost:4200/');
  }

  user_login() {
    const user = element(by.xpath("//input[@placeholder='Username']"));
    const pwd = element(by.xpath("//input[@placeholder='Password']"));
    const login = element(by.css(".btn.btn-sm"));
    //user
    user.click();
    user.clear();
    user.sendKeys("Administrator");
    //browser.sleep(2000);
    //password
    pwd.click();
    pwd.clear();
    pwd.sendKeys("made4you");
    //login
    //browser.sleep(2000);
    login.click();
    //browser.sleep(2000);
    
  }
 

}

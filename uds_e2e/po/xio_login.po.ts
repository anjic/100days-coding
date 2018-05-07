import { browser, element, by } from 'protractor';

browser.driver.manage().window().maximize();

export class XioLogin {

  constructor() {
        this.navigateTo();
    }
    
  navigateTo() {
    return browser.get('https://172.30.36.110');
   
  }

  user_login() {
    //expect(browser.getTitle()).toEqual('Welcome to UDS');
    expect(browser.getTitle()).toEqual("Welcome to UDS");
   
    const user = element(by.id("id_user"));
    const pwd = element(by.id("id_password"));
    
    const login = element(by.xpath("//button[@type='submit']"));
    // //user
    user.click();
    //user.clear();
    user.sendKeys("admin");
    //browser.sleep(2000);
    // //password
    pwd.click();
    //pwd.clear();
    pwd.sendKeys("udsmam0");
    // //login
    //browser.sleep(2000);
     login.click();
    //browser.sleep(5000);
    
  }
 

}
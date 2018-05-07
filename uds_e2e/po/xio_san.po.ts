import { ElementFinder, browser, by, element } from 'protractor';
import { ElementRef } from '@angular/core/src/linker/element_ref';


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
/*
    create_san_group(){
        //const create_btn=element(by.css("button .mat-button-wrapper"));
        const create_san_btn=element(by.buttonText("Create SAN Group"));
        create_san_btn.click();
        //browser.sleep(3000);
        const san_name=element(by.xpath("//input[@placeholder='SAN Group Name']"));
        san_name.click();
        san_name.sendKeys("SAN grop1");
        //browser.sleep(3000);

        const san_comment = element(by.xpath("//input[@placeholder='SAN Group Comment']"));
        san_comment.click();
        san_comment.sendKeys("Create by protractor");
        //browser.sleep(3000);

        const create_btn =element(by.buttonText("Create"));
        create_btn.click();
    
    }*/

    edit_san_group(){

        const menu_btn = element(by.xpath("//button/span/md-icon[@class='mat-icon material-icons']"));
        //console.log("edit_btn", edit_btn);
        menu_btn.getText().then((data) => {

            console.log("#################",data);
            menu_btn.click();
            browser.sleep(3000);

            //EDIT san group
            const edit_btn = element(by.xpath("//xio-md-row-edit/section[1]"));
            edit_btn.getText().then((r)=>{
                console.log("%%%%%%%%%%%%%%%",r);
                edit_btn.click();

                const edit_san_name = element(by.xpath("//input[@formcontrolname='sangroup_name']"));
                edit_san_name.click();
                edit_san_name.clear();
                edit_san_name.sendKeys("SAN edit");
                browser.sleep(2000);

                const edit_san_comment = element(by.xpath("//input[@formcontrolname='sangroup_name']"));
                edit_san_comment.click();
                edit_san_comment.clear();
                edit_san_comment.sendKeys("SAN edited from protractor");
                browser.sleep(2000);

                const update_btn = element(by.buttonText("Update"));
                edit_san_comment.click();
                browser.sleep(2000);
            });

            /*if ( data == 'more_vert') {
                console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                edit_btn.click();
                browser.sleep(3000);
            }*/
        });               

    }

}
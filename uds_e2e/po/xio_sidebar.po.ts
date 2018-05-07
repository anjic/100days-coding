import { ElementFinder, protractor, browser, by, element } from 'protractor';

export class Xio_sidemenu {

    click_sidemenu() {

        const san_side_inner = element(by.css("xio-sidebar div.pd-san"));

        san_side_inner.isPresent().then((r) => {
            console.log(r)
            if (r) {
                console.log("####################### " + r);

                san_side_inner.click().then(function () {
                    browser.sleep(3000);
                    const side_ise = element(by.css("md-nav-list div ise-list-sidebar mat-nav-list"));
                    side_ise.isPresent().then(x=>{
                        if(x){
                            console.log("@@@@@@@@@@@@@@@@@@@@@"+x);
                        }
                        
                    })
                    
                    const ise_side = element(by.css("mat-card .san-dashboard-ise-cards-operational"));
                    ise_side.isPresent().then(r => {
                        console.log("CLICK SAN ISE card INFO........."+r);
                        browser.sleep(3000);
                        if (r) {
                            ise_side.click().then(() => {
                                browser.sleep(3000);
                                console.log("$$$$$$$$$$$$$$$$$$$ "+r);

                                return true;
                            });

                        }
                    });

                });
            }
        });

    }

    /*
    clickTab(){
        var vol = element(by.css("app-ise-landing mat-tab-labels .mat-tab-label"));
        
        // vol.count().then(n => {
        //     console.log(n);
        // });
        vol.isPresent().then((x) => {
            console.log("//////////////////" + x);
            vol.click();
        });
    }*/
}
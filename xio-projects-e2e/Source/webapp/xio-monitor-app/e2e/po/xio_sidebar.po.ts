import { ElementFinder, protractor, browser, by, element } from 'protractor';


export class Xio_sidemenu {

    click_sidemenu() {

        const san_side_inner = element(by.css("xio-sidebar div.pd-san"));

        san_side_inner.isPresent().then((r) => {
            console.log(r)
            if (r) {
                console.log("####################### " + r);
                san_side_inner.click().then(function () {
                    
                    const ise_side = element(by.css("mat-card .san-dashboard-ise-cards-operational"));
                    ise_side.isPresent().then(r => {
                        console.log("CLICK SAN ISE card INFO........."+r);
                        if (r) {
                            ise_side.click().then(() => {
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
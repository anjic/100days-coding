export interface Powersupply {
		   
    status : {
	    _attr : {
	        string : string;
	        value : string;
	    };
	    details : {
	        _attr : {
	            value : string;
	        };
	        detail : string;
	    };
    };
    model : string;
    serialnumber : string;
    led : {
        _attr : {
            string : string;
            value : string;
        };
        led : string;
    };
    temperature : {
        low : number;
        scale : string;
        warning : number;
        critical : number;
        _attr : {
            value : string;
        };
    };
    _attr : {
        self : string;
    };
    fans : string;
    manufacturingdate : string;
    position : number;
    partnumber : string;
    hwversion : string;
    id : number;

}
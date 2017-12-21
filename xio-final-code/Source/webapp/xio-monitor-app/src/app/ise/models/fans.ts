export interface Fan {
	 
    status : {
        status : string;
        _attr : {
            string : string;
            value : string;
        };
    };
    rpm : number;
     _attr : {
         self : string;
    };
    led : {
        _attr : {
            string : string;
            value : string;
        };
        led : string;
    };
    id : number;
}
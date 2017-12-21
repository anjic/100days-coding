export interface Datapac {

		status: {
			_attr: {
			    string: string;
			    value: string;
			};
			details: {
			    _attr: {
			        value: string;
			    };
			    detail: string;
			};
		};
		model: string;
		serialnumber: string;
		led: {
		    _attr: {
		        string: string;
		        value: string;
		    };
		    led: string;
		};
		temperature: {
		     low : number;
		     scale : string;
		     warning : number;
		     critical : number;
		     _attr : {
		         peak : string;
		         value : string;
		    };
		};
		 capacity : number;
		 _attr : {
		     self : string;
		};
		 taskstatus : {
		     progress : number;
		     _attr : {
		         string : string;
		         value : string;
		    };
		     type : string;
		};
		 fwversion : string;
		 manufacturingdate : string;
		 health : {
		     warning : number;
		     critical : number;
		     _attr : {
		         value : string;
		    };
		};
		 tier : {
		     tier : string;
		     _attr : {
		         string : string;
		         value : string;
		    };
		};
		 position : number;
		 partnumber : string;
		 sparelevel : number;
		 hwversion : string;
		 id : number;
		 pool : {
		     _attr : {
		         self : string;
		    };
		     globalid : string;
		};
		 redundancyhealth : {
		     healthstring : string;
		     _attr : {
		         value : string;
		    };
		     inselfhealing : string;
		};
}


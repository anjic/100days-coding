export interface Controller {
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

    fcports : {
         fcports : [
            {
                 status : {
                     status : string;
                     _attr : {
                         string : string;
                         value : string;
                    };
                };
                 bytesreceived : number;
                 lipcount : number;
                 speedsetting : number;
                 type : {
                     _attr : {
                         string : string;
                         value : string;
                    };
                     type : string;
                };
                 _attr : {
                     self : string;
                };
                 noscount : number;
                 bytestransmitted : number;
                 wwn : string;
                 speed : number;
                 id : number;
                 editFlag:boolean;
            }
        ];
         _attr : {
             self : string;
        };
    };

    _attr : {
         self : string;
    };
    
    rank : {
         _attr : {
             string : string;
             value : string;
        };
         rank : string;
    };
    
    taskstatus : {
         progress : number;
         _attr : {
             string : string;
             value : string;
        };
         type : string;
    };
    
    sfps : {
        sfps : [
            {
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
                 serialnumber : string;
                 hectxfault :string;
                 _attr : {
                     self : string;
                };
                 numlosevents :number;
                 hecportsignalloss : string;
                 manufacturingdate : string;
                 partnumber : string;
                 hwversion : string;
                 id : number;
                 numtxfltevents : number;
            }
        ];
        
        _attr : {
             self : string;
        };
    };
     
    fwversion : string;
    manufacturingdate : string;
    position : number;
    partnumber : string;
    hwversion :string;
    id : number;
}
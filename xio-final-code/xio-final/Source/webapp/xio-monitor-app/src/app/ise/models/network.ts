export interface Network {
	dhcp : {
		dhcp : string;
		_attr : {
		     string : string;
		     value : string;
		};
	};
	 _attr : {
	    self : string;
	};
	 wakeonlan : {
	    _attr : {
	        string : string;
	        value : string;
	    };
	    wakeonlan : string;
	};
	 dns : {
	    nameservers : [string];
	    domainserver : string;
	};
	ports : {
	    _attr : {
	        self :string;
	    };
	    ports : [
	        {
	            macaddress : string;
	            linkstatus : string;
	            _attr : {
	                self : string;
	            };
	            dnsname : string;
	            ipmask : string;
	            ipaddress : string;
	            gateway : string;
	        }
	    ];
	    port : {
	            macaddress : string;
	            linkstatus : string;
	            _attr : {
	                self : string;
	            };
	            dnsname : string;
	            ipmask : string;
	            ipaddress : string;
	            gateway : string;
	        };
	}	
}
export interface TimeSettings {
    'chronometer': {
        'uptime': {
            'hours': number;
            'seconds': number;
            '_attr': {
                'duration': string
            };
            'minutes': number;
            'days': number
        };
        'scale': string;
        'ntp': {
            'ntpmode': string;
            'ntpserver': string 
        };
        'dst': string;
        '_attr': {
            'self': string
        };
        'time': string;
        'date': string;
        'timezone': string;
        'timezonesetting': string;
    };

}
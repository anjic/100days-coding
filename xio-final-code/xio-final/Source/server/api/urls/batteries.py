from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.batteries import(BatteryList)
"""
@apiGroup Batteries
@apiName GetBatteriesInfo
@api {get} /ise/<ise-id>/batteries/ Display Batteries Info
@apiParam {Number} ise-id unique ISEID.

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for Batteries
@apiSuccess {String} message It gives success or error message of the Batteries
@apiSuccess {String} error It contains error message 

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504349744",
        "total": "1.11s",
        "cortex": "1.11s",
        "res_send_time": "1504349745"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "batteries": {
                    "batteries": [
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational",
                                    "value": "0"
                                },
                                "details": {
                                    "_attr": {
                                        "value": "0x00000000"
                                    },
                                    "detail": "None"
                                }
                            },
                            "serialnumber": "SN_EMU",
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
                            "temperature": {
                                "scale": "celsius",
                                "warning": 50,
                                "critical": 60,
                                "_attr": {
                                    "value": "40"
                                }
                            },
                            "partnumber": "PN_EMU",
                            "calibration": {
                                "status": {
                                    "status": "",
                                    "_attr": {
                                        "string": "Undefined",
                                        "value": "15"
                                    }
                                },
                                "windowstartday": 0,
                                "lastcaldate": "Unknown",
                                "capacity": 0,
                                "interval": 0,
                                "delay": 0,
                                "time": 0,
                                "date": 0,
                                "windowendhour": 0,
                                "cycles": 0,
                                "windowstarthour": 0,
                                "windowendday": 0
                            },
                            "charger": {
                                "status": {
                                    "_attr": {
                                        "string": "Unknown",
                                        "value": "6"
                                    },
                                    "details": "Unknown"
                                },
                                "charge": {
                                    "mvolts": 0,
                                    "rawmaxcapacity": 0,
                                    "remaining": 0,
                                    "rawremaining": 0,
                                    "maxcapacity": 0
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/batteries/1"
                            },
                            "upsmode": {
                                "_attr": {
                                    "string": "enabled",
                                    "value": "0"
                                },
                                "upsmode": ""
                            },
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "voltage": {
                                "scale": "mV",
                                "_attr": {
                                    "value": "3789"
                                }
                            },
                            "minholduptime": 0,
                            "position": 1,
                            "model": "",
                            "type": "Super Capacitor",
                            "id": 1,
                            "hwversion": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational",
                                    "value": "0"
                                },
                                "details": {
                                    "_attr": {
                                        "value": "0x00000000"
                                    },
                                    "detail": "None"
                                }
                            },
                            "serialnumber": "SN_EMU",
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
                            "temperature": {
                                "scale": "celsius",
                                "warning": 50,
                                "critical": 60,
                                "_attr": {
                                    "value": "40"
                                }
                            },
                            "partnumber": "PN_EMU",
                            "calibration": {
                                "status": {
                                    "status": "",
                                    "_attr": {
                                        "string": "Undefined",
                                        "value": "15"
                                    }
                                },
                                "windowstartday": 0,
                                "lastcaldate": "Unknown",
                                "capacity": 0,
                                "interval": 0,
                                "delay": 0,
                                "time": 0,
                                "date": 0,
                                "windowendhour": 0,
                                "cycles": 0,
                                "windowstarthour": 0,
                                "windowendday": 0
                            },
                            "charger": {
                                "status": {
                                    "_attr": {
                                        "string": "Unknown",
                                        "value": "6"
                                    },
                                    "details": "Unknown"
                                },
                                "charge": {
                                    "mvolts": 0,
                                    "rawmaxcapacity": 0,
                                    "remaining": 0,
                                    "rawremaining": 0,
                                    "maxcapacity": 0
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/batteries/2"
                            },
                            "upsmode": {
                                "_attr": {
                                    "string": "enabled",
                                    "value": "0"
                                },
                                "upsmode": ""
                            },
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "voltage": {
                                "scale": "mV",
                                "_attr": {
                                    "value": "3789"
                                }
                            },
                            "minholduptime": 0,
                            "position": 2,
                            "model": "",
                            "type": "Super Capacitor",
                            "id": 2,
                            "hwversion": ""
                        }
                    ],
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/batteries"
                    }
                }
            }
        },
        "error": false
    }
}
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "",
        "req_recv_time": "",
        "total": "",
        "cortex": "",
        "res_send_time": ""
    },
    "result": {
        "status_code": 404,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 404,
            "message": "ISE Not Found"
        }
    }
}
"""
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/batteries/$', BatteryList.as_view()),
    # url(r'^(?P<batteryid>[\w\-]+)/$', BatteryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

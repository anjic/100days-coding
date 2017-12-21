from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.controllers import(ControllersList, ControllersDetail, FcportsDetails, FcportsList)

"""
@apiGroup Controllers
@apiName GetControllersInfo
@api {get} /ise/<ise-id>/controllers/ Display ControllersInfo

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting controllers

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504359888",
        "total": "1.39s",
        "cortex": "1.38s",
        "res_send_time": "1504359889"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "controllers": {
                    "controllers": [
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
                            "model": "",
                            "serialnumber": "MXE3400065NDA132",
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
                            "temperature": {
                                "low": 10,
                                "scale": "celsius",
                                "warning": 77,
                                "critical": 87,
                                "_attr": {
                                    "value": "58"
                                }
                            },
                            "fcports": {
                                "fcports": [
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/1"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300110",
                                        "speed": 8,
                                        "id": 1
                                    },
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/2"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300111",
                                        "speed": 8,
                                        "id": 2
                                    },
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/3"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300112",
                                        "speed": 8,
                                        "id": 3
                                    },
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/4"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300113",
                                        "speed": 8,
                                        "id": 4
                                    }
                                ],
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers/1"
                            },
                            "rank": {
                                "_attr": {
                                    "string": "Primary",
                                    "value": "1"
                                },
                                "rank": ""
                            },
                            "taskstatus": {
                                "progress": -1,
                                "_attr": {
                                    "string": "None",
                                    "value": "-1"
                                },
                                "type": "None"
                            },
                            "sfps": {
                                "sfps": [
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
                                        "serialnumber": "SZG",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/1"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SZG",
                                        "hwversion": "A   SZG",
                                        "id": 1,
                                        "numtxfltevents": 0
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
                                        "serialnumber": "SZ5",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/2"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SZ5",
                                        "hwversion": "A   SZ5",
                                        "id": 2,
                                        "numtxfltevents": 0
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
                                        "serialnumber": "T1D",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/3"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   T1D",
                                        "hwversion": "A   T1D",
                                        "id": 3,
                                        "numtxfltevents": 0
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
                                        "serialnumber": "SZ9",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/4"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SZ9",
                                        "hwversion": "A   SZ9",
                                        "id": 4,
                                        "numtxfltevents": 0
                                    }
                                ],
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps"
                                }
                            },
                            "fwversion": "v4.0.0-7162",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "position": 1,
                            "partnumber": "NEWI-01-A9954989Thu Jan  1 00:00:00 1970",
                            "hwversion": "",
                            "id": 1
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
                            "model": "",
                            "serialnumber": "MXE3400065NDA14F",
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
                            "temperature": {
                                "low": 10,
                                "scale": "celsius",
                                "warning": 77,
                                "critical": 87,
                                "_attr": {
                                    "value": "53"
                                }
                            },
                            "fcports": {
                                "fcports": [
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/5"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300114",
                                        "speed": 8,
                                        "id": 5
                                    },
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/6"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300115",
                                        "speed": 8,
                                        "id": 6
                                    },
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/7"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300116",
                                        "speed": 8,
                                        "id": 7
                                    },
                                    {
                                        "status": {
                                            "status": "",
                                            "_attr": {
                                                "string": "Operational",
                                                "value": "0"
                                            }
                                        },
                                        "bytesreceived": 0,
                                        "lipcount": 0,
                                        "speedsetting": 0,
                                        "type": {
                                            "_attr": {
                                                "string": "N Port",
                                                "value": "10"
                                            },
                                            "type": ""
                                        },
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/8"
                                        },
                                        "noscount": 0,
                                        "bytestransmitted": 0,
                                        "wwn": "2000001F93300117",
                                        "speed": 8,
                                        "id": 8
                                    }
                                ],
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers/2"
                            },
                            "rank": {
                                "_attr": {
                                    "string": "Secondary",
                                    "value": "0"
                                },
                                "rank": ""
                            },
                            "taskstatus": {
                                "progress": -1,
                                "_attr": {
                                    "string": "None",
                                    "value": "-1"
                                },
                                "type": "None"
                            },
                            "sfps": {
                                "sfps": [
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
                                        "serialnumber": "SX5",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/5"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SX5",
                                        "hwversion": "A   SX5",
                                        "id": 5,
                                        "numtxfltevents": 0
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
                                        "serialnumber": "SWW",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/6"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SWW",
                                        "hwversion": "A   SWW",
                                        "id": 6,
                                        "numtxfltevents": 0
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
                                        "serialnumber": "SZ0",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/7"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SZ0",
                                        "hwversion": "A   SZ0",
                                        "id": 7,
                                        "numtxfltevents": 0
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
                                        "serialnumber": "SYA",
                                        "hectxfault": "value=\"0\" string=\"false\"",
                                        "_attr": {
                                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/8"
                                        },
                                        "numlosevents": 0,
                                        "hecportsignalloss": "value=\"0\" string=\"false\"",
                                        "manufacturingdate": "",
                                        "partnumber": "FTE8508N1LCN    A   SYA",
                                        "hwversion": "A   SYA",
                                        "id": 8,
                                        "numtxfltevents": 0
                                    }
                                ],
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps"
                                }
                            },
                            "fwversion": "v4.0.0-7162",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "position": 2,
                            "partnumber": "NEWI-01-A9954989Thu Jan  1 00:00:00 1970",
                            "hwversion": "",
                            "id": 2
                        }
                    ],
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers"
                    }
                }
            }
        },
        "error": false
    }
}

@apiError ISENotFound The particular ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

@apiErrorExample {JSON} Error-Response:
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

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 401 Unauthorized
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1505988917",
        "total": "1.08s",
        "cortex": "1.03s",
        "res_send_time": "1505988918"
    },
    "result": {
        "status_code": 401,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 401,
            "message": "401 Unauthorized"
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 504 Gateway Timeout
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
        "status_code": 504,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 504,
            "message": "ConnectionError, Retry.."
        }
    }
}
"""
"""
@apiGroup Controllers
@apiName GetParticularControllersInfo
@api {get} /ise/<ise-id>/controllers/<controller-id> Display ParticularController

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} controller-id unique Controller ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting particulardriveinfo

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504360036",
        "total": "1.15s",
        "cortex": "1.14s",
        "res_send_time": "1504360037"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "controllers": {
                    "controller": {
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
                        "model": "",
                        "serialnumber": "MXE3400065NDA132",
                        "led": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "led": ""
                        },
                        "temperature": {
                            "low": 10,
                            "scale": "celsius",
                            "warning": 77,
                            "critical": 87,
                            "_attr": {
                                "value": "59"
                            }
                        },
                        "fcports": {
                            "fcports": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "bytesreceived": 0,
                                    "lipcount": 0,
                                    "speedsetting": 0,
                                    "type": {
                                        "_attr": {
                                            "string": "N Port",
                                            "value": "10"
                                        },
                                        "type": ""
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/1"
                                    },
                                    "noscount": 0,
                                    "bytestransmitted": 0,
                                    "wwn": "2000001F93300110",
                                    "speed": 8,
                                    "id": 1
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "bytesreceived": 0,
                                    "lipcount": 0,
                                    "speedsetting": 0,
                                    "type": {
                                        "_attr": {
                                            "string": "N Port",
                                            "value": "10"
                                        },
                                        "type": ""
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/2"
                                    },
                                    "noscount": 0,
                                    "bytestransmitted": 0,
                                    "wwn": "2000001F93300111",
                                    "speed": 8,
                                    "id": 2
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "bytesreceived": 0,
                                    "lipcount": 0,
                                    "speedsetting": 0,
                                    "type": {
                                        "_attr": {
                                            "string": "N Port",
                                            "value": "10"
                                        },
                                        "type": ""
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/3"
                                    },
                                    "noscount": 0,
                                    "bytestransmitted": 0,
                                    "wwn": "2000001F93300112",
                                    "speed": 8,
                                    "id": 3
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "bytesreceived": 0,
                                    "lipcount": 0,
                                    "speedsetting": 0,
                                    "type": {
                                        "_attr": {
                                            "string": "N Port",
                                            "value": "10"
                                        },
                                        "type": ""
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports/4"
                                    },
                                    "noscount": 0,
                                    "bytestransmitted": 0,
                                    "wwn": "2000001F93300113",
                                    "speed": 8,
                                    "id": 4
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fcports"
                            }
                        },
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers/1"
                        },
                        "rank": {
                            "_attr": {
                                "string": "Primary",
                                "value": "1"
                            },
                            "rank": ""
                        },
                        "taskstatus": {
                            "progress": -1,
                            "_attr": {
                                "string": "None",
                                "value": "-1"
                            },
                            "type": "None"
                        },
                        "sfps": {
                            "sfps": [
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
                                    "serialnumber": "SZG",
                                    "hectxfault": "value=\"0\" string=\"false\"",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/1"
                                    },
                                    "numlosevents": 0,
                                    "hecportsignalloss": "value=\"0\" string=\"false\"",
                                    "manufacturingdate": "",
                                    "partnumber": "FTE8508N1LCN    A   SZG",
                                    "hwversion": "A   SZG",
                                    "id": 1,
                                    "numtxfltevents": 0
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
                                    "serialnumber": "SZ5",
                                    "hectxfault": "value=\"0\" string=\"false\"",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/2"
                                    },
                                    "numlosevents": 0,
                                    "hecportsignalloss": "value=\"0\" string=\"false\"",
                                    "manufacturingdate": "",
                                    "partnumber": "FTE8508N1LCN    A   SZ5",
                                    "hwversion": "A   SZ5",
                                    "id": 2,
                                    "numtxfltevents": 0
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
                                    "serialnumber": "T1D",
                                    "hectxfault": "value=\"0\" string=\"false\"",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/3"
                                    },
                                    "numlosevents": 0,
                                    "hecportsignalloss": "value=\"0\" string=\"false\"",
                                    "manufacturingdate": "",
                                    "partnumber": "FTE8508N1LCN    A   T1D",
                                    "hwversion": "A   T1D",
                                    "id": 3,
                                    "numtxfltevents": 0
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
                                    "serialnumber": "SZ9",
                                    "hectxfault": "value=\"0\" string=\"false\"",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps/4"
                                    },
                                    "numlosevents": 0,
                                    "hecportsignalloss": "value=\"0\" string=\"false\"",
                                    "manufacturingdate": "",
                                    "partnumber": "FTE8508N1LCN    A   SZ9",
                                    "hwversion": "A   SZ9",
                                    "id": 4,
                                    "numtxfltevents": 0
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/sfps"
                            }
                        },
                        "fwversion": "v4.0.0-7162",
                        "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                        "position": 1,
                        "partnumber": "NEWI-01-A9954989Thu Jan  1 00:00:00 1970",
                        "hwversion": "",
                        "id": 1
                    },
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers"
                    }
                }
            }
        },
        "error": false
    }
}

@apiError ControllerNotFound/IseNotFound The particular Controller/ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1506077012",
        "total": "1.12s",
        "cortex": "1.07s",
        "res_send_time": "1506077014"
    },
    "result": {
        "status_code": 404,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 404,
            "message": "Requested Controller not found."
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 401 Unauthorized
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1505988917",
        "total": "1.08s",
        "cortex": "1.03s",
        "res_send_time": "1505988918"
    },
    "result": {
        "status_code": 401,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 401,
            "message": "401 Unauthorized"
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 504 Gateway Timeout
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
        "status_code": 504,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 504,
            "message": "ConnectionError, Retry.."
        }
    }
}
"""
"""
@apiGroup Controllers
@apiName UpdateControllerDetail

@api {put} /ise/<ise-id>/controllers/<controller-id> Update Controller Details

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} controller-id unique Controller ID
@apiParam {String} led Enable/Disable LED

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {json} Input
{
	"led":"enabled"
}

@apiSuccessExample Success-Response:
HTTP/1.1 201 Created
{
    "message": "success",
    "time_taken": {
        "python": "",
        "req_recv_time": "",
        "total": "",
        "cortex": "",
        "res_send_time": ""
    },
    "result": {
        "status_code": 201,
        "response": {
            "data": "Controller 1 Activity LED has been enabled"
        },
        "error": false
    }
}
@apiErrorExample {JSON} Error-Response:
HTTP/1.1 400 Bad Request
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
        "status_code": 400,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 400,
            "message": "Controller 1 Activity LED toggle failed. Bad parameter. 1"
        }
    }
}
"""
"""
@apiGroup Controllers
@apiName GetFCportsList
@api {get} /ise/<ise-id>/fcports/ Display FCports

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting fcports

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1512635034",
        "total": "1.61s",
        "cortex": "1.60s",
        "res_send_time": "1512635036"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "fcports": {
                    "fcports": [
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Operational",
                                    "value": "0"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/1"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300100",
                            "speed": 8,
                            "id": 1
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Link Down",
                                    "value": "5"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/2"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300101",
                            "speed": 8,
                            "id": 2
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Link Down",
                                    "value": "5"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/3"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300102",
                            "speed": 8,
                            "id": 3
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Link Down",
                                    "value": "5"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/4"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300103",
                            "speed": 8,
                            "id": 4
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Link Down",
                                    "value": "5"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/5"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300104",
                            "speed": 8,
                            "id": 5
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Operational",
                                    "value": "0"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/6"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300105",
                            "speed": 8,
                            "id": 6
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Link Down",
                                    "value": "5"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/7"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300106",
                            "speed": 8,
                            "id": 7
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Link Down",
                                    "value": "5"
                                }
                            },
                            "bytesreceived": 0,
                            "lipcount": 0,
                            "speedsetting": 1,
                            "type": {
                                "_attr": {
                                    "string": "N Port",
                                    "value": "10"
                                },
                                "type": ""
                            },
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/8"
                            },
                            "noscount": 0,
                            "bytestransmitted": 0,
                            "wwn": "2000001F93300107",
                            "speed": 8,
                            "id": 8
                        }
                    ],
                    "_attr": {
                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports"
                    }
                }
            }
        },
        "error": false
    }
}


@apiError ISENotFound The particular ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

@apiErrorExample {JSON} Error-Response:
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

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 401 Unauthorized
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1505988917",
        "total": "1.08s",
        "cortex": "1.03s",
        "res_send_time": "1505988918"
    },
    "result": {
        "status_code": 401,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 401,
            "message": "401 Unauthorized"
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 504 Gateway Timeout
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
        "status_code": 504,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 504,
            "message": "ConnectionError, Retry.."
        }
    }
}
"""
"""
@apiGroup Controllers
@apiName GetParticularFCport
@api {get} /ise/<ise-id>/fcports/<fcportsid> Display ParticularFCports

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} fcportsid unique FCports ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting particular fcportsdetail

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1512635371",
        "total": "1.61s",
        "cortex": "1.60s",
        "res_send_time": "1512635373"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "fcports": {
                    "fcport": {
                        "status": {
                            "status": "",
                            "_attr": {
                                "string": "Operational",
                                "value": "0"
                            }
                        },
                        "bytesreceived": 0,
                        "lipcount": 0,
                        "speedsetting": 1,
                        "type": {
                            "_attr": {
                                "string": "N Port",
                                "value": "10"
                            },
                            "type": ""
                        },
                        "_attr": {
                            "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports/1"
                        },
                        "noscount": 0,
                        "bytestransmitted": 0,
                        "wwn": "2000001F93300100",
                        "speed": 8,
                        "id": 1
                    },
                    "_attr": {
                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fcports"
                    }
                }
            }
        },
        "error": false
    }
}

@apiError ISENotFound The particular ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

@apiErrorExample {JSON} Error-Response:
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

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 401 Unauthorized
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1505988917",
        "total": "1.08s",
        "cortex": "1.03s",
        "res_send_time": "1505988918"
    },
    "result": {
        "status_code": 401,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 401,
            "message": "401 Unauthorized"
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 504 Gateway Timeout
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
        "status_code": 504,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 504,
            "message": "ConnectionError, Retry.."
        }
    }
}
"""
"""
@apiGroup Controllers
@apiName UpdateFCportdetails
@api {put} /ise/<ise-id>/fcports/<fcportsid> Update ParticularFCport

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} fcportsid unique FCport-ID
@apiParam {String/Number} fcportspeed FCportsSpeed

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input
{
   "fcportspeed":"auto | speed"
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "result": {
        "status_code": 201,
        "response": {
            "data": "FC Port1 Speed Setting has been modified"
        },
        "error": false
    }
}

@apiError BadRequest Invalid or missing parameter
@apiError IseNotFound The particular Ise is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 400 Bad Request
{
    "message": "fail",
    "result": {
        "status_code": 400,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 400,
            "message": "Bad parameter."
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1506077012",
        "total": "1.12s",
        "cortex": "1.07s",
        "res_send_time": "1506077014"
    },
    "result": {
        "status_code": 404,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 404,
            "message": "Requested ISE not found."
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 401 Unauthorized
{
    "message": "fail",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1505988917",
        "total": "1.08s",
        "cortex": "1.03s",
        "res_send_time": "1505988918"
    },
    "result": {
        "status_code": 401,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 401,
            "message": "401 Unauthorized"
        }
    }
}

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 504 Gateway Timeout
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
        "status_code": 504,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 504,
            "message": "ConnectionError, Retry.."
        }
    }
}
"""
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/controllers/$', ControllersList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/controllers/(?P<ctlid>[\w\-]+)/$', ControllersDetail.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/fcports/$', FcportsList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/fcports/(?P<fcportsid>[\w\-]+)/$', FcportsDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

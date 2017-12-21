from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.drives import(DrivesList, DrivesDetails)
"""
@apiGroup Drives
@apiName GetDrivesList
@api {get} /ise/<ise-id>/drives/ Display DrivesList

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting driveslist

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504362876",
        "total": "2.04s",
        "cortex": "2.04s",
        "res_send_time": "1504362878"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "drives": {
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives"
                    },
                    "drives": [
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "31"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600213",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/1"
                            },
                            "position": 1,
                            "wwn": "5002538A4760AB71",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "31"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600127",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/2"
                            },
                            "position": 2,
                            "wwn": "5002538A4760A611",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "31"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600128",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/3"
                            },
                            "position": 3,
                            "wwn": "5002538A4760A621",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "32"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600130",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/4"
                            },
                            "position": 4,
                            "wwn": "5002538A4760A641",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "32"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600125",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/5"
                            },
                            "position": 5,
                            "wwn": "5002538A4760A5F1",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600180",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/6"
                            },
                            "position": 6,
                            "wwn": "5002538A4760A961",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600155",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/7"
                            },
                            "position": 7,
                            "wwn": "5002538A4760A7D1",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600131",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/8"
                            },
                            "position": 8,
                            "wwn": "5002538A4760A651",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600119",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/9"
                            },
                            "position": 9,
                            "wwn": "5002538A4760A591",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "30"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600129",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/10"
                            },
                            "position": 10,
                            "wwn": "5002538A4760A631",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "31"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600195",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/11"
                            },
                            "position": 11,
                            "wwn": "5002538A4760AA51",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "32"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600197",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/12"
                            },
                            "position": 12,
                            "wwn": "5002538A4760AA71",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "31"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600194",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/13"
                            },
                            "position": 13,
                            "wwn": "5002538A4760AA41",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "32"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600193",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/14"
                            },
                            "position": 14,
                            "wwn": "5002538A4760AA31",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "32"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600222",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/15"
                            },
                            "position": 15,
                            "wwn": "5002538A4760AC01",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600196",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/16"
                            },
                            "position": 16,
                            "wwn": "5002538A4760AA61",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600135",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/17"
                            },
                            "position": 17,
                            "wwn": "5002538A4760A691",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600133",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/18"
                            },
                            "position": 18,
                            "wwn": "5002538A4760A671",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "29"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600134",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/19"
                            },
                            "position": 19,
                            "wwn": "5002538A4760A681",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Operational"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                }
                            },
                            "capacity": 975,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "30"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "S3M8NX0J600136",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "on",
                                        "value": "2"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "GXL0",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/20"
                            },
                            "position": 20,
                            "wwn": "5002538A4760A6A1",
                            "servoversion": 0,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/1"
                                },
                                "poolid": 1
                            },
                            "productid": "MZILS960HEHP/007"
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/21"
                            },
                            "position": 21,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/22"
                            },
                            "position": 22,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/23"
                            },
                            "position": 23,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/24"
                            },
                            "position": 24,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/25"
                            },
                            "position": 25,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/26"
                            },
                            "position": 26,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/27"
                            },
                            "position": 27,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/28"
                            },
                            "position": 28,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/29"
                            },
                            "position": 29,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/3"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/30"
                            },
                            "position": 30,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/31"
                            },
                            "position": 31,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/32"
                            },
                            "position": 32,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/33"
                            },
                            "position": 33,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/34"
                            },
                            "position": 34,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/35"
                            },
                            "position": 35,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/36"
                            },
                            "position": 36,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/37"
                            },
                            "position": 37,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/38"
                            },
                            "position": 38,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/39"
                            },
                            "position": 39,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/4"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/40"
                            },
                            "position": 40,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/41"
                            },
                            "position": 41,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/42"
                            },
                            "position": 42,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/43"
                            },
                            "position": 43,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/44"
                            },
                            "position": 44,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/45"
                            },
                            "position": 45,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/46"
                            },
                            "position": 46,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/47"
                            },
                            "position": 47,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/48"
                            },
                            "position": 48,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/49"
                            },
                            "position": 49,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/5"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/50"
                            },
                            "position": 50,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/51"
                            },
                            "position": 51,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/52"
                            },
                            "position": 52,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/53"
                            },
                            "position": 53,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/54"
                            },
                            "position": 54,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/55"
                            },
                            "position": 55,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/56"
                            },
                            "position": 56,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/57"
                            },
                            "position": 57,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/58"
                            },
                            "position": 58,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/59"
                            },
                            "position": 59,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        },
                        {
                            "status": {
                                "_attr": {
                                    "string": "Not Installed"
                                },
                                "detail": "None"
                            },
                            "medium": {
                                "medium": "",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/6"
                                }
                            },
                            "capacity": 0,
                            "temperature": {
                                "scale": "celsius",
                                "_attr": {
                                    "value": "0"
                                }
                            },
                            "reducedcapacity": 0,
                            "serialnumber": "",
                            "statusleds": {
                                "amber": {
                                    "amber": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "blue": {
                                    "blue": "",
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    }
                                },
                                "green": {
                                    "_attr": {
                                        "string": "off",
                                        "value": "1"
                                    },
                                    "green": ""
                                }
                            },
                            "fwversion": "",
                            "voltage": {
                                "range5v": 0,
                                "scale": "mV",
                                "range12v": 0
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/drives/60"
                            },
                            "position": 60,
                            "wwn": 0,
                            "servoversion": "",
                            "pool": {
                                "_attr": {
                                    "self": ""
                                },
                                "poolid": 0
                            },
                            "productid": ""
                        }
                    ]
                }
            }
        },
        "error": false
    }
}

@apiError ISENotFound The particular ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

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
@apiGroup Drives
@apiName GetParticularDrivesInfo
@api {get} /ise/<ise-id>/drives/drive_id/ Display ParticularDriveInfo

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} drive-id unique Drive-ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting particulardriveinfo

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.06s",
        "req_recv_time": "1506076932",
        "total": "1.11s",
        "cortex": "1.05s",
        "res_send_time": "1506076933"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "drives": {
                    "_attr": {
                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/drives"
                    },
                    "drive": {
                        "status": {
                            "_attr": {
                                "string": "Operational"
                            },
                            "detail": "None"
                        },
                        "medium": {
                            "medium": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/media/1"
                            }
                        },
                        "capacity": 1950,
                        "temperature": {
                            "scale": "celsius",
                            "_attr": {
                                "value": "32"
                            }
                        },
                        "reducedcapacity": 0,
                        "serialnumber": "S2B3NYAG900068",
                        "statusleds": {
                            "amber": {
                                "amber": "",
                                "_attr": {
                                    "string": "off",
                                    "value": "1"
                                }
                            },
                            "blue": {
                                "blue": "",
                                "_attr": {
                                    "string": "blinking",
                                    "value": "4"
                                }
                            },
                            "green": {
                                "_attr": {
                                    "string": "on",
                                    "value": "2"
                                },
                                "green": ""
                            }
                        },
                        "fwversion": "TT00",
                        "voltage": {
                            "range5v": 0,
                            "scale": "mV",
                            "range12v": 0
                        },
                        "_attr": {
                            "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/drives/1"
                        },
                        "position": 1,
                        "wwn": "5002538A059153B1",
                        "servoversion": 0,
                        "pool": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/pools/1"
                            },
                            "poolid": 1
                        },
                        "productid": "MZILS1T9HCHP/003"
                    }
                }
            }
        },
        "error": false
    }
}

@apiError DriveNotFound The particular Drive is not found
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
            "message": "Requested DRIVE not found."
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
@apiGroup Drives
@apiName UpdateParticularDrive
@api {put} /ise/<ise-id>/drives/drive_id/ Update ParticularDrive

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} drive-id unique Drive-ID
@apiParam {String} led Enable/Disable LED

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input
{
    "led":"enabled"
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
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
        "status_code": 200,
        "response": {
            "data": "Array Activity LED has been enabled"
        },
        "error": false
    }
}

@apiError BadRequest Invalid or missing parameter
@apiError DriveNotFound The particular Drive is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

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
            "message": "Array Activity LED toggle failed. Bad parameter."
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
            "message": "Requested DRIVE not found."
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
    url(r'^ise/(?P<ise_id>[\w\-]+)/drives/$', DrivesList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/drives/(?P<drive_id>[\w\-]+)/$',DrivesDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

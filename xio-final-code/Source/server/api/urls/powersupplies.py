from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.powersupplies import(PowersupplyList, PowersupplyDetail)

"""
@apiGroup Powersupply
@apiName GetPowersupplyInfo
@api {get} /ise/<ise-id>/powersupplies/ Display Powersupply Info

@apiParam {Integer} ise-id unique ISE ID

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for Powersupply
@apiSuccess {String} message It gives success or error message of the Powersupply
@apiSuccess {String} error It contains error message

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504446568",
        "total": "1.13s",
        "cortex": "1.13s",
        "res_send_time": "1504446569"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "powersupplies": {
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies"
                    },
                    "powersupplies": [
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
                            "serialnumber": "XXXXXXXXXX",
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
                                "warning": 70,
                                "critical": 75,
                                "_attr": {
                                    "value": "28"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/1"
                            },
                            "fans": "",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "position": 1,
                            "partnumber": "S-1600CB-3",
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
                            "serialnumber": "Not Avai6",
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
                                "warning": 70,
                                "critical": 75,
                                "_attr": {
                                    "value": "30"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/2"
                            },
                            "fans": "",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "position": 2,
                            "partnumber": "Not Avai2",
                            "hwversion": "",
                            "id": 2
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
                            "serialnumber": "USE2600063FOM043",
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
                                "warning": 70,
                                "critical": 75,
                                "_attr": {
                                    "value": "26"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/3"
                            },
                            "fans": "",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "position": 3,
                            "partnumber": "PCA-00569-01-B",
                            "hwversion": "",
                            "id": 3
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
                            "serialnumber": "Not Avai8",
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
                                "warning": 70,
                                "critical": 75,
                                "_attr": {
                                    "value": "25"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/4"
                            },
                            "fans": "",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "position": 4,
                            "partnumber": "Not Avai4",
                            "hwversion": "",
                            "id": 4
                        }
                    ]
                }
            }
        },
        "error": false
    }
}
@apiError ISENotFound The particular ISE is not found

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
"""
@apiGroup Powersupply
@apiName GetParticularPowersupplyInfo
@api {get} /ise/<ise-id>/powersupplies/<powersupplies-id> Display Particular Powersupply Info

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} powersupplies-id unique Powersupplies ID

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for Powersupply
@apiSuccess {String} message It gives success or error message of the Powersupply
@apiSuccess {String} error It contains error message

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504446808",
        "total": "1.12s",
        "cortex": "1.12s",
        "res_send_time": "1504446809"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "powersupplies": {
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies"
                    },
                    "powersupply": {
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
                        "serialnumber": "XXXXXXXXXX",
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
                            "warning": 70,
                            "critical": 75,
                            "_attr": {
                                "value": "29"
                            }
                        },
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/1"
                        },
                        "fans": "",
                        "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                        "position": 1,
                        "partnumber": "S-1600CB-3",
                        "hwversion": "",
                        "id": 1
                    }
                }
            }
        },
        "error": false
    }
}

@apiError ISENotFound The Powersupply is not found

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504447023",
        "total": "1.13s",
        "cortex": "1.12s",
        "res_send_time": "1504447024"
    },
    "result": {
        "status_code": 404,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 404,
            "message": "Requested POWERSUPPLY not found."
        }
    }
}
"""
"""
@apiGroup Powersupply
@apiName UpdatePowersupplyDetail

@api {put} /ise/<ise-id>/powersupplies/<powersupplies-id> Update Powersupply Details

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} powersupplies-id unique Powersupplies ID

@apiParam {String} led Enable/Disable LED

@apiParamExample {json} Input
{
	"led":"enabled"
}

@apiSuccessExample {json} Success-Response:
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
            "data": "Power Supply 1 Activity LED has been enabled"
        },
        "error": false
    }
}
@apiErrorExample {json} Error-Response:
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
            "message": "Invalid or Missing Parameter"
        }
    }
}
"""
urlpatterns = [url(r'^ise/(?P<ise_id>[\w\-]+)/powersupplies/$',
                   PowersupplyList.as_view()),
               url(r'^ise/(?P<ise_id>[\w\-]+)/powersupplies/(?P<pw_id>[\w\-]+)/$',
                   PowersupplyDetail.as_view()),
               ]

urlpatterns = format_suffix_patterns(urlpatterns)

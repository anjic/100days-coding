from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.media import(MediumList, MediumDetail)
"""
@apiGroup Media
@apiName GetMediaInfo
@api {get} /ise/<ise-id>/media/ Display MediaInfo

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting MediaInfo

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504443348",
        "total": "1.12s",
        "cortex": "1.12s",
        "res_send_time": "1504443349"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "media": {
                    "media": [
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
                            "serialnumber": "",
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
                                "warning": 50,
                                "critical": 60,
                                "_attr": {
                                    "peak": "0",
                                    "value": "34"
                                }
                            },
                            "capacity": 0,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                            },
                            "taskstatus": {
                                "progress": -1,
                                "_attr": {
                                    "string": "None",
                                    "value": "-1"
                                },
                                "type": "None"
                            },
                            "fwversion": "0 ()",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "health": {
                                "warning": 100,
                                "critical": 87,
                                "_attr": {
                                    "value": "100"
                                }
                            },
                            "tier": {
                                "tier": "",
                                "_attr": {
                                    "string": "Flash",
                                    "value": "5"
                                }
                            },
                            "position": 1,
                            "partnumber": "",
                            "sparelevel": 20,
                            "hwversion": "",
                            "id": 1,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/6001F933001100000000000100000000"
                                },
                                "globalid": "6001F933001100000000000100000000"
                            },
                            "redundancyhealth": {
                                "healthstring": "(Data is redundant)",
                                "_attr": {
                                    "value": "125"
                                },
                                "inselfhealing": "No"
                            }
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
                            "serialnumber": "",
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
                                "warning": 50,
                                "critical": 60,
                                "_attr": {
                                    "peak": "0",
                                    "value": "34"
                                }
                            },
                            "capacity": 0,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                            },
                            "taskstatus": {
                                "progress": -1,
                                "_attr": {
                                    "string": "None",
                                    "value": "-1"
                                },
                                "type": "None"
                            },
                            "fwversion": "0 ()",
                            "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                            "health": {
                                "warning": 100,
                                "critical": 87,
                                "_attr": {
                                    "value": "100"
                                }
                            },
                            "tier": {
                                "tier": "",
                                "_attr": {
                                    "string": "Flash",
                                    "value": "5"
                                }
                            },
                            "position": 2,
                            "partnumber": "",
                            "sparelevel": 20,
                            "hwversion": "",
                            "id": 2,
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/6001F933001100000000000100000000"
                                },
                                "globalid": "6001F933001100000000000100000000"
                            },
                            "redundancyhealth": {
                                "healthstring": "(Data is redundant)",
                                "_attr": {
                                    "value": "125"
                                },
                                "inselfhealing": "No"
                            }
                        }
                    ],
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media"
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
@apiGroup Media
@apiName GetMediumInfo
@api {get} /ise/<ise-id>/media/<mediumid> Display MediumInfo

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} mediumid unique MediumID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting mediuminfo

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504443483",
        "total": "1.10s",
        "cortex": "1.10s",
        "res_send_time": "1504443484"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "media": {
                    "medium": {
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
                        "serialnumber": "",
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
                            "warning": 50,
                            "critical": 60,
                            "_attr": {
                                "peak": "0",
                                "value": "34"
                            }
                        },
                        "capacity": 0,
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                        },
                        "taskstatus": {
                            "progress": -1,
                            "_attr": {
                                "string": "None",
                                "value": "-1"
                            },
                            "type": "None"
                        },
                        "fwversion": "0 ()",
                        "manufacturingdate": "Thu Jan  1 00:00:00 1970",
                        "health": {
                            "warning": 100,
                            "critical": 87,
                            "_attr": {
                                "value": "100"
                            }
                        },
                        "tier": {
                            "tier": "",
                            "_attr": {
                                "string": "Flash",
                                "value": "5"
                            }
                        },
                        "position": 1,
                        "partnumber": "",
                        "sparelevel": 20,
                        "hwversion": "",
                        "id": 1,
                        "pool": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/pools/6001F933001100000000000100000000"
                            },
                            "globalid": "6001F933001100000000000100000000"
                        },
                        "redundancyhealth": {
                            "healthstring": "(Data is redundant)",
                            "_attr": {
                                "value": "125"
                            },
                            "inselfhealing": "No"
                        }
                    },
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media"
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
@apiGroup Media
@apiName UpdateMediumDetail
@api {put} /ise/<ise-id>/media/<mediumid> Update MediumDetails

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} mediumid unique Medium ID
@apiParam {String} led Enable/Disable LED

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input.
{
	"led":"enabled"
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "result":{
      "status_code":201,
      "response":{
         "data":"Medium 1 Activity LED has been disabled"
      },
      "error":false
   }
}

@apiError BadRequest Invalid or missing parameter
@apiError ISENotFound The particular ISE is not found
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
            "message": "Invalid or missing parameter"
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

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504446029",
        "total": "3.85s",
        "cortex": "3.84s",
        "res_send_time": "1504446033"
    },
    "result": {
        "status_code": 404,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 404,
            "message": "Requested Medium not found."
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
"""
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/media/$', MediumList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/media/(?P<mediumid>[\w\-]+)/$', MediumDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

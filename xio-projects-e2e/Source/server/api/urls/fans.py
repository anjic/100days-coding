from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.fans import(FanDetail, FanList)
"""
@apiGroup Fans
@apiName GetFansList
@api {get} /ise/<ise-id>/fans/ Display FansList

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting FansList

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504372297",
        "total": "1.10s",
        "cortex": "1.10s",
        "res_send_time": "1504372299"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "fans": {
                    "fans": [
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Operational",
                                    "value": "0"
                                }
                            },
                            "rpm": 17880,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/1"
                            },
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
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
                            "rpm": 17730,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/2"
                            },
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
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
                            "rpm": 17250,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/3"
                            },
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
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
                            "rpm": 17700,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/4"
                            },
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
                            "id": 4
                        },
                        {
                            "status": {
                                "status": "",
                                "_attr": {
                                    "string": "Operational",
                                    "value": "0"
                                }
                            },
                            "rpm": 17850,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/5"
                            },
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
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
                            "rpm": 17760,
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/6"
                            },
                            "led": {
                                "_attr": {
                                    "string": "disabled",
                                    "value": "0"
                                },
                                "led": ""
                            },
                            "id": 6
                        }
                    ],
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans"
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
@apiGroup Fans
@apiName GetFanDetail
<<<<<<< HEAD
@api {get} /ise/<ise-id>/fans/<fan-id> Display FanInfo

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} fan-id unique Fan ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting FanInfo

=======
@api {get} /ise/<ise-id>/fans/<fan-id> Display Fan Info

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} fan-id unique Fan ID

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for displaying list of fans
@apiSuccess {String} message It gives success or error message
@apiSuccess {String} error It contains error messages

>>>>>>> 863a87f6d21c24fb2de922fa957a7caf9945a90b
@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504373324",
        "total": "1.10s",
        "cortex": "1.10s",
        "res_send_time": "1504373325"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "fans": {
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans"
                    },
                    "fan": {
                        "status": {
                            "status": "",
                            "_attr": {
                                "string": "Operational",
                                "value": "0"
                            }
                        },
                        "rpm": 17910,
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/1"
                        },
                        "led": {
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            },
                            "led": ""
                        },
                        "id": 1
                    }
                }
            }
        },
        "error": false
    }
}

@apiError FanNotFound The particular FAN is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

@apiErrorExample {JSON} Error-Response:
HTTP/1.1 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504373700",
        "total": "1.09s",
        "cortex": "1.09s",
        "res_send_time": "1504373701"
    },
    "result": {
        "status_code": 400,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 400,
            "message": "Invalid Id"
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
@apiGroup Fans
@apiName UpdateFanDetail
@api {put} /ise/<ise-id>/fans/<fan-id> Update Fan Details

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} Fan-id unique Fan ID
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
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "fans updated": "1"
            }
        },
        "error": false
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
            "message": "Bad parameter. 1"
        }
    }
}

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
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/fans/$', FanList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/fans/(?P<fanid>[\w\-]+)/$', FanDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

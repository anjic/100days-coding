from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.network import(NetworkList, NetworkDetail)

"""
@apiGroup Network
@apiName GetNetworkInfo
@api {get} /ise/<ise-id>/network/ Display Network Info

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for NetworkInfo
@apiSuccess {String} message It gives success or error message of the NetworkInfo
@apiSuccess {String} error It contains error message

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504441846",
        "total": "1.13s",
        "cortex": "1.13s",
        "res_send_time": "1504441847"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "network": {
                    "dhcp": {
                        "dhcp": "",
                        "_attr": {
                            "string": "disabled",
                            "value": "0"
                        }
                    },
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network"
                    },
                    "wakeonlan": {
                        "_attr": {
                            "string": "enabled",
                            "value": "1"
                        },
                        "wakeonlan": ""
                    },
                    "dns": {
                        "nameservers": [
                            "String not found",
                            "String not found"
                        ],
                        "domainserver": "String not found"
                    },
                    "ports": {
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network/ports"
                        },
                        "ports": [
                            {
                                "macaddress": "00:09:3D:02:61:71",
                                "linkstatus": "Connected",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network/ports/1"
                                },
                                "dnsname": "10.20.238.9",
                                "ipmask": "255.255.240.0",
                                "ipaddress": "10.20.238.9",
                                "gateway": "10.20.224.1"
                            },
                            {
                                "macaddress": "00:09:3D:02:61:3F",
                                "linkstatus": "Connected",
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network/ports/2"
                                },
                                "dnsname": "10.20.238.10",
                                "ipmask": "255.255.240.0",
                                "ipaddress": "10.20.238.10",
                                "gateway": "10.20.224.1"
                            }
                        ]
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
@apiGroup Network
@apiName GetParticularNetworkInfo
@api {get} /ise/<ise-id>/network/<network-id> Display Particular Network Info

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} network-id unique Network ID

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ParticularNetworkInfo
@apiSuccess {String} message It gives success or error message of the ParticularNetworkInfo
@apiSuccess {String} error It contains error message

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504441914",
        "total": "1.12s",
        "cortex": "1.11s",
        "res_send_time": "1504441915"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "network": {
                    "dhcp": {
                        "dhcp": "",
                        "_attr": {
                            "string": "disabled",
                            "value": "0"
                        }
                    },
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network"
                    },
                    "wakeonlan": {
                        "_attr": {
                            "string": "enabled",
                            "value": "1"
                        },
                        "wakeonlan": ""
                    },
                    "dns": {
                        "nameservers": [
                            "String not found",
                            "String not found"
                        ],
                        "domainserver": "String not found"
                    },
                    "ports": {
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network/ports"
                        },
                        "port": {
                            "macaddress": "00:09:3D:02:61:71",
                            "linkstatus": "Connected",
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network/ports/1"
                            },
                            "dnsname": "10.20.238.9",
                            "ipmask": "255.255.240.0",
                            "ipaddress": "10.20.238.9",
                            "gateway": "10.20.224.1"
                        }
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
"""
@apiGroup Network
@apiName UpdateParticularNetworkInfo
@api {put} /ise/<ise-id>/network/<network-id> Update Particular Network

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} network-id Network ID

@apiParam {String} ipaddress Network IP address
@apiParam {String} ipmask Network IP mask
@apiParam {String} gateway Network Gateway
@apiParam {String} DHCP Enable/Disable LED

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {json} Input
{
  "dhcp": "disabled",
  "network": {
    "0": {
      "ipaddress": "10.20.227.120",
      "ipmask": "255.255.240.1",
      "gateway": "10.20.224.1"
    }
  },
  "nameserver": [
    "10.10.10.9",
    "10.20.20.90"
  ]
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
  "message": "success",
  "result": {
    "status_code": 200,
    "response": {
      "data": "Network 1 Updated Successfully "
    },
    "error": false
  }
}
"""
"""
@apiGroup Network
@apiName UpdateNetworkDetail
@api {put} /ise/<ise-id>/network/ Update Network Details

@apiParam {Number} ise-id unique ISE ID
@apiParam {String} DHCP Enable/Disable LED

@apiParamExample {json} Input
{
"dhcp":"disabled"
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
            "data": "Network Configuration has been changed."
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
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/network/$', NetworkList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/network/(?P<network_id>[\w\-]+)/$', NetworkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

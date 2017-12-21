from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.ise_views import (IseList, IseDetail, IseSanMap,
                                 SanIseMap, IseManagement, AdvancedSettings,
                                 IseStatus, IseLed, IseInitialize, IseIpUpdate)
"""
@apiGroup ISE
@apiName GetISEAdvancedSettings
@api {get} /ise/<ise-id>/advance-settings/ Display AdvancedSettingsInfo

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for AdvanceSettings

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.57s",
        "req_recv_time": "1512471298",
        "total": "1.75s",
        "cortex": "1.17s",
        "res_send_time": "1512471299"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "running": true,
                "warning": false,
                "identify": false,
                "shutdown": false,
                "initialize": false,
                "reformat": false,
                "restart": false
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
@apiGroup ISE
@apiName UpdateISEAdvancedSettings
@api {put} /ise/<ise-id>/advance-settings/ Update AdvancedSettingsInfo

@apiParam {Number} ise-id unique ISE ID

@apiParam {String} reformat To Reformat the ISE
@apiParam {String} initialize To initialize the ISE
@apiParam {String} shutdown To shutdown the ISE
@apiParam {String} restart  To restart the ISE
@apiParam {String} identify Identify ISE

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {json} Input
{
   "reformat":false,
   "initialize":true,
   "shutdown":false,
   "restart":false,
   "identify":false
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
  "message":"success",
  "result":{
     "status_code":200,
     "response":{
        "data":{
           "running":false,
           "identify":false,
           "shutdown":false,
           "initialize":true,
           "reformat":false,
           "restart":false
        }
     },
     "error":false
  }
}
"""
"""
@apiGroup ISE
@apiName GetSanIseMap
@api {get} /ise/<ise-id>/sangroup_map/ Display SanIseMapInfo

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting SanIseMapInfo

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.20s",
        "req_recv_time": "1506344142",
        "total": "0.20s",
        "cortex": "0.0s",
        "res_send_time": "1506344142"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": [
                {
                    "sangroup_id": 1,
                    "checked": true,
                    "sangroup_name": "xio test"
                }
            ]
        },
        "error": false
    }
}
"""
"""
@apiGroup ISE
@apiName UpdateSanIseMap
@api {put} /ise/<ise-id>/sangroup_map/ Update SanIseMapInfo

@apiParam {Number} ise-id unique ISE ID

@apiParam {String} ise_id Unique ISEID
@apiParam {String} ise_name Name of the ISE
@apiParam {List} added Added sangroup_id to map with ISE
@apiParam {List} removed  Removed sangroup_id from the ISE

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {json} Input
{
   "ise_id":"36",
   "ise_name":"",
   "added":[2],
   "removed":[]
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "result":{
      "status_code":200,
      "response":{
         "data":"Mapping Done Successfully"
      },
      "error":false
   }
}
"""
"""
@apiGroup ISE
@apiName GetIseSanMap
@api {get} /sangroup/<id>/ise-map/ Display IseSanMapInfo

@apiParam {Number} id unique Sangroup ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting IseSanMapInfo

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.03s",
        "req_recv_time": "1506346707",
        "total": "0.03s",
        "cortex": "0.0s",
        "res_send_time": "1506346707"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": [
                {
                    "ip_secondary": "10.20.225.136",
                    "ise_name": "ISE-3DE100RT",
                    "checked": true,
                    "id": 1,
                    "ip_primary": "10.20.225.48"
                },
                {
                    "ip_secondary": "10.20.238.6",
                    "ise_name": "ISE-USE2600053GOI05C",
                    "checked": true,
                    "id": 2,
                    "ip_primary": "10.20.238.4"
                },
                {
                    "ip_secondary": "10.20.238.14",
                    "ise_name": "ISE-USE26000368OW009",
                    "checked": true,
                    "id": 3,
                    "ip_primary": "10.20.238.12"
                }
            ]
        },
        "error": false
    }
}
"""
"""
@apiGroup ISE
@apiName UpdateIseSanMap
@api {put} /sangroup/<id>/ise-map/ Update IseSanMapInfo

@apiParam {Number} id unique Sangroup ID

@apiParam {String} sangroup_id Unique SangroupId
@apiParam {List} added Added ise_id to map with ISE
@apiParam {List} removed  Removed ise_id from the ISE

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input
{
   "added":[
      35
   ],
   "removed":[

   ],
   "san_group_id":"2"
}

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "result":{
      "status_code":200,
      "response":{
         "data":"Mapping Done Successfully"
      },
      "error":false
   }
}
"""
"""
@apiGroup ISE
@apiName IseDetail
@api {get} /ise-details/<id>/ Display IseDetail

@apiParam {Number} id unique Ise ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting IseDetail

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "1.05s",
        "req_recv_time": "1506347350",
        "total": "1.05s",
        "cortex": "0.0s",
        "res_send_time": "1506347351"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "ip_secondary": "10.20.225.136",
                "ise_name": "ISE-3DE100RT",
                "prefered": false,
                "contactphone": "",
                "raw_data": "{\"status\":{\"status\":\"\",\"_attr\":{\"string\":\"Warning\",\"value\":\"1\"}},\"contactemail\":\"\",\"serialnumber\":\"3DE100RT\",\"vendor\":\"XIOTECH\",\"name\":\"ISE-3DE100RT\",\"globalid\":\"3DE100RT\",\"_attr\":{\"self\":\"http://10.20.225.136/storage/arrays/3DE100RT\"},\"capabilities\":[{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Storage\",\"value\":\"3\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Block Server\",\"value\":\"15\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Encryption\",\"value\":\"41\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Basic ISE Mirror\",\"value\":\"40001\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"ISE Data Migration\",\"value\":\"40002\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"ISE Mirror Copy\",\"value\":\"40003\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Active-Active ISE Mirror\",\"value\":\"40004\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"ISE Mirror Witness\",\"value\":\"40005\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Orchestrator-disabled\",\"value\":\"47001\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Performance Response Time in Microseconds\",\"value\":\"49001\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"IO Access Mapping\",\"value\":\"49002\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Volume Affinity\",\"value\":\"49003\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Volume Quality of Service IOPS\",\"value\":\"49004\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Thin Provisioning\",\"value\":\"49005\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Clones\",\"value\":\"49006\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Thin-Clones\",\"value\":\"49007\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Thin CADP\",\"value\":\"49008\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Affinity Conversion\",\"value\":\"49009\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"Thick to Thin Conversion\",\"value\":\"49010\"}},{\"capability\":\"\",\"_attr\":{\"type\":\"source\",\"string\":\"One Step Snap Create\",\"value\":\"49011\"}}],\"controllers\":{\"controllers\":[{\"status\":{\"status\":\"\",\"_attr\":{\"string\":\"Operational\",\"value\":\"0\"}},\"macaddress\":\"00:1F:93:20:03:30\",\"_attr\":{\"self\":\"http://10.20.225.136/storage/arrays/3DE100RT/controllers/1\"},\"rank\":{\"_attr\":{\"string\":\"Primary\",\"value\":\"1\"},\"rank\":\"\"},\"fwversion\":\"v3.3.2-5281\",\"dnsname\":\"10.20.225.136\",\"ipaddress\":\"10.20.225.48\"},{\"status\":{\"status\":\"\",\"_attr\":{\"string\":\"Operational\",\"value\":\"0\"}},\"macaddress\":\"00:1F:93:20:03:88\",\"_attr\":{\"self\":\"http://10.20.225.136/storage/arrays/3DE100RT/controllers/2\"},\"rank\":{\"_attr\":{\"string\":\"Secondary\",\"value\":\"0\"},\"rank\":\"\"},\"fwversion\":\"v3.3.2-5281\",\"dnsname\":\"10.20.225.48\",\"ipaddress\":\"10.20.225.136\"}],\"_attr\":{\"self\":\"http://10.20.225.136/storage/arrays/3DE100RT/controllers\"}},\"chronometer\":{\"timezone\":\"MST\",\"dst\":\"enabled\",\"_attr\":{\"date\":\"21-Sep-2017\",\"time\":\"01:42:58\"},\"timezonesetting\":\"MST\"},\"location\":\"\",\"contactname\":\"\",\"address\":\"\",\"contactphone\":\"\",\"model\":\"ISE3401\",\"id\":\"2000001F93104B00\"}",
                "serial_no": "3DE100RT",
                "mrc1_status": true,
                "username": "administrator",
                "contactemail": "",
                "contact": {
                    "phone": null,
                    "email": null,
                    "location": null,
                    "name": null,
                    "address": null
                },
                "status": null,
                "root_node_id": null,
                "contactname": "",
                "address": "",
                "time_stamp": "2017-09-21T07:43:10.591232Z",
                "password": "SoIezqjwAoWOJm12Rf7RUg==",
                "mrc2_status": true,
                "id": 1,
                "ip_primary": "10.20.225.48",
                "location": ""
            }
        },
        "error": false
    }
}
@apiError ISENotFound The particular ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password

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
@apiGroup ISE
@apiName IseStatus
@api {get} /ise/<ise-id>/status/ Display IseStatus

@apiParam {Number} ise-id unique Ise ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting IseStatus

@apiSuccessExample Success-Response:
{
    "message": "success",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1506345237",
        "total": "1.11s",
        "cortex": "1.06s",
        "res_send_time": "1506345238"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "arrays": {
                    "array": {
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
                        "globalid": "USE26000368OW009"
                    },
                    "_attr": {
                        "self": "https://10.20.238.12/storage/arrays"
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
@apiGroup ISE
@apiName GetIseLedStatus
@api {get} /ise/<ise-id>/led/ Display LedStatus

@apiParam {Number} ise-id unique Ise ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting LedStatus

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.05s",
        "req_recv_time": "1506345653",
        "total": "1.13s",
        "cortex": "1.08s",
        "res_send_time": "1506345654"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "arrays": {
                    "array": {
                        "files": {
                            "files": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/files"
                            }
                        },
                        "iomap": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/iomap"
                            },
                            "iomap": ""
                        },
                        "ipaddress1": "10.20.238.12",
                        "ipaddress2": "10.20.238.14",
                        "serialnumber": "USE26000368OW009",
                        "licenseusers": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/licenseusers"
                            },
                            "licenseusers": ""
                        },
                        "batteries": {
                            "batteries": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/batteries/1"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/batteries/2"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/batteries"
                            }
                        },
                        "licenses": {
                            "licenses": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/licenses"
                            }
                        },
                        "encryptionstatus": {
                            "encryptionstatus": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "partnumber": "PCA-00563-01-B-1",
                        "id": "2000001F93300100",
                        "contactphone": "",
                        "network": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/network"
                            },
                            "network": ""
                        },
                        "media": {
                            "media": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Warning",
                                            "value": "1"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/media/1"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Warning",
                                            "value": "1"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/media/2"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Warning",
                                            "value": "1"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/media/3"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/media"
                            }
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "snmp": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/snmp"
                            },
                            "snmp": ""
                        },
                        "capabilities": [
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Storage",
                                    "value": "3"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Block Server",
                                    "value": "15"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Management Controller",
                                    "value": "28"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Encryption",
                                    "value": "41"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Basic ISE Mirror",
                                    "value": "40001"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "ISE Data Migration",
                                    "value": "40002"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "ISE Mirror Copy",
                                    "value": "40003"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Active-Active ISE Mirror",
                                    "value": "40004"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "ISE Mirror Witness",
                                    "value": "40005"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Performance Response Time in Microseconds",
                                    "value": "49001"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "IO Access Mapping",
                                    "value": "49002"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Volume Affinity",
                                    "value": "49003"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Volume Quality of Service IOPS",
                                    "value": "49004"
                                }
                            },
                            {
                                "capability": "",
                                "_attr": {
                                    "type": "source",
                                    "string": "Thin Provisioning",
                                    "value": "49005"
                                }
                            }
                        ],
                        "contactemail": "",
                        "fans": {
                            "fans": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Undefined",
                                            "value": "99999"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans/0"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Undefined",
                                            "value": "99999"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans/0"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Undefined",
                                            "value": "99999"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans/0"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Undefined",
                                            "value": "99999"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans/0"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Undefined",
                                            "value": "99999"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans/0"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Undefined",
                                            "value": "99999"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans/0"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/fans"
                            }
                        },
                        "discoveredarrays": {
                            "_attr": {
                                "returned": "optional"
                            },
                            "discoveredarrays": ""
                        },
                        "location": "",
                        "virtualizerattached": 0,
                        "performance": {
                            "performance": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/performance"
                            }
                        },
                        "revision": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/revision"
                            },
                            "revision": ""
                        },
                        "status": {
                            "_attr": {
                                "string": "Uninitialized",
                                "value": "3"
                            },
                            "details": {
                                "_attr": {
                                    "value": "0x00000010"
                                },
                                "detail": "Ready to be initialized"
                            }
                        },
                        "led": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "led": ""
                        },
                        "contactname": "",
                        "globalid": "USE26000368OW009",
                        "subscriptions": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/subscriptions"
                            },
                            "subscriptions": ""
                        },
                        "powersupplies": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/powersupplies"
                            },
                            "powersupplies": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/powersupplies/1"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/powersupplies/2"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/powersupplies/3"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/powersupplies/4"
                                    }
                                }
                            ]
                        },
                        "vendor": "XIOTECH",
                        "productversion": "",
                        "address": "",
                        "manufacturer": "XIOTECH",
                        "jobs": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/jobs"
                            },
                            "jobs": ""
                        },
                        "name": "",
                        "_attr": {
                            "self": "https://10.20.238.12/storage/arrays/USE26000368OW009"
                        },
                        "controllers": {
                            "controllers": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/controllers/1"
                                    }
                                },
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/controllers/2"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/controllers"
                            }
                        },
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "chronometer": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/chronometer"
                            },
                            "chronometer": ""
                        },
                        "hosts": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/hosts"
                            },
                            "hosts": ""
                        },
                        "temperature": {
                            "low": 10,
                            "scale": "celsius",
                            "warning": 77,
                            "critical": 87,
                            "_attr": {
                                "value": "57"
                            }
                        },
                        "volumes": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/volumes"
                            },
                            "volumes": ""
                        },
                        "encryption": {
                            "encryption": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/encryption"
                            }
                        },
                        "pools": {
                            "pools": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/pools"
                            }
                        },
                        "model": "ISE4400",
                        "endpoints": {
                            "endpoints": "",
                            "_attr": {
                                "self": "https://10.20.238.12/storage/endpoints"
                            }
                        },
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.238.12/storage/allocations"
                            },
                            "allocations": ""
                        }
                    },
                    "_attr": {
                        "self": "https://10.20.238.12/storage/arrays"
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
@apiGroup ISE
@apiName UpdateIseLedStatus
@api {put} /ise/<ise-id>/led/ Update LedStatus

@apiParam {Number} ise-id unique Ise ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} led Enable/Disable LED

@apiParamExample {json} Input.
{
    "led":"enabled"
}

@apiSuccessExample Success-Response:
HTTP/1.1 201 Created
{
    "message": "success",
    "result": {
        "status_code": 201,
        "response": {
            "data": "LED has been enabled"
        },
        "error": false
    }
}

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
            "message": "Activity LED toggle failed. Bad parameter. 1"
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
@apiGroup ISE
@apiName IseList
@api {get} /ise-list/ Display IseList

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting IseList

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.04s",
        "req_recv_time": "1506348131",
        "total": "0.04s",
        "cortex": "0.0s",
        "res_send_time": "1506348131"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": [
                {
                    "id": 1,
                    "root_node_id": null,
                    "ise_name": "ISE-3DE100RT",
                    "raw_data": "\"{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Warning\\\",\\\"value\\\":\\\"1\\\"}},\\\"contactemail\\\":\\\"\\\",\\\"serialnumber\\\":\\\"3DE100RT\\\",\\\"vendor\\\":\\\"XIOTECH\\\",\\\"name\\\":\\\"ISE-3DE100RT\\\",\\\"globalid\\\":\\\"3DE100RT\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.225.136/storage/arrays/3DE100RT\\\"},\\\"capabilities\\\":[{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Storage\\\",\\\"value\\\":\\\"3\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Block Server\\\",\\\"value\\\":\\\"15\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Encryption\\\",\\\"value\\\":\\\"41\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Basic ISE Mirror\\\",\\\"value\\\":\\\"40001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Data Migration\\\",\\\"value\\\":\\\"40002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Copy\\\",\\\"value\\\":\\\"40003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Active-Active ISE Mirror\\\",\\\"value\\\":\\\"40004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Witness\\\",\\\"value\\\":\\\"40005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Orchestrator-disabled\\\",\\\"value\\\":\\\"47001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Performance Response Time in Microseconds\\\",\\\"value\\\":\\\"49001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"IO Access Mapping\\\",\\\"value\\\":\\\"49002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Affinity\\\",\\\"value\\\":\\\"49003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Quality of Service IOPS\\\",\\\"value\\\":\\\"49004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin Provisioning\\\",\\\"value\\\":\\\"49005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Clones\\\",\\\"value\\\":\\\"49006\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin-Clones\\\",\\\"value\\\":\\\"49007\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin CADP\\\",\\\"value\\\":\\\"49008\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Affinity Conversion\\\",\\\"value\\\":\\\"49009\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thick to Thin Conversion\\\",\\\"value\\\":\\\"49010\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"One Step Snap Create\\\",\\\"value\\\":\\\"49011\\\"}}],\\\"controllers\\\":{\\\"controllers\\\":[{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:1F:93:20:03:30\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.225.136/storage/arrays/3DE100RT/controllers/1\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Primary\\\",\\\"value\\\":\\\"1\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v3.3.2-5281\\\",\\\"dnsname\\\":\\\"10.20.225.136\\\",\\\"ipaddress\\\":\\\"10.20.225.48\\\"},{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:1F:93:20:03:88\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.225.136/storage/arrays/3DE100RT/controllers/2\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Secondary\\\",\\\"value\\\":\\\"0\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v3.3.2-5281\\\",\\\"dnsname\\\":\\\"10.20.225.48\\\",\\\"ipaddress\\\":\\\"10.20.225.136\\\"}],\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.225.136/storage/arrays/3DE100RT/controllers\\\"}},\\\"chronometer\\\":{\\\"timezone\\\":\\\"MST\\\",\\\"dst\\\":\\\"enabled\\\",\\\"_attr\\\":{\\\"date\\\":\\\"21-Sep-2017\\\",\\\"time\\\":\\\"01:42:58\\\"},\\\"timezonesetting\\\":\\\"MST\\\"},\\\"location\\\":\\\"\\\",\\\"contactname\\\":\\\"\\\",\\\"address\\\":\\\"\\\",\\\"contactphone\\\":\\\"\\\",\\\"model\\\":\\\"ISE3401\\\",\\\"id\\\":\\\"2000001F93104B00\\\"}\"",
                    "serial_no": "3DE100RT",
                    "ip_primary": "10.20.225.48",
                    "ip_secondary": "10.20.225.136",
                    "mrc1_status": true,
                    "mrc2_status": true,
                    "username": "administrator",
                    "password": "SoIezqjwAoWOJm12Rf7RUg==",
                    "time_stamp": "2017-09-21T07:43:10.591232Z",
                    "status": null,
                    "contactphone": "",
                    "contactemail": "",
                    "contactname": "",
                    "location": "",
                    "address": "",
                    "prefered": false,
                    "sangroup": [
                        {
                            "comment": "",
                            "sangroup_name": "xio test",
                            "sangroup_id": 1
                        }
                    ]
                },
                {
                    "id": 2,
                    "root_node_id": null,
                    "ise_name": "ISE-USE2600053GOI05C",
                    "raw_data": "\"{\\\"status\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"},\\\"details\\\":{\\\"_attr\\\":{\\\"value\\\":\\\"0x00000000\\\"},\\\"detail\\\":\\\"None\\\"}},\\\"contactemail\\\":\\\"\\\",\\\"serialnumber\\\":\\\"USE2600053GOI05C\\\",\\\"vendor\\\":\\\"XIOTECH\\\",\\\"name\\\":\\\"ISE-USE2600053GOI05C\\\",\\\"globalid\\\":\\\"USE2600053GOI05C\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.4/storage/arrays/USE2600053GOI05C\\\"},\\\"capabilities\\\":[{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Storage\\\",\\\"value\\\":\\\"3\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Block Server\\\",\\\"value\\\":\\\"15\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Basic ISE Mirror\\\",\\\"value\\\":\\\"40001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Data Migration\\\",\\\"value\\\":\\\"40002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Copy\\\",\\\"value\\\":\\\"40003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Active-Active ISE Mirror\\\",\\\"value\\\":\\\"40004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Witness\\\",\\\"value\\\":\\\"40005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Orchestrator-disabled\\\",\\\"value\\\":\\\"47001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Performance Response Time in Microseconds\\\",\\\"value\\\":\\\"49001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"IO Access Mapping\\\",\\\"value\\\":\\\"49002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Affinity\\\",\\\"value\\\":\\\"49003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Quality of Service IOPS\\\",\\\"value\\\":\\\"49004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin Provisioning\\\",\\\"value\\\":\\\"49005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Clones\\\",\\\"value\\\":\\\"49006\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin-Clones\\\",\\\"value\\\":\\\"49007\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin CADP\\\",\\\"value\\\":\\\"49008\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Affinity Conversion\\\",\\\"value\\\":\\\"49009\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thick to Thin Conversion\\\",\\\"value\\\":\\\"49010\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"One Step Snap Create\\\",\\\"value\\\":\\\"49011\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Data Deduplication\\\",\\\"value\\\":\\\"49012\\\"}}],\\\"controllers\\\":{\\\"controllers\\\":[{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:09:3D:02:61:3A\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.4/storage/arrays/USE2600053GOI05C/controllers/1\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Primary\\\",\\\"value\\\":\\\"1\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-7204\\\",\\\"dnsname\\\":\\\"10.20.238.4\\\",\\\"ipaddress\\\":\\\"10.20.238.4\\\"},{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:09:3D:02:61:C1\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.4/storage/arrays/USE2600053GOI05C/controllers/2\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Secondary\\\",\\\"value\\\":\\\"0\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-7204\\\",\\\"dnsname\\\":\\\"10.20.238.6\\\",\\\"ipaddress\\\":\\\"10.20.238.6\\\"}],\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.4/storage/arrays/USE2600053GOI05C/controllers\\\"}},\\\"chronometer\\\":{\\\"timezone\\\":\\\"MST\\\",\\\"dst\\\":\\\"disabled\\\",\\\"_attr\\\":{\\\"date\\\":\\\"21-Sep-2017\\\",\\\"time\\\":\\\"01:41:29\\\"},\\\"timezonesetting\\\":\\\"MST\\\"},\\\"location\\\":\\\"\\\",\\\"contactname\\\":\\\"\\\",\\\"address\\\":\\\"\\\",\\\"contactphone\\\":\\\"\\\",\\\"model\\\":\\\"ISE4400\\\",\\\"id\\\":2001010101010000}\"",
                    "serial_no": "USE2600053GOI05C",
                    "ip_primary": "10.20.238.4",
                    "ip_secondary": "10.20.238.6",
                    "mrc1_status": true,
                    "mrc2_status": true,
                    "username": "administrator",
                    "password": "SoIezqjwAoWOJm12Rf7RUg==",
                    "time_stamp": "2017-09-21T07:45:14.285709Z",
                    "status": null,
                    "contactphone": "",
                    "contactemail": "",
                    "contactname": "",
                    "location": "",
                    "address": "",
                    "prefered": false,
                    "sangroup": [
                        {
                            "comment": "",
                            "sangroup_name": "xio test",
                            "sangroup_id": 1
                        }
                    ]
                },
                {
                    "id": 3,
                    "root_node_id": null,
                    "ise_name": "ISE-USE26000368OW009",
                    "raw_data": "\"{\\\"status\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"},\\\"details\\\":{\\\"_attr\\\":{\\\"value\\\":\\\"0x00000000\\\"},\\\"detail\\\":\\\"None\\\"}},\\\"contactemail\\\":\\\"\\\",\\\"serialnumber\\\":\\\"USE26000368OW009\\\",\\\"vendor\\\":\\\"XIOTECH\\\",\\\"name\\\":\\\"ISE-USE26000368OW009\\\",\\\"globalid\\\":\\\"USE26000368OW009\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.12/storage/arrays/USE26000368OW009\\\"},\\\"capabilities\\\":[{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Storage\\\",\\\"value\\\":\\\"3\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Block Server\\\",\\\"value\\\":\\\"15\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Encryption\\\",\\\"value\\\":\\\"41\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Basic ISE Mirror\\\",\\\"value\\\":\\\"40001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Data Migration\\\",\\\"value\\\":\\\"40002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Copy\\\",\\\"value\\\":\\\"40003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Active-Active ISE Mirror\\\",\\\"value\\\":\\\"40004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Witness\\\",\\\"value\\\":\\\"40005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Orchestrator-disabled\\\",\\\"value\\\":\\\"47001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Performance Response Time in Microseconds\\\",\\\"value\\\":\\\"49001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"IO Access Mapping\\\",\\\"value\\\":\\\"49002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Affinity\\\",\\\"value\\\":\\\"49003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Quality of Service IOPS\\\",\\\"value\\\":\\\"49004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin Provisioning\\\",\\\"value\\\":\\\"49005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Clones\\\",\\\"value\\\":\\\"49006\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin-Clones\\\",\\\"value\\\":\\\"49007\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin CADP\\\",\\\"value\\\":\\\"49008\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Affinity Conversion\\\",\\\"value\\\":\\\"49009\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thick to Thin Conversion\\\",\\\"value\\\":\\\"49010\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"One Step Snap Create\\\",\\\"value\\\":\\\"49011\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Data Deduplication\\\",\\\"value\\\":\\\"49012\\\"}}],\\\"controllers\\\":{\\\"controllers\\\":[{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:09:3D:02:61:62\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.12/storage/arrays/USE26000368OW009/controllers/1\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Primary\\\",\\\"value\\\":\\\"1\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-0\\\",\\\"dnsname\\\":\\\"10.20.238.12\\\",\\\"ipaddress\\\":\\\"10.20.238.12\\\"},{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:09:3D:02:60:F4\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.12/storage/arrays/USE26000368OW009/controllers/2\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Secondary\\\",\\\"value\\\":\\\"0\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-0\\\",\\\"dnsname\\\":\\\"10.20.238.14\\\",\\\"ipaddress\\\":\\\"10.20.238.14\\\"}],\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.12/storage/arrays/USE26000368OW009/controllers\\\"}},\\\"chronometer\\\":{\\\"timezone\\\":\\\"MST\\\",\\\"dst\\\":\\\"disabled\\\",\\\"_attr\\\":{\\\"date\\\":\\\"21-Sep-2017\\\",\\\"time\\\":\\\"03:04:27\\\"},\\\"timezonesetting\\\":\\\"MST\\\"},\\\"location\\\":\\\"\\\",\\\"contactname\\\":\\\"\\\",\\\"address\\\":\\\"\\\",\\\"contactphone\\\":\\\"\\\",\\\"model\\\":\\\"ISE4400\\\",\\\"id\\\":\\\"2000001F93300100\\\"}\"",
                    "serial_no": "USE26000368OW009",
                    "ip_primary": "10.20.238.12",
                    "ip_secondary": "10.20.238.14",
                    "mrc1_status": true,
                    "mrc2_status": true,
                    "username": "administrator",
                    "password": "SoIezqjwAoWOJm12Rf7RUg==",
                    "time_stamp": "2017-09-21T10:04:36.943916Z",
                    "status": 0,
                    "contactphone": "",
                    "contactemail": "",
                    "contactname": "",
                    "location": "",
                    "address": "",
                    "prefered": false,
                    "sangroup": [
                        {
                            "comment": "",
                            "sangroup_name": "xio test",
                            "sangroup_id": 1
                        }
                    ]
                }
            ]
        },
        "error": false
    }
}
"""
"""
@apiGroup ISE
@apiName IseManagement
@api {put} /ise/<id>/management/ Update IseAttributes

@apiParam {String} name Name of the ISE
@apiParam {String} contactname ContactName
@apiParam {String} address Address of the contact
@apiParam {String} location  Location of the contact
@apiParam {String} contactemail Contactemail of the contact
@apiParam {String} contactphone Contactphone of the contact
@apiParam {Boolean} prefered_ise Set as the default ise
@apiParam {Number} id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input
{
   "data":{
      "name":"ISE-3DE100RT",
      "contactname":"msystech",
      "address":"ASV",
      "location":"omr,chennai",
      "contactemail":"msys@msystech.com",
      "contactphone":"0987654321",
      "prefered_ise":false
   },
   "id":"36"
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "result":{
      "status_code":200,
      "response":{
         "data":{
            "ise_name":"ISE-3DE100RT",
            "success_message":"Updated Successfully"
         }
      },
      "error":false
   }
}
"""
"""
@apiGroup ISE
@apiName DeleteParticularISE
@api {delete} /ise/<id>/management/ Delete ParticularISE

@apiParam {Number} id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "result":{
      "status_code":200,
      "response":{
         "data":{
            "delete_message":"ISE Removed Successfully"
         }
      },
      "error":false
   }
}
@apiError BadRequest Bad Request
@apiErrorExample {JSON} Error-Response:
HTTP/1.1 400 Bad Request
{
   "message":"fail",
   "result":{
      "status_code":400,
      "response":{
         "data":[

         ]
      },
      "error":{
         "status_code":400,
         "message":"ISE Present in one or more SAN Group"
      }
   }
}
"""
"""
@apiGroup ISE
@apiName IseInitialize
@api {get} /ise/<id>/initialize/ Get IseInitializeStatus

@apiParam {Number} id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for IseInitializeStatus

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "time_taken":{
      "python":"0.00s",
      "req_recv_time":"1512474435",
      "total":"0.00s",
      "cortex":"0.0s",
      "res_send_time":"1512474435"
   },
   "result":{
      "status_code":200,
      "response":{
         "data":{
            "initialize":"finished"
         }
      },
      "error":false
   }
}
"""
urlpatterns = [
    url(r'^ise/(?P<id>[\w\-]+)/advance-settings/$', AdvancedSettings.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/management/$', IseManagement.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/sangroup_map/$', SanIseMap.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/status/$', IseStatus.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/led/$', IseLed.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/initialize/$', IseInitialize.as_view()),
    url(r'^sangroup/(?P<id>[\w\-]+)/ise-map/$', IseSanMap.as_view()),
    url(r'^ise-details/(?P<id>[\w\-]+)/$', IseDetail.as_view()),
    url(r'^ise-list/', IseList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/ip-update/$', IseIpUpdate.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

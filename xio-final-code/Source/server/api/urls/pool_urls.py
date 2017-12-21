from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.pool_views import(PoolsList, PoolsDetail, 
                                PoolsChart, DataReduction)
"""
@apiGroup StoragePools
@apiName GetPoolsList
@api {get} /ise/<ise-id>/pools/ Display PoolsList

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting poolslist

@apiSuccessExample {JSON} {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504445330",
        "total": "1.15s",
        "cortex": "1.14s",
        "res_send_time": "1504445331"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "pools": {
                    "_attr": {
                        "self": "https://10.20.238.9/storage/pools"
                    },
                    "pool": {
                        "available": {
                            "_attr": {
                                "total": "12636"
                            },
                            "byredundancy": {
                                "raid-1": 6318,
                                "raid-0": 12636,
                                "raid-5": 10109
                            }
                        },
                        "Flashquota": 0,
                        "id": 1,
                        "size": 14014,
                        "DedupProvisioned": {
                            "SystemData": 687,
                            "UserData": 640
                        },
                        "media": {
                            "media": [
                                {
                                    "tier": {
                                        "tier": "",
                                        "_attr": {
                                            "string": "Flash",
                                            "value": "5"
                                        }
                                    },
                                    "_attr": {
                                        "self": "http://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                    },
                                    "health": 125
                                },
                                {
                                    "tier": {
                                        "tier": "",
                                        "_attr": {
                                            "string": "Flash",
                                            "value": "5"
                                        }
                                    },
                                    "_attr": {
                                        "self": "http://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                    },
                                    "health": 125
                                }
                            ],
                            "_attr": {
                                "self": "http://10.20.238.9/storage/arrays/USE26000368OW028/media"
                            }
                        },
                        "Flashavailable": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 0
                            }
                        },
                        "ThinThreshold": 75,
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
                        "used": {
                            "_attr": {
                                "total": "1378"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 625
                            }
                        },
                        "globalid": "6001F933001100000000000100000000",
                        "Flashcapacity": 0,
                        "Flashprovisioned": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 0
                            }
                        },
                        "FastSheettotal": 0,
                        "Flashused": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 0
                            }
                        },
                        "provisioned": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 625
                            }
                        },
                        "name": "Pool 1",
                        "DedupUsed": {
                            "SystemData": 687,
                            "UserData": 12
                        },
                        "SlowSheettotal": 59796,
                        "_attr": {
                            "self": "https://10.20.238.9/storage/pools/6001F933001100000000000100000000"
                        },
                        "FastSheetallocated": 0,
                        "volumes": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/volumes"
                            },
                            "volumes": ""
                        },
                        "SlowSheetallocated": 5881
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
@apiGroup StoragePools
@apiName CreatePool
@api {post} /ise/<ise-id>/pools/ Create Pool

@apiParam {Number} ise-id unique ISE ID

@apiParam {Number} media DataPacID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input:
{
  "media": "2"
}

@apiSuccessExample {JSON} {JSON} Success-Response:
HTTP/1.1 202 Accepted
{
   "message":"success",
   "result":{
      "status_code":202,
      "response":{
         "data":"Add Pool request in progress"
      },
      "error":false
   }
}

@apiError ISENotFound The particular ISE is not found
@apiError ConnectionError GatewayTimeout
@apiError Unauthorization Invalid username or password
@apiError BadRequest Bad Request

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
         "message":"At least one Datapac is already part of a pool"
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
@apiGroup StoragePools
@apiName DisplayParticularPool
@api {get} /ise/<ise-id>/pools/<pool-id> Get ParticularPool

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} pool-id unique Pool ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for AdvanceSettings

@apiSuccessExample {JSON} {JSON} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504445682",
        "total": "1.15s",
        "cortex": "1.14s",
        "res_send_time": "1504445684"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "pools": {
                    "_attr": {
                        "self": "https://10.20.238.9/storage/pools"
                    },
                    "pool": {
                        "available": {
                            "_attr": {
                                "total": "12636"
                            },
                            "byredundancy": {
                                "raid-1": 6318,
                                "raid-0": 12636,
                                "raid-5": 10109
                            }
                        },
                        "Flashquota": 0,
                        "id": 1,
                        "size": 14014,
                        "DedupProvisioned": {
                            "SystemData": 687,
                            "UserData": 640
                        },
                        "media": {
                            "media": [
                                {
                                    "tier": {
                                        "tier": "",
                                        "_attr": {
                                            "string": "Flash",
                                            "value": "5"
                                        }
                                    },
                                    "_attr": {
                                        "self": "http://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
                                    },
                                    "health": 125
                                },
                                {
                                    "tier": {
                                        "tier": "",
                                        "_attr": {
                                            "string": "Flash",
                                            "value": "5"
                                        }
                                    },
                                    "_attr": {
                                        "self": "http://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                    },
                                    "health": 125
                                }
                            ],
                            "_attr": {
                                "self": "http://10.20.238.9/storage/arrays/USE26000368OW028/media"
                            }
                        },
                        "Flashavailable": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 0
                            }
                        },
                        "ThinThreshold": 75,
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
                        "used": {
                            "_attr": {
                                "total": "1378"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 625
                            }
                        },
                        "globalid": "6001F933001100000000000100000000",
                        "Flashcapacity": 0,
                        "Flashprovisioned": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 0
                            }
                        },
                        "FastSheettotal": 0,
                        "Flashused": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 0
                            }
                        },
                        "provisioned": {
                            "_attr": {
                                "total": "0"
                            },
                            "byredundancy": {
                                "raid-1": 0,
                                "raid-0": 0,
                                "raid-5": 625
                            }
                        },
                        "name": "Pool 1",
                        "DedupUsed": {
                            "SystemData": 687,
                            "UserData": 12
                        },
                        "SlowSheettotal": 59796,
                        "_attr": {
                            "self": "https://10.20.238.9/storage/pools/6001F933001100000000000100000000"
                        },
                        "FastSheetallocated": 0,
                        "volumes": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/volumes"
                            },
                            "volumes": ""
                        },
                        "SlowSheetallocated": 5881
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
        "python": "0.00s",
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
            "message": "Requested STORAGE POOL not found."
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
@apiGroup StoragePools
@apiName UpdateParticularPool
@api {put} /ise/<ise-id>/pools/<pool-id> Update Particular Pool

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} pool-id unique Pool ID

@apiParam {Number} media DataPacID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiParamExample {JSON} Input
{
  "media": "3"
}

@apiSuccessExample {JSON} Success-Response:
HTTP/1.1 201 Created
{
   "message":"success",
   "result":{
      "status_code":201,
      "response":{
         "data":"Pool: 6001F933001000000997000100000000 expanded"
      },
      "error":false
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
        "python": "0.00s",
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
            "message": "Requested STORAGE POOL not found."
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
            "status_codePools": 401,
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
@apiGroup StoragePools
@apiName DeleteParticularPool
@api {delete} /ise/<ise-id>/pools/<pool-id> Delete ParticularPool

@apiParam {Number} ise-id unique ISE ID
@apiParam {Number} pool-id unique Pool ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code

@apiSuccessExample {JSON} {JSON} Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "result":{
      "status_code":200,
      "response":{
         "data":{
            "deleted_pool":"6001F933001000000927000100000000"
         }
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
            "message": "Deleting last pool not allowed. Use reformat"
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
            "message": "Requested STORAGE POOL not found."
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
@apiGroup StoragePools
@apiName PoolsChart
@api {get} /ise/<ise-id>/pools-chart/ Display Pools Chart

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting poolschartdetails

@apiSuccessExample {JSON} {} Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1512631664",
        "total": "2.00s",
        "cortex": "2.00s",
        "res_send_time": "1512631666"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "overall_total": 20999,
                "overall_used": 130,
                "overall_size": 21129,
                "pool_size": 21129
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
@apiGroup StoragePools
@apiName Datareduction
@api {get} /ise/<ise-id>/datareduction/ Display Datareduction

@apiParam {Number} ise-id unique ISE ID

@apiSuccess {String} message It gives success or failure message
@apiSuccess {String} result It gives response_data and status code
@apiSuccess {String} time_taken It contains response time taken for getting poolslist

@apiSuccessExample {JSON} Success-Response:
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1512631583",
        "total": "1.58s",
        "cortex": "1.57s",
        "res_send_time": "1512631585"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "datareduction": {
                    "date": "07-Dec-2017",
                    "_attr": {
                        "self": "https://10.20.238.12/storage/arrays/USE26000368OW009/datareduction"
                    },
                    "dedup": {
                        "blocksize": 8,
                        "buckets": "",
                        "percent": " 0.00",
                        "ratio": " 0.00"
                    },
                    "time": "00:26:20"
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
        "python": "1.10s",
        "req_recv_time": "",
        "total": "1.10s",
        "cortex": "0.00s",
        "res_send_time": ""
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
    url(r'^ise/(?P<ise_id>[\w\-]+)/pools/$', PoolsList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/pools/(?P<pool_id>[\w\-]+)/$',PoolsDetail.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/pools-chart/$', PoolsChart.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/datareduction/$', DataReduction.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.array_info import(ArrayIopsChart, ArrayLatencyChart,
                                 ArrayDedupChart, IseStorageInfo,
                                 IseCardInfo, IseHardwareInfo,
                                 ArrayQueueDepthChart, ArrayDataRateChart,
                                 IseInfo, IseHosts)
"""
@apiGroup Array Info
@apiName GetIseInfo
@api {get} /ise/<ise-id>/ise-info/ Display Ise Info

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseDetails
@apiSuccess {String} message It gives success or error message of the IseDetails
@apiSuccess {String} error It contains error message 

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK

{
    "message": "success",
    "time_taken": {
        "python": "1.91s",
        "req_recv_time": "1504260226",
        "total": "1.91s",
        "cortex": "0.00s",
        "res_send_time": "1504260228"
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
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/files"
                            }
                        },
                        "iomap": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/iomap"
                            },
                            "iomap": ""
                        },
                        "ipaddress1": "10.20.238.9",
                        "ipaddress2": "10.20.238.10",
                        "serialnumber": "USE26000368OW028",
                        "licenseusers": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/licenseusers"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/batteries/1"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/batteries/2"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/batteries"
                            }
                        },
                        "licenses": {
                            "licenses": "",
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/licenses"
                            }
                        },
                        "led": {
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            },
                            "led": ""
                        },
                        "partnumber": "PCA-00563-01-B-1",
                        "id": "2000001F93300110",
                        "contactphone": "",
                        "network": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/network"
                            },
                            "network": ""
                        },
                        "media": {
                            "media": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/1"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media/2"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/media"
                            }
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "snmp": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/snmp"
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
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/1"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/2"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/3"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/4"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/5"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans/6"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/fans"
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
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/performance"
                            }
                        },
                        "revision": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/revision"
                            },
                            "revision": ""
                        },
                        "status": {
                            "_attr": {
                                "string": "Warning",
                                "value": "1"
                            },
                            "details": {
                                "_attr": {
                                    "value": "0x02000400"
                                },
                                "detail": "One or more MRCs in degraded state"
                            }
                        },
                        "vendor": "XIOTECH",
                        "contactname": "",
                        "globalid": "USE26000368OW028",
                        "subscriptions": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/subscriptions"
                            },
                            "subscriptions": ""
                        },
                        "powersupplies": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/1"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/2"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/3"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/powersupplies/4"
                                    }
                                }
                            ]
                        },
                        "productversion": "",
                        "address": "",
                        "manufacturer": "XIOTECH",
                        "jobs": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/jobs"
                            },
                            "jobs": ""
                        },
                        "name": "ISE-USE26000368OW028",
                        "_attr": {
                            "self": "https://10.20.238.9/storage/arrays/USE26000368OW028"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers/1"
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
                                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers/2"
                                    }
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/controllers"
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
                                "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/chronometer"
                            },
                            "chronometer": ""
                        },
                        "hosts": {
                            "host": {
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/hosts/1"
                                },
                                "globalid": 1
                            },
                            "_attr": {
                                "self": "https://10.20.238.9/storage/hosts"
                            }
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
                        "volumes": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/volumes"
                            },
                            "volumes": [
                                {
                                    "status": {
                                        "status": "",
                                        "_attr": {
                                            "string": "Operational",
                                            "value": "0"
                                        }
                                    },
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000071000200000000"
                                    },
                                    "globalid": "6001F933001100000071000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000072000200000000"
                                    },
                                    "globalid": "6001F933001100000072000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000073000200000000"
                                    },
                                    "globalid": "6001F933001100000073000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000074000200000000"
                                    },
                                    "globalid": "6001F933001100000074000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000075000200000000"
                                    },
                                    "globalid": "6001F933001100000075000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000076000200000000"
                                    },
                                    "globalid": "6001F933001100000076000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000077000200000000"
                                    },
                                    "globalid": "6001F933001100000077000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000078000200000000"
                                    },
                                    "globalid": "6001F933001100000078000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000079000200000000"
                                    },
                                    "globalid": "6001F933001100000079000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000007A000200000000"
                                    },
                                    "globalid": "6001F93300110000007A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000007B000200000000"
                                    },
                                    "globalid": "6001F93300110000007B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000007C000200000000"
                                    },
                                    "globalid": "6001F93300110000007C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000007E000200000000"
                                    },
                                    "globalid": "6001F93300110000007E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000081000200000000"
                                    },
                                    "globalid": "6001F933001100000081000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000082000200000000"
                                    },
                                    "globalid": "6001F933001100000082000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000083000200000000"
                                    },
                                    "globalid": "6001F933001100000083000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000084000200000000"
                                    },
                                    "globalid": "6001F933001100000084000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000085000200000000"
                                    },
                                    "globalid": "6001F933001100000085000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000086000200000000"
                                    },
                                    "globalid": "6001F933001100000086000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000087000200000000"
                                    },
                                    "globalid": "6001F933001100000087000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000088000200000000"
                                    },
                                    "globalid": "6001F933001100000088000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000089000200000000"
                                    },
                                    "globalid": "6001F933001100000089000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000008A000200000000"
                                    },
                                    "globalid": "6001F93300110000008A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000008B000200000000"
                                    },
                                    "globalid": "6001F93300110000008B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000008C000200000000"
                                    },
                                    "globalid": "6001F93300110000008C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000008D000200000000"
                                    },
                                    "globalid": "6001F93300110000008D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000008E000200000000"
                                    },
                                    "globalid": "6001F93300110000008E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000008F000200000000"
                                    },
                                    "globalid": "6001F93300110000008F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000090000200000000"
                                    },
                                    "globalid": "6001F933001100000090000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000091000200000000"
                                    },
                                    "globalid": "6001F933001100000091000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000092000200000000"
                                    },
                                    "globalid": "6001F933001100000092000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000093000200000000"
                                    },
                                    "globalid": "6001F933001100000093000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000094000200000000"
                                    },
                                    "globalid": "6001F933001100000094000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000095000200000000"
                                    },
                                    "globalid": "6001F933001100000095000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000096000200000000"
                                    },
                                    "globalid": "6001F933001100000096000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000097000200000000"
                                    },
                                    "globalid": "6001F933001100000097000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000098000200000000"
                                    },
                                    "globalid": "6001F933001100000098000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000099000200000000"
                                    },
                                    "globalid": "6001F933001100000099000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000009A000200000000"
                                    },
                                    "globalid": "6001F93300110000009A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000009B000200000000"
                                    },
                                    "globalid": "6001F93300110000009B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000009C000200000000"
                                    },
                                    "globalid": "6001F93300110000009C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000009D000200000000"
                                    },
                                    "globalid": "6001F93300110000009D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000009E000200000000"
                                    },
                                    "globalid": "6001F93300110000009E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000009F000200000000"
                                    },
                                    "globalid": "6001F93300110000009F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A0000200000000"
                                    },
                                    "globalid": "6001F9330011000000A0000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A1000200000000"
                                    },
                                    "globalid": "6001F9330011000000A1000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A2000200000000"
                                    },
                                    "globalid": "6001F9330011000000A2000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A3000200000000"
                                    },
                                    "globalid": "6001F9330011000000A3000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A4000200000000"
                                    },
                                    "globalid": "6001F9330011000000A4000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A5000200000000"
                                    },
                                    "globalid": "6001F9330011000000A5000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A6000200000000"
                                    },
                                    "globalid": "6001F9330011000000A6000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A7000200000000"
                                    },
                                    "globalid": "6001F9330011000000A7000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A8000200000000"
                                    },
                                    "globalid": "6001F9330011000000A8000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000A9000200000000"
                                    },
                                    "globalid": "6001F9330011000000A9000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000AA000200000000"
                                    },
                                    "globalid": "6001F9330011000000AA000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000AB000200000000"
                                    },
                                    "globalid": "6001F9330011000000AB000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000AC000200000000"
                                    },
                                    "globalid": "6001F9330011000000AC000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000AD000200000000"
                                    },
                                    "globalid": "6001F9330011000000AD000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000AE000200000000"
                                    },
                                    "globalid": "6001F9330011000000AE000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000AF000200000000"
                                    },
                                    "globalid": "6001F9330011000000AF000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B0000200000000"
                                    },
                                    "globalid": "6001F9330011000000B0000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B1000200000000"
                                    },
                                    "globalid": "6001F9330011000000B1000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B2000200000000"
                                    },
                                    "globalid": "6001F9330011000000B2000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B3000200000000"
                                    },
                                    "globalid": "6001F9330011000000B3000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B4000200000000"
                                    },
                                    "globalid": "6001F9330011000000B4000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B5000200000000"
                                    },
                                    "globalid": "6001F9330011000000B5000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B6000200000000"
                                    },
                                    "globalid": "6001F9330011000000B6000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B7000200000000"
                                    },
                                    "globalid": "6001F9330011000000B7000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B8000200000000"
                                    },
                                    "globalid": "6001F9330011000000B8000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000B9000200000000"
                                    },
                                    "globalid": "6001F9330011000000B9000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000BA000200000000"
                                    },
                                    "globalid": "6001F9330011000000BA000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000BB000200000000"
                                    },
                                    "globalid": "6001F9330011000000BB000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000BC000200000000"
                                    },
                                    "globalid": "6001F9330011000000BC000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000BD000200000000"
                                    },
                                    "globalid": "6001F9330011000000BD000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000BE000200000000"
                                    },
                                    "globalid": "6001F9330011000000BE000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000BF000200000000"
                                    },
                                    "globalid": "6001F9330011000000BF000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C0000200000000"
                                    },
                                    "globalid": "6001F9330011000000C0000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C1000200000000"
                                    },
                                    "globalid": "6001F9330011000000C1000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C2000200000000"
                                    },
                                    "globalid": "6001F9330011000000C2000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C3000200000000"
                                    },
                                    "globalid": "6001F9330011000000C3000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C4000200000000"
                                    },
                                    "globalid": "6001F9330011000000C4000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C5000200000000"
                                    },
                                    "globalid": "6001F9330011000000C5000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C6000200000000"
                                    },
                                    "globalid": "6001F9330011000000C6000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C7000200000000"
                                    },
                                    "globalid": "6001F9330011000000C7000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C8000200000000"
                                    },
                                    "globalid": "6001F9330011000000C8000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000C9000200000000"
                                    },
                                    "globalid": "6001F9330011000000C9000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000CA000200000000"
                                    },
                                    "globalid": "6001F9330011000000CA000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000CB000200000000"
                                    },
                                    "globalid": "6001F9330011000000CB000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000CC000200000000"
                                    },
                                    "globalid": "6001F9330011000000CC000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000CD000200000000"
                                    },
                                    "globalid": "6001F9330011000000CD000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000CE000200000000"
                                    },
                                    "globalid": "6001F9330011000000CE000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000CF000200000000"
                                    },
                                    "globalid": "6001F9330011000000CF000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D0000200000000"
                                    },
                                    "globalid": "6001F9330011000000D0000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D1000200000000"
                                    },
                                    "globalid": "6001F9330011000000D1000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D2000200000000"
                                    },
                                    "globalid": "6001F9330011000000D2000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D3000200000000"
                                    },
                                    "globalid": "6001F9330011000000D3000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D4000200000000"
                                    },
                                    "globalid": "6001F9330011000000D4000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D5000200000000"
                                    },
                                    "globalid": "6001F9330011000000D5000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D6000200000000"
                                    },
                                    "globalid": "6001F9330011000000D6000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D7000200000000"
                                    },
                                    "globalid": "6001F9330011000000D7000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D8000200000000"
                                    },
                                    "globalid": "6001F9330011000000D8000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000D9000200000000"
                                    },
                                    "globalid": "6001F9330011000000D9000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000DA000200000000"
                                    },
                                    "globalid": "6001F9330011000000DA000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000DB000200000000"
                                    },
                                    "globalid": "6001F9330011000000DB000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000DC000200000000"
                                    },
                                    "globalid": "6001F9330011000000DC000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000DD000200000000"
                                    },
                                    "globalid": "6001F9330011000000DD000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000DE000200000000"
                                    },
                                    "globalid": "6001F9330011000000DE000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000DF000200000000"
                                    },
                                    "globalid": "6001F9330011000000DF000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E0000200000000"
                                    },
                                    "globalid": "6001F9330011000000E0000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E1000200000000"
                                    },
                                    "globalid": "6001F9330011000000E1000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E2000200000000"
                                    },
                                    "globalid": "6001F9330011000000E2000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E3000200000000"
                                    },
                                    "globalid": "6001F9330011000000E3000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E4000200000000"
                                    },
                                    "globalid": "6001F9330011000000E4000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E5000200000000"
                                    },
                                    "globalid": "6001F9330011000000E5000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E6000200000000"
                                    },
                                    "globalid": "6001F9330011000000E6000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E7000200000000"
                                    },
                                    "globalid": "6001F9330011000000E7000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E8000200000000"
                                    },
                                    "globalid": "6001F9330011000000E8000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000E9000200000000"
                                    },
                                    "globalid": "6001F9330011000000E9000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000EA000200000000"
                                    },
                                    "globalid": "6001F9330011000000EA000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000EB000200000000"
                                    },
                                    "globalid": "6001F9330011000000EB000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000EC000200000000"
                                    },
                                    "globalid": "6001F9330011000000EC000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000ED000200000000"
                                    },
                                    "globalid": "6001F9330011000000ED000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000EE000200000000"
                                    },
                                    "globalid": "6001F9330011000000EE000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000EF000200000000"
                                    },
                                    "globalid": "6001F9330011000000EF000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F0000200000000"
                                    },
                                    "globalid": "6001F9330011000000F0000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F1000200000000"
                                    },
                                    "globalid": "6001F9330011000000F1000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F2000200000000"
                                    },
                                    "globalid": "6001F9330011000000F2000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F3000200000000"
                                    },
                                    "globalid": "6001F9330011000000F3000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F4000200000000"
                                    },
                                    "globalid": "6001F9330011000000F4000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F5000200000000"
                                    },
                                    "globalid": "6001F9330011000000F5000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F6000200000000"
                                    },
                                    "globalid": "6001F9330011000000F6000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F7000200000000"
                                    },
                                    "globalid": "6001F9330011000000F7000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F8000200000000"
                                    },
                                    "globalid": "6001F9330011000000F8000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000F9000200000000"
                                    },
                                    "globalid": "6001F9330011000000F9000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000FA000200000000"
                                    },
                                    "globalid": "6001F9330011000000FA000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000FB000200000000"
                                    },
                                    "globalid": "6001F9330011000000FB000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000FC000200000000"
                                    },
                                    "globalid": "6001F9330011000000FC000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000FD000200000000"
                                    },
                                    "globalid": "6001F9330011000000FD000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000FE000200000000"
                                    },
                                    "globalid": "6001F9330011000000FE000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F9330011000000FF000200000000"
                                    },
                                    "globalid": "6001F9330011000000FF000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000100000200000000"
                                    },
                                    "globalid": "6001F933001100000100000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000101000200000000"
                                    },
                                    "globalid": "6001F933001100000101000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000102000200000000"
                                    },
                                    "globalid": "6001F933001100000102000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000103000200000000"
                                    },
                                    "globalid": "6001F933001100000103000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000104000200000000"
                                    },
                                    "globalid": "6001F933001100000104000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000105000200000000"
                                    },
                                    "globalid": "6001F933001100000105000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000106000200000000"
                                    },
                                    "globalid": "6001F933001100000106000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000107000200000000"
                                    },
                                    "globalid": "6001F933001100000107000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000108000200000000"
                                    },
                                    "globalid": "6001F933001100000108000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000109000200000000"
                                    },
                                    "globalid": "6001F933001100000109000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000010A000200000000"
                                    },
                                    "globalid": "6001F93300110000010A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000010B000200000000"
                                    },
                                    "globalid": "6001F93300110000010B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000010C000200000000"
                                    },
                                    "globalid": "6001F93300110000010C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000010D000200000000"
                                    },
                                    "globalid": "6001F93300110000010D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000010E000200000000"
                                    },
                                    "globalid": "6001F93300110000010E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000010F000200000000"
                                    },
                                    "globalid": "6001F93300110000010F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000110000200000000"
                                    },
                                    "globalid": "6001F933001100000110000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000111000200000000"
                                    },
                                    "globalid": "6001F933001100000111000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000112000200000000"
                                    },
                                    "globalid": "6001F933001100000112000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000113000200000000"
                                    },
                                    "globalid": "6001F933001100000113000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000114000200000000"
                                    },
                                    "globalid": "6001F933001100000114000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000115000200000000"
                                    },
                                    "globalid": "6001F933001100000115000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000116000200000000"
                                    },
                                    "globalid": "6001F933001100000116000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000117000200000000"
                                    },
                                    "globalid": "6001F933001100000117000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000118000200000000"
                                    },
                                    "globalid": "6001F933001100000118000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000119000200000000"
                                    },
                                    "globalid": "6001F933001100000119000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000011A000200000000"
                                    },
                                    "globalid": "6001F93300110000011A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000011B000200000000"
                                    },
                                    "globalid": "6001F93300110000011B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000011C000200000000"
                                    },
                                    "globalid": "6001F93300110000011C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000011D000200000000"
                                    },
                                    "globalid": "6001F93300110000011D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000011E000200000000"
                                    },
                                    "globalid": "6001F93300110000011E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000011F000200000000"
                                    },
                                    "globalid": "6001F93300110000011F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000120000200000000"
                                    },
                                    "globalid": "6001F933001100000120000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000121000200000000"
                                    },
                                    "globalid": "6001F933001100000121000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000122000200000000"
                                    },
                                    "globalid": "6001F933001100000122000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000123000200000000"
                                    },
                                    "globalid": "6001F933001100000123000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000124000200000000"
                                    },
                                    "globalid": "6001F933001100000124000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000125000200000000"
                                    },
                                    "globalid": "6001F933001100000125000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000126000200000000"
                                    },
                                    "globalid": "6001F933001100000126000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000127000200000000"
                                    },
                                    "globalid": "6001F933001100000127000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000128000200000000"
                                    },
                                    "globalid": "6001F933001100000128000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000129000200000000"
                                    },
                                    "globalid": "6001F933001100000129000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000012A000200000000"
                                    },
                                    "globalid": "6001F93300110000012A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000012B000200000000"
                                    },
                                    "globalid": "6001F93300110000012B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000012C000200000000"
                                    },
                                    "globalid": "6001F93300110000012C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000012D000200000000"
                                    },
                                    "globalid": "6001F93300110000012D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000012E000200000000"
                                    },
                                    "globalid": "6001F93300110000012E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000012F000200000000"
                                    },
                                    "globalid": "6001F93300110000012F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000130000200000000"
                                    },
                                    "globalid": "6001F933001100000130000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000131000200000000"
                                    },
                                    "globalid": "6001F933001100000131000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000132000200000000"
                                    },
                                    "globalid": "6001F933001100000132000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000133000200000000"
                                    },
                                    "globalid": "6001F933001100000133000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000134000200000000"
                                    },
                                    "globalid": "6001F933001100000134000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000135000200000000"
                                    },
                                    "globalid": "6001F933001100000135000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000136000200000000"
                                    },
                                    "globalid": "6001F933001100000136000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000137000200000000"
                                    },
                                    "globalid": "6001F933001100000137000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000138000200000000"
                                    },
                                    "globalid": "6001F933001100000138000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000139000200000000"
                                    },
                                    "globalid": "6001F933001100000139000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000013A000200000000"
                                    },
                                    "globalid": "6001F93300110000013A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000013B000200000000"
                                    },
                                    "globalid": "6001F93300110000013B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000013C000200000000"
                                    },
                                    "globalid": "6001F93300110000013C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000013D000200000000"
                                    },
                                    "globalid": "6001F93300110000013D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000013E000200000000"
                                    },
                                    "globalid": "6001F93300110000013E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000013F000200000000"
                                    },
                                    "globalid": "6001F93300110000013F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000140000200000000"
                                    },
                                    "globalid": "6001F933001100000140000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000141000200000000"
                                    },
                                    "globalid": "6001F933001100000141000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000142000200000000"
                                    },
                                    "globalid": "6001F933001100000142000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000143000200000000"
                                    },
                                    "globalid": "6001F933001100000143000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000144000200000000"
                                    },
                                    "globalid": "6001F933001100000144000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000145000200000000"
                                    },
                                    "globalid": "6001F933001100000145000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000146000200000000"
                                    },
                                    "globalid": "6001F933001100000146000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000147000200000000"
                                    },
                                    "globalid": "6001F933001100000147000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000148000200000000"
                                    },
                                    "globalid": "6001F933001100000148000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000149000200000000"
                                    },
                                    "globalid": "6001F933001100000149000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000014A000200000000"
                                    },
                                    "globalid": "6001F93300110000014A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000014B000200000000"
                                    },
                                    "globalid": "6001F93300110000014B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000014C000200000000"
                                    },
                                    "globalid": "6001F93300110000014C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000014D000200000000"
                                    },
                                    "globalid": "6001F93300110000014D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000014E000200000000"
                                    },
                                    "globalid": "6001F93300110000014E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000014F000200000000"
                                    },
                                    "globalid": "6001F93300110000014F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000150000200000000"
                                    },
                                    "globalid": "6001F933001100000150000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000151000200000000"
                                    },
                                    "globalid": "6001F933001100000151000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000152000200000000"
                                    },
                                    "globalid": "6001F933001100000152000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000153000200000000"
                                    },
                                    "globalid": "6001F933001100000153000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000154000200000000"
                                    },
                                    "globalid": "6001F933001100000154000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000155000200000000"
                                    },
                                    "globalid": "6001F933001100000155000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000156000200000000"
                                    },
                                    "globalid": "6001F933001100000156000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000157000200000000"
                                    },
                                    "globalid": "6001F933001100000157000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000158000200000000"
                                    },
                                    "globalid": "6001F933001100000158000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000159000200000000"
                                    },
                                    "globalid": "6001F933001100000159000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000015A000200000000"
                                    },
                                    "globalid": "6001F93300110000015A000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000015B000200000000"
                                    },
                                    "globalid": "6001F93300110000015B000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000015C000200000000"
                                    },
                                    "globalid": "6001F93300110000015C000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000015D000200000000"
                                    },
                                    "globalid": "6001F93300110000015D000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000015E000200000000"
                                    },
                                    "globalid": "6001F93300110000015E000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F93300110000015F000200000000"
                                    },
                                    "globalid": "6001F93300110000015F000200000000"
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
                                        "self": "https://10.20.238.9/storage/volumes/6001F933001100000160000200000000"
                                    },
                                    "globalid": "6001F933001100000160000200000000"
                                }
                            ]
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/pools"
                            },
                            "pool": {
                                "status": {
                                    "status": "",
                                    "_attr": {
                                        "string": "Operational",
                                        "value": "0"
                                    }
                                },
                                "_attr": {
                                    "self": "https://10.20.238.9/storage/pools/6001F933001100000000000100000000"
                                },
                                "globalid": "6001F933001100000000000100000000"
                            }
                        },
                        "model": "ISE4400",
                        "endpoints": {
                            "endpoints": [
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/5001438021E389CC"
                                    },
                                    "globalid": "5001438021E389CC"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/5001438021E389CE"
                                    },
                                    "globalid": "5001438021E389CE"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670601"
                                    },
                                    "globalid": "21000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670600"
                                    },
                                    "globalid": "21000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670603"
                                    },
                                    "globalid": "21000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670602"
                                    },
                                    "globalid": "21000024FF670602"
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/endpoints"
                            }
                        },
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/allocations"
                            },
                            "allocations": [
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670601"
                                    },
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670600"
                                    },
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670603"
                                    },
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670602"
                                    },
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670602"
                                }
                            ]
                        }
                    },
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays"
                    }
                }
            }
        },
        "error": false
    }
}
"""
"""
@apiGroup Array-Info
@apiName GetIseInfo
@api {get} /ise/<ise-id>/ise-info/ Display Ise Info

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseHardware
@apiSuccess {String} message It gives success or error message of the IseHardware
@apiSuccess {String} error It contains error message 

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
@apiGroup Array-Info
@apiName GetIseHosts
@api {get} /ise/<ise-id>/ise-hosts/ Display Ise Hosts

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseHosts
@apiSuccess {String} message It gives success or error message of the IseHosts
@apiSuccess {String} error It contains error message 

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504261826",
        "total": "1.81s",
        "cortex": "1.80s",
        "res_send_time": "1504261827"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "hosts": {
                    "ise_id": 1,
                    "host": {
                        "comment": "",
                        "name": "LAB55",
                        "_attr": {
                            "self": "https://10.20.238.9/storage/hosts/1"
                        },
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.238.9/storage/allocations"
                            },
                            "allocations": [
                                {
                                    "volumename": "V1",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 1,
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 1,
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 1,
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000710002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 1,
                                    "globalid": "6001F9330011000000710002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203820.92",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 2,
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203820.92",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 2,
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203820.92",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 2,
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203820.92",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000720002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 2,
                                    "globalid": "6001F9330011000000720002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203820.95",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 3,
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203820.95",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 3,
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203820.95",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 3,
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203820.95",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000730002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 3,
                                    "globalid": "6001F9330011000000730002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.0",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 4,
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.0",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 4,
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.0",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 4,
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.0",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000740002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 4,
                                    "globalid": "6001F9330011000000740002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.04",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 5,
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.04",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 5,
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.04",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 5,
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.04",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000750002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 5,
                                    "globalid": "6001F9330011000000750002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.07",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 6,
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.07",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 6,
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.07",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 6,
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.07",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000760002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 6,
                                    "globalid": "6001F9330011000000760002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.11",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 7,
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.11",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 7,
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.11",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 7,
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.11",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000770002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 7,
                                    "globalid": "6001F9330011000000770002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.15",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 8,
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.15",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 8,
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.15",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 8,
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.15",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000780002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 8,
                                    "globalid": "6001F9330011000000780002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.19",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 9,
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.19",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 9,
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.19",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 9,
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.19",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F9330011000000790002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 9,
                                    "globalid": "6001F9330011000000790002000000002000001F9330011021000024FF670602"
                                },
                                {
                                    "volumename": "V1-1504203821.23",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670601"
                                    },
                                    "lun": 10,
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670601"
                                },
                                {
                                    "volumename": "V1-1504203821.23",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670600"
                                    },
                                    "lun": 10,
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670600"
                                },
                                {
                                    "volumename": "V1-1504203821.23",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670603"
                                    },
                                    "lun": 10,
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670603"
                                },
                                {
                                    "volumename": "V1-1504203821.23",
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/allocations/6001F93300110000007A0002000000002000001F9330011021000024FF670602"
                                    },
                                    "lun": 10,
                                    "globalid": "6001F93300110000007A0002000000002000001F9330011021000024FF670602"
                                }
                            ]
                        },
                        "mirroredvolumes": {
                            "mirroredvolumes": "",
                            "_attr": {
                                "string": "false",
                                "value": "0"
                            }
                        },
                        "endpoints": {
                            "endpoints": [
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670601"
                                    },
                                    "globalid": "21000024FF670601"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670600"
                                    },
                                    "globalid": "21000024FF670600"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670603"
                                    },
                                    "globalid": "21000024FF670603"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.238.9/storage/endpoints/21000024FF670602"
                                    },
                                    "globalid": "21000024FF670602"
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.238.9/storage/endpoints"
                            }
                        },
                        "type": "Windows",
                        "id": 1
                    },
                    "_attr": {
                        "self": "https://10.20.238.9/storage/hosts"
                    },
                    "hosts": [
                        {
                            "ise_id": 1,
                            "hosts": "LAB55",
                            "host_id": 1
                        }
                    ]
                }
            }
        },
        "error": false
    }
}
"""
"""
@apiGroup Array-Info
@apiName GetIseHosts
@api {get} /ise/<ise-id>/ise-hosts/ Display Ise Info

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseHosts
@apiSuccess {String} message It gives success or error message of the IseHosts
@apiSuccess {String} error It contains error message 

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
@apiGroup Array-Info
@apiName GetIseStorageInfo
@api {get} /ise/<ise-id>/hardware-info/ Display Ise Hardware Info

@apiSuccess {String} result Displays the result
@apiSuccess {String} response It gives response
@apiSuccess {String} data  It contains attributes of the IseHardware
@apiSuccess {String} timetaken It contains response time taken for IseHardware

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "1.10s",
        "req_recv_time": "1504263846",
        "total": "5.47s",
        "cortex": "4.36s",
        "res_send_time": "1504263851"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "uptime": [
                    {
                        "mrc1_uptime": {
                            "hours": 17,
                            "seconds": 30,
                            "_attr": {
                                "duration": "P0DT17H0M30S"
                            },
                            "minutes": 0,
                            "days": 0
                        }
                    }
                ],
                "led": {
                    "led": "enabled"
                },
                "battery": {
                    "battery1": {
                        "string": "Operational",
                        "value": "0"
                    },
                    "battery2": {
                        "string": "Operational",
                        "value": "0"
                    }
                },
                "powersupply": {
                    "ps2": {
                        "string": "Operational",
                        "value": "0"
                    },
                    "ps1": {
                        "string": "Operational",
                        "value": "0"
                    }
                },
                "alert": [
                    "Volume 02 (Storage 01)",
                    "Volume 02 (Storage 01)",
                    "Volume 05 (Storage 01)"
                ],
                "iops": [
                    "Volume 04 (Storage 01)",
                    "Volume 08 (Storage 01)",
                    "Volume 08 (Storage 01)"
                ],
                "blowersps2": {},
                "blowersps1": {},
                "mrc": {
                    "mrc1": {
                        "value": "0"
                    },
                    "mrc2": {
                        "value": "1"
                    }
                },
                "datapac": {
                    "datapac1": {
                        "value": "0x00000000"
                    },
                    "datapac2": {
                        "value": "0x00000000"
                    }
                }
            }
        },
        "error": false
    }
}
"""
"""
@apiGroup Array-Info
@apiName GetIseStorageInfo
@api {get} /ise/<ise-id>/hardware-info/ Display Ise Hardware Info

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseHardware
@apiSuccess {String} message It gives success or error message of the IseHardware
@apiSuccess {String} error It contains error message 

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
@apiGroup Array-Info
@apiName GetIseCardInfo
@api {get} /ise/<ise-id>/card-info/ Display IseCardInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseCard
@apiSuccess {String} message It gives success or error message of the IseCard
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "1.07s",
        "req_recv_time": "1504264230",
        "total": "4.32s",
        "cortex": "3.25s",
        "res_send_time": "1504264235"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "status": {
                    "_attr": {
                        "string": "Warning",
                        "value": "1"
                    },
                    "details": {
                        "_attr": {
                            "value": "0x02000400"
                        },
                        "detail": "One or more MRCs in degraded state"
                    }
                },
                "mrc2_status": "1",
                "ipaddress1": "10.20.238.9",
                "name": "ISE-USE26000368OW028",
                "ipaddress2": "10.20.238.10",
                "serial_no": "USE26000368OW028",
                "mrc2_fwversion": "v4.0.0-7162",
                "hosts": 1,
                "volumes": 237,
                "time": "04:10:34",
                "date": "01-Sep-2017",
                "led": {
                    "_attr": {
                        "string": "enabled",
                        "value": "1"
                    },
                    "led": ""
                },
                "endpoints": 6,
                "mrc1_status": "0",
                "pool": 1,
                "mrc1_fwversion": "v4.0.0-7162"
            }
        },
        "error": false
    }
}
"""
"""
@apiGroup Array-Info
@apiName GetIseCardInfo
@api {get} /ise/<ise-id>/card-info/ Display IseCardInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseCard
@apiSuccess {String} message It gives success or error message of the IseCard
@apiSuccess {String} error It contains error message

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
@apiGroup Array-Info
@apiName IseStorageInfo
@api {get} /ise/<ise-id>/storage-info/ Display IseStorageInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseStorage
@apiSuccess {String} message It gives success or error message of the IseStorage
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "1.40s",
        "req_recv_time": "1504264591",
        "total": "1.40s",
        "cortex": "0.00s",
        "res_send_time": "1504264593"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "size": {
                    "total_size": 14014,
                    "total_used": 1378,
                    "total_available": 12636,
                    "raid_available": {
                        "raid-1": 6318,
                        "raid-0": 12636,
                        "raid-5": 10109
                    }
                }
            }
        },
        "error": false
    }
}
"""
"""
@apiGroup Array-Info
@apiName IseStorageInfo
@api {get} /ise/<ise-id>/storage-info/ Display IseStorageInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for IseStorage
@apiSuccess {String} message It gives success or error message of the IseStorage
@apiSuccess {String} error It contains error message 

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
@apiGroup Array-Info
@apiName ArrayDataRateChart
@api {get} /ise/<ise-id>/array-datarate-chart/ Display ArrayDataRateChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayDataRateChart
@apiSuccess {String} message It gives success or error message of the ArrayDataRateChart
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.54s",
        "req_recv_time": "1504265234",
        "total": "0.54s",
        "cortex": "0.00s",
        "res_send_time": "1504265235"
    },
    "result": {
    "response": {
        "data": [
                {
                    "color": "#ff7f0e",
                    "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                    ],
                    "key": "readkbps"
                },
            {
                "color": "#2ca02c",
                "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                ],
                "key": "writekbps"
            },
            {
                "color": "#7777ff",
                "values": [
                {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                ],
                "key": "totalkbps"
            }
        ]
    }
}
}

"""
"""
@apiGroup Array-Info
@apiName ArrayDataRateChart
@api {get} /ise/<ise-id>/array-datarate-chart/ Display ArrayDataRateChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayDataRateChart
@apiSuccess {String} message It gives success or error message of the ArrayDataRateChart
@apiSuccess {String} error It contains error message

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
@apiGroup Array-Info
@apiName ArrayQueueDepthChart
@api {get} /ise/<ise-id>/array-queuedepth-chart/ Display ArrayQueueDepthChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayQueueDepthChart
@apiSuccess {String} message It gives success or error message of the ArrayQueueDepthChart
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "result": "success",
    "response": {
        "data": [
            {
                "color": "#ff7f0e",
                "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                ],
                "key": "queuedepth"
            }
        ]
    }
}
"""
"""
@apiGroup Array-Info
@apiName ArrayQueueDepthChart
@api {get} /ise/<ise-id>/array-queuedepth-chart/ Display ArrayQueueDepthChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayQueueDepthChart
@apiSuccess {String} message It gives success or error message of the ArrayQueueDepthChart
@apiSuccess {String} error It contains error message

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
@apiGroup Array-Info
@apiName ArrayIopsChart
@api {get} /ise/<ise-id>/array-iops-chart/ Display ArrayIopsChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayIopsChart
@apiSuccess {String} message It gives success or error message of the ArrayIopsChart
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.54s",
        "req_recv_time": "1504265234",
        "total": "0.54s",
        "cortex": "0.00s",
        "res_send_time": "1504265235"
    },
    "result": {
    "response": {
        "data": [
                {
                    "color": "#ff7f0e",
                    "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                    ],
                    "key": "readiops"
                },
            {
                "color": "#2ca02c",
                "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                ],
                "key": "writeiops"
            },
            {
                "color": "#7777ff",
                "values": [
                {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                ],
                "key": "totaliops"
            }
        ]
    }
}
}
"""
"""
@apiGroup Array-Info
@apiName ArrayIopsChart
@api {get} /ise/<ise-id>/array-iops-chart/ Display ArrayIopsChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayIopsChart
@apiSuccess {String} message It gives success or error message of the ArrayIopsChart
@apiSuccess {String} error It contains error message

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
@apiGroup Array-Info
@apiName ArrayLatencyChart
@api {get} /ise/<ise-id>/array-latency-chart/ Display ArrayLatencyChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayLatencyChart
@apiSuccess {String} message It gives success or error message of the ArrayLatencyChart
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.54s",
        "req_recv_time": "1504265234",
        "total": "0.54s",
        "cortex": "0.00s",
        "res_send_time": "1504265235"
    },
    "result": {
    "response": {
        "data": [
                {
                    "color": "#ff7f0e",
                    "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                    ],
                    "key": "readlatency"
                },
            {
                "color": "#2ca02c",
                "values": [
                        {
                            "y": 0,
                            "x": "2017-09-01T04:36:57Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:37:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:38:17Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:27Z"
                        },
                        {
                            "y": 0,
                            "x": "2017-09-01T04:40:57Z"
                        }
                ],
                "key": "writelatency"
            }
        ]
    }
}
"""
"""
@apiGroup Array-Info
@apiName ArrayLatencyChart
@api {get} /ise/<ise-id>/array-latency-chart/ Display ArrayLatencyChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayLatencyChart
@apiSuccess {String} message It gives success or error message of the ArrayLatencyChart
@apiSuccess {String} error It contains error message

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
@apiGroup Array-Info
@apiName ArrayDedupChart
@api {get} /ise/<ise-id>/array-dedup-chart/ Display ArrayDedupChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayDedupChart
@apiSuccess {String} message It gives success or error message of the ArrayDedupChart
@apiSuccess {String} error It contains error message

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "result": "success",
    "response": {
        "data": [
            {
                "color": "#7777ff",
                "values": [
                        {
                            "y": 36,
                            "x": 587
                        },
                        {
                            "y": 54,
                            "x": 505
                        },
                        {
                            "y": 68,
                            "x": 833
                        }
                    ],
                "key": "dedup"
            }
        ]
    }
}
"""
"""
@apiGroup Array-Info
@apiName ArrayDedupChart
@api {get} /ise/<ise-id>/array-dedup-chart/ Display ArrayDedupChartInfo

@apiSuccess {String} result It contains response and its attributes
@apiSuccess {String} timetaken It contains response time taken for ArrayDedupChart
@apiSuccess {String} message It gives success or error message of the ArrayDedupChart
@apiSuccess {String} error It contains error message

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
    url(r'^ise/(?P<ise_id>[\w\-]+)/ise-info/$', IseInfo.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/ise-hosts/$', IseHosts.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/hardware-info/$', IseHardwareInfo.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/card-info/$', IseCardInfo.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/storage-info/$', IseStorageInfo.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/array-datarate-chart/$', ArrayDataRateChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/array-queuedepth-chart/$', ArrayQueueDepthChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/array-iops-chart/$', ArrayIopsChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/array-latency-chart/$', ArrayLatencyChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/array-dedup-chart/$', ArrayDedupChart.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

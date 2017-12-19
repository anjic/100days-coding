from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.host_views import(HostsList, HostDetail, Allocation)

"""
@apiGroup Hosts
@apiName GetHostsList
@api {get} /<ise-id>/ise/hosts Display List of Hosts

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Host

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "result": "success",
    "response": {
        "values": 200,
        "data": {
            "hosts": {
                "_attr": {
                    "self": "https://10.20.225.48/storage/hosts"
                },
                "hosts": [
                    {
                        "comment": "ssss",
                        "name": "REMOTEhost1",
                        "_attr": {
                            "self": "https://10.20.225.48/storage/hosts/1"
                        },
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": [
                                {
                                    "volumename": "REMOTEVOL",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EC00002000000002000001F93104B002100001B320E865D"
                                    },
                                    "lun": 0,
                                    "globalid": "6001F93104B000010EC00002000000002000001F93104B002100001B320E865D"
                                },
                                {
                                    "volumename": "REMOTEVOL",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EC00002000000002000001F93104B002101001B322E865D"
                                    },
                                    "lun": 0,
                                    "globalid": "6001F93104B000010EC00002000000002000001F93104B002101001B322E865D"
                                },
                                {
                                    "volumename": "xml",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F0C0002000000002000001F93104B002100001B320E865D"
                                    },
                                    "lun": 10,
                                    "globalid": "6001F93104B000010F0C0002000000002000001F93104B002100001B320E865D"
                                },
                                {
                                    "volumename": "xml",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F0C0002000000002000001F93104B002101001B322E865D"
                                    },
                                    "lun": 10,
                                    "globalid": "6001F93104B000010F0C0002000000002000001F93104B002101001B322E865D"
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
                                        "self": "https://10.20.225.48/storage/endpoints/2100001B320E865D"
                                    },
                                    "globalid": "2100001B320E865D"
                                },
                                {
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/endpoints/2101001B322E865D"
                                    },
                                    "globalid": "2101001B322E865D"
                                }
                            ],
                            "_attr": {
                                "self": "https://10.20.225.48/storage/endpoints"
                            }
                        },
                        "type": "Windows",
                        "id": 1
                    },
                    {
                        "comment": "t",
                        "name": "hh",
                        "_attr": {
                            "self": "https://10.20.225.48/storage/hosts/3"
                        },
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": [
                                {
                                    "volumename": "test-vol",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EF20002000000002000001F93104B00210000E08B88B07F"
                                    },
                                    "lun": 150,
                                    "globalid": "6001F93104B000010EF20002000000002000001F93104B00210000E08B88B07F"
                                },
                                {
                                    "volumename": "vol2",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EF30002000000002000001F93104B00210000E08B88B07F"
                                    },
                                    "lun": 100,
                                    "globalid": "6001F93104B000010EF30002000000002000001F93104B00210000E08B88B07F"
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
                            "endpoint": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/endpoints/210000E08B88B07F"
                                },
                                "globalid": "210000E08B88B07F"
                            },
                            "_attr": {
                                "self": "https://10.20.225.48/storage/endpoints"
                            }
                        },
                        "type": "Windows",
                        "id": 3
                    }
                ]
            }
        }
    }
}
"""

"""
@apiGroup Hosts
@apiName GetParticularHost
@api {get} /<ise-id>/ise/hosts/<host-id>/ Display Particular Host

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Host

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK

{
    "result": "success",
    "response": {
        "values": 200,
        "data": {
            "hosts": {
                "host": {
                    "comment": "",
                    "name": "IO-Host",
                    "_attr": {
                        "self": "https://10.20.225.48/storage/hosts/1"
                    },
                    "allocations": {
                        "_attr": {
                            "self": "https://10.20.225.48/storage/allocations"
                        },
                        "allocations": [
                            {
                                "volumename": "IO-Volume",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B00210000E08B88B07F"
                                },
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B00210000E08B88B07F"
                            },
                            {
                                "volumename": "IO-Volume",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B002101001B322E865D"
                                },
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B002101001B322E865D"
                            },
                            {
                                "volumename": "IO-Volume",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B002100001B320E865D"
                                },
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B002100001B320E865D"
                            },
                            {
                                "volumename": "IO-Volume",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B00210100E08BA8B07F"
                                },
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B00210100E08BA8B07F"
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
                                    "self": "https://10.20.225.48/storage/endpoints/210000E08B88B07F"
                                },
                                "globalid": "210000E08B88B07F"
                            },
                            {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/endpoints/2101001B322E865D"
                                },
                                "globalid": "2101001B322E865D"
                            },
                            {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/endpoints/2100001B320E865D"
                                },
                                "globalid": "2100001B320E865D"
                            },
                            {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/endpoints/210100E08BA8B07F"
                                },
                                "globalid": "210100E08BA8B07F"
                            }
                        ],
                        "_attr": {
                            "self": "https://10.20.225.48/storage/endpoints"
                        }
                    },
                    "type": "Windows",
                    "id": 1
                },
                "_attr": {
                    "self": "https://10.20.225.48/storage/hosts"
                }
            }
        }
    }
}
"""
"""
@apiGroup Hosts
@apiName UpdateParticularHost
@api {post} /ise/<ise-id>/hosts/<host-id> Update Particular Host

@apiParam {Integer} host-id Unique HostID.

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Volume

@apiSuccessExample Success-Response:
HTTP/1.1 201 Created
{  
   "result":"success",
   "response":{  
      "values":201,
      "data":"A host was modified: Host",
      "removed_endpoint_res":[  

      ]
   }
}
"""
"""
@apiGroup Hosts
@apiName DeleteParticularHost
@api {delete} /ise/<ise-id>/hosts/<host-id> Delete Particular Host

@apiParam {Integer} host-id Unique HostID.

@apiSuccess {Integer} host-id Unique HostID.

@apiSuccessExample Success-Response:
    HTTP 204 No Content
"""
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/hosts/(?P<hostid>[\w\-]+)/allocation/$', Allocation.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/hosts/(?P<hostid>[\w\-]+)/$', HostDetail.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/hosts/$', HostsList.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

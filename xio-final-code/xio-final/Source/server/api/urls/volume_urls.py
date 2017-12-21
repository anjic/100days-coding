from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.volume_views import( VolumesList,
                                    VolumeDetail,
                                    Allocation,
                                    VolumeChart)

"""
@apiGroup Volumes
@apiName GetVolumesList
@api {get} /<ise-id>/ise/volumes Display List of Volumes

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Volume

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK

{
    "result": "success",
    "response": {
        "values": 200,
        "data": {
            "volumes": {
                "_attr": {
                    "self": "https://10.20.225.48/storage/volumes"
                },
                "volumes": [
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 20480,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF2000200000000",
                        "size": 10,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "allocation": {
                                "hostname": "hh",
                                "lun": 150,
                                "globalid": "6001F93104B000010EF20002000000002000001F93104B00210000E08B88B07F",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EF20002000000002000001F93104B00210000E08B88B07F"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            }
                        },
                        "globalid": "6001F93104B000010EF2000200000000",
                        "createdate": "Wed May  3 10:39:42 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "test-vol",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF2000200000000"
                        },
                        "localid": 16,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 1280,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 15,
                        "snapshots": "",
                        "MapMaxWritten": 14336,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF3000200000000",
                        "size": 7,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 245760,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-1",
                                    "value": "1"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 896,
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
                        "allocpercent": 100,
                        "allocations": {
                            "allocation": {
                                "hostname": "hh",
                                "lun": 100,
                                "globalid": "6001F93104B000010EF30002000000002000001F93104B00210000E08B88B07F",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EF30002000000002000001F93104B00210000E08B88B07F"
                                }
                            },
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            }
                        },
                        "globalid": "6001F93104B000010EF3000200000000",
                        "createdate": "Wed May  3 10:42:38 2017",
                        "MapNumberSheetsAllocated": 60,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "vol2",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF3000200000000"
                        },
                        "localid": 17,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "fully allocated",
                                "value": "0"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 896,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 12288,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF4000200000000",
                        "size": 6,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 768,
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
                        "allocpercent": 100,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EF4000200000000",
                        "createdate": "Wed May  3 10:46:45 2017",
                        "MapNumberSheetsAllocated": 32,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "test123",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF4000200000000"
                        },
                        "localid": 18,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "fully allocated",
                                "value": "0"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 768,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 45056,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EC0000200000000",
                        "size": 22,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 100.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 2816,
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
                        "allocpercent": 100,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": [
                                {
                                    "hostname": "REMOTEhost1",
                                    "lun": 0,
                                    "globalid": "6001F93104B000010EC00002000000002000001F93104B002100001B320E865D",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EC00002000000002000001F93104B002100001B320E865D"
                                    }
                                },
                                {
                                    "hostname": "REMOTEhost1",
                                    "lun": 0,
                                    "globalid": "6001F93104B000010EC00002000000002000001F93104B002101001B322E865D",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010EC00002000000002000001F93104B002101001B322E865D"
                                    }
                                }
                            ]
                        },
                        "globalid": "6001F93104B000010EC0000200000000",
                        "createdate": "Thu Apr 27 07:01:53 2017",
                        "MapNumberSheetsAllocated": 118,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 45029,
                        "productid": "ISE3401",
                        "name": "REMOTEVOL",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EC0000200000000"
                        },
                        "localid": 19,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 2816,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 14336,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF5000200000000",
                        "size": 7,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EF5000200000000",
                        "createdate": "Wed May  3 10:48:16 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "qos",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF5000200000000"
                        },
                        "localid": 20,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 896,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 15,
                        "snapshots": "",
                        "MapMaxWritten": 20480,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF6000200000000",
                        "size": 10,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 245760,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-1",
                                    "value": "1"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 1280,
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
                        "allocpercent": 100,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EF6000200000000",
                        "createdate": "Wed May  3 10:49:54 2017",
                        "MapNumberSheetsAllocated": 86,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "qos1",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF6000200000000"
                        },
                        "localid": 21,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "fully allocated",
                                "value": "0"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 1280,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 10240,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF7000200000000",
                        "size": 5,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EF7000200000000",
                        "createdate": "Wed May  3 12:44:13 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "fggh",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF7000200000000"
                        },
                        "localid": 22,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 640,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 47104,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF8000200000000",
                        "size": 23,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EF8000200000000",
                        "createdate": "Wed May  3 13:17:37 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "karthik",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF8000200000000"
                        },
                        "localid": 23,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 2944,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 15,
                        "snapshots": "",
                        "MapMaxWritten": 16384,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EF9000200000000",
                        "size": 8,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 245760,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-1",
                                    "value": "1"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 1024,
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
                        "allocpercent": 100,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EF9000200000000",
                        "createdate": "Wed May  3 13:18:43 2017",
                        "MapNumberSheetsAllocated": 69,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "karthi",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EF9000200000000"
                        },
                        "localid": 24,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "fully allocated",
                                "value": "0"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 1024,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "nnnn",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 14336,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EFA000200000000",
                        "size": 7,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EFA000200000000",
                        "createdate": "Thu May  4 07:59:54 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "yyt",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EFA000200000000"
                        },
                        "localid": 25,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 896,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 15,
                        "snapshots": "",
                        "MapMaxWritten": 2048,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EFB000200000000",
                        "size": 1,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 245760,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-1",
                                    "value": "1"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EFB000200000000",
                        "createdate": "Thu May  4 08:05:44 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "test",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EFB000200000000"
                        },
                        "localid": 26,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 128,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 47104,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F0B000200000000",
                        "size": 23,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F0B000200000000",
                        "createdate": "Thu May  4 10:46:28 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "ccc",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F0B000200000000"
                        },
                        "localid": 27,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 2944,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 6144,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010EFF000200000000",
                        "size": 3,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010EFF000200000000",
                        "createdate": "Thu May  4 08:28:12 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "ffd",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010EFF000200000000"
                        },
                        "localid": 28,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 384,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 6144,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F05000200000000",
                        "size": 3,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F05000200000000",
                        "createdate": "Thu May  4 10:21:15 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "de",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F05000200000000"
                        },
                        "localid": 29,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 384,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 2048,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F06000200000000",
                        "size": 1,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F06000200000000",
                        "createdate": "Thu May  4 10:21:54 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "er",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F06000200000000"
                        },
                        "localid": 30,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 128,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 2048,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F08000200000000",
                        "size": 1,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F08000200000000",
                        "createdate": "Thu May  4 10:31:11 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "tess",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F08000200000000"
                        },
                        "localid": 31,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 128,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 8192,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F0A000200000000",
                        "size": 4,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F0A000200000000",
                        "createdate": "Thu May  4 10:39:40 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "ret",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F0A000200000000"
                        },
                        "localid": 32,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 512,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 2048,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F0C000200000000",
                        "size": 1,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": [
                                {
                                    "hostname": "REMOTEhost1",
                                    "lun": 10,
                                    "globalid": "6001F93104B000010F0C0002000000002000001F93104B002100001B320E865D",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F0C0002000000002000001F93104B002100001B320E865D"
                                    }
                                },
                                {
                                    "hostname": "REMOTEhost1",
                                    "lun": 10,
                                    "globalid": "6001F93104B000010F0C0002000000002000001F93104B002101001B322E865D",
                                    "_attr": {
                                        "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F0C0002000000002000001F93104B002101001B322E865D"
                                    }
                                }
                            ]
                        },
                        "globalid": "6001F93104B000010F0C000200000000",
                        "createdate": "Thu May  4 10:55:34 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "xml",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F0C000200000000"
                        },
                        "localid": 33,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 128,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 2048,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F0F000200000000",
                        "size": 1,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F0F000200000000",
                        "createdate": "Mon May  8 10:52:50 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "tom",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F0F000200000000"
                        },
                        "localid": 34,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 128,
                        "QosStatusStr": "Okay"
                    },
                    {
                        "comment": "",
                        "iomap": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "iomap": ""
                        },
                        "mirrors": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/mirrors"
                            },
                            "mirrors": ""
                        },
                        "MapSheetMappableEntries": 24,
                        "snapshots": "",
                        "MapMaxWritten": 2048,
                        "IOPSburst": 0,
                        "iops": 0,
                        "QosSeconds": 0,
                        "IOPSmin": 0,
                        "id": "6001F93104B000010F10000200000000",
                        "size": 1,
                        "vendorid": "XIOTECH",
                        "MapSheetsSizeInBlocks": 393216,
                        "QosStatus": 0,
                        "BlocksInBytes": 512,
                        "configurationpolicy": {
                            "writecache": "Write-Back",
                            "redundancy": {
                                "_attr": {
                                    "string": "RAID-5",
                                    "value": "5"
                                },
                                "redundancy": ""
                            }
                        },
                        "affinity": {
                            "_attr": {
                                "string": "CADP",
                                "value": "0"
                            },
                            "flashpercent": 0.0
                        },
                        "type": "Primary",
                        "MapNumberAllocated": 0,
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
                        "allocpercent": 0,
                        "allocations": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/allocations"
                            },
                            "allocations": ""
                        },
                        "globalid": "6001F93104B000010F10000200000000",
                        "createdate": "Mon May  8 10:52:53 2017",
                        "MapNumberSheetsAllocated": 0,
                        "wp": {
                            "_attr": {
                                "string": "disabled",
                                "value": "0"
                            },
                            "wp": ""
                        },
                        "MapNumberWritten": 0,
                        "productid": "ISE3401",
                        "name": "tom-1494237597.42",
                        "MapWrittenEntrySizeInBlocks": 1024,
                        "_attr": {
                            "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F10000200000000"
                        },
                        "localid": 35,
                        "qosmode": {
                            "qosmode": "",
                            "_attr": {
                                "string": "enabled",
                                "value": "1"
                            }
                        },
                        "IOPSmax": 0,
                        "alloctype": {
                            "_attr": {
                                "string": "thin provisioned",
                                "value": "1"
                            },
                            "alloctype": ""
                        },
                        "pools": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools"
                            },
                            "pool": {
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                                },
                                "id": 1,
                                "globalid": "6001F93104B000010E21000100000000"
                            }
                        },
                        "MapEntrySizeInBlocks": 16384,
                        "MapNumberProvisioned": 128,
                        "QosStatusStr": "Okay"
                    }
                ]
            }
        }
    }
}
"""
"""
@apiGroup Volumes
@apiName CreateNewVolume
@api {post} /<ise-id>/ise/volumes Create Volumes

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Volume

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
    {
    result: "success",
    response:{values: 201, data: "A new volume created: msystest(6001F93104B000010EFD000200000000)"}
    }
"""
"""
@apiGroup Volumes
@apiName GetParticularVolume
@api {get} /ise/<ise-id>/volumes/<volume-id>/ Display Particular Volume

@apiparam {String} volume-id Unique VolumeID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Volume

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "result": "success",
    "response": {
        "values": 200,
        "data": {
            "volumes": {
                "volume": {
                    "comment": "",
                    "iomap": {
                        "_attr": {
                            "string": "disabled",
                            "value": "0"
                        },
                        "iomap": ""
                    },
                    "mirrors": {
                        "_attr": {
                            "self": "https://10.20.225.48/storage/mirrors"
                        },
                        "mirrors": ""
                    },
                    "MapSheetMappableEntries": 24,
                    "snapshots": "",
                    "MapMaxWritten": 2045952,
                    "IOPSburst": 0,
                    "iops": 1435,
                    "QosSeconds": 0,
                    "IOPSmin": 0,
                    "id": "6001F93104B000010F12000200000000",
                    "size": 999,
                    "vendorid": "XIOTECH",
                    "MapSheetsSizeInBlocks": 393216,
                    "QosStatus": 0,
                    "BlocksInBytes": 512,
                    "configurationpolicy": {
                        "writecache": "Write-Back",
                        "redundancy": {
                            "_attr": {
                                "string": "RAID-5",
                                "value": "5"
                            },
                            "redundancy": ""
                        }
                    },
                    "affinity": {
                        "_attr": {
                            "string": "CADP",
                            "value": "0"
                        },
                        "flashpercent": 0.55
                    },
                    "type": "Primary",
                    "MapNumberAllocated": 4366,
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
                    "allocpercent": 3,
                    "allocations": {
                        "_attr": {
                            "self": "https://10.20.225.48/storage/allocations"
                        },
                        "allocations": [
                            {
                                "hostname": "IO-Host",
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B00210000E08B88B07F",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B00210000E08B88B07F"
                                }
                            },
                            {
                                "hostname": "IO-Host",
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B002101001B322E865D",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B002101001B322E865D"
                                }
                            },
                            {
                                "hostname": "IO-Host",
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B002100001B320E865D",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B002100001B320E865D"
                                }
                            },
                            {
                                "hostname": "IO-Host",
                                "lun": 1,
                                "globalid": "6001F93104B000010F120002000000002000001F93104B00210100E08BA8B07F",
                                "_attr": {
                                    "self": "https://10.20.225.48/storage/allocations/6001F93104B000010F120002000000002000001F93104B00210100E08BA8B07F"
                                }
                            }
                        ]
                    },
                    "globalid": "6001F93104B000010F12000200000000",
                    "createdate": "Tue May  9 07:09:11 2017",
                    "MapNumberSheetsAllocated": 182,
                    "wp": {
                        "_attr": {
                            "string": "disabled",
                            "value": "0"
                        },
                        "wp": ""
                    },
                    "MapNumberWritten": 69787,
                    "productid": "ISE3401",
                    "name": "IO-Volume",
                    "MapWrittenEntrySizeInBlocks": 1024,
                    "_attr": {
                        "self": "https://10.20.225.48/storage/volumes/6001F93104B000010F12000200000000"
                    },
                    "localid": 16,
                    "qosmode": {
                        "qosmode": "",
                        "_attr": {
                            "string": "enabled",
                            "value": "1"
                        }
                    },
                    "IOPSmax": 0,
                    "alloctype": {
                        "_attr": {
                            "string": "thin provisioned",
                            "value": "1"
                        },
                        "alloctype": ""
                    },
                    "pools": {
                        "_attr": {
                            "self": "https://10.20.225.48/storage/pools"
                        },
                        "pool": {
                            "_attr": {
                                "self": "https://10.20.225.48/storage/pools/6001F93104B000010E21000100000000"
                            },
                            "id": 1,
                            "globalid": "6001F93104B000010E21000100000000"
                        }
                    },
                    "MapEntrySizeInBlocks": 16384,
                    "MapNumberProvisioned": 127872,
                    "QosStatusStr": "Okay"
                },
                "_attr": {
                    "self": "https://10.20.225.48/storage/volumes"
                }
            }
        }
    }
}

"""
"""
@apiGroup Volumes
@apiName UpdateParticularVolume
@api {post} /ise/<ise-id>/volumes/<volume-id>/ Update Particular Volume


@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the Volume

@apiSuccessExample Success-Response:
HTTP/1.1 201 Created
    {
    result: "success", 
    response: {values: 201, data: "Volume msystest was modified."}
    }

"""
"""
@apiGroup Volumes
@apiName DeleteParticularVolume
@api {delete} /ise/<ise-id>/volumes/<volume-id>/ Delete Particular Volume

@apiParam {Integer} volume-id Unique VolumeID.

@apiSuccess {Integer} volume-id Unique VolumeID.

@apiSuccessExample Success-Response:
    HTTP 204 No Content
"""
urlpatterns = [
    
    url(r'^ise/(?P<ise_id>[\w\-]+)/volumes/allocation/$', Allocation.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/volumes/(?P<volume_id>[\w\-]+)/$', VolumeDetail.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/volumes/$', VolumesList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/volumes-chart/$', VolumeChart.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

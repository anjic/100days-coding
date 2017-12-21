from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.sangroup_views import (SanGroupList, SanGroupDetail,
                                      SanGroupHost)
"""
@apiGroup Sangroup
@apiName GetSangroupList
@api {get} /sangroup/ Display List of Sangroup

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for displaying list of Sangroups.
@apiSuccess {String} message It gives success or error message.
@apiSuccess {String} error It contains error messages.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.02s",
        "req_recv_time": "1507792773",
        "total": "0.02s",
        "cortex": "0.0s",
        "res_send_time": "1507792773"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": [
                {
                    "sangroup_id": 2,
                    "sangroup_name": "G4",
                    "comment": "",
                    "created_date": "2017-10-03T09:37:10.810924Z",
                    "updated_date": "2017-10-03T09:37:10.810960Z",
                    "created_by": "",
                    "modified_by": "",
                    "is_delete": false,
                    "ise": [
                        {
                            "ise_name": "NAME",
                            "id": 9
                        },
                        {
                            "ise_name": "ISE-USE26000368OW009",
                            "id": 10
                        }
                    ]
                },
                {
                    "sangroup_id": 3,
                    "sangroup_name": "G3",
                    "comment": "",
                    "created_date": "2017-10-03T09:41:27.465443Z",
                    "updated_date": "2017-10-03T09:41:27.465476Z",
                    "created_by": "1",
                    "modified_by": "1",
                    "is_delete": false,
                    "ise": [
                        {
                            "ise_name": "ISE-3DE100RT",
                            "id": 8
                        },
                        {
                            "ise_name": "ISE-1BC100C5",
                            "id": 7
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
@apiGroup Sangroup
@apiName CreateSangroup
@api {post} /sangroup/ Create Sangroup

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for creating Sangroup.
@apiSuccess {String} message It gives success or error message.
@apiSuccess {String} error It contains error messages.

@apiParam {String} comment unique ISE ID.

@apiParamExample {json} Input.
{
  'comment': 'test sangroup', 
  'sangroup_name': 'test', 
}

@apiSuccessExample Success-Response:
HTTP/1.1 201 Created
{
   "message":"success",
   "time_taken":{
      "python":"",
      "req_recv_time":"",
      "total":"",
      "cortex":"",
      "res_send_time":""
   },
   "result":{
      "status_code":201,
      "response":{
         "data":{
            "sangroup_id":4,
            "sangroup_name":"test",
            "comment":"test sangroup",
            "created_date":"2017-09-03T14:14:11.058350Z",
            "updated_date":"2017-09-03T14:14:11.058422Z",
            "created_by":"1",
            "modified_by":"1",
            "is_delete":false
         }
      },
      "error":false
   }
}

@apiError BadRequest BadRquest
@apiError ConnectionError GatewayTimeout

@apiErrorExample Error-Response:
HTTP/1.1 400 Bad Request
{
   "message":"fail",
   "time_taken":{
      "python":"",
      "req_recv_time":"",
      "total":"",
      "cortex":"",
      "res_send_time":""
   },
   "result":{
      "status_code":400,
      "response":{
         "data":[

         ]
      },
      "error":{
         "status_code":400,
         "message":{
            "sangroup_name":[
               "SanGroup with this sangroup name already exists."
            ]
         }
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
@apiGroup Sangroup
@apiName GetParticularSangroup
@api {get} /sangroup/<id> Display Particular Sangroup

@apiparam {Integer} id Unique SangroupID

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for displaying particular Sangroup.
@apiSuccess {String} message It gives success or error message.
@apiSuccess {String} error It contains error messages.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504450041",
        "total": "4.35s",
        "cortex": "4.34s",
        "res_send_time": "1504450046"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "comment": "",
                "updated_date": "2017-08-31T07:52:01.294644Z",
                "sangroup_name": "msys",
                "modified_by": "",
                "is_delete": false,
                "created_by": "",
                "created_date": "2017-08-31T07:52:01.294554Z",
                "sangroup_id": 1,
                "ise": [
                    {
                        "ip_secondary": "10.20.238.10",
                        "ise_name": "ISE-USE26000368OW028",
                        "raw_data": "\"{\\\"status\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"},\\\"details\\\":{\\\"_attr\\\":{\\\"value\\\":\\\"0x00000000\\\"},\\\"detail\\\":\\\"None\\\"}},\\\"contactemail\\\":\\\"\\\",\\\"serialnumber\\\":\\\"USE26000368OW028\\\",\\\"vendor\\\":\\\"XIOTECH\\\",\\\"name\\\":\\\"ISE-USE26000368OW028\\\",\\\"globalid\\\":\\\"USE26000368OW028\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.10/storage/arrays/USE26000368OW028\\\"},\\\"capabilities\\\":[{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Storage\\\",\\\"value\\\":\\\"3\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Block Server\\\",\\\"value\\\":\\\"15\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Basic ISE Mirror\\\",\\\"value\\\":\\\"40001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Data Migration\\\",\\\"value\\\":\\\"40002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Copy\\\",\\\"value\\\":\\\"40003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Active-Active ISE Mirror\\\",\\\"value\\\":\\\"40004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Witness\\\",\\\"value\\\":\\\"40005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Orchestrator-disabled\\\",\\\"value\\\":\\\"47001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Performance Response Time in Microseconds\\\",\\\"value\\\":\\\"49001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"IO Access Mapping\\\",\\\"value\\\":\\\"49002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Affinity\\\",\\\"value\\\":\\\"49003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Quality of Service IOPS\\\",\\\"value\\\":\\\"49004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin Provisioning\\\",\\\"value\\\":\\\"49005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Clones\\\",\\\"value\\\":\\\"49006\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin-Clones\\\",\\\"value\\\":\\\"49007\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin CADP\\\",\\\"value\\\":\\\"49008\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Affinity Conversion\\\",\\\"value\\\":\\\"49009\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thick to Thin Conversion\\\",\\\"value\\\":\\\"49010\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"One Step Snap Create\\\",\\\"value\\\":\\\"49011\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Data Deduplication\\\",\\\"value\\\":\\\"49012\\\"}}],\\\"controllers\\\":{\\\"controllers\\\":[{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:09:3D:02:61:71\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.10/storage/arrays/USE26000368OW028/controllers/1\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Secondary\\\",\\\"value\\\":\\\"0\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-7155\\\",\\\"dnsname\\\":\\\"10.20.238.10\\\",\\\"ipaddress\\\":\\\"10.20.238.9\\\"},{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:09:3D:02:61:3F\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.10/storage/arrays/USE26000368OW028/controllers/2\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Primary\\\",\\\"value\\\":\\\"1\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-7155\\\",\\\"dnsname\\\":\\\"10.20.238.9\\\",\\\"ipaddress\\\":\\\"10.20.238.10\\\"}],\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.238.10/storage/arrays/USE26000368OW028/controllers\\\"}},\\\"chronometer\\\":{\\\"timezone\\\":\\\"MST\\\",\\\"dst\\\":\\\"disabled\\\",\\\"_attr\\\":{\\\"date\\\":\\\"31-Aug-2017\\\",\\\"time\\\":\\\"00:51:35\\\"},\\\"timezonesetting\\\":\\\"MST\\\"},\\\"location\\\":\\\"\\\",\\\"contactname\\\":\\\"\\\",\\\"address\\\":\\\"\\\",\\\"contactphone\\\":\\\"\\\",\\\"model\\\":\\\"ISE4400\\\",\\\"id\\\":\\\"2000001F93300110\\\"}\"",
                        "serial_no": "USE26000368OW028",
                        "hosts": 3,
                        "volumes": 237,
                        "pools": 1,
                        "time_stamp": "2017-08-31T07:52:01.245Z",
                        "endpoints": 6,
                        "id": 1,
                        "ip_primary": "10.20.238.9",
                        "size": {
                            "total_size": 14014,
                            "total_used": 1378,
                            "available": 12636
                        }
                    },
                    {
                        "ip_secondary": "10.20.228.252",
                        "ise_name": "FooBar",
                        "raw_data": "\"{\\\"status\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Warning\\\",\\\"value\\\":\\\"1\\\"},\\\"details\\\":{\\\"_attr\\\":{\\\"value\\\":\\\"0x00000002\\\"},\\\"detail\\\":\\\"Component Degraded\\\"}},\\\"contactemail\\\":\\\"\\\",\\\"serialnumber\\\":\\\"1BC100C5\\\",\\\"vendor\\\":\\\"XIOTECH\\\",\\\"name\\\":\\\"FooBar\\\",\\\"globalid\\\":\\\"1BC100C5\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.227.120/storage/arrays/1BC100C5\\\"},\\\"capabilities\\\":[{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Storage\\\",\\\"value\\\":\\\"3\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Block Server\\\",\\\"value\\\":\\\"15\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Basic ISE Mirror\\\",\\\"value\\\":\\\"40001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Data Migration\\\",\\\"value\\\":\\\"40002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Copy\\\",\\\"value\\\":\\\"40003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Active-Active ISE Mirror\\\",\\\"value\\\":\\\"40004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"ISE Mirror Witness\\\",\\\"value\\\":\\\"40005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Orchestrator-disabled\\\",\\\"value\\\":\\\"47001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Performance Response Time in Microseconds\\\",\\\"value\\\":\\\"49001\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"IO Access Mapping\\\",\\\"value\\\":\\\"49002\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Affinity\\\",\\\"value\\\":\\\"49003\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Volume Quality of Service IOPS\\\",\\\"value\\\":\\\"49004\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin Provisioning\\\",\\\"value\\\":\\\"49005\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Clones\\\",\\\"value\\\":\\\"49006\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin-Clones\\\",\\\"value\\\":\\\"49007\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thin CADP\\\",\\\"value\\\":\\\"49008\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Affinity Conversion\\\",\\\"value\\\":\\\"49009\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Thick to Thin Conversion\\\",\\\"value\\\":\\\"49010\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"One Step Snap Create\\\",\\\"value\\\":\\\"49011\\\"}},{\\\"capability\\\":\\\"\\\",\\\"_attr\\\":{\\\"type\\\":\\\"source\\\",\\\"string\\\":\\\"Data Deduplication\\\",\\\"value\\\":\\\"49012\\\"}}],\\\"controllers\\\":{\\\"controllers\\\":[{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:1F:93:20:05:78\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.227.120/storage/arrays/1BC100C5/controllers/1\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Primary\\\",\\\"value\\\":\\\"1\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-0\\\",\\\"dnsname\\\":\\\"10.20.227.120\\\",\\\"ipaddress\\\":\\\"10.20.227.120\\\"},{\\\"status\\\":{\\\"status\\\":\\\"\\\",\\\"_attr\\\":{\\\"string\\\":\\\"Operational\\\",\\\"value\\\":\\\"0\\\"}},\\\"macaddress\\\":\\\"00:1F:93:20:06:FC\\\",\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.227.120/storage/arrays/1BC100C5/controllers/2\\\"},\\\"rank\\\":{\\\"_attr\\\":{\\\"string\\\":\\\"Secondary\\\",\\\"value\\\":\\\"0\\\"},\\\"rank\\\":\\\"\\\"},\\\"fwversion\\\":\\\"v4.0.0-0\\\",\\\"dnsname\\\":\\\"10.20.228.252\\\",\\\"ipaddress\\\":\\\"10.20.228.252\\\"}],\\\"_attr\\\":{\\\"self\\\":\\\"http://10.20.227.120/storage/arrays/1BC100C5/controllers\\\"}},\\\"chronometer\\\":{\\\"timezone\\\":\\\"MST\\\",\\\"dst\\\":\\\"disabled\\\",\\\"_attr\\\":{\\\"date\\\":\\\"01-Sep-2017\\\",\\\"time\\\":\\\"00:45:57\\\"},\\\"timezonesetting\\\":\\\"MST\\\"},\\\"location\\\":\\\"\\\",\\\"contactname\\\":\\\"\\\",\\\"address\\\":\\\"\\\",\\\"contactphone\\\":\\\"\\\",\\\"model\\\":\\\"ISE3401\\\",\\\"id\\\":\\\"20001F9317827500\\\"}\"",
                        "serial_no": "1BC100C5",
                        "time_stamp": "2017-09-01T07:47:54.276Z",
                        "id": 2,
                        "ip_primary": "10.20.227.120"
                    }
                ]
            }
        },
        "error": false
    }
}

@apiError NotFound The particular Sangroup is not found

@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
  "detail": "Not found."
}

"""
"""
@apiGroup Sangroup
@apiName UpdateParticularSangroup
@api {get} /sangroup/<id> Update Particular Sangroup

@apiParam {Integer} id Unique SangroupID

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for updating Sangroup.
@apiSuccess {String} message It gives success or error message.
@apiSuccess {String} error It contains error messages.

@apiParamExample {json} Input.
{
    "sangroup_id":3,
    "sangroup_name":"xio",
    "comment":"test sangroup",
    "created_by":"1",
    "modified_by":"1",
}

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "time_taken":{
      "python":"",
      "req_recv_time":"",
      "total":"",
      "cortex":"",
      "res_send_time":""
   },
   "result":{
      "status_code":200,
      "response":{
         "data":{
            "sangroup_id":3,
            "sangroup_name":"xio",
            "comment":"test sangroup",
            "created_date":"2017-09-03T14:14:11.058350Z",
            "updated_date":"2017-09-03T14:48:56.377023Z",
            "created_by":"1",
            "modified_by":"1",
            "is_delete":false
         }
      },
      "error":false
   }
}

@apiError BadRequest Invalid or missing parameter

@apiErrorExample Error-Response:
HTTP/1.1 400 Bad Request
{
   "message":"fail",
   "time_taken":{
      "python":"",
      "req_recv_time":"",
      "total":"",
      "cortex":"",
      "res_send_time":""
   },
   "result":{
      "status_code":400,
      "response":{
         "data":[

         ]
      },
      "error":{
         "status_code":400,
         "message":{
            "sangroup_name":[
               "SanGroup with this sangroup name already exists."
            ]
         }
      }
   }
}
"""
"""
@apiGroup Sangroup
@apiName DeleteParticularSangroup
@api {get} /sangroup/<id> Delete Particular Sangroup

@apiParam {Integer} id Unique SangroupID.

@apiSuccess {Integer} id Unique SangroupID.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
   "message":"success",
   "time_taken":{
      "python":"",
      "req_recv_time":"",
      "total":"",
      "cortex":"",
      "res_send_time":""
   },
   "result":{
      "status_code":200,
      "response":{
         "data":{
            "deleted_san":"xio"
         }
      },
      "error":false
   }
}

@apiError BadRequest Invalid or missing parameter

@apiErrorExample Error-Response:
HTTP/1.1 400 Bad Request
{
   "message":"fail",
   "time_taken":{
      "python":"",
      "req_recv_time":"",
      "total":"",
      "cortex":"",
      "res_send_time":""
   },
   "result":{
      "status_code":400,
      "response":{
         "data":[

         ]
      },
      "error":{
         "status_code":400,
         "message":"SAN Group Mapped with one or more ISE"
      }
   }
}
"""
"""
@apiGroup Sangroup
@apiName SanGroupHosts
@api {get} /sangroup/<id>/hosts ParticularSangroupHosts

@apiParam {Integer} id Unique SangroupID.

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for displaying list of Sangroups.
@apiSuccess {String} message It gives success or error message.
@apiSuccess {String} error It contains error messages.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1512113695",
        "total": "1.37s",
        "cortex": "1.36s",
        "res_send_time": "1512113697"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": [
                {
                    "ise_id": 33,
                    "host_comment": "",
                    "id": 1,
                    "name": "lab142a",
                    "ise_name": "ISE-USE2600053GOH08C"
                },
                {
                    "ise_id": 33,
                    "host_comment": "",
                    "id": 2,
                    "name": "lab142b",
                    "ise_name": "ISE-USE2600053GOH08C"
                }
            ]
        },
        "error": false
    }
}
"""
urlpatterns = [
    url(r'^(?P<id>[\w\-]+)/hosts/$', SanGroupHost.as_view()),
    url(r'^(?P<id>[\w\-]+)/$', SanGroupDetail.as_view()),
    url(r'^$', SanGroupList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

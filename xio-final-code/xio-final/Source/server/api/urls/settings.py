from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.settings import (MailUserList, MailUserDetails, Schedule, Smtp)

"""
@apiGroup Settings
@apiName GetMailUserList
@api {get} /ise/<ise-id>/settings/mailuser/ Display MailUserList
@apiParam {Integer} ise-id unique ISE ID.

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for Powersupply.
@apiSuccess {String} message It gives success or error message of the Powersupply.
@apiSuccess {String} error It contains error message.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1504502084",
        "total": "0.01s",
        "cortex": "0.0s",
        "res_send_time": "1504502084"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": [
                {
                    "id": 1,
                    "name": "divya",
                    "email": "divyajothy.d@msystechnologies.com",
                    "ise_id": 1,
                    "is_active": true,
                    "normal": true,
                    "critical": true,
                    "severe": false,
                    "error": true,
                    "warning": false,
                    "informational": false
                },
                {
                    "id": 2,
                    "name": "nandhini",
                    "email": "nandhini@msystechnologies.com",
                    "ise_id": 1,
                    "is_active": true,
                    "normal": false,
                    "critical": true,
                    "severe": false,
                    "error": true,
                    "warning": false,
                    "informational": true
                }
            ]
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
@apiGroup Settings
@apiName CreateMailUser
@api {post} /ise/<ise-id>/settings/mailuser/ Create MailUser

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for creating MailUser.
@apiSuccess {String} message It gives success or error message.
@apiSuccess {String} error It contains error messages.

@apiParam {String} comment unique ISE ID.

@apiParamExample {json} Input.
{
   'name':'xio',
   'normal':False,
   'informational':True,
   'ise_id':1,
   'severe':False,
   'critical':True,
   'error':True,
   'warning':False,
   'email':'xio@msystechnologies.com'
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
         "data":"New User Created Succesfully"
      },
      "error":false
   }
}
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
            "non_field_errors":[
               "The fields ise_id, email must make a unique set."
            ]
         }
      }
   }
}
"""
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/settings/mailuser/$', MailUserList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/settings/mailuser/(?P<user_id>[\w]+)/$', MailUserDetails.as_view()),
    url(r'^settings/schedule/$', Schedule.as_view()),
    url(r'^settings/smtp/$', Smtp.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

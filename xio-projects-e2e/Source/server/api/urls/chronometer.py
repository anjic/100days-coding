from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.chronometer import(ChronometerList, ChronometerDetail)
"""
@apiGroup Chronometer
@apiName GetAllChronometerInfo
@api {get} /ise/<ise-id>/chronometer/ Display All Chronometer Info
@apiParam {Number} ise-id unique ISE ID.

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for Chronometer.
@apiSuccess {String} message It gives success or error message of the Chronometer.
@apiSuccess {String} error It contains error messages.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.00s",
        "req_recv_time": "1504351225",
        "total": "1.12s",
        "cortex": "1.11s",
        "res_send_time": "1504351226"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "chronometer": {
                    "uptime": {
                        "hours": 17,
                        "seconds": 47,
                        "_attr": {
                            "duration": "P1DT17H16M47S"
                        },
                        "minutes": 16,
                        "days": 1
                    },
                    "scale": "24-Hour",
                    "ntp": {
                        "ntpmode": "automatic",
                        "ntpserver": "time.nist.gov"
                    },
                    "dst": "disabled",
                    "_attr": {
                        "self": "https://10.20.238.9/storage/arrays/USE26000368OW028/chronometer"
                    },
                    "time": "04:20:25",
                    "date": "02-Sep-2017",
                    "timezone": "MST",
                    "timezonesetting": "Mountain Standard Time"
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
urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/chronometer/$', ChronometerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

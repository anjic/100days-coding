from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.performance import(PerformanceList, HostIopsChart,
                                  HostDataRateChart, HostQueueDepthChart,
                                  HostLatencyChart, VolumeLatencyChart,
                                  VolumeQueueDepthChart, VolumeDataRateChart,
                                  VolumeIopsChart, ControllerLatencyChart,
                                  ControllerQueueDepthChart, ControllerDataRateChart,
                                  ControllerIopsChart)
"""
@apiGroup Performance
@apiName ControllerLatencyChart
@api {get} /ise/<ise-id>/controllers-latency-chart/<controller-id> Display ControllerLatencyChartInfo

@apiParam {Integer} controller-id Unique ControllerID
@apiParam {Integer} ise-id unique ISE ID.

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for ControllerLatencyChartInfo.
@apiSuccess {String} message It gives success or error message of the ControllerLatencyChartInfo.
@apiSuccess {String} error It contains error message.

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readlatency"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writelatency"
            }
        ]
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
@apiGroup Performance
@apiName ControllerQueueDepthChart
@api {get} /ise/<ise-id>/controllers-queuedepth-chart/<controller-id> Display ControllerQueueDepthChartInfo

@apiParam {Integer} controller-id Unique ControllerID
@apiParam {Integer} ise-id unique ISE ID.

@apiSuccess {String} result It contains response and its attributes.
@apiSuccess {String} timetaken It contains response time taken for ControllerQueueDepthChartInfo.
@apiSuccess {String} message It gives success or error message of the ControllerQueueDepthChartInfo.
@apiSuccess {String} error It contains error message.

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "queuedepth"
            }
        ]
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
@apiGroup Performance
@apiName ControllerDataRateChart
@api {get} /ise/<ise-id>/controllers-datarate-chart/<controller-id> Display ControllerDataRateChartInfo

@apiParam {Integer} controller-id Unique ControllerID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the ControllerDataRateChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readkbps"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writekbps"
            },
            {
                "color": "#7777ff",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "totalkbps"
            }
        ]
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
@apiGroup Performance
@apiName ControllerIopsChart
@api {get} /ise/<ise-id>/controllers-iops-chart/<controller-id> Display ControllerIopsChartInfo

@apiParam {Integer} controller-id Unique ControllerID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the ControllerIopsChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readiops"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writeiops"
            },
            {
                "color": "#7777ff",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "totaliops"
            }
        ]
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
@apiGroup Performance
@apiName VolumeLatencyChart
@api {get} /ise/<ise-id>/volumes-latency-chart/<volume-id> Display VolumeLatencyChartInfo

@apiParam {Integer} volume-id Unique VolumeID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the VolumeLatencyChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readlatency"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writelatency"
            }
        ]
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
@apiGroup Performance
@apiName VolumeQueueDepthChart
@api {get} /ise/<ise-id>/volumes-queuedepth-chart/<volume-id> Display VolumeQueueDepthChartInfo

@apiParam {Integer} volume-id Unique VolumeID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the VolumeQueueDepthChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "queuedepth"
            }
        ]
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
@apiGroup Performance
@apiName VolumeDataRateChart
@api {get} /ise/<ise-id>/volumes-datarate-chart/<volume-id> Display VolumeDataRateChartInfo

@apiParam {Integer} volume-id Unique VolumeID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the VolumeDataRateChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readkbps"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writekbps"
            },
            {
                "color": "#7777ff",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "totalkbps"
            }
        ]
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
@apiGroup Performance
@apiName VolumeIopsChart
@api {get} /ise/<ise-id>/volumes-iops-chart/<volume-id> Display VolumeIopsChartInfo

@apiParam {Integer} volume-id Unique VolumeID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the VolumeIopsChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readiops"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writeiops"
            },
            {
                "color": "#7777ff",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "totaliops"
            }
        ]
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
@apiGroup Performance
@apiName HostLatencyChart
@api {get} /ise/<ise-id>/hosts-latency-chart/<host-id> Display HostLatencyChartInfo

@apiParam {Integer} host-id Unique HostID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the HostLatencyChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readlatency"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writelatency"
            }
        ]
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
@apiGroup Performance
@apiName HostQueueDepthChart
@api {get} /ise/<ise-id>/hosts-queuedepth-chart/<host-id> Display HostQueueDepthChartInfo

@apiParam {Integer} host-id Unique HostID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the HostQueueDepthChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "queuedepth"
            }
        ]
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
@apiGroup Performance
@apiName HostDataRateChart
@api {get} /ise/<ise-id>/hosts-datarate-chart/<host-id> Display HostDataRateChartInfo

@apiParam {Integer} host-id Unique HostID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the HostDataRateChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readkbps"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writekbps"
            },
            {
                "color": "#7777ff",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "totalkbps"
            }
        ]
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
@apiGroup Performance
@apiName HostIopsChart
@api {get} /ise/<ise-id>/hosts-iops-chart/<host-id> Display HostIopsChartInfo

@apiParam {Integer} host-id Unique HostID

@apiSuccess {String} result Displays the result
@apiSuccess {Integer} response It gives response as status code
@apiSuccess {String} data  It contains attributes of the HostIopsChart

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
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "readiops"
            },
            {
                "color": "#2ca02c",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "writeiops"
            },
            {
                "color": "#7777ff",
                "values": [
                    {
                        "y": 10,
                        "x": []
                    }
                ],
                "key": "totaliops"
            }
        ]
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
    url(r'^ise/(?P<id>[\w\-]+)/controllers-latency-chart/(?P<controller_id>[\w\-]+)', ControllerLatencyChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/controllers-queuedepth-chart/(?P<controller_id>[\w\-]+)', ControllerQueueDepthChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/controllers-datarate-chart/(?P<controller_id>[\w\-]+)', ControllerDataRateChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/controllers-iops-chart/(?P<controller_id>[\w\-]+)', ControllerIopsChart.as_view()),

    url(r'^ise/(?P<id>[\w\-]+)/volumes-latency-chart/(?P<volume_id>[\w\-]+)', VolumeLatencyChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/volumes-queuedepth-chart/(?P<volume_id>[\w\-]+)', VolumeQueueDepthChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/volumes-datarate-chart/(?P<volume_id>[\w\-]+)', VolumeDataRateChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/volumes-iops-chart/(?P<volume_id>[\w\-]+)', VolumeIopsChart.as_view()),

    url(r'^ise/(?P<id>[\w\-]+)/hosts-latency-chart/(?P<host_name>[\w\-]+)', HostLatencyChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/hosts-queuedepth-chart/(?P<host_name>[\w\-]+)', HostQueueDepthChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/hosts-datarate-chart/(?P<host_name>[\w\-]+)', HostDataRateChart.as_view()),
    url(r'^ise/(?P<id>[\w\-]+)/hosts-iops-chart/(?P<host_name>[\w\-]+)', HostIopsChart.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/performance/$', PerformanceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

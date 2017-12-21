from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from api.views.users import (UsersList, UserDetails, Login, UserPassword)
"""
@apiGroup User
@apiName GetUsersList
@api {get} /user/ Display List of Users

@apiSuccess {Integer} id Unique UserID.
@apiSuccess {String} first_name Firstname of the User(optional)
@apiSuccess {String} last_name  Lastname of the User(optional)
@apiSuccess {String} email      Email of the User
@apiSuccess {Boolean} is_active Whether User is active or not(optional)
@apiSuccess {Boolean} is_staff  Whether User is admin or not(optional)
@apiSuccess {Integer} groups  GroupID
@apiSuccess {String} group_name group name in which the user belongs.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "result": "success",
    "response": {
        "data": [
            {
                "id": 1,
                "first_name": "MSys",
                "last_name": "Technologies",
                "username": "msys",
                "email": "msys@example.com",
                "is_active": true,
                "is_staff": true,
                "groups": [],
                "sudo_user": false
            },
            {
                "id": 2,
                "first_name": "Test",
                "last_name": "MSys",
                "username": "test",
                "email": test@gmail.com",
                "is_active": true,
                "is_staff": true,
                "groups": [],
                "sudo_user": false
            }
        ]
    }
}
"""
"""
@apiGroup User
@apiName CreateUser
@api {post} /user/ Create New User

@apiParam {String} username     Optional Username of the User
@apiParam {String} [firstname]  Optional Firstname of the User
@apiParam {String} [lastname]   Optional Lastname of the User
@apiParam {String} email        Mandatory Email of the User
@apiParam {String} password     Mandatory password of the User

@apiSuccess {Integer} id        Unique UserID.
@apiSuccess {String} username   Username of the User(optional)
@apiSuccess {String} first_name Firstname of the User(optional)
@apiSuccess {String} last_name  Lastname of the User(optional)
@apiSuccess {String} email      Email of the User
@apiSuccess {String} password   password of the User


@apiParamExample {json} Input
{
    "first_name": "msys",
    "last_name": "msys",
    "username": "msys",
    "email": "msys@example.com",
    "password":"admin123"
}

@apiSuccessExample Success-Response:
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
            "data": "New User Created Succesfully"
        },
        "error": false
    }
}

@apiError BadRequest Invalid or missing parameter

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
            "message": "duplicate key value violates unique constraint auth_user_username_key DETAIL:  Key (username)=(1msys) already exists."
        }
    }
}
"""
"""
@apiGroup User
@apiName GetParticularUser
@api {get} /user/<user_id>/ Display Particular User

@apiSuccess {Integer} id Unique UserID.
@apiSuccess {String} first_name Firstname of the User(optional)
@apiSuccess {String} last_name  Lastname of the User(optional)
@apiSuccess {String} email      Email of the User
@apiSuccess {Boolean} is_active Whether User is active or not(optional)
@apiSuccess {Boolean} is_staff  Whether User is admin or not(optional)
@apiSuccess {Integer} groups  GroupID

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "message": "success",
    "time_taken": {
        "python": "0.02s",
        "req_recv_time": "1507900901",
        "total": "0.02s",
        "cortex": "0.0s",
        "res_send_time": "1507900901"
    },
    "result": {
        "status_code": 200,
        "response": {
            "data": {
                "id": 1,
                "first_name": "msys",
                "last_name": "msys",
                "username": "msys",
                "email": "msys@mail.com",
                "is_active": true,
                "is_staff": false,
                "groups": []
            }
        },
        "error": false
    }
}

@apiError UserNotFound The particular User is not found

@apiErrorExample Error-Response:
HTTP 404 Not Found
{
    "message": "fail",
    "time_taken": {
        "python": "0.01s",
        "req_recv_time": "1507901114",
        "total": "0.01s",
        "cortex": "0.0s",
        "res_send_time": "1507901114"
    },
    "result": {
        "status_code": 404,
        "response": {
            "data": []
        },
        "error": {
            "status_code": 404,
            "message": "User Not Found"
        }
    }
}
"""
"""
@apiGroup User
@apiName UpdateUser
@api {put} /user/id/ Update UserDetails

@apiParam {String} [firstname]  Optional Firstname of the User
@apiParam {String} [lastname]   Optional Lastname of the User
@apiParam {String} email        Mandatory Email of the User
@apiParam {String} password     Mandatory password of the User
@apiParam {Boolean} [is_active] Optional active status to check whether user is active or not
@apiParam {Boolean} [is_staff]  Optional to assign Whether User is admin or not

@apiSuccess {Integer} id Unique UserID
@apiSuccess {String} first_name Firstname of the User(optional)
@apiSuccess {String} last_name  Lastname of the User(optional)
@apiSuccess {String} email      Email of the User
@apiSuccess {Boolean} is_active Whether User is active or not(optional)
@apiSuccess {Boolean} is_staff  Whether User is admin or not(optional)
@apiSuccess {Integer} groups  GroupID

@apiParamExample {json} Input
{
  "username": "msys",
  "first_name": "Technologies",
  "last_name": "MSys",
  "email": "msys@example.com",
  "confirmpassword": "",
  "id": 1
}

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
    "result": "success",
    "response": {
        "data": [
            {
                "id": 1,
                "first_name": "MSys",
                "last_name": "Technologies",
                "username": "msys",
                "email": "msys@example.com",
                "is_active": true,
                "is_staff": true,
                "groups": []
            }
}

@apiError BadRequest Duplicate entry 'name' for key 'username'
@apiErrorExample {json} Error-Response:
    HTTP/1.1 400 Bad Request
        {
        "result":"fail",
        "response":
                  {
                  "data":"(1062, \"Duplicate entry 'name' for key 'username'\")"
                  }
        }

"""
"""
@apiGroup User
@apiName DeleteUser
@api {delete} /user/id/ Delete User Details

@apiParam {Integer} id Unique UserID

@apiSuccess {Integer} id Unique UserID

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
            "deleted_user":"msys"
         }
      },
      "error":false
   }
}

@apiError BadRequest Bad Request
@apiError UserNotFound The particular User is not found

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
         "message":"User cannot delete own account"
      }
   }
}

@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
"""
"""
@apiGroup User
@apiName Login
@api {post} /login/ Login

@apiParamExample {json} Input
{
"username":"<username>"
"password":"<password>"
}

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
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
        "status_code": 200,
        "response": {
            "data": {
                "username": "msys",
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vaGFuIn0.t6Ya-j9cuyOJQpbxFmV5tv2AfJi1UcG9n2Hg89boUjQ"
            }
        },
        "error": false
    }
}

@apiError BadRequest Invalid or missing parameter

@apiErrorExample Error-Response:
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
            "message": "Invalid Username or Password"
        }
    }
}
"""
"""
@apiGroup User
@apiName UpdateUserpassword
@api {put} /user-password/ UpdateUserpassword

@apiParamExample {json} Input
{
  "curr_password": "admin123",
  "new_password": "msys123",
  "confirm_password": "msys123"
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
      "status_code":201,
      "response":{
         "data":"Password Changed Succesfully"
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
         "message":"Invalid Password"
      }
   }
}

"""
urlpatterns = [
    url(r'^login/$', Login.as_view()),
    url(r'^user/(?P<id>[\w\-]+)/$', UserDetails.as_view()),
    url(r'^user/$', UsersList.as_view()),
    url(r'^user-password/$', UserPassword.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

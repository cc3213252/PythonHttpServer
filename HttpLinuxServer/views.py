import traceback
import warnings
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from HttpLinuxServer.Requests.user_info_request_handler import UserInfoRequestHandler

__author__ = '9'

def get_params(request):
    warnings.filterwarnings(u'ignore')
    if request.method == "GET":
        raise Http404('Only POSTs are allowed')
        #params = request.GET
    elif request.method == "POST":
        params = request.GET
        print params
        return params

@csrf_exempt
def get_user_info_list(request):
    try:
        user_info_handler = UserInfoRequestHandler(get_params(request), request)
        user_info_handler.prepare_get_params()
        return user_info_handler.get_response()
    except:
        traceback.print_exc()
        raise Http404

@csrf_exempt
def update_user_info_list(request):
    try:
        user_info_handler = UserInfoRequestHandler(get_params(request), request)
        user_info_handler.prepare_update_params()
        return user_info_handler.get_update_response()
    except:
        traceback.print_exc()
        raise Http404

@csrf_exempt
def add_user_info_list(request):
    try:
        user_info_handler = UserInfoRequestHandler(get_params(request), request)
        user_info_handler.prepare_add_params()
        return user_info_handler.get_add_response()
    except:
        traceback.print_exc()
        raise Http404

@csrf_exempt
def delete_user_info_list(request):
    try:
        user_info_handler = UserInfoRequestHandler(get_params(request), request)
        user_info_handler.prepare_delete_params()
        return user_info_handler.get_delete_response()
    except:
        traceback.print_exc()
        raise Http404
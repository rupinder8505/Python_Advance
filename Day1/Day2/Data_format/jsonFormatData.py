
from flask import jsonify
def return_success(data,message = None):
    return return_result(data,message)
def return_fail(data,message = None):
    return return_result(data,message,False)
def return_result(data=None,message = None,status=True):
    result_dict={'data':data,'status':status,'message':message}
    return jsonify(result_dict)
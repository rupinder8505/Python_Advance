from flask import Flask,jsonify
from Data_format import jsonFormatData as jn

app = Flask(__name__) ## obj of Flask class , __name__ will call __main__

@app.route('/')
def index():
    return "Hello World"

@app.route("/s/<name>")
def s_func(name):
    return "Hello" +name

'''

def return_success(data,message = None):
    return_result(data,message)
def return_fail(data,message = None):
    return_result(data,message,False)
def return_result(data=None,message = None,status=True):
    result_dict={'data':data,'status':status,'message':message}
    return jsonify(result_dict)
'''
@app.route("/sum/<int1>/<int2>")
def sum_func(int1,int2):
    try:
        int1 = int(int1)
        int2 = int(int2)
        sum = int1 + int2
        return jn.return_success(sum,"Final Result") 
    except Exception:
        return jn.return_fail(None,"Fail")

app.run(debug=True)
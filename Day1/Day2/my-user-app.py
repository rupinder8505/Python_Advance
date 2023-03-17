from Data_format import jsonFormatData as jn
import databaseHandler as dh
import requests as request
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/init')
def initDBroute():
    db1=dh.DatabaseHandler("myDb")
    db1.initDatabase()
    return jn.return_success(None,message="Database has been craeted!")

@app.route('/listUser')
def getLisOfUsers():
    db1=dh.DatabaseHandler("myDb")
    userList = db1.list_user()
    return jn.return_success(userList)

@app.route('/updateUser/<uid>',methods=['PUT'])
def updateUser(uid):
    col = request.form["col"]
    val = request.form["val"]
    db =dh.DatabaseHandler("myDb")
    db.update_user({col:val},uid)
    return jn.return_success(None,'updated user')

@app.route('/newUser',methods=['POST'])
def newUser():
    fname = request.form["fname"]
    lname = request.form["lname"]
    db =dh.DatabaseHandler("myDb")
    db.new_user(fname,lname)
    return jn.return_success(None,'updated user')

@app.route('/deleteUser/<uid>')
def deleteUser(uid):
    db =dh.DatabaseHandler("myDb")
    db.delete_user(uid)
    return jn.return_success(None,'user deleted')


app.run(debug=True)
"""
db1 = dh.DatabaseHandler("myDb")

db1.initDatabase()

db1.new_user("jane","Doe")

update_info = {"first_name":"Kim","last_name":"Doe"}

db1.update_user(update_info,1)

userList = db1.list_user()

print(userList)"""
# -*- coding: utf-8 -*-
from flask import  Flask ,request,render_template
from  geventwebsocket.websocket import WebSocket,WebSocketError
from  geventwebsocket.handler import WebSocketHandler
from  gevent.pywsgi import WSGIServer
from baseFunction import checkUser,addUser,getImg,changePassword
import pymysql
import json
app = Flask(__name__)
user_socket_dict={}
img_dict={}
@app.route('/')
def index():
    return render_template('loginPage.html')
@app.route('/friends/<username>')
def showFriends(username):
    return render_template("members.html",img_dict=img_dict,username=username);

@app.route('/chatroom/<username>')
def chatRoom(username):
    return render_template("chatroom.html",username=username);
@app.route("/register/")
def registerPage():
    return render_template("register.html")
@app.route('/login/<username>/<password>')
def login(username,password):
    user_socket=request.environ.get("wsgi.websocket")
    print("I am in login")
    if not user_socket:
        return "请以WEBSOCKET方式连接"
    result="error"
    try:
    	result=str(checkUser(username,password))
    	user_socket.send(result)
    except WebSocketError as e:
    	user_socket.send("0")
    	print(e)
    print(result)
    return result
@app.route('/change/<username>/<oldpassword>/<newpassword>')
def changepwd(username,oldpassword,newpassword):
    user_socket=request.environ.get("wsgi.websocket")
    if not user_socket:
        return "请以WEBSOCKET方式连接"
    result="error"
    try:
        result=changePassword(username,oldpassword,newpassword)
        user_socket.send(result)
    except WebSocketError as e:
        user_socket.send(result)
        print(e)
    return result
@app.route('/register/<username>/<password>')
def register(username,password):
	user_socket=request.environ.get("wsgi.websocket")
	if not user_socket:
		return "请以WEBSOCKET方式连接"
	result="error"
	try:
		result=addUser(username,password)
		user_socket.send(result)
	except WebSocketError as e:
		print(e)
	print(result)
	return result

@app.route('/ws/<username>')
def wx(username):
    user_socket=request.environ.get("wsgi.websocket")
    if not user_socket:
        return "请以WEBSOCKET方式连接"
    user_socket_dict[username]=user_socket
    img_dict[username]=getImg()
    user_socket.send(json.dumps({"sender":username,"img_url":img_dict[username]}))
    while True:
        try:
            user_msg=user_socket.receive()
            print(user_msg)
            try:
                msg_dict=eval(user_msg)
            except Exception as e:
                print(e)
            for toname,usersocket in user_socket_dict.items():
                if usersocket==user_socket:
                    continue
                try:
                    usersocket.send(user_msg)
                except:
                    user_socket_dict.pop(toname)
        except WebSocketError as e:
            user_socket_dict.pop(username)
            print(e)
            break

http_serve=WSGIServer(("0.0.0.0",10086),app,handler_class=WebSocketHandler)
http_serve.serve_forever()
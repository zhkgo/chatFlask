from flask import  Flask ,request,render_template
from  geventwebsocket.websocket import WebSocket,WebSocketError
from  geventwebsocket.handler import WebSocketHandler
from  gevent.pywsgi import WSGIServer

import json

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('websocket.html')

# user_socket_list = []
user_socket_dict={}



@app.route('/ws/<username>')
def ws(username):
    user_socket=request.environ.get("wsgi.websocket")
    if not user_socket:
        return "请以WEBSOCKET方式连接"

    user_socket_dict[username]=user_socket
    print(user_socket_dict)

    while True:
        try:
            user_msg = user_socket.receive()
            for user_name,u_socket in user_socket_dict.items():

                who_send_msg={
                    "send_user":username,
                    "send_msg":user_msg
                }

                if user_socket == u_socket:
                    continue
                u_socket.send(json.dumps(who_send_msg))

        except WebSocketError as e:
            user_socket_dict.pop(username)
            print(user_socket_dict)
            print(e)

if __name__ == '__main__':

    http_serve=WSGIServer(("0.0.0.0",5000),app,handler_class=WebSocketHandler)
    http_serve.serve_forever()

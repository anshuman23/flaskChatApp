from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)
    
if __name__ == '__main__':
    #socketio.run(app) #This WILL NOT WORK. The tutorial was sucky. Use the command below
    socketio.run(app, host='0.0.0.0', debug = True, port = 3110, use_reloader = True) #Open localhost:3110 to run this in your browser -.-

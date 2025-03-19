from flask import Flask, send_from_directory
import threading
import socketio
import os

socket = socketio.Client()
app = Flask(__name__)
server = 'http://172.18.0.2:5000'

@app.route('/')
def home():    
    return '<img src="/received.png">'

@app.route('/received.png')
def serve_image():
    return send_from_directory(os.getcwd(), 'received.png')

@socket.on('update')
def on_update():
    os.system(f"curl {server}/image.png -o received.png") 

def connect():
    try:
        socket.connect(server)
        socket.wait()
    except Exception as e:
        print(f"{e}")
    
    if socket.connected:
        socket.disconnect()

if __name__ == '__main__':
    thread = threading.Thread(target=connect)
    thread.daemon = True
    thread.start()
    app.run(host='0.0.0.0', port=5001)

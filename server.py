from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import cv2
import threading
import time
import os

camera = cv2.VideoCapture(0)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/image.png')
def serve_image():
    return send_from_directory(os.getcwd(), 'image.png')

def capture():
    while True:
        _, image = camera.read()
        cv2.imwrite('image.png', image)
        socketio.emit('update')
        time.sleep(10)

if __name__ == '__main__':
    thread = threading.Thread(target=capture)
    thread.daemon = True
    thread.start()
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)
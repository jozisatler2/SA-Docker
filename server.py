from flask import Flask, send_from_directory
import cv2
import threading
import time
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/')
def home():    
    return '<img src="/image.png">'

@app.route('/image.png')
def serve_image():
    return send_from_directory(os.getcwd(), 'image.png')

def capture():
    while True:
        _, image = camera.read()
        cv2.imwrite('image.png', image)
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target=capture)
    thread.daemon = True
    thread.start()
    app.run()
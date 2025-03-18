from flask import Flask
import cv2
import threading
import time
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/')
def home():    
    return "Hello"

def capture():
    while True:
        _, image = camera.read()
        os.system("rm -f image.png")
        cv2.imwrite('image.png', image)
        time.sleep(10)

if __name__ == '__main__':
    thread = threading.Thread(target=capture)
    thread.daemon = True
    thread.start()
    app.run()
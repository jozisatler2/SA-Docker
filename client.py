from flask import Flask
import socketio

socket = socketio.Client()
server = 'http://localhost:5000'

@socket.on('update')
def on_update():
    print("update")

def connect():
    try:
        socket.connect(server)
        socket.wait()
    except Exception as e:
        print(f"{e}")
    
    if socket.connected:
        socket.disconnect()

if __name__ == '__main__':
    connect()
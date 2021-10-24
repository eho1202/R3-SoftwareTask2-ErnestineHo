import socket
import os
from pynput import keyboard 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 65432
s.connect((host, port))
os.system('cls')
print("Connected")
print("Available controls: speeds 0 - 5 and wasd")
print("Enter the speed value first then direction value")
print("Press 'esc' to disconnect anytime")

def on_press(key):
    try:
        s.send(format(key.char).encode())
        if key.char == 'w':
            print("Going Forward")
        elif key.char == 'a':
            print("Turning Left")
        elif key.char == 's':
            print("Going Backward")
        elif key.char == 'd':
            print("Turning Right")
    except AttributeError:
        if key == keyboard.Key.esc:
            print("Disconnected")
            s.close()
            listener.stop()

# Collect events until pressed 
with keyboard.Listener(
    on_press=on_press) as listener:
    listener.join()
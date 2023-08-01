import socket
from pynput import keyboard

HOST = "172.20.10.11"  # The Jackal's hostname or IP address
PORT = 65432  # The port used by the server

def on_press(key):
    if key == keyboard.Key.up:
        print ('up')
        s.sendall(b'up')
    elif key == keyboard.Key.down:
        print ('down')
        s.sendall(b'down')
    elif key == keyboard.Key.left:
        print ('left')
        s.sendall(b'left')
    elif key == keyboard.Key.right:
        print ('right')
        s.sendall(b'right')



def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

    #s.sendall(b"Hello, world")
    data = s.recv(1024)

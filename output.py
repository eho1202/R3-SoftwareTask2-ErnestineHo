import socket
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 65432
s.bind((host, port))
s.listen(1)
os.system('cls')
print("Waiting for connections")

conn, addr = s.accept()
print ("Connection address: ", addr)

speeds = ['0', '1', '2', '3', '4', '5']

while True:
    data = conn.recv(1024).decode()
    for i in range(6):
        if data == speeds[i]: # if data corresponds to any number in the speeds array
            global converted_speeds
            converted_speeds = 255 / 5 * int(data)
            print(f"Speed set to {data}")
    
    if data == 'w':
        print(f"[f{converted_speeds}][f{converted_speeds}][f{converted_speeds}][f{converted_speeds}]")
    elif data == 'a':
        print(f"[r{converted_speeds}][r{converted_speeds}][f{converted_speeds}][f{converted_speeds}]")
    elif data == 's':
        print(f"[r{converted_speeds}][r{converted_speeds}][r{converted_speeds}][r{converted_speeds}]")
    elif data == 'd':
        print(f"[f{converted_speeds}][f{converted_speeds}][r{converted_speeds}][r{converted_speeds}]")
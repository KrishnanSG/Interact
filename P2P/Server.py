import socket
from _thread import *
import threading
import sys

print_lock = threading.Lock()

def client_req():

    PORT=5051

    client = socket.socket()
    host = socket.gethostname()

    client.connect(('192.168.43.166',PORT))
    client.send(b"Hi Server")
    print("client listening on Port 5051 ...")

    with open('received_file', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = client.recv(1024)
            print('data=', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()

    print('Successfully got the file')

    print("Data from server:",client.recv(1024))

    client.close()


def create_server():
    PORT = 5050

    server = socket.socket()
    host = socket.gethostname()

    server.bind((host, PORT))
    server.listen()

    print("Server listening on Port 5050 ...")

    while True:
        try:
            c, client_addr = server.accept()
            print("Someone connected from ", client_addr)

            data = c.recv(1024)
            print("Server Received ", repr(data))

            filename = '../README.md'
            f = open(filename, 'rb')
            l = f.read(1024)
            while (l):
                c.send(l)
                print('Sent ', repr(l))
                l = f.read(1024)
            f.close()

            print('Done sending')

            c.send(b"Thank you for connecting")

            c.close()
        except KeyboardInterrupt:
            server.close()
            print("Prev")
            exit()

print("Program starts")

def create_client_req():
    try:
        ch = input("Do you want to create server request? (y/n)")
        while ch=='y':
            client_req()
            ch = input("Do you want to create server request? (y/n)")
        print("Completed all requests")
        print_lock.release()
    except EOFError:
        print_lock.release()
        exit()


print()
print_lock.acquire()
start_new_thread(create_client_req, ())
create_server()





import socket
import sys
import time

from . import utils

class NetworkManager:

    REQUEST_BLOOMFILTER  = 2  
    REQUEST_BLOOMFILTER_PADDING  = [5,4,3,1]

    REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER = 3 # Acknowledge two and send bloomfilter
    REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER_PADDING  = [1,3,5,1]


    REQUEST_SEND_ACTUAL_LINES = 4
    # Variable to tell if the current user is host or client
    status = ""
    queue = []

    def __init__(self, request_handler):
        self.handler = request_handler

    def check_if_incoming_data(self):
        try:
            # TODO: Make it work for more than 1kb of data
            data = self.socket.recv(1024)

            # print("Data received in ", self.status, ' data=', repr(data))

            req = utils.parse_received_data(data)
            self.handler.handle_request(req)
            return tuple([00, ''])
        except BlockingIOError as e:
            # print(e)
            # No data to read
            return tuple([00, ''])


    def send_data(self, data, request_type):
        # if(self.status=="client"):
            # print(self.socket)
            if request_type == self.REQUEST_BLOOMFILTER:
                padding = bytes(self.REQUEST_BLOOMFILTER_PADDING)
            elif request_type == self.REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER:
                padding = bytes(self.REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER_PADDING)

            print("Sending data...", data)
            if isinstance(data, bytes):
                data = padding + data
                self.socket.send(data)
            else:
                self.socket.send(padding + str.encode(data))

    def send_request(self, request):
            print("Sending data...")
            print(request)
            self.socket.send(request.get_type_byte() + request.get_message_bytes())

    def create_host(self):
        self.status="host"
        server = socket.socket()
        host = socket.gethostname()

        server.bind((host, 5050))
        self.socket = server
        print("\nHi ",host," we have hosted the server at")
        print("IP:",server.getsockname()[0])
        print("Port:",server.getsockname()[1])
        print("Share IP and Port with your friend to start sync.\n")
        server.listen()

        c, client_addr = server.accept()
        self.socket = c
        print("Incoming request from", client_addr, "...")
        print("Connected to ", client_addr, "!")
        c.setblocking(False)            


    def create_client(self,ip,port):
        self.status="client"
        client = socket.socket()
        self.socket = client
        host = socket.gethostname()
        client.connect((ip,port))
        client.setblocking(False)
        print("\nHi ",host," you are succesfully connected to")
        print("IP:",ip)
        print("Port:",port)

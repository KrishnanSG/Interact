import socket
import sys
import time

from . import utils

MAX_RECEIVABLE_CONTENT_SIZE = 500000
class NetworkManager:

    # Variable to tell if the current user is host or client
    status = ""
    queue = []

    def __init__(self, request_handler):
        self.handler = request_handler

    def check_if_incoming_data(self):
        try:
            data = self.socket.recv(MAX_RECEIVABLE_CONTENT_SIZE)
            req = utils.parse_received_data(data)
            self.handler.handle_request(req)
            return tuple([00, ''])
        except BlockingIOError as e:
            # print(e)
            # No data to read
            return tuple([00, ''])


    def send_request(self, request):
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

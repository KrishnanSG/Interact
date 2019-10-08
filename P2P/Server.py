import socket
import sys
import time


class NetworkManager:

    REQUEST_BLOOMFILTER  = 2  
    REQUEST_BLOOMFILTER_PADDING  = [5,4,3,1]

    REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER = 3 # Acknowledge two and send bloomfilter
    REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER_PADDING  = [1,3,5,1]


    REQUEST_SEND_ACTUAL_LINES = 4
    # Variable to tell if the current user is host or client
    status = ""
    queue = []

    def check_if_incoming_data(self):
        try:
            # TODO: Make it work for more than 1kb of data
            data = self.socket.recv(1024)

            print("Data received in ", self.status, ' data=', repr(data))

            padding = data[0:4]
            if padding == bytes(self.REQUEST_BLOOMFILTER_PADDING):
                bloom_filter = data[4:]
                print("REQUEST_BLOOMFILTER_PADDING")
                a = tuple([self.REQUEST_BLOOMFILTER, bloom_filter])
                print(a)
                return a

            elif padding == bytes(self.REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER_PADDING):
                bloom_filter = data[4:]
                print("REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER")
                return tuple([self.REQUEST_ACKNOWLEDGE_SEND_BLOOMFILTER, bloom_filter])

            return tuple([00, ''])
        except BlockingIOError as e:
            print(e)
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
        # else:
            # print("Sending data from server...")
            # self.socket.send(str.encode("abcdefgh"))


    def create_host(self):
        self.status="host"
        server = socket.socket()
        host = socket.gethostname()

        server.bind((host,5051))
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
        # c.send(str.encode('sd'))
        # self.socket.send(str.encode('sdsdsa'))
        # while True:
        #     try:
        #         if input("Do u want to send:")=='y':
        #             text=input("Enter text:")

        #             c.send(str.encode(text))
        #         else:
        #             data = c.recv(1024)
        #             print('data=', repr(data))
                

        #     except KeyboardInterrupt:
        #         server.close()
        #         exit()
            


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

        #try:
        # while True:
            
        #     if input("Do u want to send")=='y':
        #         text=input("Enter text:")
        #         client.send(str.encode(text))
        #     else:
        #         try:
        #             data = client.recv(1024)
        #             print('data=', repr(data))
        #         except BlockingIOError: 
        #                 # No data to read
        #                 pass
            
 

        # to handle error while client connection
        # except:
        #    print("Invaild credentials. Make sure your friend has started the server.")

        
# p2p = NetworkManager()
# if sys.argv[1]=='1':
#     p2p.create_host()
# else:
#     # ip = input("Enter an IP: ")
#     ip = '127.0.1.1' 
#     port = int(input("Enter a PORT: "))
#     p2p.create_client(ip,port)

# while True:
#     p2p.check_if_incoming_data()
#     # p2p.check_pending_outgoing()
#     p2p.send_data("sadasdasdasdffd")
#     time.sleep(1)
    

    




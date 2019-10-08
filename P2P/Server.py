import socket
import sys
import time

class NetworkManager:
    # Variable to tell if the current user is host or client
    status = ""
    queue = []

    def check_if_incoming_data(self):
        try:
            merged_data = bytes()
            data = self.socket.recv(1024)
            merged_data = data
            while data and data != b'':
                merged_data += data
                print("Data received in ", self.status, ' data=', repr(merged_data))

                data = self.socket.recv(1024)

            print("Data received in ", self.status, ' data=', repr(merged_data))
        except Exception as e:
            # print(e)
            # No data to read
            pass

    def send_data(self, data):
        # if(self.status=="client"):
            # print(self.socket)
            print("Sending data...", data)
            if isinstance(data, bytes):
                self.socket.send(data)
            else:
                self.socket.send(str.encode(data))
        # else:
            # print("Sending data from server...")
            # self.socket.send(str.encode("abcdefgh"))


    def create_host(self):
        self.status="host"
        server = socket.socket()
        host = socket.gethostname()

        server.bind((host,5050))
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
    

    




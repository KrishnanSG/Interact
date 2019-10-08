import socket
import sys
import time

class Networking:
    # Variable to tell if the current user is host or client
    status = ""
    def create_host(self):
        self.status="host"
        server = socket.socket()
        host = socket.gethostname()

        server.bind((host,5050))

        print("\nHi ",host," we have hosted the server at")
        print("IP:",server.getsockname()[0])
        print("Port:",server.getsockname()[1])
        print("Share IP and Port with your friend to start sync.\n")
        server.listen()
        c, client_addr = server.accept()
        print("Incoming request from", client_addr)
        while True:
            try:
                if input("Do u want to send:")=='y':
                    text=input("Enter text:")
                    
                    c.send(str.encode(text))
                else:
                    data = c.recv(1024)
                    print('data=', repr(data))
                

            except KeyboardInterrupt:
                server.close()
            


    def create_client(self,ip,port):
        self.status="client"
        client = socket.socket()
        host = socket.gethostname()
        client.connect((ip,port))
        print("\nHi ",host," you are succesfully connected to")
        print("IP:",ip)
        print("Port:",port)

        #try:
        while True:
            
            if input("Do u want to send")=='y':
                text=input("Enter text:")
                client.send(str.encode(text))
            else:
                data = client.recv(1024)
                print('data=', repr(data))
            
                

        # to handle error while client connection
        # except:
        #    print("Invaild credentials. Make sure your friend has started the server.")

        
p2p = Networking()
if sys.argv[1]=='1':
    p2p.create_host()
else:
    p2p.create_client("192.168.43.37",5050)

    
    

    




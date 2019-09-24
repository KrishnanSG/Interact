import socket

PORT = 5050

client = socket.socket()
host = socket.gethostname()
host_ip = socket.gethostbyname(host)

client.connect((host,PORT))
client.send(b"Hi Server")
print("client listening on Port 5050 ...")

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
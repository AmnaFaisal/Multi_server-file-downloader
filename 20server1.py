from socket import *
from FileProcessing import *
serverPort = 60000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("server1 is waiting to connect")

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("got connection from: ", addr)

        filename = "tedtalk.mp4"
        f = open(filename, 'rb')

        chunkSize = connectionSocket.recv(1024)
        seek_data = connectionSocket.recv(1024)
        offset_data = connectionSocket.recv(1024)

        seek_ = seek_data.decode('utf8')
        offset_ = offset_data.decode('utf8')
        chunk_ = chunkSize.decode('utf8')

        chunk = int(float(chunk_))
        start = int(float(offset_))
        seek_from = int(float(seek_))

        f.seek(start, seek_from)

        a = f.read(1024)

        while a:
            connectionSocket.send(a)
            a = f.read(1024)

        print("sent data")
        f.close()

        print("server1 sending data successful")
        connectionSocket.close()

except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError) as e:
    print("closing connection from server 1")
    exit(0)

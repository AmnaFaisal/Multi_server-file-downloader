from socket import *
from FileProcessing import *
serverPort = 60001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("server2 waiting for connection")

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("connection to: ", addr)

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

        print("server2 sending data successful")
        connectionSocket.close()

except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError) as e:
    print("closing connection from server2")
    exit(0)

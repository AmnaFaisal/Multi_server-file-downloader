#importing libraries & file
from socket import *
from threading import *
import time
from FileProcessing import *


#main client
def main():
    try:
        sockets = []
        for x in range(4):
            client_socket = socket(AF_INET, SOCK_STREAM)
            sockets.append(client_socket)
        ports = [60000, 60001, 60002, 60003]
        ip = "120.0.0.1"

        threads = 0
        servers = []
        connectionUnsuccessful = 0
        connectionMade = 0

        socket_list = []
        file_list = []

        i = 0

     #creating and connecting with sockets
        for (sock, port) in zip(sockets, ports):
            try:
                sock.connect((ip, port))
                socket_list.append(sock)
                connectionMade += 1
                i += 1
            except (ConnectionRefusedError, ConnectionAbortedError, ConnectionError):
                connectionUnsuccessful += 1
                i += 1
                print("server ", i, " failed to connect")

        print("success:", connectionMade)
        activeServers = connectionMade                                     #taking in the number of servers available


        fileSizeOri = 2602687
        print("size of the file is ", fileSizeOri)
        chunkSize = int(fileSizeOri / activeServers)
        print("size of each chunk is to be: ", chunkSize)

        fileSent = 0
        start = 0
        seek = 0

        for x in socket_list:                                # threading

            try:
                threads += 1
                server = Thread(target=get_file, args=(x, threads, chunkSize, seek, start))
                servers.append(server)
                server.start()
                time.sleep(1)
                recvfile = fileName(threads)
                file_size = FileSize(recvfile)
                print("file size3: ", file_size)
                start = file_size
                seek = 1
                file_list.append(recvfile)
                fileSent += 1
                server.join()

            except (ConnectionRefusedError, ConnectionAbortedError, ConnectionError):
                print("server ", threads, "failed")

        print()
        FileCombination(file_list)

    except ZeroDivisionError:
        print("file transfer unsuccessful")
        temp = input("to terminate the program type 1 : ")
        if temp == "1":
            print("terminating")
            exit(0)


if __name__ == '__main__':
    main()

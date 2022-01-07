import os

def FileSize(filename):

    file_stats = os.stat(filename)
    fileSize = file_stats.st_size

    print("file size2: ", fileSize)
    return fileSize


def fileName(num):

    filesArr = ["file1.mp4", "file2.mp4", "file3.mp4", "file4.mp4", "file5.mp4",
             "file6.mp4", "file7.mp4", "file8.mp4", "file9.mp4", "file10.mp4"]
    file = filesArr[num]
    return file

def get_file(sock, thread_no, chunk, seek, start):

    sock.send(str(chunk).encode('utf8'))
    sock.send(str(seek).encode('utf8'))
    sock.send(str(start).encode('utf8'))

    filename = fileName(thread_no)

    with open(filename, 'wb') as f:
        recv_size = 0

        while True:
            data = sock.recv(1024)
            recv_size += len(data)
            f.write(data)
            if recv_size >= chunk:

                break
            elif not data:
                break
        print("received data from server ", thread_no)
        f.close()

    file_stats = os.stat(filename)
    file_size1 = file_stats.st_size
    print("file_size1: ", file_size1)



def FileCombination(filesArr):

    with open("recv_file.mp4", 'wb') as recvFile:
        for x in filesArr:
            try:
                f = open(x, 'rb')
                data = f.read(1024)
                recvFile.write(data)
                while data:
                    data = f.read(1024)
                    recvFile.write(data)
                f.close()

            except (FileNotFoundError, FileExistsError):
                pass
        recvFile.close()

    print("File sent successfully")

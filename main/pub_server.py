import time
import main.folder as folder
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')
my_list = folder.contents(input("Please enter folder path: "))
k = len(my_list) - 1
print("Publisher started")
while True:
    time.sleep(1)
    socket.send_string("FOLDER" + '\t%s' % my_list.__getitem__(k))
    k -= 1
    if k == -1:
        socket.send_string("FOLDER" + '\t%s' % "--------finished---------")
        k = len(my_list) - 1

import socket
import sys
try: 
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("failed")
    print("error code: "+str(msg[0])+", error msg: "+msg[1])
    exit(0)
print("success")
host=''
port = 8888
try:
    s.bind((host, port))
except socket.error as msg:
    print("bind failed error code: "+str(msg[0])+", error msg: "+msg[1])
    exit(0)

s.listen(2)
print("now lisning")
conn, addr = s.accept()
print("Client at: "+addr[0]+";"+str(addr[1]))
message = conn.recv(1024)
message = message + "Hello"
conn.sendall(message.encode("UTF-8"))
import socket
import sys
try: 
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("failed")
    print("error code: "+str(msg[0])+", error msg: "+msg[1])
    exit(0)
print("success")
host="www.google.com"
port = 80
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("host name not found")
    exit(0)
print("ip address of "+host+" is: "+remote_ip)
s.connect((remote_ip, port))
print("Socket connected to "+host+" on ip: "+remote_ip)

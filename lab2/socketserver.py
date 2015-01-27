import socket
import thread

def clientHandle(sock):
    message = str(sock.recv(1024))
    reply = message[:-2] + " Ben\n"
    sock.sendall(reply.encode("UTF-8"))
    sock.close()    

def main():
    host=''
    port = 8888 
    try:
        mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySock.bind((host, port))
        mySock.listen(5)
        while(1):
                (clientSocket, address) = mySock.accept()
                thread.start_new_thread(clientHandle, (clientSocket, ))       
    except socket.error as msg:
        print("failed to bind.")
        print("error code: "+str(msg[0])+", error msg: "+msg[1])        
        
    finally:
        mySock.close()    

if __name__ == "__main__":
    main()
        
    
#    HOST, PORT = "localhost", 8080
#    SocketServer.TCPServer.allow_reuse_address = True
#    # Create the server, binding to localhost on port 8080
#    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)
#    # Activate the server; this will keep running until you
#    # interrupt the program with Ctrl-C
#    server.serve_forever()
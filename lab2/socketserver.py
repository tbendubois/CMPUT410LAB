import socket

def getSocket():
    aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return aSocket

if __name__ == "__main__":
    mySock = getSocket()
    mySock.bind((socket.gethostname(), 8080))
    mySock.listen(5)
    
    while(1):
        (clientSocket, address) = mySock.accept()
        
        ct = client_thread(clientSocket)
        ct.run()
    
#    HOST, PORT = "localhost", 8080
#    SocketServer.TCPServer.allow_reuse_address = True
#    # Create the server, binding to localhost on port 8080
#    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)
#    # Activate the server; this will keep running until you
#    # interrupt the program with Ctrl-C
#    server.serve_forever()
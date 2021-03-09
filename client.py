import socket

host, port = ('localhost',5566)
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    ClientSocket.connect((host,port))
    print("Client connected !")

    msg = "Client Message V2"
    msg = msg.encode("utf8")
    ClientSocket.sendall(msg)
except:
    print("Connection Failed !")
finally:
    ClientSocket.close()
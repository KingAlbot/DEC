import socket 

conn = socket.socket()

conn.connect( ("127.0.0.1", 14900) )

try:
    while True:
        print("Client:", end="")
        conn.send(input().encode())
        data = conn.recv(16384)
        print("Server:" + data.decode("utf-8") )
except Exception:
    conn.close()

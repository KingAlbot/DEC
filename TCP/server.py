import socket

sock = socket.socket()
sock.bind( ("", 14900) )
sock.listen(10)
conn, addr = sock.accept()

try:
    while True:
        data = conn.recv(16384)
        udata = data.decode("utf-8")
        print("Client:" + udata)
        print("Server:", end="")
        conn.send(input().encode())
except Exception:
    conn.close()


import socket

# We connect to a (host,port) tuple
CONNECTION_ADDR = ("127.0.0.1", 5312)
response = "test message"

if __name__ == "__main__":
    # Connect to external server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to {}'.format(CONNECTION_ADDR))
    sock.connect(CONNECTION_ADDR)
    # Receive message from outgoing server
    fd = sock.makefile()
    print("[Server] \"{}\"".format(fd.readline().strip()))
    # Send a predefined message
    sock.sendall(response.encode())
    print("[Client] \"{}\"".format(response))
    print("[Server] \"{}\"".format(fd.readline().strip()))
    sock.close()
    # Wait for a response and disconnect.

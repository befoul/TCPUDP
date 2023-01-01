import socket

# Create a TCP/IP socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
tcp_sock.connect(("www.example.com", 80))

# Send data
tcp_sock.sendall(b"GET / HTTP/1.1\r\n\r\n")

# Receive data
data = tcp_sock.recv(1024)

# Close socket
tcp_sock.close()

# Print received data
print(data)

# Create a UDP/IP socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
udp_sock.sendto(b"Hello, World!", ("www.example.com", 80))

# Receive data (blocking)
data, addr = udp_sock.recvfrom(1024)

# Close socket
udp_sock.close()

# Print received data and address
print(data)
print(addr)

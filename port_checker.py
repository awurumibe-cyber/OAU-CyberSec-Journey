import socket

target = input("Enter target IP address: ")
port = int(input("Enter port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

result = sock.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN.")
else:
    print(f"Port {port} is CLOSED.")

sock.close()Test-NetConnection 127.0.0.1 -Port 9000
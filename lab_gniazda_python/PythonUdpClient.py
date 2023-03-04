import socket

serverIP = "127.0.0.1"
serverPort = 9008
# msg = "Ping Python Udp!"
# msg = "żółta gęś"
msg_bytes = (300).to_bytes(4, byteorder='little')

print('PYTHON UDP CLIENT')
print('Sending ', msg_bytes)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.sendto(bytes(msg, 'utf8'), (serverIP, serverPort))
client.sendto(msg_bytes, (serverIP, serverPort))

buff, address = client.recvfrom(1024)

print('received:', int.from_bytes(buff, byteorder='little'))




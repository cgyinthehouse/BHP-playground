#!/usr/bin/python3
import socket
target_host = '127.0.0.1'
target_port = 9998

# 建立socket物件
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 客戶端連接到主機
client.connect((target_host, target_port))

# 傳送資料
# client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
client.send(b'AAAAAAA')

# 接受資料
response = client.recv(4096)

print(response.decode())
client.close()

#!/usr/bin/python3
import socket

target_host = '127.0.0.1'
target_port = 9997

# 建立socket物件
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 傳送資料
client.sendto(b'AAABBCCC', (target_host, target_port))

# 接收資料
data, addr = client.recvfrom(4096)

print(data.decode)
client.close()

import socket										# 导入socket模块
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# 创建一个socket:
s.connect(('www.dangdang.com', 80))						# 建立与新浪网站连接
#发送数据请求
s.send(b'GET / HTTP/1.1\r\nHost: www.dangdang.com\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
#b''是一个空字节，join()是列表的函数,buffer是一个字节串的列表,使用空字节把buffer这个字节列表连接在一起,成为一个新的字节串
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina2.html', 'wb') as f:
    f.write(html)

import socket
import time
import threading
# 导入socket模块
def tcplink(sock, addr):
    print('接收一个来自%s:%s连接请求' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('来自 %s:%s 连接关闭了.' % addr)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))								#监听本机9999端口
s.listen(5)											#连接的最大数量为5
print('等待客户端连接...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


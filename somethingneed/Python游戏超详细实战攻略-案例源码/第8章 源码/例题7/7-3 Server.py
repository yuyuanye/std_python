import socket        # 导入socket模块
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888)) 								# 绑定端口
#创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
print('Bind UDP on 8888...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    print('received:',data)
    p=data.decode('utf-8').split(",");
    x=int(p[0]);
    y=int(p[1]);
    print(p[0],p[1])
    pos=str(x+1)+","+str(y+1)
    s.sendto(pos.encode('utf-8'),addr)


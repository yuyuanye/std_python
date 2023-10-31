import socket										# 导入socket模块
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
x=input("请输入x坐标")
y= input("请输入y坐标")
data=str(x)+","+str(y)
s.sendto(data.encode('utf-8'), ('127.0.0.1', 8888))
# 接收服务器加1后坐标数据:
data2, addr = s.recvfrom(1024)
print("接收服务器加1后坐标数据: " , data2.decode('utf-8')) 	# decode()解码

s.close()
input("")

#导入模块
import socket

#实例初始化
client=socket.socket()
#访问的服务器端的IP和port
ip_port=("127.0.0.1",8888)
#连接主机
client.connect(ip_port)
#接收主机信息
data=client.recv(1024)
#打印接收的数据
#此处的byte型数据特指python3.x以上
print(data.decode())

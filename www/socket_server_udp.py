#导入模块
import socket

#创建实例，如果没有参数默认TCP连接方式
sk=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#定义绑定的IP和port
ip_port=("127.0.0.1",8888)
#绑定监听
sk.bind(ip_port)
#不断循环，不断接受数据

#不断接收客户端发来的消息
while True:
	#接收客户端消息
	data=sk.recv(1024)
	#打印数据
	print(data.decode())
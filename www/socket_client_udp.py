#导入模块
import socket

#实例初始化
sk=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#访问的服务器端的IP和port
ip_port=("127.0.0.1",8888)

#循环数据的输入
while True:
	#输入发送的消息
	msg_input=input("请输入发送的消息：")
	#退出循环的条件
	if msg_input=="exit":
		break
	#消息发送
	sk.sendto(msg_input.encode(), ip_port)
#发送关闭信息
sk.close()

	
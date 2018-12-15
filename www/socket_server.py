#导入模块
import socket
import random

#创建实例
sk=socket.socket()
#定义绑定的IP和port
ip_port=("127.0.0.1",8888)
#绑定监听
sk.bind(ip_port)
#最大连接数
sk.listen(5)
#不断循环，不断接受数据
while True:
	#提升信息
	print("正在进行等待接受数据......")
	#接受数据
	conn, address=sk.accept()
	#定义信息
	msg="连接成功!"
	#返回信息
	#python3.x以上，网络数据的发送和接受都是byte类型
	#如果发送的数据是str型则需要进行编码
	conn.send(msg.encode())
	#不断接收客户端发来的消息
	while True:
		#接收客户端消息
		data=conn.recv(1024)
		#打印数据
		print(data.decode())
		#接收到退出指令
		if data==b'exit':
			break
		#处理客户端数据
		conn.send(data)
		#发送随机数信息
		conn.send(str(random.randint(1,1000)).encode())
	#主动关闭连接
	conn.close()
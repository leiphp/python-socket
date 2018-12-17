#可以与socket_client.py配对使用
#导入模块
import socketserver
import random

#定义一个类
class MyServer(socketserver.BaseRequestHandler):
	#首先执行setup
	def setup(self):
		pass
		
	#然后执行handle	
	def handle(self):
		#定义连接变量
		conn=self.request
		#发送消息定义
		msg="Hello World"
		#消息发送
		conn.send(msg.encode())
		#进入循环，不断接收客户端的消息
		while True:
			#接收客户端消息
			data=conn.recv(1024)
			#打印消息
			print(data.decode())
			#接收到exit ,循环退出
			if data==b'exit':
				break
			conn.send(data)
			conn.send(str(random.randint(1,1000)).encode())
		conn.close()
		
	#最后执行finish
	def finish(self):
		pass
		
		
if __name__=="__main__":
	#创建多线程实例
	server=socketserver.ThreadingTCPServer(("127.0.0.1",8888),MyServer)
	#开启异步多线程，等待连接
	server.serve_forever()
		

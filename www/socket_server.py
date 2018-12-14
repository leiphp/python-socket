#导入模块
import socket

#创建实例
sk=socket.socket()
#定义绑定的IP和port
ip_port=("127.0.0.1",8888)
#绑定监听
sk.bind(ip_port)
#最大连接数
sk.listen(5)
#提升信息
print("正在进行等待接受数据......")
#接受数据
conn, address=sk.accept()
#定义信息
msg="Hello World!"
#返回信息
#python3.x以上，网络数据的发送和接受都是byte类型
#如果发送的数据是str型则需要进行编码
conn.send(msg.encode())
#主动关闭连接
conn.close()
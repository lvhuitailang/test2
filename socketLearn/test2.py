from socket import *
ip_port = ('172.25.246.42',12306)
buffer_size = 1024

udp_server = socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)
name = input('请输入你的网名:\n').strip()
while True:
    msg,addr = udp_server.recvfrom(buffer_size) #获取信息和地址
    print(msg.decode('utf8'),addr)
    send_msg = name + input('>>>').strip()
    udp_server.sendto(send_msg.encode('utf8'),addr)


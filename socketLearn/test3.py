from socket import *
ip_port = ('172.25.100.33',12306) #服务端
buffer_size = 1024
udp_client = socket(AF_INET,SOCK_DGRAM)
name = (input('请输入你的网名:')+':').strip()
while True:
    msg = name + input('>>>').strip()
    udp_client.sendto(msg.encode('utf8'),ip_port)
    back_msg,addr = udp_client.recvfrom(buffer_size)#获取信息和地址
    print(back_msg.decode('utf8'),addr)

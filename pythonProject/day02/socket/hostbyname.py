import socket
host=socket.gethostname()
addr=socket.gethostbyname(host)
print("您的主机名是："+host)
print("您的IP地址是："+addr)
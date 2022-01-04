# coding:utf-8

import socket

from datetime import datetime
# 线程池
from multiprocessing.dummy import Pool as ThreadPool

# 目标IP
remote_server_ip = "47.99.142.216"
# 目标ip启用端口
ports = []
# 设置连接超时为0.5s，在校园网中使用时可以适当延长时间
socket.setdefaulttimeout(0.5)

# 端口扫描
def scan_port(port):
    try:
        # 创建套接字
        s = socket.socket()
        # connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
        # connect_ex（）和connect（）一样都需要传入，ip和port
        # 连接成功时返回 0 ，连接失败时候返回编码，例如：10061
        res = s.connect_ex((remote_server_ip, port))

        if res == 0:  # 如果端口开启 发送 hello 获取banner

            print(f'Port {port}: OPEN')

        s.close()

    except Exception as e:

        print(str(e.message))


if __name__ == '__main__':

    for i in range(1, 65535):
        ports.append(i)

    # 显示扫描时间
    t1 = datetime.now()
    # 设置线程池
    pool = ThreadPool(processes=1000)
    # map() 会根据提供的函数对指定序列做映射。
    results = pool.map(scan_port, ports)

    pool.close()

    print('Multiprocess Scanning Completed in  ', datetime.now() - t1)

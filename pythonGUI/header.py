#date：2021/12/30
#作者：云南大学 kento

import re, urllib.request, socket
import http.client, threading, queue
import sys
from importlib import reload

reload(sys)

q = queue.Queue()


def writeFileU(fileName, text):
    f = open(fileName, "a+")
    f.write(text + "\n")
    f.close()


def geturls(ip, port):
    URLS = ['', 'phpinfo.php', 'phpmyadmin/', 'xampp/', 'zabbix/', 'jmx-console/', '.svn/entries', 'nagios/',
            'index.action', 'login.action', 'mysql']
    ip = "".join(ip)
    port = "".join(port)

    for url in URLS:
        try:
            iport = ip + ":" + port
            conn = httplib.HTTPConnection(iport)
            conn.request('GET', '/' + url)
            res = conn.getresponse()
            print(iport)
            html = res.read()
            if res.status == 200:
                writeFileU(filename, iport)
                try:
                    title = re.search('<title>(.*?)</title>', html).group(1)
                    print(title.decode('gb2312').encode('utf-8'))
                    writeFileU(filename, title.decode('gb2312').encode('utf-8'))
                except:
                    pass

            else:
                conn.close()
        except:
            pass


def worker():
    while not q.empty():
        iport = q.get()
        iports = iport.split("----")
        ip = iports[0].rsplit()
        port = iports[1].rsplit()
        geturls(ip, port)
        q.task_done()


if __name__ == '__main__':
    #确保传参正确
    if len(sys.argv) < 2:
        print('python header.py file.txt')
        sys.exit()

    sb = sys.argv[1]
    host = sys.argv[1]
    filename = sb + "ports.txt"
    lines = open(host, "r")
    for line in lines:
        line = line.rstrip()
        q.put(line)

    for i in range(50):
        t = threading.Thread(target=worker)
        t.start()

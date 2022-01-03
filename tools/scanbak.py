#2021/12/30
#云南大学 kento

import urllib.request
import queue
import threading
import sys


def bytes2human(n):
    """
    >>> bytes2human(10000)
    9K
    >>> bytes2human(100001221)
    95M
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10

    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return '%sB' % n


def gethtml(url, bak):
    try:
        urlbak = url + bak
        #print(urlbak)
        req = urllib.request.urlopen(urlbak, timeout=10)
        if req.code == 200:
            meta = req.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            m = bytes2human(file_size)
            content_type = meta.getheaders('Content-Type')[0].split(';')[0]
            if file_size == 0:
                return False
            if 'html' in content_type:
                return False
            else:
                print('%s ---- %s ---- %s ' % (urlbak, m, content_type))
                return '%s ---- %s ---- %s ' % (urlbak, m, content_type)
        else:
            return False
    except:
        return False


def writefile(fileName, c):
    f = open(fileName, "a")
    f.write(c + "\n")
    f.close()


q = queue.Queue()


def scanner(url):
    for i in bekadd(url):
        c = gethtml(url, i)
        if c != False:
            writefile("bak.txt", c)


def worker():
    while not q.empty():
        url = q.get()
        scanner(url)
        q.task_done()


def bekadd(url):
    listbak = ['/1.zip', '/1.rar', '/web.rar', '/web.zip', '/www.rar', '/www.zip', '/wwwroot.rar', '/wwwroot.zip',
               '/backup.rar', '/backup.zip', '/database.rar', '/database.zip', '/databak.rar', '/databak.zip',
               '/databackup.rar', '/databackup.zip', '/databack.zip', '/sql.rar', '/sql.zip']
    wwwurl = url[url.find("http://") + 7:].rstrip("/")
    urldomain = url[url.rfind('.', 0, url.rfind('.')) + 1:].rstrip("/")
    urlcenter = urldomain[0:urldomain.rfind('.')].rstrip("/")
    wwwurl = "/" + wwwurl
    urldomain = "/" + urldomain
    urlcenter = "/" + urlcenter
    listbak.append(wwwurl + ".rar")
    listbak.append(wwwurl + ".zip")
    listbak.append(urldomain + ".rar")
    listbak.append(urldomain + ".zip")
    listbak.append(urlcenter + ".rar")
    listbak.append(urlcenter + ".zip")
    return listbak


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('python scanbak.py url.txt')
        sys.exit()

    lines = open(sys.argv[1], "r")
    for line in lines:
        line = line.rstrip()
        q.put(line)

    for i in range(100):
        t = threading.Thread(target=worker)
        t.start()



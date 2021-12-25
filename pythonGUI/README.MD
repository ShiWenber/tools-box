# pythonGUI
通过C语言编译的dll加上python代码实现混合语言编程，用python实现图形界面，调用c来实现函数

```
gitpod /workspace/a-work-for-python-class $ /home/gitpod/.pyenv/versions/3.8.12/bin/python /workspace/a-work-for-python-class/pythonGUI/GUI.pyTraceback (most recent call last):
  File "/workspace/a-work-for-python-class/pythonGUI/GUI.py", line 2, in <module>
    from PyQt5 import QtCore, QtWidgets
```
上述问题的出现解决方法(仅仅适用于gitpod类型的在线编译器，在本机上应该考虑是否是使用错了编译路径，pip安装的默认路径是python官方的，不是minGW提供的python编译路径)：
https://blog.csdn.net/Felaim/article/details/108726908

使用pyqt5的designer能够用图形化的方式进行页面设计，更便捷，可以将业务逻辑代码和ui界面代码分成两个页面

 unable to access 'https://github.com/wenboshicn/a-work-for-python-class.git/': OpenSSL SSL_read: Connection was reset, errno 10054
 解决方式：
 https://blog.csdn.net/weixin_43883666/article/details/114738288
 
import qrcode#导入qrcode库, 用于生成二维码
import datetime#导入datetime库用于生成带时间的图片名
import os,getpass#导入getpass库用于获取系统的用户名
#输入待转换的字符串
str = input("Enter the string to be converted:")
print("Input:"+str)
#采用默认方式生成二维码
img = qrcode.make(str)
#获取当前时间,转化成字符串
timenow = datetime.datetime.now()
timestr = timenow.strftime("%Y-%m-%d-%H-%M-%S")
#生成带时间的二维码图片名,图片保存在桌面上
name = "C:\\Users\\{0}\\Desktop\\{1}.png".format(getpass.getuser(), timestr)
print("Save as :", name)
#保存二维码图片
img.save(name)
print("Success!")
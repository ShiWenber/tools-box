from PIL import Image#导入Image库用与操作图片文件
import datetime
def image_to_txt(imgname):
    #获取当前时间,转换成字符串
    timenow = datetime.datetime.now()
    timestr = timenow.strftime("%Y-%m-%d-%H-%M-%S")
    #生成的Txt文件用<原图片文件名+ 当前时间字符串+ ".txt"后缀>作为文件名
    namestr = "{0}-{1}.txt".format(imgname, timestr)
    #打开或创建一个TxT文件文件
    txt = open(namestr, "w+")
    #打开图片文件文件
    print("Open Image File [{0}]".format(imgname))
    try:
        img = Image.open(imgname)
    except:
        print("Error to Open [{0}]!".format(imgname))
    #判断图片文件的格式, 这里必须为"RGB"格式, 如果不是"RGB"格式, 
    #则用convert函数转换成"RGB"格式.
    if "RGB" == img.mode:
        print("Size{0},Format({1}),Color({2})".format(img.size, img.format, img.mode))
    else:
        print("Not a RGB image file!")
        img = img.convert("RGB")
        print("Convert to RGB Success!")
    #获取图片文件宽和高
    width = img.size[0]
    height = img.size[1]
    bei = 0
    #如果图片文件大于400*400像素,则对图片进行缩放,缩放比例依照宽度和高度中的最大值
    if width >= height:
        max = width
    else:
        max = height
    if max >= 400:
        bei = max / 400
        width = int(width / bei)
        height = int(height / bei)
        img = img.resize((width, height))
        print("Image Size too large, Resize to", img.size)
    #把图片文件转换成纯黑白的图片
    img = img.convert("1")
    index = 0
    print("Start Process!")
    for w in range(width):#遍历图片的宽度,[0, width)
        #显示进度
        index += 1
        print("#", end="")
        txt.write("/")
        if index >= 60:#大于60换行
            index = 0
            print("")
        for h in range(height):#遍历图片的高度[0, height)
            xiangsu = img.getpixel((w, h))#获取图片当前坐标点的像素值
            #print("w=", w, "h=", h, "xiangsu=", xiangsu)
            if xiangsu != 0:#因为是纯黑白图像,所以像素颜色只有0或255两种值
                txt.write("_")#非0则往txt中写入"_"表示白色
                #print("w=", w, "h=", h, "xiangsu=", xiangsu)
            else:
                txt.write("*")#0则往txt中写入"*"表示黑色
                #print("w=", w, "h=", h, "xiangsu=", xiangsu)
        txt.write("/")
        txt.write("\n")
    #保存新生成的TXT文件
    print("\nProcess Done!")
    print("Save File As [{0}]".format(namestr))
    txt.close()
    print("Save Done!")
name = input("Please Input Image File Name:")
print("Start")
try:
    image_to_txt(name)
except:
    print("Error!")
print("Over")
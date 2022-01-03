# 小组作业要求

一、作业题目

1. 以小组为单位开发一个Python程序；
2. 必须在Github上创建项目，把项目的代码推送到Github上；
3. 项目必须编写一个 README.md；
4. 项目需提交一份报告；

二、README.md 内容要求（请不要把个人信息写到 README.md 当中）

- 项目功能简介
- 程序运行方式
- 程序运行截图

三、报告要求（生成PDF版，加密；在Github的项目仓库里创建一个目录‘doc’，把报告的PDF放到‘doc’目录当中）

（一）封面

（二）项目成员信息

分别列出每个同学的：

- 学院
- 专业
- 姓名
- 学号
- 在小组项目中主要做了哪些工作

（三）项目介绍（和README内容相同）

- 项目功能介绍
- 程序运行方式
- 程序运行截图

（四）小组项目心得体会

四、作业提交方式

各小组分别在2022年1月3日前，在课程QQ群里 at 老师，告知如下信息：

- 你是哪个小组
- 你们组的项目仓库URL是什么
- 你们小组的PDF报告的压缩密码是什么

# 工具使用说明和环境说明

## 功能一

### 模块一：文件格式转换模块

支持文件类型为xlsx或xls与csv文件类型之间的相互转换，该模块以第三方库xlrd、codecs、csv以及pandas四个库组成实现，通过以分行读取目标文件，并将按行读取的内容写入内存，最终保存到新文件实现格式转换。

#### excel文件转换为csv文件

```python
def xlsx_to_csv(path):
    workbook = xlrd.open_workbook(path)
    table = workbook.sheet_by_index(0)
    name = input("转换之后的文件名：")
    with codecs.open(f'{name}.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)
    print()
```


#### csv文件转为excel文件

```python
def csv_to_xlsx(path):
    csv_1 = pd.read_csv(path, encoding='utf-8')
    file_name = input("转换之后的文件名：")
    sheet_name = input("第一张表格的名字：")
    csv_1.to_excel(f'{file_name}.xlsx', sheet_name=f'{sheet_name}')
    print("转换成功")
    print()
```

### 模块二：文件读取

本模块支持读取excel文件以及csv文件，并在终端输出展示部分文件内容，此外，该模块所需的库只有pandas一个。

#### 读取excel文件
```python
def read_xlsx(path):
    data = pd.read_excel(path)
    print("获取到的数据为：")
    print(data.values)
    print()
```

#### 读取csv文件

```python
def read_csv(path):
    data = pd.read_csv(path)
    print("获取到的数据为：")
    print(data)
    print()
```

### 模块三：功能选择

#### 功能菜单

```python
def menu():
    while True:
        print("—————————————功能选择———————————")
        print("1.文件转换")
        print("2.文件读取")
        print("3.退出程序")
        choice = input("请输入您的选择：")
        if choice == '1':
            print("选择转换类型：")
            print("1.excel转为csv")
            print("2.csv转为excel")
            choice1 = input("选择准换类型：")
            if choice1 == '1':
                path_xlsx = input(r"请输入文件地址(格式为：C:\xxx\xxx\xxx.xlsx)：")
                xlsx_to_csv(path_xlsx)
            elif choice1 == '2':
                path_csv = input(r"请输入文件地址(格式为：C:\xxx\xxx\xxx.csv)：")
                csv_to_xlsx(path_csv)

        if choice == '2':
            print("选择读取类型：")
            print("1.excel")
            print("2.csv")
            choice2 = input("选择读取类型：")
            if choice2 == '1':
                path_xlsx = input(r"请输入文件地址(格式为：C:\xxx\xxx\xxx.xlsx)：")
                read_xlsx(path_xlsx)
            elif choice2 == '2':
                path_csv = input(r"请输入文件地址(格式为：C:\xxx\xxx\xxx.csv)：")
                read_csv(path_csv)

        if choice == '3':
            print("欢迎下次使用")
            break
```

以while循环嵌套if条件语句的形式，选择用户所需的功能。

### 运行方式

直接运行主函数：

```python
if __name__ == '__main__':
    menu()
```

即可进入程序选择。

#### 运行截图

#### 文件选择

 <img src="https://github.com/sheepstar1/Substation/blob/main/3.png" width="1476" height="792" alt="正在加载请稍后"/>

#### 文件转换

 <img src="https://github.com/sheepstar1/Substation/blob/main/2.png" width="1476" height="792" alt="正在加载请稍后"/>
 
#### 文件加载

 <img src="https://github.com/sheepstar1/Substation/blob/main/1.png" width="1476" height="792" alt="正在加载请稍后"/>

## 功能二

用于把图片转换成TXT文件的Python小工具,用到了pillow等第三方库.原理是打开一幅图片,先对图片进行格式转换和缩放,然后对图像二值化,转换成纯黑白的图像,接着依次读取图片每个像素的值写入到文本文件中,如果该值不为0则写入@,否则写入空格.

## 功能三

第二个工具用来生成二维码，用到了qrcode等第三方库，输入要生成二维码的图片文件等，然后输出生成的二维码到桌面上.

![1](README.assets/zhuanhuan%202022-01-01%20191911.png)

![二维码两张](README.assets/QTcode.png)

![二维码一张](README.assets/QTcode1.png)

![2](README.assets/zhuanhuan%202022-01-01%20190836.png)

![3](README.assets/erweima%202022-01-01%20190659.png)

![4](README.assets/2022-01-01-18-27-12.png)

**项目心得体会**

通过这次小组作业，在项目的分工和组织过程中，我学会了使用gitpod来完成项目，以前我在完成项目时都是使用vscode或pycharm等写完以后再和小组成员讨论进度。在这次项目中，我们使用了github来管理我们的项目，极大的简化了管理项目的复杂程度。

同时，在完成项目的过程中，我也加深了对python这门编程语言的熟悉和理解，我发现python语言虽然不一定是最好的编程语言，但是python一定是最好的编写脚本的语言，同时也是最接近自然语言的一门编程语言。在这次项目的完成过程中，因为我做的时信息收集模块的代码编写，所以，我对一些网络的知识也有了新的认识，并且也能够熟练的使用socket库和requests库，当然，在代码中也使用到了多线程来解决代码运行效率不足的问题，这也是我第一次使用python的多线程编程

总而言之，在这次的项目完成过程中，我不仅仅时学会了github的使用，提高了我对于项目的管理能力。同时，独立完成项目以后也提高了我自己使用python编程的能力。

**主要工作**
完成了小组项目中scanbak和prot两个项目模块的代码实现以及测试。

**Port模块介绍**

**项目功能介绍**

端口扫描是渗透测试中信息收集里很重要的一个部分，厉害的黑客或者渗透工程师，仅仅通过扫描服务器端口的开启情况就能够大致判断出网站的类型以及开启的服务。这里port模块主要是用来扫描服务器的端口开启情况。这里使用到了multiprocessing.dummy库，因为需要提高扫描的效率，所以也需要使用到多线程，然后我们需要设置扫描的服务器IP,以及连接的时间，这里因为测试时使用的是校园网，所以这里连接时间可以适当的延长：

![](README.assets\图1.png)

图 1 port连接部分

接下来是端口扫描部分，使用socket来创建连接，然后对于函数的比较详细的解释也已经写到了注释中：

![](README.assets/图2.png)

图 2 端口扫描部分

**程序运行方式**

这里程序的运行方式是只需设置好IP就可以直接点击run运行了，在如下位置设置需要扫描的IP：

![](README.assets/图3.png)

图 3 IP输入位置

**程序运行截图**

这里测试程序时为了避免造成不必要的网络安全问题，使用的是我自己的VPS：

![](README.assets/图4.png)

图 4 扫描结果

这里可以看到扫描的效率还是可以的，并且也是正确的扫描出了结果。

**scanbak模块介绍**

**项目功能简介**

这是一个在渗透测试中扫描文件敏感目录的脚本，因为渗透测试中，信息收集是很重要的一个阶段，前期信息收集的工作直接决定了渗透工作的效果，虽然现在市面上的自动化信息收集工具有很多，但是有的时候功能过于集中，这里这个脚本主要是用来扫描网站的敏感文件目录。

程序主要是实现了扫描敏感文件目录是否存在，以及当文件存在时，读出文件的大小，同时为了提高扫描的效率这里使用了多线程操作：

1.  敏感文件扫描功能：

    ![](README.assets/图片1.png)

    图 1 url补全模块

这里对于网站敏感目录的识别方式，主要是通过在url后面加上字典中存储的常见的敏感文件目录名。

1.  敏感文件输出模块：

    ![](README.assets/图片2.png)

    图 2 敏感文件输出模块

这里对于文件大小的识别主要是通过信息报文中的Content-Length消息头的数据。并通过Content-Type消息头来判断文件的类型。

**程序运行方式**

程序的运行方式是通过命令行运行，这里需要传入两个参数，第一个是需要运行的程序的文件名，以及想要扫描的文件目录，如下所示：

![](README.assets/图片3.png)
图 3 命令行运行

这里为了防止输入错误，导致程序崩溃，也做了输入的检测，如果输入的参数不正确也会报错：

![](README.assets/图片4.png)

图 4 输入报错

**程序运行截图**

这里程序运行完以后的数据会写入到当前文件夹的bak.txt文件中，为了避免有什么问题，这里我们在本地用phpstudy搭建一个web服务器测试一下：

![](README.assets/图片5.png)

图 5 测试网站

这里在url.txt文件中写入本地web服务器的url，然后运行程序查看结果：

![](README.assets/图片6.png)

图 6 扫描结果

这里可以看到程序正确扫描出了我放在WWW目录下的几个敏感文件。

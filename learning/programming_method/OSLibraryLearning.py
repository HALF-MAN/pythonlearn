"""
    -os库是Python标准库，包含几百个函数
    -常用路径操作、进程管理、环境参数等几类
        -路径操作：os.path子库，处理文件路径及信息
        -进程管理：启动系统中其他程序
        -环境参数：获得系统软硬件信息等环境参数
    路径操作
        os.path子库以path为入口，用于操作和处理文件路径
        import os.path或者import os.path as op
        os.path.abspath(path)   返回path在当前系统中的绝对路径
                >>>os.path.abspath("file.txt")
                'C:\\Users\\Tian Song\\Python36-32\\file.txt'
        os.path.normpath(path)  归一化path的表示形式，统一用\\分隔路径
                >>>os.path.normpath("D://PYE//file.txt")
                'D:\\PYE\\file.txt'
        os.path.relpath(path)   返回当前程序与文件之间的相对路径(relativepath)
                >>>os.path.relpath("C://PYE//file.txt")
                '..\\..\\..\\..\\..\\..\\..\\PYE\\file.txt'
        os.path.dirname(path)   返回path中的目录名称
                >>>os.path.dirname("D://PYE//file.txt")
                'D://PYE'
        os.path.basename(path)  返回path中最后的文件名称
                >>>os.path.basename("D://PYE//file.txt")
                'file.txt'
        os.path.join(path,*paths)   组合path与paths，返回一个路径字符串
                >>>os.path.join("D:/","PYE/file.txt")
                'D:/PYE/file.txt'
        os.path.exists(path)    判断path对应文件或目录是否存在，返回True或False
                >>>os.path.exists("D://PYE//file.txt")
                False
        os.path.isfile(path)    判断path所对应是否为已存在的文件，返回True或False
                >>>os.path.isfile("D://PYE//file.txt")
                True
        os.path.isdir(path)     判断path所对应是否为已存在的目录，返回True或False
                >>>os.path.isdir("D://PYE//file.txt")
                False
        os.path.getatime(path)  返回path对应文件或目录上一次的访问时间
                >>>os.path.getatime("D:/PYE/file.txt")
                1518356633.7551725
        os.path.getmtime(path)  返回path对应文件或目录最近一次的修改时间
                >>>os.path.getmtime("D:/PYE/file.txt")
                1518356633.7551725
        os.path.getctime(path)  返回path对应文件或目录的创建时间
                >>>time.ctime(os.path.getctime("D:/PYE/file.txt"))
                'Sun Feb 11 21:43:53 2018'
        os.path.getsize(path)   返回path对应文件的大小，以字节为单位
                >>>os.path.getsize("D:/PYE/file.txt")
                180768
    os库之进程管理
        os.system(command)
            -执行程序或命令command
            -在Windows系统中，返回值为cmd的调用返回信息
        import os
        >>>os.system("C:\\Windows\\System32\\calc.exe")
        0返回0表示程序的正确运行
        给程序附加参数直接空格后添加，下面让画图程序默认打开一幅图片
        os.system("C:\\Windows\\System32\\mspaint.exe \
            D:\\PYECourse\\grwordcloud.png")
    os库之环境参数
        os.chdir(path)  修改当前程序操作的路径
            >>>os.chdir("D:")
        os.getcwd()     返回程序的当前路径
            >>>os.getcwd()
            'D:\\'
        os.getlogin()   获得当前系统登录用户名称
            >>>os.getlogin()
            'Tian Song'
        os.cpu_count()  获得当前系统的CPU数量
            >>>os.cpu_count()
            8
        os.urandom(n)   获得n个字节长度的随机字符串，通常用于加解密运算
            >>>os.urandom(10)
            b'7\xbe\xf2!\xc1=\x01gL\xb3'
"""
import os
#这个地方后面程序的参数只能传绝对路径
# 传入相对路径他会把当前程序文件所在的路径作为基础路径,在当前路径下寻找文件。
os.system("C:\\Windows\\System32\\mspaint.exe \
            D:\\IdeaProjects\\pythonlearn\\learning\\resources\\ywcloud.png")
#使用chdir()函数更改当前操作路径后可以顺利找到文件
print(os.getcwd())
os.chdir("../resources")
print(os.getcwd())
os.system("C:\\Windows\\System32\\mspaint.exe \
            ywcloud.png")
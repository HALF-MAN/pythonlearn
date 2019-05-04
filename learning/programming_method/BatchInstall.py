import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests",
        "jieba", "beautifulsoup4", "wheel", "networkx", "sympy",
        "pyinstaller", "django", "flask", "werobot", "pyqt5",
        "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}
try:
    """
        os.system无法获取指令输出
        通过 os.popen() 返回的是 file read 的对象，
        对其进行读取 read() 的操作可以看到执行的输出。
        通过 commands.getstatusoutput() 一个方法就可以获得到返回值和输出，非常好用。
        (status, output) = commands.getstatusoutput('cat /proc/cpuinfo')
        print status, output
    """
    output = os.popen("pip3 list")
    ls = output.read()
    for lib in libs:
        #已安装的库跳过
        if lib not in ls:
            os.system("pip3 install "+lib)
    print("Successful")
except:
    print("Failed Somehow")
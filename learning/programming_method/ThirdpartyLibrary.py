"""
13万个第三方库https://pypi.org/
    -PyPI: Python Package Index
    -PSF(python software foundation):维护的展示全球Python计算生态的主站
    -学会检索并利用PyPI，找到合适的第三方库开发程序
    实例：开发与区块链相关的程序
    -第1步：在pypi.org搜索blockchain
    -第2步：挑选适合开发目标的第三方库作为基础
    -第3步：完成自己需要的功能
安装Python第三方库
    三种方法
    -方法1(主要方法): 使用pip命令
    -方法2: 集成安装方法
    -方法3: 文件安装方法
    pip安装方法
        D:\>pip –h
            Usage:
            pip <command> [options]
            Commands:
            install Install packages.
            download Download packages.
            uninstall Uninstall packages.
            freeze Output installed packages in requirements format.
            list List installed packages.
            show Show information about installed packages.
            check Verify installed packages have compatible dependencies.
            search Search PyPIfor packages.
            wheel Build wheels from your requirements.
            help Show help for commands.
        D:\>pip install <第三方库名>
        -安装指定的第三方库
        D:\>pip install –U <第三方库名>
        -使用-U标签更新已安装的指定第三方库
        D:\>pip uninstall <第三方库名>
        -卸载指定的第三方库
        D:\>pip download <第三方库名>
        -下载但不安装指定的第三方库
        D:\>pip show <第三方库名>
        -列出某个指定第三方库的详细信息
        D:\>pip search <关键词>
        -根据关键词在名称和介绍中搜索第三方库
        D:\>pip list
        -列出当前系统已经安装的第三方库
    第三方库的集成安装方法
        集成安装：结合特定Python开发工具的批量安装
        Anaconda
            https://www.continuum.io
            -支持近800个第三方库
            -包含多个主流工具
            -适合数据计算领域开发
    第三方库的文件安装方法
        为什么有些第三方库用pip可以下载，但无法安装？
        -某些第三方库pip下载后，需要编译再安装
        -如果操作系统没有编译环境，则能下载但不能安装
        -可以直接下载编译后的版本用于安装吗？
        UCI页面http://www.lfd.uci.edu/~gohlke/pythonlibs/
        该网站提供了一些windows环境下编译好的第三方库
        实例：安装wordcloud库
            -步骤1：在UCI页面上搜索wordcloud
            -步骤2：下载对应版本的文件
            -步骤3：使用pip install <文件名>安装
"""
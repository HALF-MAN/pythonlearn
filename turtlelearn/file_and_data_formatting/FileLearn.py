"""
    python 文件读取和写入
    文件打开：
        <变量名> = open(<文件名>, <打开模式>)
            打开模式：
                'r'     只读模式，默认值，如果文件不存在，返回FileNotFoundError
                'w'     覆盖写模式，文件不存在则创建，存在则完全覆盖
                'x'     创建写模式，文件不存在则创建，存在则返回FileExistsError
                'a'     追加写模式，文件不存在则创建，存在则在文件最后追加内容
                'b'     二进制文件模式
                't'     文本文件模式，默认值
                '+'     与r/w/x/a一同使用，在原功能基础上增加同时读写功能
    文件关闭：
        <变量名>.close() 建议打开的文件在使用完后要关闭，如果忘记关闭，python解释器在程序正常退出时也会关闭文件
    文件内容的读取：
        <f>.read(size=-1)读入全部内容，如果给出参数，读入前size长度
        <f>.readline(size=-1)读入一行内容，如果给出参数，读入该行前size长度
        <f>.readlines(hint=-1)读入文件所有行，以每行为元素形成列表，如果给出参数，读入前hint行
        例：
            for line in fo.readlines():
                print(line) #一次读入，分行处理
            for line in fo:
                print(line)#分行读入，逐行处理，注意：这直接使用fo in 遍历文件采用的是分行处理
    数据的文件写入：
        <f>.write(s)    向文件写入一个字符串或字节流
                        >>>f.write("中国是一个伟大的国家!")
        <f>.writelines(lines)   将一个元素全为字符串的列表写入文件
                                >>>ls = ["中国", "法国", "美国"]
                                >>>f.writelines(ls)
                                中国法国美国 #注意，这里读取的时候是按列表方式读，
                                写入文件的实际状态是字符串拼接在一起，并没有按行写入
    文件操作指针的位置：
        <f>.seek(offset)    改变当前文件操作指针的位置，offset含义如下：
                            0 – 文件开头； 1 – 当前位置； 2 – 文件结尾
                            >>>f.seek(0) #回到文件开头
"""
fo = open("../resources/output.txt", "w+", encoding="utf-8")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
fo.seek(0) #调整位置指针到文件开始
for line in fo:
    print(line)

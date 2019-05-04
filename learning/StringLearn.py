#学习字符串操作

"""
操作符及使用               描述
x+ y                  连接两个字符串x和y
n *x 或x *n           复制n次字符串x
x in s                果x是s的子串，返回True，否则返回False
len(x)                长度，返回字符串x的长度
len("一二三456")       结果为6
str(x)                任意类型x所对应的字符串形式
str(1.23)             结果为"1.23"str([1,2])结果为"[1,2]"
hex(x)或oct(x)        数x的十六进制或八进制小写形式字符串
hex(425)              结果为"0x1a9"
oct(425)              结果为"0o651"
chr(u)                x为Unicode编码，返回其对应的字符
ord(x)                x为字符，返回其对应的Unicode编码
str.lower()或str.upper()         返回字符串的副本，全部字符小写/大写
"AbCdEfGh".lower()    结果为"abcdefgh"
str.split(sep=None)   返回一个列表，由str根据sep被分隔的部分组成
"A,B,C".split(",")    结果为['A','B','C']
str.count(sub)        返回子串sub在str中出现的次数
"an apple a day".count("a")    结果为4
str.replace(old, new)       返回字符串str副本，所有old子串被替换为new
"python".replace("n","n123.io")    结果为"python123.io"
str.center(width[,fillchar])       字符串str根据宽度width居中，fillchar可选
"python".center(20,"=")          结果为'=======python======='
str.strip(chars)       从str中去掉在其左侧和右侧chars中列出的字符
"= python= ".strip("=np")      结果为"ytho"
str.join(iter)        在iter变量除最后元素外每个元素后增加一个str
",".join("12345")       结果为"1,2,3,4,5"#主要用于字符串分隔等

"{1}:计算机{0}的CPU占用率为{2}%".format("2018-10-10","C",10)
：  引导符号
<填充>    用于填充的单个字符
<对齐>    < 左对齐,> 右对齐,^ 居中对齐
<宽度>    槽设定的输出宽度
<,>       数字的千位分隔符
<.精度>    浮点数小数精度或字符串最大输出长度
<类型>    整数类型b, c, d, o, x, X    浮点数类型e, E, f, %

>>>"{0:=^20}".format("PYTHON")
'=======PYTHON======='
>>>"{0:*>20}".format("BIT")
'*****************BIT'
>>>"{:10}".format("BIT")
'BIT '
>>>"{0:,.2f}".format(12345.6789)
'12,345.68'
>>>"{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425)
'110101001,Ʃ,425,651,1a9,1A9'
>>>"{0:e},{0:E},{0:f},{0:%}".format(3.14)
'3.140000e+00,3.140000E+00,3.140000,314.000000%'


字符串类型及操作
-正向递增序号、反向递减序号、<字符串>[M:N:K]
-+、*、in、len()、str()、hex()、oct()、ord()、chr()
-.lower()、.upper()、.split()、.count()、.replace()
-.center()、.strip()、.join(）、.format()格式化
"""




# if "" in str:
#     print("yes")
# weekend = "星期一星期二星期三星期四星期五星期六星期日"
# tmp = eval(input("请输入请星期数字(1-7)："))
# tmp = (tmp - 1) * 3
# print(wekend[tmp:tmp+3])

# weekend1 = "一二三四五六日"
# tmp = eval(input("请输入请星期数字(1-7)："))
# print("星期"+weekend1[tmp-1])


#字符串提取切片
#字符串[M:N:K]
#从m到n包括n不包括m,k为每隔k个取一个
str = "hello world"
print(str[0:-1]) #注意：此时不包括最后一个字符d

#字符串操作符
# +,*,len(),str(),hex(),oct(),ord()把一个符号编程Unicode码,chr()把一个Unicode码变成字符
for i in range(12):
    print(chr(9800+i), end="")  #end为空表示不换行
print()
print(ord('a'))

#居中，宽度20，=填充
print("python".center(20, '='))

#删除掉字符串两边的字符，参数指定删除的字符序列
print("= python= ".strip(' =py'))

#插入到每个字符后面
print(",".join("12345"))

#字符串格式化
#<字符串>.format(<逗号分隔符的参数>)
#每个大括号都是一个槽,数字代表参数的顺序
"{1}:计算机{0}的CPU占用率为{2}%".format("2018-10-10", "C", 10)

#{<参数序号>:<格式控制标记>}
#主要包括填充，对其，宽度，<,>,<.精度>，<类型>
#填充：用于填充的单个字符
#对其：<左对齐，>右对齐，^居中对其
#宽度：槽设定的输出宽度
#下面这条语句是以=填充，^表示居中对其，20表示宽度
print("{0:=^20}".format("PYTHON"))
print("{0:*>20}".format("BIT"))
print("{:10}".format("BIT")) #省略填充字符，默认是空格

#数字的千位分隔符<,>
#点数小数的精度或者字符串最大输出长度<.精度>
#整数类型:b,c,d,o,x,X
#浮点类型：e,E,f,%
print("{0:,.2f}".format(12345.6789))
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
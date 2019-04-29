#学习字符串操作

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
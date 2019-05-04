n, s = 10, 100
str = "hello"
def test(a=1, *b, c):
    global str
    for i in b:
        print(i)
    print(a)
    str = "world"
test(2, c= 3)
print(str)
'''
基本数据类型，无论是否重名，局部变量和全局变量不同，
除非使用global指定用全局变量量
组合数据类型，如果局部变量未真实创建，则为全局变量
'''
'''
lambda函数
函数名 = lambda <参数>:<表达式>
    等价于   def <函数名>(<参数>):
                <函数体>
                return <返回值>
'''
import random
#默认的种子是当前第一次调用random()函数的系统时间
#设置种子可以保证之后的random函数生成随机数序列是一致的
random.seed(10)
print(random.random())
print(random.random())
print(random.random())

#生成[a,b]之间的随机整数
random.randint(10, 100)

#生成一个[m,n)之间以k为步长的随机整数
print(random.randrange(10, 100, 10))

#生成一个k比特长的随机整数
random.getrandbits(16)

#生成一个[a,b]之间的随机小数
random.uniform(10, 100)

#从序列seq中随机选择一个元素
random.choice([1, 2, 3, 4, 5, 6])

#将序列seq中元素随机排列，返回打乱后的序列
s = [1, 2, 3, 4, 5]
random.shuffle(s)
print(s)

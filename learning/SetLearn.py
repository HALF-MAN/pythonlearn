#集合练习
#不包含相同元素，元素不能改变
a = {"python", 123,  ("python", 123)}
b = set("pypy123")
#{'p', '1', '2', 'y', '3'}
print(b)
c = {"python", 123, "python", 123}
#{"python", 123}

#集合间操作
#并，差，交，补
# |,-,&,^
#S<=T,S<T判断S和T的子集关系
#S>=T,S>T判断S和T的包含关系
d = {"p", "y", 123}
e = set("pypy123")
f = d - e
print(f)

#S.add(x) 如果x不在集合S中，将x增加到S
#S.discard(x)移除S元素x,如果x不在集合S中，不报错
#S.remove(x)移除S元素x,如果x不在集合S中,产生KeyError异常
#S.cleat()移除S中所有元素
#S.pop()随机返回S中的一个元素，更新S，若S为空产生KeyError异常
#S.copy()返回集合S的一个副本
#len(S)返回集合S的元素个数
#X in S 判断S中元素X，在集合中返回True否者返回False
#X not in S
#set(X)将其他类型变量转换为集合类型,该类型变量必须是可迭代的(iterable)
#for item in A: 遍历集合，不保证元素顺序
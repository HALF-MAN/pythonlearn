"""
    字典类型，其它语言里一般叫map,一种键值对的集合，键值对是无序的
    采用{}或者dict()创建，键与值之间用:分割
    {<键>:<值>,<键1>:<值1>...}

    <字典变量> = {<键>:<值>,<键1>:<值1>...}
    获取字典中某一键值对的值
    <值> = <字典>[<键>]
    改变某一键对应的值
    <字典>[<键>] = <值>

函数或方法：
    del d[k]   删除字典中d中键k对应的数据值
    k in d     判断k是否在字典中，返回值是True或者False
    d.keys()   返回字典中所有键
    d.values() 返回字典中所有值
    d.items()  返回字典中所有键值对信息
    d.get(k, <default>) 键存在，返回对应的值，不存在，返回default值
    d.pop(k, <default>) 键存在，取出对应的值，不存在，返回default值
    d.popitem() 随机从字典d中取出一个键值对，以元组形式返回
    d.clear() 删除所有键值对
    d.len(d)返回d中元素个数
"""
d = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
print(d["中国"])

'''默认类型为字典类型,
集合类型(set)也是用{}表示，所以集合类型声明时不能用空大括号形式
因为已经预留给字典类型，生成空集合，可使用set()函数
'''
de = {}
print(type(de))

print("中国" in d)
'''
返回字典的key和value信息
dict_keys(['中国', '美国', '法国'])
dict_values(['北京', '华盛顿', '巴黎'])
注意:这里返回的不是列表类型，是字典的的keys类型和valuesl类型，
     可使用for in 遍历的类型
    不能用列表的方法去操作它
'''
print(d.keys())
print(d.values())
'''
如果中国存在。返回值，不存在，返回第二个默认的参数
'''
print(d.get("中国", "伊斯兰堡"))
print(d.get("巴基斯坦", "伊斯兰堡"))
print(d.popitem())
d1 = dict(one=1, two=2)
d2 = dict({"one": 1})
print(d1)
print(d2)
'''
这里遍历时如果只写d,则只是对key进行遍历
返回键值对，要调用d.items()
'''
for k, v in d.items():
    print(k, "，", v)




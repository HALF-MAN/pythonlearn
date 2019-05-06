"""
使用type()
首先，我们来判断对象类型，使用type()函数：
基本类型都可以用type()判断：
type(123)

如果一个变量指向函数或者类，也可以用type()判断：
type(abs)

但是type()函数返回的是什么类型呢？它返回对应的Class类型。
如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
type(123)==type(456)
type(123)==int
type('abc')==type('123')
type('abc')==str
type('abc')==type(123)

要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
 import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True

使用isinstance()
对于class的继承关系来说，使用type()就很不方便。
我们要判断class的类型，可以使用isinstance()函数。
isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

能用type()判断的基本类型也可以用isinstance()判断：
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True

并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True

总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，
它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

>>> len('ABC')
3
>>> 'ABC'.__len__()
3

我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

>>> class MyDog(object):
...     def __len__(self):
...         return 100
...
>>> dog = MyDog()
>>> len(dog)
100

剩下的都是普通属性或方法，比如lower()返回小写的字符串：
>>> 'ABC'.lower()
'abc'

仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，
我们可以直接操作一个对象的状态：
>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19

如果试图获取不存在的属性，会抛出AttributeError的错误：
>>> getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'
可以传入一个default参数，如果属性不存在，就返回默认值：
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404

也可以获得对象的方法：
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81

小结
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

sum = obj.x + obj.y
就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')
一个正确的用法的例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
如果存在，则该对象是一个流，
如果不存在，则无法读取。hasattr()就派上了用场。
请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，
不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
"""

class Student(object):
    def __init__(self, name, score, idcard):
        self._name = name
        self.__score__ = score
        self.__idcard = idcard
    def print(self):
        print("名字：{}\n分数：{}".format(self._name, self.__score__))

c = Student("job", 95, '134225546')
f = getattr(c, "print")
name = getattr(c, "_name")
score = getattr(c, "__score__")
#此方法不能访问私有变量，目前没有找到方法通过getattr()方法获取
# idcard = getattr(c, "__idcard")
if __name__ == '__main__':
    c.__score__ = 100
    print(c.__score__)
    f()
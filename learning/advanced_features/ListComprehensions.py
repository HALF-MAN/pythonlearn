"""
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
    列表生成式则可以用一行语句代替循环生成上面的list：
        >>> [x * x for x in range(1, 11)]
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
        >>> [x * x for x in range(1, 11) if x % 2 == 0]
        [4, 16, 36, 64, 100]
    使用两层循环，可以生成全排列：
        >>> [m + n for m in 'ABC' for n in 'XYZ']
        ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    三层和三层以上的循环就很少用到了。
    列表生成式也可以使用两个变量来生成list：
        >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
        >>> [k + '=' + v for k, v in d.items()]
        ['y=B', 'x=A', 'z=C']
    把一个list中所有的字符串变成小写：
        >>> L = ['Hello', 'World', 'IBM', 'Apple']
        >>> [s.lower() for s in L]
        ['hello', 'world', 'ibm', 'apple']
    非字符串类型没有lower()方法，所以列表生成式会报错.
"""
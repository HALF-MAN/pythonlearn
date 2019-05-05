"""
    对这种经常取指定索引范围的操作，用循环十分繁琐，
    因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
        L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
        L[:3]如果第一个索引是0，还可以省略：
        L[-2:]类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
        L[:10:2]前10个数，每两个取一个
        L[:]就可以原样复制一个list
    字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
        'ABCDEFG'[:3]
    tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple

"""
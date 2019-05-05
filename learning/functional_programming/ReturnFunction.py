"""
函数作为返回值
    高函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    求和函数如果不需要求和，在后面的代码中根据需要再计算
    def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
    实现了懒加载计算，预先设置参数，需要时再执行计算
    >>> f = lazy_sum(1, 3, 5, 7, 9)
    >>> f
    <function lazy_sum.<locals>.sum at 0x101c6ed90>
    >>> f()
    25
    在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，
    内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
    相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

    请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
        >>> f1 = lazy_sum(1, 3, 5, 7, 9)
        >>> f2 = lazy_sum(1, 3, 5, 7, 9)
        >>> f1==f2
        False
        f1()和f2()的调用结果互不影响
    闭包:
        注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
        其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
        另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
    def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
    f1, f2, f3 = count()
    在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
    你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
    >>> f1()
    9
    >>> f2()
    9
    >>> f3()
    9
    全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
    等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
    返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
    def count():
        def f(j):
            def g():
                return j*j
            return g
        fs = []
        for i in range(1, 4):
            fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
        return fs
    缺点是代码较长，可利用lambda函数缩短代码。
"""
"""
    def createCounter():
    i = 0
    def counter():
        i = 1 + i
        return i
    return counter
报错：
UnboundLocalError: local variable 'i' referenced before assignment
这是因为，当你在当前作用域中的给变量赋值时，该变量将成为该作用域的局部变量，并在外部范围中隐藏任何类似命名的变量。
所以在执行i = 1 + i的时候。因为i被重新赋值了，所以i的作用域编程counter函数范围。
同时将它原来在createCounter函数范围的同名变量i消除。然后，执行1 + i的时候就出错了，此时i还没有定义呢！所以报错：UnboundLocalError: local variable 'i' referenced before assignment。
def createCounter1():
    li = [0]
    def counter():
        li[0] += 1
        return li[0]
    return counter
引用类型不会被覆盖
"""

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
def createCounter1():
    li = [0]
    def counter():
        li[0] += 1
        return li[0]
    return counter
def main():
    f1, f2, f3 = count()
    print(f1(), f2(), f3())
    counter = createCounter1()
    print(counter())

if __name__ == '__main__':
    main()
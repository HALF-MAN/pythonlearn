try:
    guess = eval(input())
    if guess > 99 or guess < 99:
        print("猜错了")
    else:
        print("猜对了")
except NameError:
    print("发生了异常：输入的不是整数")
else:
    print("没有发生异常")

finally:
    print("不管发生不发生异常都要执行")


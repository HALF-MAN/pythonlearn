#进度条
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale - i)
    c = (i/scale)*100
    # c = (i + (1 - i)*0.03)**2
    dur = time.perf_counter() - start
    #/r表示把光标移到行首，end=""表示不换行，默认为\n即为换行符
    print(("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur)), end="")
    time.sleep(1)
print("执行结束".center(scale//2), "-")

# for i in range(scale+1):
#     print(("\r{:3}%".format(i)), end="")
#     time.sleep(1)
#学习time库

import time
#time(),ctime(),gmtime()
print(time.ctime())
print(time.gmtime())

'''
时间格式化
strftime()
注意：gmtime返回的是UTC时区（0时区）的struct_time，我们是东八区
'''
date = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", date))
timeStr = "2018-01-26 12:55:20"
timeStruct = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")

'''程序的当前时间，获取cpu时钟时间，较准确'''
start = time.perf_counter()
end = time.perf_counter()
print(end - start)

'''通过sleep休眠'''
time.sleep(3.3)



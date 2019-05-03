"""
自动轨迹绘制
"""
import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("../resources/data.txt", encoding="utf-8")
for line in f:
    #去掉当前行末尾的换行符
    line = line.replace("\n", "")
    #用逗号分隔当前行，并把分割后得到的列表中的每个元素应用eval函数，
    # 这里的map就是起到每个元素作为参数传递到前面的函数中去
    #最后再把获取的值组成一个list追加到datals中
    datals.append(list(map(eval, line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()

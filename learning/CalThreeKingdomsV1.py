#CalThreeKingdomsV1.py
#三国人物出场统计,含有非人名，功能不完善
import jieba
import time
txt = open("resources/threekingdoms.txt", "r", encoding='UTF-8').read()
tm = time.perf_counter()
words = jieba.lcut(txt)
print("分词花费时间:{}s".format(time.perf_counter()-tm))
tm1 = time.perf_counter()
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
print("统计花费时间：{}s".format(time.perf_counter()-tm1))
tm2 = time.perf_counter()
items.sort(key=lambda x: x[1], reverse=True)
print("排序花费时间：{}s".format(time.perf_counter()-tm2))
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

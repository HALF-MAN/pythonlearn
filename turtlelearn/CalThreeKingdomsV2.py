#CalThreekingdomsV2.py
#三国演义人物出场统计升级版

import jieba
import time
txt = open("resources/ThreeKingdoms.txt", "r", encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人",
            "不可", "不能", "如此", "商议",
            "如何", "主公", "军士", "左右",
            "军马", "引兵", "次日", "大喜",
            "天下", "东吴", "于是", "今日",
            "不敢", "魏兵", "陛下", "一人",
            "都督", "人马", "不知"}
tm = time.perf_counter()
words = jieba.lcut(txt)
print("分词花费时间:{}s".format(time.perf_counter()-tm))
tm1 = time.perf_counter()
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
print("统计花费时间：{}s".format(time.perf_counter()-tm1))
tm2 = time.perf_counter()
items.sort(key=lambda x: x[1], reverse=True)
print("排序花费时间：{}s".format(time.perf_counter()-tm2))
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
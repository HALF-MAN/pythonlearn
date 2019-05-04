"""
    政府工作报告词云
"""
import jieba
import wordcloud
from scipy.misc import imread
# mask = imread("fivestart.png")
f = open("../resources/新时代中国特色社会主义.txt", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="../resources/msyh.ttc",
                        width=1000, height=700,
                        background_color="white",
                        max_words=15
                        )
w.generate(txt)
w.to_file("../resources/grwordcloud.png")

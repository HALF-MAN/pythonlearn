"""
    jieba是用来中文分词的第三方库
    原理：
        利用一个中文词库，确定汉字之间的关联概率
        汉字之间概率大的组成词组，形成分词结果
        除了分词，用户还可以添加自定义的词组
    分词的三种模式：
        精确模式：把文本精确的切分开，不存在冗余单词
        全模式：把文本中所有可能的词语都扫描出来，有冗余
        搜索引擎模式：在精确模式基础上，对长词再次切分
    常用函数：
        jieba.lcut(s) 精确模式，返回一个列表类型的分词结果
        jieba.lcut(s, cut_all=True) 全模式，返回一个列表类型分词结果，存在冗余
        jieba.lcut_for_search(s) 搜索引擎模式，返回一个列表类型的分词结果，存在冗余
        jieba.add_word(w) 向分词词典增加新词
"""
import jieba
s = "中国是一个伟大的国家"
s1 = "中华人民共和国是伟大的"
s3 = "蟒蛇语言"
print(jieba.lcut(s1))
print(jieba.lcut(s1, cut_all=True))
print(jieba.lcut_for_search(s1))

#给中文词库添加新词
print(jieba.lcut_for_search(s3))
jieba.add_word("蟒蛇语言")
print(jieba.lcut_for_search(s3))
jieba.del_word("蟒蛇语言")


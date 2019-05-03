"""
wordcloud库基本使用:
    wordcloud库把词云当作一个WordCloud对象
    -wordcloud.WordCloud()代表一个文本对应的词云
    -可以根据文本中词语出现的频率等参数绘制词云
    -词云的绘制形状、尺寸和颜色都可以设定
wordcloud库常规方法：
    -以WordCloud对象为基础
    -配置参数、加载文本、输出文件
    w = wordcloud.WordCloud()
    w.generate(txt)     向WordCloud对象w中加载文本txt
    >>>w.generate("Python and WordCloud")
    w.to_file(filename)     将词云输出为图像文件，.png或.jpg格式
    >>>w.to_file("outfile.png")
    width   指定词云对象生成图片的宽度，默认400像素
    >>>w=wordcloud.WordCloud(width=600)
    height  指定词云对象生成图片的高度，默认200像素
    >>>w=wordcloud.WordCloud(height=400)
    min_font_size   指定词云中字体的最小字号，默认4号
    >>>w=wordcloud.WordCloud(min_font_size=10)
    max_font_size   指定词云中字体的最大字号，根据高度自动调节
    >>>w=wordcloud.WordCloud(max_font_size=20)
    font_step   指定词云中字体字号的步进间隔，默认为1
    >>>w=wordcloud.WordCloud(font_step=2)
    font_path   指定字体文件的路径，默认None
    >>>w=wordcloud.WordCloud(font_path="msyh.ttc")
    max_words   指定词云显示的最大单词数量，默认200
    >>>w=wordcloud.WordCloud(max_words=20)
    stop_words  指定词云的排除词列表，即不显示的单词列表
    >>>w=wordcloud.WordCloud(stop_words={"Python"})
    mask    指定词云形状，默认为长方形，需要引用imread()函数
    >>>from scipy.miscimport imread
    >>>mk=imread("pic.png")
    >>>w=wordcloud.WordCloud(mask=mk)
    background_color    指定词云图片的背景颜色，默认为黑色
    >>>w=wordcloud.WordCloud(background_color="white")
    文本————————>词云
    ①分隔: 以空格分隔单词
    ②统计: 单词出现次数并过滤
    ③字体: 根据统计配置字号
    ④布局: 颜色环境尺寸

"""
import wordcloud
c = wordcloud.WordCloud()
c.generate("wordcloud by Python")
c.to_file("../resources/pywordcloud.png")

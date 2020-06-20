# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/20 10:10
# 文件名称 : 匹配.py
# 开发工具 : PyCharm
import re
# 正则表达式字符见笔记,r'\bm\w*\b'匹配m开头的单词
# 匹配字符串(使用re模块)
pattern1 = r'mr_\w'
string1 = 'MR_SHOP mr_shop'
match = re.match(pattern1, string1, re.I)     # 指定正则表达式和要匹配的字符串,
# re.I不区分字母大小写,re.A不匹配汉字(默认区分且匹配),
# 仅从字符串开始处匹配,返回大写M的match对象,否则返回None
print(match)
pattern2 = r'(13[4-9]\d{8})|(15[01289]\d{8})$'  # 匹配手机号的模式字符串
# match.start(), match.end()可以显示起始和结束位置,match.group()可以显示匹配到的对象
match01 = match.start()
print(match01)
match02 = match.end()
print(match02)
match03 = match.group()
print(match03)
search = re.search(pattern1, string1, re.I)     # 在整个字符串(区别于match)搜索第一个匹配的对象,
# 返回大写M的match对象,否则返回None,
# 语法规则同match
print(search)
findall = re.findall(pattern1, string1, re.I)   # 在整个字符串(区别于match)搜索所有(区别于search)匹配的对象,
# 返回匹配到的字符串的列表,否则返回空列表,
# 语法规则同match
print(findall)
# 替换
string2 = re.sub(pattern1, 'USTC_S', string1, 1, re.I)  # 指定正则表达式,用于替换的字符串(即替换的匹配结果),原始字符串,
# 替换的最大次数(默认0,替换所有)
# re.I不区分字母大小写,re.A不匹配汉字(默认区分且匹配)
# 返回替换后的字符串
print(string2)
# re.split(pattern, string[, maxsplit, flags])用正则表达式分割字符串,返回分割后的字符串列表

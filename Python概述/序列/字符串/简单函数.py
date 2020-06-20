# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/18 17:14
# 文件名称 : 简单函数.py
# 开发工具 : PyCharm
str1 = '我的 fasad ccdntaaaasised s dafa'
print(len(str1.encode()))
print(len(str1.encode('gbk')))  # 计算字节数,空表示UTF-8,gbk需要另外说明
# 索引避免超出范围的方法
try:
    print(str1[1])
except IndexError:
    print('Error')
# 分割
list1 = str1.split('a', 4)
print(list1)  # 默认分隔符是空白字符,分割次数无限次,
# 连续的分隔符在一起会把后面的几个打出空格替代,
# 若指定参数n,分割n+1次,最后一个元素包含未分割的剩余字符串
# 合并
str2 = 'a'.join(list1)  # 指定分隔符,括号内是可迭代对象(即列表元组都行),字符串前端不会加上分隔符
print(str2)
# 检索
print(str1.count('a', 0, 19))  # 指定字符串和要检索的子字符串,起始位置默认首尾,返回出现次数
print(str1.find('a', 0, 15))  # 指定字符串和要检索的子字符串,起始位置默认首尾,返回第一次出现的位置
print(str1.rfind('a', 0, 15))  # 同上,从右边开始
print(str1.index('a', 0, 15))  # 同上,也有.rindex
print(str1.startswith('我的', 0, 15))  # 检查是否以指定字符串开头,默认首尾
print(str1.upper())  # 小写转大写
print(str1.lower())  # 大写转小写
print(str2.strip('a'))  # 只去除左右两端的对应字符,默认空格等,.lstrip()只去除左边的,.rstrip()只去除右边的
# 格式化
# 使用%,具体格式见笔记
template = '编号:%09d\t公司名称:%s\t官网:http://www.%s.com'  # 定义模板,三个%就是要转换的内容
item = (7, '百度', 'baidu')
print(template % item)
# 使用format()方法,具体格式见笔记
template = '编号:{:0>9s}\t公司名称:{:s}\t官网:http://www.{:s}.com'
context1 = template.format('7', '百度', 'baidu')
print(context1)

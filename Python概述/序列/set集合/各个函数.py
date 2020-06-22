# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/21 10:53
# 文件名称 : 各个函数.py
# 开发工具 : PyCharm
# 几乎同数学定义的集合,不可有重复元素,可用于去重
# 创建
s1 = {1, 2, 3, 4, 5, 6, 1, 2}    # 重复元素只会保留一个,无序集合,没有索引
s2 = set({})    # {}表示空字典,用set()强制转换
# set()也可以直接用于自动去重(例如用于列表)
# 添加,删除元素
s1.add(7)   # 这里不可以加可迭代对象,只能是单个元素
if 7 in s1:
    s1.remove(7)
else:
    print(r'value does not exist')
e = s1.pop()    # 随机删除一个元素,并返回他
s2.clear()  # 删除所有元素,得到空集合
del s2      # 删除整个集合
# 运算符号:&交    |并     -差      ^对称差集

# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/13 13:05
# 文件名称 : 各个函数.py
# 开发工具 : PyCharm
# 创建新列表
seq1 = ['one', 'two', 'three', 'four', 'five', 'six']
seq2 = []  # 一般用来接收函数返回值
seq3 = list(range(1, 9, 2))  # 不包括9
# 遍历元素的方法
for i in seq1:
    print(i)
for i, e in enumerate(seq1):  # enumerate(sequence, start = n)从第n个开始组合为一个索引序列,并列出数据和下标
    print(i, e)
# 访问元素的方法
print(seq1)
print(seq1[-1])
print(seq1[0:4:2])  # 不包括最后的4号
# 更新
# 添加
seq1.append('eight')  # 直接添加到末尾
print(seq1)
seq1.insert(6, 'seven')  # 添加到指定位置,原来的元素后移
print(seq1)
seq1.extend(seq3)  # 在最后添加一个列表
print(seq1)
# 修改: 直接用索引重新赋值
# 删除
del seq1[8]
del seq1[9]  # 用索引删除
if 5 in seq1:
    seq1.remove(5)
if 7 in seq1:
    seq1.remove(7)  # 用值删除,用if防止报错
# 统计计算
seq1.append('one')
print(seq1.count('one'))  # 统计某元素出现的次数
if 'one' in seq1:
    print(seq1.index('one'))  # 返回首次出现的索引
print(sum(seq3, 50))  # 计算数值列表中元素总和,再加上50
# 排序
seq4 = ['one', 'two', 'three', 'four', 'five', 'six']
seq4.sort(key=str.lower, reverse=False)     # 不区分大小写(省略时区分,大写在升序前面),
# False为默认值升序,True降序,直接修改原列表
print(seq4)
seq5 = ['one', 'two', 'three', 'four', 'five', 'six']
print(sorted(seq5, key=str.lower, reverse=False))   # 不改变原列表
print(seq5)
# 反序:seq1.reverse()和reversed(seq1)区别同上
# 列表推导式
import random
seq6 = [random.randint(10, 100)for i in range(10)]
print(seq6)
# 等价于以下
import random
seq7 = []
for i in range(10):
    seq7.append(random.randint(10, 100))
print(seq7)
# 表达式:list0 = [Expression for i in range(10)/list/list if condition]数值/指定需求列表/选择符合条件的元素


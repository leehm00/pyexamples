# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/18 16:56
# 文件名称 : 各个函数.py
# 开发工具 : PyCharm
# 创建
seq1 = ('one', 'two', 'three', 'four', 'five', 'six')
seq2 = ()  # 一般用来接收函数返回值
seq3 = tuple(list(range(1, 9, 2)))  # 不包括9
# 访问元素同列表
# 修改元组元素:不可单独修改某元素,元组是不可变序列,
#             可以整个重新赋值元组
#             可以对元组进行连接组合,直接序列相加
seq = seq1 + seq3
print(seq)
# 元组推导式:类似列表推导式
num = (i for i in range(10))
for i in num:
    print(i, end=' ')    # 不换行

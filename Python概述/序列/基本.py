# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/19 14:59
# 文件名称 : 基本.py
# 开发工具 : PyCharm
# 用列表演示
seq1 = ['one', 'two', 'three', 'four', 'five', 'six']
seq3 = list(range(1, 9, 2))
print(seq1[-2])     # 索引为负数表示倒序
print(seq1[1:5:2])      # 切片seq1[[start]:[end:step]]不包括end
seq2 = ['seven', 'eight', 'nine', 'ten']
seq4 = seq1 + seq2   # 相同类型序列直接拼接到一起
seq5 = 3 * seq2     # 3个此序列相加(一般用于输出指定个数的空格或者符号)
print('one' in seq1)
print('ten' in seq1)    # 判断元素是否在序列中
print(len(seq1))    # 计算长度
print(max(seq1))    # 找出最大元素
print(sum(seq3))    # 计算数字序列的和

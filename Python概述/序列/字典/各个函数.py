# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/20 11:00
# 文件名称 : 各个函数.py
# 开发工具 : PyCharm
# 认为字典是无序的,key为一,value不唯一(可以看作数学中的函数)元组可以作为key,但是列表不可以
# 创建和删除
d1 = {1: 1, 2: 2}
d2 = {}     # 或d2 = dict(),创建空字典
seq1 = ['one', 'two', 'three', 'four', 'five', 'six']
seq2 = [1, 2, 3, 4, 5, 6]
d3 = dict(zip(seq2, seq1))  # 两个元素数相同的列表,通过zip()返回一个zip对象,用dict()强制转换为字典
d4 = dict.fromkeys(seq2)    # 创建只有key没有value的字典
del d2  # 直接删除字典
d2 = {}
d2.clear()      # 删除为空字典
# 通过key值访问字典元素(全部输出直接prin()即可)
print(d3[2] if 2 in d3 else 'Error')    # 通过if避免报错
print(d3.get(2, 'Error'))   # 通过.get方法访问
# 遍历
print(d3.items())   # 返回一个可遍历的元组列表,每对key,value组成元组,再组成列表
for key, value in d3.items():   # 单独打印出来
    print(key, value)
print(d3.keys())    # 获取所有的keys
print(d3.values())  # 获取所有的values
# 添加,删除元素
d3[7] = 'seven'     # 直接添加,若key已存在则修改
if 7 in d3:     # 删除指定元素并防止报错
    del d3[7]
# 字典推导式:类似于列表推导式,换成{}即可
# {key表达式:value表达式 for循环}
d5 = {i: j for i, j in zip(seq2, seq1)}

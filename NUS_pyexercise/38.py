# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/3 11:39
# 文件名称 : 38.py
# 开发工具 : PyCharm
a = int(input())
b = int(input())
c = int(input())
square_numbers = []
for i in range(1, 11):
    square_numbers.append(i*i)
if a in square_numbers:
    print('True')
else:
    print('False')
if b in square_numbers:
    print('True')
else:
    print('False')
if c in square_numbers:
    print('True')
else:
    print('False')

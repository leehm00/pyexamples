# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/24 22:24
# 文件名称 : 27.py
# 开发工具 : PyCharm
a = input()
b = input()
c = input()
yours = input()
a1 = a + b + c
a2 = a + c + b
a3 = b + c + a
a4 = b + a + c
a5 = c + a + b
a6 = c + b + a
if yours == a1 or yours == a2 or yours == a3 or yours == a4 or yours == a5 or yours == a6:
    print('No')
else:
    print('Yes')

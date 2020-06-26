# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/24 9:31
# 文件名称 : 25.py
# 开发工具 : PyCharm
a = input()
b = input()
c = input()
d = input()
e = d.split()
if int(e[0]) == 1:
    x = a
    a = b
    b = x
if int(e[1]) == 1:
    x = b
    b = c
    c = x
if int(e[2]) == 1:
    x = a
    a = c
    c = x
print(a)
print(b)
print(c)

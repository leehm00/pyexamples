# _*_ coding.utf-8 _*_
# 开发人员 : lenvovo
# 开发时间 : 2020/2/10  10:14
# 文件名称 : 12.py
# 开发工具 : PyCharm
import math
a = float(input())
b = float(input())
c = float(input())
delta = math.sqrt(b*b-4*a*c)
x1 = (-b - delta)/(2*a)
x2 = (-b + delta)/(2*a)
print(x1)
print(x2)
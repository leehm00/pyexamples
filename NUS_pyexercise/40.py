# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/3 17:14
# 文件名称 : 40.py
# 开发工具 : PyCharm
global a, b, c


def f(n):
    s = 0
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    else:
        return a * f(n - 1) + b * f(n - 2) + c * f(n - 3)


n = int(input())
s1 = input()
s = s1.split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
print(f(n))

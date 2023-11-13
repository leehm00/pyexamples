# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/4 11:36
# 文件名称 : 41.py
# 开发工具 : PyCharm


def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return f(n / 2)
    else:
        return f(n-1)+1


n = int(input())
print(f(n))

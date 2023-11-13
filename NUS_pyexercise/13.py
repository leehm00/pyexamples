# _*_ coding.utf-8 _*_
# 开发人员 : lenvovo
# 开发时间 : 2020/2/10  15:18
# 文件名称 : 13.py
# 开发工具 : PyCharm
def jiecheng(n):
    f = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            f = f * i
        return f

def zuhe(m,n):
    return jiecheng(n)/jiecheng(n-m)/jiecheng(m)

a = int(input())
b = int(input())
n = int(input())
x = 0
y = 0
for i in range(0,n+1):
    if i % 4 == 0:
        x += zuhe(i, n) * a ** (n - i) * b ** i
    if i % 4 == 1:
        y += zuhe(i, n) * a ** (n - i) * b ** i
    if i % 4 == 2:
        x -= zuhe(i, n) * a ** (n - i) * b ** i
    if i % 4 == 3:
        y -= zuhe(i, n) * a ** (n - i) * b ** i
print(int(x))
print(int(y))
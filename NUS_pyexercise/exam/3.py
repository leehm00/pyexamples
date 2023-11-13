# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/18 20:28
# 文件名称 : 3.py
# 开发工具 : PyCharm
a = [0 for i in range(31)]
a[0] = 1
a[2] = 3
for i in range(1, 31, 2):
    a[i] = 0
for i in range(4, 31, 2):
    a[i] = a[i - 2] * 4 - a[i - 4]

while 1:
    n = input()
    if n == '-1':
        break
    print(a[int(n)])
exit()

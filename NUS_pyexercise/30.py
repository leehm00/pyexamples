# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/26 11:49
# 文件名称 : 30.py
# 开发工具 : PyCharm
a = input()
s = input()
ss = s.split()
for i in range(int(a)):
    b = 0
    for j in range(int(ss[i])):
        b += (j + 1) * (j + 1)
    print(b, end=' ')

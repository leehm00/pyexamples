# _*_ coding.utf-8 _*_
# 开发人员 : Leehm
# 开发时间 : 2020/2/11  17:07
# 文件名称 : 18.py
# 开发工具 : PyCharm
a = input()
b = int(input())
c = input()
d = a.split()
e = d[b:]
f = ' '.join(e)
print(f.count(c))
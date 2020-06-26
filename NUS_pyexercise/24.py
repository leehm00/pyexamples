# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/23 22:21
# 文件名称 : 24.py
# 开发工具 : PyCharm
s = input()
a = s.split()
if int(a[0])&int(a[1]) <= int(a[4]) < int(a[2])+int(a[3]):
    s1 = 0
else:
    s1 = 1
if int(a[2])|int(a[3]) < int(a[0]) <= int(a[3])*int(a[4]):
    s2 = 1
else:
    s2 = 0
if s2 == 0 and s1 ==0:
    print(True)
else:
    print(False)

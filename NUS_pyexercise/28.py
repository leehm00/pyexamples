# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/26 11:35
# 文件名称 : 28.py
# 开发工具 : PyCharm
s1 = input()
s2 = input()
a1 = s1.split()
a2 = s2.split()
s = 0
for i in range(int(a1[1])):
    s += int(a2[i])
print(s)

# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/5 12:08
# 文件名称 : 42.py
# 开发工具 : PyCharm
s1 = input()
s = s1.split()
a = int(s[0])
b = int(s[1])
while not a == b:
    if a>b:
        a = int(a/2)
    else:
        b = int(b/2)
print(a)

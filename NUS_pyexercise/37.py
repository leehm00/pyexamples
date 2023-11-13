# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/3 11:18
# 文件名称 : 37.py
# 开发工具 : PyCharm
s = input()
s1 = []
for i in reversed(s):
    s1.append(i)
flag = 1
for i in range(len(s)):
    if not s[i] == s1[i]:
        flag = 0
if flag == 1:
    print('Yes')
else:
    print('No')

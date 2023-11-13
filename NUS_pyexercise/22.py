# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/23 18:21
# 文件名称 : 22.py
# 开发工具 : PyCharm
s = input()
s1 = s.split()
if (int(s1[1]) >= 60 or int(s1[2]) >= 60) and int(s1[0]) > 60:
    print(True)
else:
    print(False)

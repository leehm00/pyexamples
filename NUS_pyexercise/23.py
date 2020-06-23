# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/23 18:50
# 文件名称 : 23.py
# 开发工具 : PyCharm
a = input()
b = a.split()
ab = bin(int(b[0]))
c = 0 - int(b[1])
print(ab[c])
if ab[c] == 1:
    print(True)
else:
    print(False)

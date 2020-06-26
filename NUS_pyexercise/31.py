# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/26 12:03
# 文件名称 : 31.py
# 开发工具 : PyCharm
n = int(input())
num = 0
i = 2
for i in range(2, n):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num += 1
print(num)

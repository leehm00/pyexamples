# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/26 12:03
# 文件名称 : 31.py
# 开发工具 : PyCharm
import math
n = int(input())
res = []
for i in range(2, n):
        flag = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = 1
        if flag == 0:
            res.append(i)
print(len(res))



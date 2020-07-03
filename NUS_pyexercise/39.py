# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/3 11:46
# 文件名称 : 39.py
# 开发工具 : PyCharm
import math


def isprime(n):
    if n <= 1:
        return False

    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n


n = int(input())
summation = 0
for i in range(1, n + 1):
    if i == 1:
        summation += 10
    elif isprime(i):
        summation += i * i
    elif isSqr(i):
        summation += 2 * math.sqrt(i) + 1
    else:
        summation += int(math.sqrt(i))
print(int(summation))

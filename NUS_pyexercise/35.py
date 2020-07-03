# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/1 18:42
# 文件名称 : 35.py
# 开发工具 : PyCharm
a = input()
s = a.split()
count = 1
for i in range(1, int(s[0])+1):
    if not (i % 3 == 0 or i % 5 == 0 or str(i).count('5') > 0 or str(i).count('3') > 0):
        print(i)
        count += 1
    if count > int(s[1]):
        break

# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/18 20:49
# 文件名称 : 205.py
# 开发工具 : PyCharm
while 1:
    n = input()
    if n == '0':
        break
    integers = n.split()
    del integers[0]
    max = int(integers[0])
    for i in integers:
        if int(i) > max:
            max = int(i)
    print(max)
exit()

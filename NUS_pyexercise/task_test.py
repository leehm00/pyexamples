# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/8 11:58
# 文件名称 : 46.py
# 开发工具 : PyCharm
s1 = input()
s = s1.split()
lights = []
for i in range(int(s[1])*int(s[0])):
    lights.append(0)
ops = []
for i in range(int(s[2])):
    ops.append(input())
for i in ops:
    op = i.split()
    if op[0] == '1':
        lights[(int(op[1]) - 1)*int(op[2])] = 1
    if op[0] == '2':
        lights[(int(op[1]) - 1)*int(op[2])] = 0
    if op[0] == '3':
        for j in range(int(s[1])):
            if lights[(int(op[1])-1)*int(s[1])+j] == 1:
                lights[(int(op[1]) - 1) * int(s[1]) + j] = 0
            else:
                lights[(int(op[1]) - 1) * int(s[1]) + j] = 1
    count = 0
    for x in lights:
        if x == 1:
            count += 1
    print(lights)
    print(count)

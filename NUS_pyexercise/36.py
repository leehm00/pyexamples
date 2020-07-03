# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/2 22:36
# 文件名称 : 36.py
# 开发工具 : PyCharm
a = input()
number = a.split()
a1 = input()
cake = input()
cakes = cake.split()
people = a1.split()
count = 1
boys = []
girls = []
for i in people:
    if count % 2 == 0:
        boys.append(int(i))
    else:
        girls.append(int(i))
    count += 1
count_cake = 1
for i in cakes:
    if count_cake % 2 == 0:
        count_boy = -1
        while boys[count_boy] < int(i):
            count_boy -= 1
        print(2*(int(number[0]) + count_boy + 1))
    else:
        count_girl = 1
        while girls[count_girl-1] < int(i):
            count_girl += 1
        print(2*count_girl - 1)
    count_cake += 1

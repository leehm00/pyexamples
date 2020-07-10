# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/8 11:20
# 文件名称 : 45.py
# 开发工具 : PyCharm
s1 = input()
s = s1.split()
max_size1 = input()
max_size = max_size1.split()
store1 = input()
store = store1.split()
days = []
count = 0
for i in range(5 * int(s[1])):
    days.append(input())
for i in days:
    day = i.split()
    if day[0] == '1':
        if int(max_size[int(day[1])-1]) - int(store[int(day[1])-1]) > int(day[2]):
            store[int(day[1])-1] = str(store[int(day[1])-1] + int(day[2]))
        else:
            store[int(day[1])-1] = str(int(max_size[int(day[1])-1]))

    if day[0] == '2':
        if int(store[int(day[1])-1]) >= int(day[2]):
            store[int(day[1])-1] = str(int(store[int(day[1])-1]) - int(day[2]))

    count += 1
    if count % 5 == 0:
        print(' '.join(store))


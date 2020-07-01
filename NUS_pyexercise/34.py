# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/1 10:39
# 文件名称 : 34.py
# 开发工具 : PyCharm
a = input()
name = input()
names = name.split()
grade = input()
grades = grade.split()
d = []
for i in range(int(a[2])):
    d.append(input())
for i in range(int(a[2])):
    seen_names = names[int(d[i][0])-1: int(d[i][2])]
    s = set(seen_names)
    seen_grades = grades[int(d[i][0])-1: int(d[i][2])]
    lists = list(s)
    all_sum = 0
    for j in lists:
        count = 0
        grade1 = 0
        while j in seen_names:
            x = seen_names.index(j)
            grade1 += int(seen_grades[x])
            count += 1
            del seen_names[x]
            del seen_grades[x]
        one_ave = grade1/count
        all_sum += one_ave
    print(all_sum/len(lists))

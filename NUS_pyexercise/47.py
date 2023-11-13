# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/9 18:59
# 文件名称 : 47.py
# 开发工具 : PyCharm
s = input()
a = []
count = 0
for i in s:
    if i == '[':
        count = 0
    elif i == ']':
        count = len(a) - 1
    elif i == '-':
        if 0 <= count - 1 <= len(a) - 1:
            del a[count - 1]
            count -= 1
    elif i == '_':
        a.insert(count, ' ')
        count += 1
    elif i == '>':
        if 0 <= count - 1 <= len(a) - 2:
            count += 1
    elif i == '<':
        if 1 <= count - 1 <= len(a) - 1:
            count -= 1
        print('hh', count - 1)
    else:
        a.insert(count, i)
        count += 1
if not a:
    print('?')
else:
    print(''.join(a))

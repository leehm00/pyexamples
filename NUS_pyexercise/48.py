# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/10 9:49
# 文件名称 : 48.py
# 开发工具 : PyCharm


class Stack():  # 定义类
    def __init__(self):  # 产生一个空的容器
        self.__list = []

    def push(self, item):  # 入栈
        self.__list.append(item)

    def pop(self):  # 出栈
        return self.__list.pop()

    def speek(self):  # 返回栈顶元素
        return self.__list[-1]

    def is_empty(self):  # 判断是否已为空
        return not self.__list

    def size(self):  # 返回栈中元素个数
        return len(self.__list)


s = Stack()
s1 = input()
x = s1.split()
a = []
for i in range(int(x[0])):
    a.append(input())
for i in a:
    op = i.split()
    if op[0] == '1':
        if s.is_empty():
            print('?')
        else:
            print(s.pop())
    if op[0] == '2':
        s.push(int(op[1]))

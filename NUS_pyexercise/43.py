# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/5 15:10
# 文件名称 : 43.py
# 开发工具 : PyCharm


class Stack(object):
    """堆栈"""

    def __init__(self):
        self._stack = []

    def pop(self):
        return self._stack.pop()

    def push(self, x):
        self._stack.append(x)


def solve(bds):
    """根据后缀表达式求值"""
    jisuan = {
        '*': lambda x, y: x * y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y
    }
    s = Stack()
    for x in bds:
        if x in '*+-':
            num2, num1 = s.pop(), s.pop()
            r = jisuan[x](int(num1), int(num2))
            s.push(r)
        else:
            s.push(x)

    return s.pop()


s1 = input()
s = s1.split()
s.reverse()
print(solve(s))

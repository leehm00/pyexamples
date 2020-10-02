# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/8 11:58
# 文件名称 : 46.py
# 开发工具 : PyCharm
class Stack(object):
    """堆栈"""

    def __init__(self):
        self._stack = []

    def pop(self):
        return self._stack.pop()

    def push(self, x):
        self._stack.append(x)


S = Stack()
s_empty = Stack()
S.push('1')
print(S.pop())
if not S == s_empty:
    print(S.pop())

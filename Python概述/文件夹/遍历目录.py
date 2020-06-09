# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/9 21:34
# 文件名称 : 遍历目录.py
# 开发工具 : PyCharm
import os
path = os.walk('E:\文档\py examples')
for i in path:
    print(i, '\n')

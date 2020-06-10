# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/9 21:34
# 文件名称 : 遍历目录.py
# 开发工具 : PyCharm
import os
path = 'E:\文档\py examples\Python概述'
for root, dirs, files in os.walk(path):
    for name in dirs:
        print(os.path.join(root, name))     #输出遍历的子目录
    for name in files:
        print('\t', os.path.join(root, name))    #输出遍历的文件

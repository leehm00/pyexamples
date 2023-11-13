# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/8 21:06
# 文件名称 : 递归调用创建多级目录.py
# 开发工具 : PyCharm
import os


def mkdir(path):
    if not os.path.isdir(path):
        mkdir(os.path.split(path)[0])
    else:
        return
    os.mkdir(path)


mkdir('E:\文档\py examples\Python概述\python\wuli\wala')

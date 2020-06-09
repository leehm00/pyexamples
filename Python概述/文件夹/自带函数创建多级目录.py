# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/8 21:34
# 文件名称 : 自带函数创建多级目录.py
# 开发工具 : PyCharm
import os
if not (os.path.exists('E:\文档\py examples\Python概述')):
    os.makedirs('E:\文档\py examples\Python概述\python\wuli\wala')
else:
    print('当文件已存在时，无法创建该文件')

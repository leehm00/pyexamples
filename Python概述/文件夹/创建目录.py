# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/8 18:47
# 文件名称 : 创建目录.py
# 开发工具 : PyCharm
import os

if not (os.path.exists('E:\文档\py examples\Python概述')):
    os.mkdir('E:\文档\py examples\Python概述')
else:
    print('当文件已存在时，无法创建该文件')

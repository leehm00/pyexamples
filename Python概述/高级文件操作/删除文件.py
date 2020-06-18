# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/10 18:40
# 文件名称 : 删除文件.py
# 开发工具 : PyCharm
import os

if (os.path.exists('E:\文档\py examples\Python概述\demo1\demo.txt')):  # 先判断是否存在
    os.remove('E:\文档\py examples\Python概述\demo1\demo.txt')
    print('删除成功')
else:
    print('当路径不存在时，无法删除')

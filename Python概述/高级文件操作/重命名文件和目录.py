# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/10 18:49
# 文件名称 : 重命名文件和目录.py
# 开发工具 : PyCharm
import os

if (os.path.exists('E:\文档\py examples\Python概述\demo1')):  # 先判断是否存在
    os.rename('E:\文档\py examples\Python概述\demo1', 'E:\文档\py examples\Python概述\demo')
    print('重命名成功')
else:
    print('当路径不存在时，无法重命名')

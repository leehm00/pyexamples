# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/7 19:19
# 文件名称 : 路径.py
# 开发工具 : PyCharm
import os
print(os.getcwd())
# with open('message.txt') as file:   #通过相对路径打开文件
#    pass
with open('../demo1/demo.txt', encoding='UTF-8') as file:  # 或者用\\代替/
    print(file.read())
print(os.path.abspath('../demo1/demo.txt'))
print(os.path.join('/Python概述', 'demo1\demo.txt'))  # 若都是相对路径拼接后也是相对路径,
# 不会判断路径是否真实存在,多个绝对路径以最后出现的为准

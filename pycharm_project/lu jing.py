# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/7 19:19
# 文件名称 : lu jing.py
# 开发工具 : PyCharm
import os
print(os.getcwd())
#with open('message.txt') as file:   #通过相对路径打开文件
    #pass
with open('demo1/demo.txt', encoding='UTF-8') as file:  #或者用\\代替/
    print(file.read())
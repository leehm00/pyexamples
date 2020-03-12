# _*_ coding.utf-8 _*_
# 开发人员 : Leehm
# 开发时间 : 2020/2/14  21:22
# 文件名称 : demo.py
# 开发工具 : PyCharm
with open('message.txt', 'r') as file:
    message = file.readlines()
    for i in message:
        print(i)
    print(message)

# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/23 9:29
# 文件名称 : 继承.py
# 开发工具 : PyCharm


class Fruit:  # 驼峰式命名法:大写字母开头,后面的每个单词首字母也大写
    """水果类"""
    color = '绿色'  # 类属性

    def harvest(self, color):
        print('水果是' + color + '的')  # 输出形式参数color
        print('水果已收获')
        print('水果原来是' + Fruit.color + '的')  # 输出类属性


class Apple(Fruit):  # 括号内是要继承的基类名称,多个用逗号分隔,默认继承object
    """类的帮助信息"""
    color = '红色'

    def __init__(self):
        print('我是苹果')


class Orange(Fruit):
    """
    类的帮助信息
    """
    color = '橙色'

    def __init__(self):
        print('我是橘子')


apple = Apple()     # 创建Apple实例
apple.harvest(apple.color)      # 调用harvest方法,继承了基类的实例方法和类属性
orange = Orange()
orange.harvest(orange.color)

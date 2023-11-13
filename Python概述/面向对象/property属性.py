# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 16:31
# 文件名称 : property属性.py
# 开发工具 : PyCharm
# 类和实例属性返回的是储存的值,property访问的是计算后所得的值
# 通过@property将一个方法转换为属性,也称装饰器
# 好处在于可以用方法名访问到值,不需要括号


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rect(800, 600)
print('Area = ', rect.area)
# rect.area = 480000这样的语句会报错,property属性不可以赋值

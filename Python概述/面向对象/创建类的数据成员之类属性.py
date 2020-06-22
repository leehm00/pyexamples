# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 10:22
# 文件名称 : 创建类的数据成员之类属性.py
# 开发工具 : PyCharm
# 在类之中定义的变量:
# 1.类属性:在类中,并且在方法体外实现,所有实例之间共享值


class Geese:
    """大雁类"""
    neck = 'neck'
    wing = 'wing'
    leg = 'leg'  # 类属性,使用时类名.类属性即实现
    number = 0

    def __init__(self):  # 构造方法只能有一个
        Geese.number += 1
        print('第%d只大雁' % Geese.number)
        print(Geese.neck, Geese.wing, Geese.leg, Geese.beak)


Geese.beak = 'Beak'     # 在后面也可以添加类属性,这样都会有这个属性
list1 = []
for i in range(4):
    list1.append(Geese())  # 创建大雁类实例
print('一共%d只' % Geese.number)

# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 11:04
# 文件名称 : 创建类的数据成员之实例属性.py
# 开发工具 : PyCharm
# 在类之中定义的变量:
# 2.实例属性:在类中,并且在方法体内实现,只作用于当前实例


class Geese:
    """大雁类"""
    def __init__(self):  # 构造方法只能有一个
        self.neck = 'neck'
        self.wing = 'wing'
        self.leg = 'leg'    # 实例属性
        print('大雁类')
        print(self.neck, self.wing, self.leg)   # 访问实例属性


geese = Geese()
print(geese.leg)

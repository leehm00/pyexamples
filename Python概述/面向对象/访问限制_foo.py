# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 11:16
# 文件名称 : 访问限制_foo.py
# 开发工具 : PyCharm
# _foo:protected类本身和子类可以访问,可以通过实例访问


class Swan:
    """swan"""
    _neck_swan = 'neck_swan'  # 保护类型的属性

    def __init__(self):
        print(Swan._neck_swan)  # 访问该属性


swan = Swan()
print(swan._neck_swan)      # 通过实例名访问保护类型的属性

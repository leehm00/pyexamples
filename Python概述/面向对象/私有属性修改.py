# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 16:27
# 文件名称 : 私有属性修改.py
# 开发工具 : PyCharm


class Swan:
    """swan"""
    __neck_swan = 'neck_swan'  # 私有类型的属性

    def __init__(self):
        print(Swan.__neck_swan)  # 访问该属性,可行
    def my(self):
        print('方法中的私有属性', Swan.__neck_swan)


swan = Swan()
# print(swan.__neck_swan)      # 通过实例名不可以访问私有类型的属性
print(swan._Swan__neck_swan)    # 只有这样的格式可以在类定义之外访问
swan._Swan__neck_swan = 'neck'      # 这样的格式可以对私有属性进行修改
print('修改后', swan._Swan__neck_swan)
swan.my()   # 但是并没有改变在方法中调用的私有属性的值

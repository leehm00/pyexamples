# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 16:19
# 文件名称 : 访问限制__foo.py
# 开发工具 : PyCharm
# __foo:private类本身可以访问,类实例不可访问,仅可以通过实例名._类名__foo访问


class Swan:
    """swan"""
    __neck_swan = 'neck_swan'  # 私有类型的属性

    def __init__(self):
        print(Swan.__neck_swan)  # 访问该属性,可行


swan = Swan()
# print(swan.__neck_swan)      # 通过实例名不可以访问私有类型的属性
print(swan._Swan__neck_swan)    # 只有这样的格式可以在类定义之外访问

# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 9:21
# 文件名称 : 创建实例.py
# 开发工具 : PyCharm
# 类是一组相似事物的统称
# 定义


class Geese:    # 驼峰式命名法:大写字母开头,后面的每个单词首字母也大写
    """大雁类"""
    pass
# 若创建类时没有创建__init__()方法,或者是在__init__()方法中只有一个def参数的话,parameterlist可以省略,
# 否则指定的就是__init__()方法需要传递的参数


WildGoose = Geese()
print(WildGoose)

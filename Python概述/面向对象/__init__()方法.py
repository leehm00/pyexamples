# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 9:36
# 文件名称 : __init__()方法.py
# 开发工具 : PyCharm
# 相当于构造方法,创建类的实例时会被自动执行


class Geese:
    """大雁类"""
    def __init__(self, beak, wing, claw):   # 构造方法只能有一个
        print('大雁类')    # 判断init是否执行了
        print(beak, wing, claw)


beak1 = 'beak1'
wing1 = 'wing1'
claw1 = 'claw1'
WildGoose = Geese(beak1, wing1, claw1)      # 传入init的三个参数,self自动传入

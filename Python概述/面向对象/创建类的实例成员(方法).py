# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 10:15
# 文件名称 : 创建类的实例成员(方法).py
# 开发工具 : PyCharm
# 与函数类似,第一个参数必须是self且必须是包含此参数


class Geese:
    """大雁类"""

    def __init__(self, beak, wing, claw):  # 构造方法只能有一个
        print('大雁类')  # 判断init是否执行了
        print(beak, wing, claw)

    def fly(self, state='可以飞'):  # 飞行方法,制定了默认值
        print(state)


beak1 = 'beak1'
wing1 = 'wing1'
claw1 = 'claw1'
WildGoose = Geese(beak1, wing1, claw1)  # 传入init的三个参数,self自动传入
WildGoose.fly('fly1')

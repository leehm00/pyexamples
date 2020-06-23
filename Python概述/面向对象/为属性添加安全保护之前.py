# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/22 18:25
# 文件名称 : 为属性添加安全保护之前.py
# 开发工具 : PyCharm
# 私有属性(前加__)一般不可读取也不可修改


class TVShow:
    def __init__(self, show):
        self.__show = show

    def show(self):
        return self.__show  # 返回私有属性


tv_show = TVShow('战狼')
print(tv_show.show())

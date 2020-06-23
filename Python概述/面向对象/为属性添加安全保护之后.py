# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/23 9:07
# 文件名称 : 为属性添加安全保护之后.py
# 开发工具 : PyCharm


class TVShow:
    list_film = ['a', 'b', 'c', 'd']

    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show      # 返回私有属性

    @show.setter
    def show(self, value):
        if value in TVShow.list_film:   # 判断是否在列表中
            self.__show = '您选择了' + value + '稍后将播放'      # 修改返回的值
        else:
            self.__show = '您选择的电影不存在'


tv_show = TVShow('a')   # 创建实例
print('正在播放', tv_show.show)     # 获取属性值
print('可以从', tv_show.list_film, '中选择')
tv_show.show = 'b'
print(tv_show.show)

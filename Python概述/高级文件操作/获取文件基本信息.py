# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/6/10 19:02
# 文件名称 : 获取文件基本信息.py
# 开发工具 : PyCharm
import os


def formatTime(longtime):  # 格式化时间
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))


def formatByte(number):  # 格式化大小
    for (scale, label) in [(1024 * 1024 * 1024, 'GB'), (1024 * 1024, 'MB'), (1024, 'KB')]:
        if number >= scale:  # 比1单位大
            return '%.2f %s' % (number * 1.0 / scale, label)
        elif number == 1:  # 等于1字节
            return '1B'
        else:  # 小于1单位
            byte = '%.2f' % (number or 0)
    return (byte[:-3] if byte.endswith('.00') else byte) + 'B'


path = 'E:\文档\py examples\Python概述\hello.py'
if os.path.exists(path):  # 先判断是否存在
    fileinfo = os.stat(path)
    # 输出基本信息
    print('索引号:', fileinfo.st_ino)
    print('设备名:', fileinfo.st_dev)
    print('文件大小:', formatByte(fileinfo.st_size))
    print('最后一次访问时间:', formatTime(fileinfo.st_atime))
    print('最后一次修改时间:', formatTime(fileinfo.st_mtime))
    print('最后一次状态变化时间:', formatTime(fileinfo.st_ctime))

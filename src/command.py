"""
主要命令

要提示mac系统必须用sudo权限

record的参数
start_key: 默认: None，直接开始
end_key: 默认`Esc`，结束记录
exclude_events: 指定不记录哪些事件
dest: 指定脚本输出文件夹
filename: 指定脚本名称
continue: 指定脚本名称，相当于append

run的参数
start_key: 默认: None，直接开始
end_key: 默认`Esc`，中途暂停
filename: 脚本名称

以后的todo，但是也只能手动编辑
if语句、while语句
"""
import platform



def write():
    """
    写入脚本文件
    :return:
    """
    device_info = 'DEVICE: {} {}'.format(
        platform.system(), platform.release()
    )
    screen_info = 'SCREEN_SIZE: {}'.format(
        ''  # 我擦，这个都跟系统有关
    )

if __name__ == '__main__':
    pass
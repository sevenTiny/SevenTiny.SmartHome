# coding=utf-8
import configparser

# 树莓派的ubuntu系统里面如果要使用计划任务，则必须写成绝对路径，意味着这里需要加前缀
# RASPBERRY_PI_PATH = '/7tniy/SevenTiny.SmartHome'

# Windows调试不需要加绝对路径
RASPBERRY_PI_PATH_ROOT = '.'

# get configuration
config = configparser.ConfigParser()
config.read(RASPBERRY_PI_PATH_ROOT + '/Utility/SmartHome.ini',encoding='UTF-8')


class Cfg_MySql:

    __tag = 'MySql'

    def __init__(self):
        pass

    def get(self, name):
        return config.get(self.__tag, name)

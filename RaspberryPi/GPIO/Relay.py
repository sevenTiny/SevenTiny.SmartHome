# coding=utf-8
import RPi.GPIO as GPIO
import time
import sys
sys.path.append('..')
import abc

# 继电器控制基类，不要直接初始化该类
class RelayBase(metaclass=abc.ABCMeta):

    # 针脚存储集合
    plist=[]

    def __init__(self):
        # Board模式
        GPIO.setmode(GPIO.BOARD)
        # 关闭提示
        GPIO.setwarnings(False)
        # 将引脚设置为输出模式
        for item in self.plist:
            # GPIO.setup(item, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(item, GPIO.OUT)

    # 启动继电器
    def open(self, p):
        GPIO.output(self.plist[p-1], GPIO.LOW)

    # 关闭继电器
    def close(self, p):
        GPIO.output(self.plist[p-1], GPIO.HIGH)

    # 打开全部
    def openall(self):
        for item in self.plist:
            GPIO.output(item, GPIO.HIGH)

    # 关闭全部
    def closeall(self):
        for item in self.plist:
            GPIO.output(item, GPIO.LOW)

# 四针脚继电器控制类
class Relay4(RelayBase):
    def __init__(self, p1, p2, p3, p4):
        self.plist = [p1, p2, p3, p4]
        super().__init__()



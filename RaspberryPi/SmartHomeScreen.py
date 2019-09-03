# coding=utf-8
from Utility.MySqlHelper import MySqlHelper
import _thread
import Adafruit_DHT
from GPIO.NixieTube import Yang4
import time
import datetime
import RPi.GPIO as GPIO
import sys
sys.path.append('..')


def WriteToDb(timenow, year, month, day, hour, temp, humi):
    smartHomeDb = MySqlHelper("SmartHome")
    smartHomeDb.executeSql("INSERT INTO DailyMonitor (DateTime,Year,Month,Day,Hour,Temperature,Humidity) VALUES ('{0}',{1},{2},{3},{4},{5},{6})".format(
        timenow, year, month, day, hour, temp, humi))


y4 = Yang4(35, 16, 22, 32, 31, 36, 38, 33, 37, 12, 18, 40)
delay = 600

# 已经写入数据库的小时标识，插入数据的同时，修改为下一个小时，用于比较是否需要写入
hasWriteToDbHour = datetime.datetime.now().hour

while(True):
    # time
    timenow = datetime.datetime.now()

    for i in range(0, delay):
        y4.Display(str(timenow.year))
        time.sleep(0.005)

    for i in range(0, delay):
        y4.Display(str(timenow.month).zfill(
            2)+'.'+str(timenow.day).zfill(2))
        time.sleep(0.005)

    for i in range(0, delay):
        y4.Display(str(timenow.hour).zfill(
            2)+'.'+str(timenow.minute).zfill(2))
        time.sleep(0.005)

    y4.Display('....')

    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    # this is bcm code
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    print('time:{0},humidity:{1}%,temperature:{2}*C'.format(
        datetime.datetime.now(), humidity, temperature))

    # 异步将数据写入mysql
    if hasWriteToDbHour == timenow.hour:
        _thread.start_new_thread(WriteToDb, (timenow, timenow.year,
                                             timenow.month, timenow.day, timenow.hour, temperature, humidity))
        if hasWriteToDbHour == 23:
            hasWriteToDbHour = 0
        else:
            hasWriteToDbHour = hasWriteToDbHour + 1

    if temperature is not None:
        for i in range(0, delay):
            y4.Display('{0:0.1f}C'.format(temperature))
            time.sleep(0.005)

    if humidity is not None:
        for i in range(0, delay):
            y4.Display('H{0:0.1f}'.format(humidity))
            time.sleep(0.005)

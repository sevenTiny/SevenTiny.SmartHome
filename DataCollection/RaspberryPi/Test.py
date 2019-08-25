# coding=utf-8
import time
import datetime
import sys
sys.path.append('..')

from Utility.MySqlHelper import MySqlHelper

smartHomeDb = MySqlHelper("SmartHome")

conn,cur = smartHomeDb.getConnAndCur()

timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cur.execute("INSERT INTO DailyMonitor (DateTime,Year,Month,Temperature,Humidity) VALUES ('{0}',{1},{2})".format(timenow,51,31))
conn.commit()

cur.close()
conn.close()
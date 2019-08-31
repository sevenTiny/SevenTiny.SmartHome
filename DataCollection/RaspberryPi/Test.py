# coding=utf-8
import time
import datetime
import sys
sys.path.append('..')

from Utility.MySqlHelper import MySqlHelper
from GPIO.Relay import Relay4

# smartHomeDb = MySqlHelper("SmartHome")

# conn,cur = smartHomeDb.getConnAndCur()

# timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# cur.execute("INSERT INTO DailyMonitor (DateTime,Year,Month,Temperature,Humidity) VALUES ('{0}',{1},{2})".format(timenow,51,31))
# conn.commit()

# cur.close()
# conn.close()

r4 = Relay4(11,13,15,29)
r4.open(4)
# r4.close(4)

# coding=utf-8
import pymysql
from Utility.Configs import Cfg_MySql

class MySqlHelper:
    conn = None

    def __init__(self, db):
        cfg_mysql = Cfg_MySql()
        self.conn = pymysql.connect(host=cfg_mysql.get('host'), port=int(cfg_mysql.get('port')), user=cfg_mysql.get('user'), passwd=cfg_mysql.get('passwd'), db=db)

    def getConnAndCur(self):
        return self.conn,self.conn.cursor()

    def executeSql(self,sql):
        conn,cur = self.getConnAndCur()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

# 用完记得释放
# cur.close()
# conn.close()

import datetime
from Utility.MySqlHelper import MySqlHelper
from flask import Flask, request, jsonify, render_template
from flask_cors import *
import configparser
from GPIO.Relay import Relay4
import sys
sys.path.append('..')

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域

# get configuration
configPaht = '/7tiny/SevenTiny.SmartHome/SmartHome.ini'
config = configparser.ConfigParser()
# config.read('.\SmartHome.ini', encoding='UTF-8')
config.read(configPaht, encoding='UTF-8')


# 测试接口
@app.route('/')
def hello_world():
    return render_template("index.html")


# 智能开关 --------------------------------

# view-智能开关页面
@app.route('/smartbuttonview')
def smartbutton_view():
    return render_template("smart_button.html")

# --- 接口 ---

# 获取4路开关列表
@app.route('/relaylist')
def relay_list():
    returnList = []
    arr = config.get('Relay', 'relays').split(',')
    for item in arr:
        returnList.append({'index': config.get(
            'Relay'+item, 'index'), 'name': config.get(
            'Relay'+item, 'name'), 'status': config.get('Relay'+item, 'status')})
    return jsonify(returnList)

# 控制4路继电器的状态，同时将开关状态写入配置文件
@app.route('/relay')
def relay_control():
    try:
        index = int(request.args.get('index'))
        status = int(request.args.get('status'))

        if index != None and status != None:
            # 初始化继电器
            r4 = Relay4(11, 13, 15, 29)
            # # set replay
            if status == 1:
                r4.open(index)
            else:
                r4.close(index)
            # write to config
            config.set('Relay'+str(index), 'status', str(status))
            config.write(open(configPaht, "w"))

        return '1'
    except Exception as err:
        print(str(err))
        return '0'


# 家庭十二时辰 --------------------------------

# view-监控web界面
@app.route('/monitorview')
def monitor_view():
    return render_template("temperature.html")

# view-温度监控界面
@app.route('/temperatureview')
def temperature_view():
    return render_template("temperature.html")

# --- 接口 ---

# 温度-当年平均
@app.route('/temperature_current_year_avg')
def temperature_current_year_avg():
    smartHomeDb = MySqlHelper("SmartHome")
    conn, cur = smartHomeDb.getConnAndCur()
    timenow = datetime.datetime.now()
    cur.execute("")
    datas = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify({"": ""})

# 温度-当月平均
@app.route('/temperature_current_month_avg')
def temperature_current_month_avg():
    smartHomeDb = MySqlHelper("SmartHome")
    conn, cur = smartHomeDb.getConnAndCur()
    timenow = datetime.datetime.now()
    cur.execute("")
    datas = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify({"": ""})

# 温度-本周
@app.route('/temperature_current_week')
def temperature_current_week():
    smartHomeDb = MySqlHelper("SmartHome")
    conn, cur = smartHomeDb.getConnAndCur()
    timenow = datetime.datetime.now()
    cur.execute("")
    datas = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify({"": ""})

# 温度-当日
@app.route('/temperature_current_day')
def temperature_current_day():
    smartHomeDb = MySqlHelper("SmartHome")
    conn, cur = smartHomeDb.getConnAndCur()
    timenow = datetime.datetime.now()
    cur.execute("SELECT `Hour`,Temperature FROM DailyMonitor WHERE Year="+str(timenow.year) +
                " AND Month="+str(timenow.month)+" AND `Day`="+str(timenow.day)+" ORDER BY `Hour`")
    datas = cur.fetchall()
    hours = []
    temperatures = []
    for item in datas:
        hours.append(item[0])
        temperatures.append(item[1])

    cur.close()
    conn.close()
    return jsonify({"hours": hours, "temperatures": temperatures})


# 上帝之眼 --------------------------------

# view-上帝之眼界面
@app.route('/godeyeview')
def godeye_view():
    return render_template("index.html")



if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # app.debug = True
    app.run(host='0.0.0.0', port=39901)
    # app.run()

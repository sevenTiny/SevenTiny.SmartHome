from flask import Flask, request, jsonify
import configparser
from GPIO.Relay import Relay4
import sys
sys.path.append('..')

app = Flask(__name__)

# get configuration
# configPath = './SmartHome.ini'
configPaht = '/7tiny/SevenTiny.SmartHome/DeviceControl/WebServer/SmartHome.ini'
config = configparser.ConfigParser()
config.read(configPaht, encoding='UTF-8')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/relaylist')
def relay_view():
    returnList = []
    arr = config.get('Relay', 'relays').split(',')
    for item in arr:
        returnList.append({'index': config.get(
            'Relay'+item, 'index'), 'name': config.get(
            'Relay'+item, 'name'), 'status': config.get('Relay'+item, 'status')})
    return jsonify(returnList)


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


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # app.debug = True
    app.run(host='0.0.0.0', port=39901)
    # app.run()

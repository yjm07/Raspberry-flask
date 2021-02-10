from flask import Flask
import wifi_scan as wf
import ble_scan as bl
import json


app = Flask(__name__, static_url_path="", static_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/wifi')
def get_wifi_list():
    _list = wf.scan_wifi()
    
    # dict to json
    result = json.dumps(_list, ensure_ascii = False)

    return result


@app.route('/ble')
def get_ble_list():
    _list = bl.scan_ble()

    result = ''
    for i in _list:
        result += i + ' '

    return result


def run():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run()

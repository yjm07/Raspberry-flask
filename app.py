from flask import Flask, render_template
import wifi_scan as wf
import connected_wifi as c_wf
import ble_scan as bl
import json


app = Flask(__name__, static_url_path="")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', data = c_wf.connected_wifi())


@app.route('/wifi')
def get_wifi_list():
    _list = wf.scan_wifi()
    
    # dict to json
    result = json.dumps(_list, ensure_ascii = False)

    return result


@app.route('/wifi_0')
def show_connected_wifi():
    _list = c_wf.connected_wifi()

    return _list


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

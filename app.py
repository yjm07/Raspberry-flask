from flask import Flask
from flask_socketio import SocketIO
import wifi as scripts
import handler as handlers


app = Flask(__name__, static_url_path="", static_folder='templates')
app.wifi_list = set()
socketio = SocketIO(app)


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/wifi')
@socketio.on('ssid_list')
def ssid_list():
    print('getting ssid list')
    app.action = 'ssid_list'
    # log('getting ssid list')

    _list = scripts.get_ssid_list()
    app.wifi_list.update(_list.split("\n"))
    _list = ""
    for item in app.wifi_list:
        _list += item + "\n"

    socketio.emit('ssid_list', _list)
    return _list 


@app.route('/wifi0')
def get_wifi_list():
    return handlers.scan_candidate_wifi()


def run(_debug=True):
    socketio.run(app, debug=_debug, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run()
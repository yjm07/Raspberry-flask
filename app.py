from flask import Flask
import wifi_scan as wf
import json


app = Flask(__name__, static_url_path="", static_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/wifi')
def get_wifi_list():
    list = wf.scan_wifi()
    
    # dict to json
    result = json.dumps(list)

    return result


def run():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run()
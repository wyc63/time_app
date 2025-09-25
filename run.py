from flask import Flask
import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    now_est = datetime.datetime.now(ZoneInfo("America/New_York"))
    return {"time": now_est.isoformat()}


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

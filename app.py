from flask import Flask
from flask import render_template
from config import HOST, PORT
app = Flask(__name__,
            static_folder="static/",
            static_url_path="/static/")

MAIN_ROUTE = "index.html"
TAKE_ROUTE = "take_return.html"
DEVICE_ROUTE = "new_device.html"

@app.route('/')
def index():
    return render_template(MAIN_ROUTE)

@app.route('/newTakeRequest')
def new_record():
    return render_template(TAKE_ROUTE)

@app.route('/newDevice')
def new_device():
    return render_template(DEVICE_ROUTE)

if __name__ == "__main__":
    app.run(HOST, PORT)
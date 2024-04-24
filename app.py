from flask import Flask
from flask import render_template
from config import HOST, PORT
app = Flask(__name__)

MAIN_ROUTE = "index.html"
TAKE_ROUTE = "take_return.html"

@app.route('/')
def index():
    return render_template(MAIN_ROUTE)

@app.route('/newTakeRequest')
def new_record():
    return render_template(TAKE_ROUTE)

if __name__ == "__main__":
    app.run(HOST, PORT)
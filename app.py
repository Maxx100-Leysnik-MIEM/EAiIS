from flask import Flask, request
from flask import render_template, Response
from config import HOST, PORT
#from modules import modules_manipulator as modman
from modules import modman
import json

app = Flask(__name__)

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

@app.route('/get_nfc',  methods=['GET'])
def get_nfc():
    id, text = modman.readNFC()
    if id == -1:
        return Response(
            "Read failed",
            status=408
        )
    return text

@app.route('/get_rfid',  methods=['GET'])
def get_rfid():
    #TODO: claim required field
    card = modman.readRFID()
    if card == -1:
        return Response(
            "Read failed",
            status=408
        )
    return card.value

@app.route('/write_nfc',  methods=['POST'])
def write_nfc():
    json = request.get_json()
    result = modman.writeNFC(json["barcode"])
    if result == -1:
        return Response(
            "Read failed",
            status=408
        )
    return result    

@app.route('/get_barcode',  methods=['GET'])
def get_barcode():
    pass

@app.route('/make_new_request',  methods=['POST'])
def make_new():
    pass

@app.route('/write_new_device',  methods=['POST'])
def write_new_device():
    print(request.get_json())

if __name__ == "__main__":
    app.run(HOST, PORT)
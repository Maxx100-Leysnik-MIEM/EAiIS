import os.path

from flask import Flask, request
from flask import render_template, Response
from config import HOST, PORT, DEBUG
if DEBUG:
    from modules import modman
else:
    from modules import modules_manipulator as modman
from openapi_client import db

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
    _id, text = modman.readNFC()
    if _id == -1:
        return Response(
            "Read failed",
            status=408
        )
    return text


@app.route('/get_rfid',  methods=['GET'])
def get_rfid():
    # TODO: claim required field
    card = modman.readRFID()
    if card == -1:
        return Response(
            "Read failed",
            status=408
        )
    if DEBUG:
        return "1111"
    return card.value


@app.route('/write_nfc',  methods=['POST'])
def write_nfc():
    _json = request.get_json()
    result = modman.writeNFC(_json["barcode"])
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
    _json = request.get_json()
    response = db.create_request(
        json={
            "items": [{"hardware": int(_json["nfc_id"]),
                       "room": 1,
                       "count": int(_json["count"])}],
            "comment": _json["comment"],
            "planned_return_date": f"{_json["planned_date"]}T23:59:59.999Z"
        })
    if response.status_code != 201:
        return Response(response, status=response.status_code)
    _id = response.json()["id"]
    response = db.take_item(
        _id,
        json={
            "user_card": _json["rfid_student"],
            "issuer_card": _json["rfid_phd"]
        })
    if response.status_code != 200:
        db.cancel_request(_id)
        return Response(response, status=response.status_code)
    return "Successful"


@app.route('/write_new_device',  methods=['POST'])
def write_new_device():
    print(request.get_json())


if __name__ == "__main__":
    app.run(HOST, PORT)

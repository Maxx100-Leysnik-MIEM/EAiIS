import os.path

from flask import Flask, request
from flask import render_template, Response
from config import HOST, PORT, DEBUG
if DEBUG:
    from modules import modman
else:
    from modules import modules_manipulator as modman
from openapi_client import db
from dotenv import load_dotenv


load_dotenv()

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
    if _json["action"] == "take":
        response = db.create_request(
            json={
                "items": [{"hardware": int(_json["nfc_id"]),
                           "room": 1,
                           "count": int(_json["count"])}],
                "comment": _json["comment"],
                "planned_return_date": f"{_json["planned_date"]}T23:59:59.999999Z"
            })
        if response.status_code != 201:
            return Response(response, status=response.status_code)
        _id = response.json()["id"]
        if DEBUG:
            _json["rfid_student"] = os.getenv("USER_CARD_DEBUG")
            _json["rfid_phd"] = os.getenv("ISSUER_CARD_DEBUG")
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
    else:
        if DEBUG:
            _json["rfid_student"] = os.getenv("USER_CARD_DEBUG")
            _json["rfid_phd"] = os.getenv("ISSUER_CARD_DEBUG")
        user_id = -1
        for i in db.get_user().json()["result"]:
            if i["card_id"] == _json["rfid_student"]:
                user_id = i["id"]
                break
        if user_id == -1:
            return "User not found"
        request_id = -1
        for i in db.get_requests().json()["result"]:
            if user_id == i["user"] and i["items"][0]["hardware"] == int(_json["nfc_id"]):
                request_id = i["id"]
                break
        if request_id == -1:
            return "Request not found"
        response = db.return_items(request_id)
        if response.status_code != 200:
            return Response(response, status=response.status_code)
        response = db.complete_request(
            request_id,
            json={
                "user_card": _json["rfid_student"],
                "issuer_card": _json["rfid_phd"]
            }
        )
        if response.status_code != 200:
            return Response(response, status=response.status_code)
        return "Successful"


@app.route('/write_new_device',  methods=['POST'])
def write_new_device():
    print(request.get_json())


if __name__ == "__main__":
    app.run(HOST, PORT)

import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()
handler = logging.FileHandler("api.log", mode="a")
handler.setFormatter(logging.Formatter("%(levelname)s %(asctime)s %(message)s"))

logger = logging.getLogger("api.log")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


class DbSession:
    def __init__(self):  # default info from .env
        self.JWT_TOKEN = os.getenv("JWT_TOKEN")
        self.URL = os.getenv("URL")

    def resp(self, link: str, method: str = "GET", headers=None, params=None, data=None, json=None) \
            -> requests.models.Response:
        if headers is None:
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN}'}
        else:
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN}', **headers}
        resp = None
        match method:
            case "GET":
                resp = requests.get(f"{self.URL}/{link}", headers=headers, params=params, data=data, json=json)
            case "POST":
                resp = requests.post(f"{self.URL}/{link}", headers=headers, params=params, data=data, json=json)
            case "PATCH":
                resp = requests.patch(f"{self.URL}/{link}",
                                      headers=headers, params=params, data=data)
        logger.info(f"{self.URL}/{link}:{method} {resp.text} Json:{json}")
        return resp

    def whoami(self):  # get info about your token
        return self.resp("get_me")

    def get_requests(self, _id: int = None):
        if _id is None:
            return self.resp("request")
        return self.resp(f"request/{_id}")

    def create_request(self, json):
        return self.resp("request", method="POST", json=json)

    def update_request(self, _id: int):
        return self.resp(f"request/{_id}", method="PATCH")

    def take_item(self, _id: int, json):
        return self.resp(
            f"request/{_id}/take?user_card={json["user_card"]}&issuer_card={json["issuer_card"]}",
            method="POST",
            json=json
        )

    def return_items(self, _id: int):
        return self.resp(f"request/{_id}/return_waiting", method="PATCH")

    def complete_request(self, _id: int, json):
        return self.resp(
            f"request/{_id}/complete?user_card={json["user_card"]}&issuer_card={json["issuer_card"]}",
            method="POST",
            json=json
        )

    def cancel_request(self, _id: int):
        return self.resp(f"request/{_id}/cancel", method="POST")

    def approve_request(self, _id: int):
        return self.resp(f"request/approve", method="PATCH", data=f"[{_id}]")

    def get_user(self, _id: int = None):  # get users list or user by id
        if _id is None:
            return self.resp("users")
        return self.resp(f"users/{_id}")

    def get_user_rooms(self, _id: int):
        return self.resp(f"users/{_id}/rooms")

    def get_hardware(self, _id: int = None):  # get hardware by id or all list
        if _id is None:
            return self.resp("hardware")
        return self.resp(f"hardware/{_id}")

    def get_hardware_remains(self):
        return self.resp("hardware/remains")

    def get_hardware_types(self):
        return self.resp("hardware/types")

    """
    GET:    hardware/types/_id (Get Type)
    PATCH:  hardware/types/_id (Update Type)
    DELETE: hardware/types/_id (Delete Type)
    """

    def get_items(self, _id: int = None):  # get item by id or all list
        if _id is None:
            return self.resp("item")
        return self.resp(f"item/{_id}")

    def get_terminals(self, _id: int = None):  # get terminal by id or all list
        if _id is None:
            return self.resp("terminal")
        return self.resp(f"terminal/{_id}")

    def get_sections(self, _id: int = None):  # get section by id or all list
        if _id is None:
            return self.resp("section")
        return self.resp(f"section/{_id}")

    def get_rooms(self, _id: int = None):  # get room by id or all list
        if _id is None:
            return self.resp("room")
        return self.resp(f"room/{_id}")

    def get_places(self, _id: int = None):  # get place by id or all list
        if _id is None:
            return self.resp("place")
        return self.resp(f"place/{_id}")

    def get_labs(self, _id: int = None):  # get lab by id or all list
        if _id is None:
            return self.resp("lab")
        return self.resp(f"lab/{_id}")

    def get_buildings(self, _id: int = None):  # get building by id or all list
        if _id is None:
            return self.resp("building")
        return self.resp(f"building/{_id}")

    def auth_callback(self):
        return self.resp("auth/callback")

    def auth_token(self):
        return self.resp("auth/token")


db = DbSession()
if __name__ == "__main__":
    while True:
        try:
            print(eval(input()))
        except Exception as e:
            print(e)

"""
db.resp(method="POST", json="name":"Testing","type":99,"image_link":"link","specifications":{"name":"TEST","type":"99"}})

id: 7
count: 2

db.get_hardware_remains().text
db.get_requests().text
db.create_request({"items": [{"hardware": 7, "room": 1, "count": 1}], "comment": "test", "planned_return_date": "2024-06-09T23:59:59.999Z"})
db.cancel_request(62)
db.take_item(63, json={"user_card": "PQR5ETWPVAM1BP7TC6LA"})
db.resp("request/63/take?user_card=PQR5ETWPVAM1BP7TC6LA", method="POST")
db.resp("request/63/take?user_card=26", method="POST", json={"user_card": "26"}).text

db.resp("users/26", method="PATCH", json={"card_id": "1111"}).text

json={"user_card": "0093B6B2", "issuer_card": "005F0FE9"}
"""

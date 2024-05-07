import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DbSession:
    def __init__(self):  # default info from .env
        self.JWT_TOKEN = os.getenv("JWT_TOKEN")
        self.URL = os.getenv("URL")

    def resp(self, link: str, method: str = "GET", headers=None, params=None, data=None) -> requests.models.Response:
        if headers is None:
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN}'}
        else:
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN}', **headers}
        resp = None
        match method:
            case "GET":
                resp = requests.get(f"{self.URL}/{link}",
                                    headers=headers, params=params, data=data)
            case "POST":
                resp = requests.post(f"{self.URL}/{link}",
                                     headers=headers, params=params, data=data)
            case "PATCH":
                resp = requests.patch(f"{self.URL}/{link}",
                                      headers=headers, params=params, data=data)
        return resp

    def post(self, link: str, headers: dict = None, params: dict = None, data: dict = None) -> requests.models.Response:
        if headers is None:
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN}'}
        else:
            headers = {'Authorization': f'Bearer {self.JWT_TOKEN}', **headers}
        resp = requests.post(f"{self.URL}/{link}",
                             headers=headers, params=params, data=data)
        return resp

    def whoami(self):  # get info about your token
        return self.resp("get_me")

    def get_user(self, _id: int = None):  # get users list or user by id
        if _id is None:
            return self.resp("users")
        return self.resp(f"users/{str(_id)}")

    def add_user(self):  # TODO
        return

    def patch_user(self, _id: int):  # TODO
        return

    def delete_user(self, _id: int):  # TODO
        return

    def get_hardware(self, _id: int = None):  # get hardware by id or all list
        if _id is None:
            return self.resp("hardware")
        return self.resp(f"hardware/{str(_id)}")

    def create_hardware(self):  # TODO
        return

    def get_hardware_remains(self):
        return self.resp("hardware/remains")

    def get_hardware_types(self):
        return self.resp("hardware/types")

    def add_hardware_type(self):  # TODO
        return

    def patch_hardware(self, _id: int):  # TODO
        return

    def delete_hardware(self, _id: int):  # TODO
        return

    """
    GET:    hardware/types/_id (Get Type)
    PATCH:  hardware/types/_id (Update Type)
    DELETE: hardware/types/_id (Delete Type)
    """

    def get_items(self, _id: int = None):  # get item by id or all list
        if _id is None:
            return self.resp("item")
        return self.resp(f"item/{str(_id)}")

    def create_item(self):  # TODO
        return

    def update_item(self, _id: int):  # TODO
        return

    def delete_item(self, _id: int):  # TODO
        return

    def get_terminals(self, _id: int = None):  # get terminal by id or all list
        if _id is None:
            return self.resp("terminal")
        return self.resp(f"terminal/{str(_id)}")

    def create_terminal(self):  # TODO
        return

    def update_terminal(self, _id: int):  # TODO
        return

    def delete_terminal(self, _id: int):  # TODO
        return

    def get_sections(self, _id: int = None):  # get section by id or all list
        if _id is None:
            return self.resp("section")
        return self.resp(f"section/{str(_id)}")

    def create_section(self):  # TODO
        return

    def update_section(self, _id: int):  # TODO
        return

    def delete_section(self, _id: int):  # TODO
        return

    def get_rooms(self, _id: int = None):  # get room by id or all list
        if _id is None:
            return self.resp("room")
        return self.resp(f"room/{str(_id)}")

    def create_room(self):  # TODO
        return

    def update_room(self, _id: int):  # TODO
        return

    def delete_room(self, _id: int):  # TODO
        return

    def get_places(self, _id: int = None):  # get place by id or all list
        if _id is None:
            return self.resp("place")
        return self.resp(f"place/{str(_id)}")

    def create_place(self):  # TODO
        return

    def update_place(self, _id: int):  # TODO
        return

    def delete_place(self, _id: int):  # TODO
        return

    def get_labs(self, _id: int = None):  # get lab by id or all list
        if _id is None:
            return self.resp("lab")
        return self.resp(f"lab/{str(_id)}")

    def create_lab(self):  # TODO
        return

    def update_lab(self, _id: int):  # TODO
        return

    def delete_lab(self, _id: int):  # TODO
        return

    def get_buildings(self, _id: int = None):  # get building by id or all list
        if _id is None:
            return self.resp("building")
        return self.resp(f"building/{str(_id)}")

    def create_building(self):  # TODO
        return

    def update_building(self, _id: int):  # TODO
        return

    def delete_building(self, _id: int):  # TODO
        return

    def auth_callback(self):
        return self.resp("auth/callback")

    def auth_token(self):
        return self.resp("auth/token")


db = DbSession()
print(db.get_user().text)  # as example

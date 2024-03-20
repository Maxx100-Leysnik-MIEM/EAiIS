import socket
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1337  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def data_to_bytes(lst):
    ans = b""
    for i in lst:
        if type(i) is int:
            ans += str.encode(f"{str(i):>16}")
        elif type(i) is str:
            ans += str.encode(f"{i:>64}")
        else:
            print(f"Unknown type: {type(i)}")
    return ans


def request():
    time.sleep(2)
    # get data
    data = [12, "123", "get"]  # id (int), equipment (str), get/give
    return data


while True:
    s.sendall(data_to_bytes(request()))
    data = s.recv(2**16).decode()
    print(data)

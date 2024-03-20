import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1337))

if __name__ == "__main__":
    # db_session.global_init("data/log.db")

    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(16 + 64 + 64).decode()
        data = [data[:16].lstrip(" "),
                data[16:16 + 64].lstrip(" "),
                data[16 + 64:16 + 64 + 64].lstrip(" ")]
        print(data)
        if "ok":
            conn.sendall(b"ok")

            event = Event()
            event.time, event.date = str(datetime.now()).split(".")[0].split()
            event.id = int(data[0])
            event.equipment = data[1]
            event.type = data[2]

            db_sess = db_session.create_session()
            db_sess.add(event)
            db_sess.commit()
        else:
            conn.sendall(b"Access denied")
    # conn.close()

import socket
from threading import Thread
from utils import get_filename
from datetime import datetime

code_memory = {}

def handle_client(conn, addr, line):
    filename = get_filename(line)
    print(f"[{line}] Прием от {addr}, файл: {filename}")
    with conn, open(filename, "a", encoding="utf-8") as f:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                code = data.decode().strip()
                today = datetime.now().strftime("%Y-%m-%d")
                if code not in code_memory.get(today, set()):
                    f.write(code + "\n")
                    f.flush()
                    code_memory.setdefault(today, set()).add(code)
                else:
                    print(f"[{line}] Повтор: {code}")
            except Exception as e:
                print(f"[{line}] Ошибка: {e}")
                break

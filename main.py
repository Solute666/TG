import socket
import threading
from config import CAMERA_CONFIG
from camera_handler import handle_client

def start_server(ip, port, line):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()
        print(f"[{line}] Слушаю {ip}:{port} ...")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, line))
            thread.start()

if __name__ == "__main__":
    for cam_name, cam_info in CAMERA_CONFIG.items():
        thread = threading.Thread(
            target=start_server,
            args=(cam_info["ip"], cam_info["port"], cam_info["line"]),
            daemon=True
        )
        thread.start()

    print("Все камеры запущены. Нажмите Ctrl+C для выхода.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Завершение работы...")

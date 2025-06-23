import socket
import threading
import logging
from config import CAMERA_CONFIG
from camera_handler import handle_client

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


def start_server(ip, port, line):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((ip, port))
            s.listen()
            logging.info("[%s] Listening on %s:%s", line, ip, port)
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr, line))
                thread.start()
    except OSError as e:
        logging.error("Failed to start server for %s: %s", line, e)


if __name__ == "__main__":
    for cam_name, cam_info in CAMERA_CONFIG.items():
        thread = threading.Thread(
            target=start_server,
            args=(cam_info["ip"], cam_info["port"], cam_info["line"]),
            daemon=True,
        )
        thread.start()

    logging.info("All cameras started. Press Ctrl+C to exit.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        logging.info("Shutting down...")

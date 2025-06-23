import logging
from datetime import datetime
from utils import get_filename

code_memory = {}


def cleanup_code_memory():
    today = datetime.now().strftime("%Y-%m-%d")
    for date in list(code_memory.keys()):
        if date != today:
            del code_memory[date]


def handle_client(conn, addr, line):
    filename = get_filename(line)
    logging.info("[%s] Connection from %s, writing to %s", line, addr, filename)
    cleanup_code_memory()
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
                    logging.info("[%s] Duplicate: %s", line, code)
            except Exception as e:
                logging.error("[%s] Error: %s", line, e)
                break

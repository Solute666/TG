import os
from datetime import datetime

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_filename(line):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%H-%M-%S")
    folder = os.path.join("logs", line, date)
    ensure_dir(folder)
    return os.path.join(folder, f"{line}_{timestamp}.txt")

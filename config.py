import json
import os

DEFAULT_CONFIG = {
    "camera1": {
        "ip": "192.168.1.101",
        "port": 9001,
        "line": "line1",
        "controller": "ctrl1"
    },
    "camera2": {
        "ip": "192.168.1.102",
        "port": 9002,
        "line": "line2",
        "controller": "ctrl2"
    },
}


def load_config():
    path = os.getenv("CAMERA_CONFIG_FILE")
    if path and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_CONFIG


CAMERA_CONFIG = load_config()

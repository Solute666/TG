import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json
import os
from importlib import reload
import config


def test_load_config_from_file(tmp_path, monkeypatch):
    config_file = tmp_path / "config.json"
    data = {"cam": {"ip": "1", "port": 1, "line": "x", "controller": "c"}}
    config_file.write_text(json.dumps(data))
    monkeypatch.setenv("CAMERA_CONFIG_FILE", str(config_file))
    reload(config)
    assert config.CAMERA_CONFIG == data

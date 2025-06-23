import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import os
from utils import get_filename
from datetime import datetime

def test_get_filename_creates_path(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    line = "lineX"
    path = get_filename(line)
    assert line in path
    date = datetime.now().strftime("%Y-%m-%d")
    assert os.path.join("logs", line, date) in os.path.dirname(path)
    assert os.path.exists(os.path.dirname(path))

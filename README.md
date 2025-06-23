# TG Camera Logging Server

This project provides a simple multithreaded TCP server to collect codes from cameras and store them in daily log files.

## Usage
1. Adjust camera configuration in `config.py` or provide a JSON file with the same structure (see example below).
2. Install requirements with `pip install -r requirements.txt`.
3. Run `python main.py` to start listening for incoming connections from cameras.
4. Log files appear in the `logs/LINE/DATE/` directories.

## Configuration
You can store configuration in a JSON file:

```json
{
  "camera1": {"ip": "192.168.1.101", "port": 9001, "line": "line1", "controller": "ctrl1"},
  "camera2": {"ip": "192.168.1.102", "port": 9002, "line": "line2", "controller": "ctrl2"}
}
```

Pass the file path in the environment variable `CAMERA_CONFIG_FILE` to override the default configuration.

## Development
- Tests are run with `pytest`.
- Temporary files and logs are ignored via `.gitignore`.
- Each camera connection is handled in a separate thread and writes to its own log file, so writing is thread-safe.


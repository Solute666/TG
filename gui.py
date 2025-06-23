from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
import sys
import threading
from config import CAMERA_CONFIG
from main import start_server

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Server GUI")
        self.start_button = QPushButton("Start Servers")
        self.start_button.clicked.connect(self.start_servers)
        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Camera Server Control"))
        layout.addWidget(self.start_button)
        layout.addWidget(self.log)
        self.setLayout(layout)

        self.threads = []
        self.started = False

    def start_servers(self):
        if self.started:
            return
        for cam_name, cam_info in CAMERA_CONFIG.items():
            thread = threading.Thread(
                target=start_server,
                args=(cam_info["ip"], cam_info["port"], cam_info["line"]),
                daemon=True,
            )
            thread.start()
            self.threads.append(thread)
            self.log.append(f"Started {cam_name} on {cam_info['ip']}:{cam_info['port']}")
        self.start_button.setEnabled(False)
        self.started = True


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

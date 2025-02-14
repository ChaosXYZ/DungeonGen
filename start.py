import sys
from PyQt6.QtWidgets import QApplication, QWidget

class BasicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DungeonGen")
        self.setGeometry(100, 100, 800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicWindow()
    window.show()
    sys.exit(app.exec())
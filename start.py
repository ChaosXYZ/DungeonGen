import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from DungeonSpawn import DungeonTab
from Home import HomeTab
from KeyGen import KeyTab
from Insert import InsertTab
from Lookup import LookupTab

class BasicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DungeonGen")
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()
        self.tabs.addTab(HomeTab(), "Home")
        self.tabs.addTab(KeyTab(), "Key Generator")
        self.tabs.addTab(DungeonTab(), "Dungeon Generator")
        self.tabs.addTab(InsertTab(), "Enter Task")
        self.tabs.addTab(LookupTab(), "View Task")
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicWindow()
    window.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class DungeonTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        layout = QVBoxLayout()
        text = QLabel("Dungeon Spawner")
        layout.addWidget(text)
        self.setLayout(layout)
    
    def parseKey(self, key):
        pass

    
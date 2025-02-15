from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class KeyTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        layout = QVBoxLayout()
        text = QLabel("KeyGenerator")
        layout.addWidget(text)
        self.setLayout(layout)
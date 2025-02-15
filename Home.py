from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class HomeTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        layout = QVBoxLayout()
        text = QLabel("Home")
        layout.addWidget(text)
        self.setLayout(layout)
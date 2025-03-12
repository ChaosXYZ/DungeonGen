from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class LookupTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        layout = QVBoxLayout()
        text = QLabel("Lookup Page")
        layout.addWidget(text)
        self.setLayout(layout)
    

    
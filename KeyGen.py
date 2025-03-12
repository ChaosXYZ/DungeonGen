from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
import random 

class KeyTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        layout = QVBoxLayout()
        text = QLabel("KeyGenerator")
        layout.addWidget(text)
        self.setLayout(layout)

    def keyGen(self, difficulty, includeMaths, includeCode, includePuzzle, includePhysical):
        numberOfMissions = max(1,random.randint(difficulty-3,difficulty))
        includeMaths = 'M' if True else 'N'
        includCode = 'C' if True else 'D'
        includePuzzle = 'P' if True else 'K'
        includePhysical = 'S' if True else 'R'

    def pad(self, mission):
        if len(str(mission)) != 4:
            return '0'*(4-len(str(mission)))+str(mission)
        return str(mission)
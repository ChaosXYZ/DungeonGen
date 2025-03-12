from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
import random
from TaskManager import TaskManager

class KeyTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.taskDB = TaskManager()
    
    def UI(self):
        layout = QVBoxLayout()
        text = QLabel("KeyGenerator")
        layout.addWidget(text)
        self.setLayout(layout)

    def keyGen(self, difficulty, includeMaths, includeCode, includePuzzle, includePhysical):
        numberOfMissions = max(1,random.randint(difficulty-3,difficulty))
        taskTypes = []
        if includeMaths:
            taskTypes.append("Maths")
        if includeCode:
            taskTypes.append("Code")
        if includePuzzle:
            taskTypes.append("Puzzle")
        if includePhysical:
            taskTypes.append("Physical")

    def pad(self, mission):
        if len(str(mission)) != 4:
            return '0'*(4-len(str(mission)))+str(mission)
        return str(mission)
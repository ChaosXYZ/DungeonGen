from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton
from TaskManager import TaskManager
class InsertTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.taskDB = TaskManager()
    
    def UI(self):
        self.layout = QVBoxLayout()  

        self.taskNameLayout = QHBoxLayout()
        self.taskNameLabel = QLabel("Task Name:")
        self.taskNameEntry = QLineEdit(self)
        self.taskNameLayout.addWidget(self.taskNameLabel)
        self.taskNameLayout.addWidget(self.taskNameEntry)
        self.layout.addLayout(self.taskNameLayout)

        self.taskDescLayout = QHBoxLayout()  
        self.taskDescLabel = QLabel("Task Description:")
        self.taskDescEntry = QLineEdit(self)
        self.taskDescLayout.addWidget(self.taskDescLabel)
        self.taskDescLayout.addWidget(self.taskDescEntry)
        self.layout.addLayout(self.taskDescLayout)

        self.taskTypeLayout = QHBoxLayout() 
        self.taskTypeLabel = QLabel("Task Type:")
        self.taskTypeComboBox = QComboBox(self)
        self.taskTypeComboBox.addItems(["Maths", "Code", "Puzzle", "Physical"]) 
        self.taskTypeLayout.addWidget(self.taskTypeLabel)
        self.taskTypeLayout.addWidget(self.taskTypeComboBox)
        self.layout.addLayout(self.taskTypeLayout)

        self.sourceLayout = QHBoxLayout() 
        self.sourceLabel = QLabel("Source:")
        self.sourceEntry = QLineEdit(self)
        self.sourceLayout.addWidget(self.sourceLabel)
        self.sourceLayout.addWidget(self.sourceEntry)
        self.layout.addLayout(self.sourceLayout)

        self.difficultyLayout = QHBoxLayout() 
        self.difficultyLabel = QLabel("Difficulty:")
        self.difficultyComboBox = QComboBox(self)
        self.difficultyComboBox.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]) 
        self.difficultyLayout.addWidget(self.difficultyLabel)
        self.difficultyLayout.addWidget(self.difficultyComboBox)
        self.layout.addLayout(self.difficultyLayout)

        self.buttonLayout = QHBoxLayout()
        self.printButton = QPushButton("Submit", self)
        self.printButton.clicked.connect(self.insert)  
        self.buttonLayout.addStretch()  
        self.buttonLayout.addWidget(self.printButton)
        self.buttonLayout.addStretch()  
        self.layout.addLayout(self.buttonLayout)

        self.setLayout(self.layout)
    
    def insert(self):
        name = self.taskNameEntry.text()
        desc = self.taskDescEntry.text()
        type = self.taskTypeComboBox.currentText()
        source = self.sourceEntry.text()
        difficulty = self.difficultyComboBox.currentText()

        if name == "" or desc == "" or source == "":
            print("ERROR")
            return

        result = self.taskDB.insert_task(name, desc, type, source, difficulty)
        if result == "Success":
            print("Works, do popup here")

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont

class HomeTab(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        layout = QVBoxLayout()

        home_title = QLabel("DunGEN")
        home_title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 10px;") 
        layout.addWidget(home_title)

        combined_text = (
            "Welcome to DunGen,  this utility app is designed for a personal project with the goal of creating unique and recreatable dungeons.\n"
            "Dungeons: These are sets of challenges that can be physical, mental, or a mix of both. They are designed to be completed as quickly as possible without sacrificing accuracy.\n"
            "Features: The app allows you to create a 'Key' for each dungeon, which can be used to generate the same dungeon each time. The same key will always recreate the same dungeon."
        )

        combined_label = QLabel(combined_text)
        combined_label.setStyleSheet("font-size: 14px; margin-bottom: 20px; line-height: 1.6;") 
        layout.addWidget(combined_label)

        release_title = QLabel("Release Notes - Version 0.1")
        release_title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")  
        layout.addWidget(release_title)

        release_notes = """
        - Initial tabs and such created
        - No content yet
        """
        
        release_notes_label = QLabel(release_notes)
        release_notes_label.setStyleSheet("font-size: 14px; line-height: 1.6;")
        layout.addWidget(release_notes_label)

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        self.setLayout(layout)
        

        self.setFont(QFont("Times New Roman", 12))

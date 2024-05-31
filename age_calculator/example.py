import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,\
      QComboBox, QGridLayout, QPushButton
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid=QGridLayout()
        #create widgets
        name_label=QLabel("Name: ")
        self.name_line_edit=QLineEdit()

        dob_label=QLabel("Date of Birth MM/DD/YYYY : ")
        self.dob_line_edit=QLineEdit()
        button=QPushButton("Calculate Age")
        button.clicked.connect(self.calc_age)
        self.output_label=QLabel("")
         
        #add widget to the grid 
        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(dob_label,1,0)
        grid.addWidget(self.dob_line_edit,1,1)
        grid.addWidget(button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)
        self.setLayout(grid)
    
    def calc_age(self):
        year=datetime.now().year
        date_of_birth=self.dob_line_edit.text()
        year_birth=datetime.strptime(date_of_birth,"%m/%d/%Y").date().year
        age=year-year_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old")


app=QApplication(sys.argv)
calc=AgeCalculator()
calc.show()
sys.exit(app.exec())




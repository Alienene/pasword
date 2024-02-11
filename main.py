from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from random import *

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)

    
    def click(self):
        s = ' '
        if self.ui.checkBox.isChecked():
            s = '0123456789'
        if self.ui.checkBox_2.isChecked():
            s += 'qwertyuiopasdfghjklzxcvbnm'

        password = ' '
        for _ in range(8):
            password += choice(s)
        
        self.ui.label.setText(password)
    

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
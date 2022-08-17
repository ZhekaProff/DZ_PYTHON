from down import download_video
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def editq(): # функция считывания поля
        text = form.lineEdit.displayText()
        name = QFileDialog.getExistingDirectory()
        download_video(text, name)

form.pb1.clicked.connect(editq)

app.exec_()
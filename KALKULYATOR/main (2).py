from PySide6.QtWidgets import  QApplication
from a_kalkuulyator import Calculator

app = QApplication()
window = Calculator()

window.show()
app.exec()

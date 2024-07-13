from PySide6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout

app = QApplication()
window = QWidget()

ustun = QVBoxLayout()
window.setLayout(ustun)

window.show()
app.exec()
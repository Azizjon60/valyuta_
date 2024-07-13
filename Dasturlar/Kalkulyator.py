from PySide6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout

# Ilovani yaratish
app = QApplication([])
window = QWidget()
window.setWindowTitle("Kalkulyator")
# ko'rinishi
window.setMinimumSize(300, 300)
window.setMaximumSize(500, 500)
# widgetlar qo'shish
ustun = QVBoxLayout()
window.setLayout(ustun)
# yozadigan widget 1
line1 = QLineEdit()
ustun.addWidget(line1)
# y.w. 2
line2 = QLineEdit()
ustun.addWidget(line2)
#
tugma = QPushButton(text='x')
ustun.addWidget(tugma)
#
window.show()
app.exec()
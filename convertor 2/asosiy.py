from PySide6.QtWidgets import QWidget,QMessageBox
from convertor_ui import Ui_Form

class Widget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chiqish)
        self.valyuta = 12665
        self.lineedit.textChanged.connect(self.chiqarish)

    def chiqarish(self):
        try:
            qiymat = int(self.lineedit.text())
            qiymat = round(qiymat / self.valyuta, 2)
            self.lineedit2.setText(str(qiymat))
        except ValueError:
            pass
    def chiqish(self):
        chiqish = QMessageBox.question(None, "Habar", 'Dasturdan chiqishni xoxlaysizmi', QMessageBox.Yes | QMessageBox.No)
        if chiqish == QMessageBox.Yes:
            self.close()

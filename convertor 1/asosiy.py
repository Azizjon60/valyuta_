from PySide6.QtWidgets import QWidget, QMessageBox
from valyuta_ui import Ui_Form

class Widget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chiqish)
        self.valyuta = 12665
        self.block_signals = False  # Initialize the custom block_signals attribute
        self.lineEdit_2.textChanged.connect(self.chiqarish)
        self.lineEdit_3.textChanged.connect(self.chiqarish_2)

    def chiqish(self):
        chiqish = QMessageBox.question(None, "Habar", "Dasturdan chiqishni istaysizmi", QMessageBox.Yes | QMessageBox.No)
        if chiqish == QMessageBox.Yes:
            self.close()

    def chiqarish(self):
        if self.block_signals:
            return
        self.block_signals = True
        try:
            qiymat = float(self.lineEdit_2.text())  # Use float instead of int
            qiymat = round(qiymat * self.valyuta, 2)
            self.lineEdit_3.setText(str(qiymat))
        except ValueError:
            pass
        self.block_signals = False

    def chiqarish_2(self):
        if self.block_signals:
            return
        self.block_signals = True
        try:
            qiymat = float(self.lineEdit_3.text())  # Use float instead of int
            qiymat = round(qiymat / self.valyuta, 2)
            self.lineEdit_2.setText(str(qiymat))
        except ValueError:
            pass
        self.block_signals = False

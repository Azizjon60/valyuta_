from PySide6.QtWidgets import QApplication, QWidget
from Kalendar_1.kalendar_ui import Ui_Form
import calendar


class Widget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
        self.sana.userDateChanged.connect(self.kunni_aniqla)

    def kunni_aniqla(self):
        dt = self.sana.date()
        kun = dt.day()
        oy = dt.month()
        yil = dt.year()

        kun_raqami = calendar.weekday(yil, oy, kun)
        hafta_kuni = self.kunlar[kun_raqami]

        result_text = f"Yil: {yil}, Oy: {oy}, Kun: {kun}, Haftaning kuni: {hafta_kuni}"
        self.label_2.setText(result_text)


if __name__ == "__main__":
    app = QApplication([])

    window = Widget()
    window.show()

    app.exec()

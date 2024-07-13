# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertorQJTLTv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(378, 198)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 50))
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: grey;\n"
"border-radius: 5px;\n"
"color: white;")

        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(532, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: grey;\n"
"border-radius: 5px;\n"
"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineedit2 = QLineEdit(self.widget)
        self.lineedit2.setObjectName(u"lineedit2")
        self.lineedit2.setMinimumSize(QSize(0, 50))
        self.lineedit2.setStyleSheet(u"border-radius: 5px;\n"
"background-color: white;")

        self.gridLayout.addWidget(self.lineedit2, 1, 1, 1, 1)

        self.lineedit = QLineEdit(self.widget)
        self.lineedit.setObjectName(u"lineedit")
        self.lineedit.setMinimumSize(QSize(0, 50))
        self.lineedit.setStyleSheet(u"border-radius: 5px;\n"
"background-color: white;")

        self.gridLayout.addWidget(self.lineedit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Chiqish", None))
        self.label.setText(QCoreApplication.translate("Form", u"UZS", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"UZD", None))
    # retranslateUi


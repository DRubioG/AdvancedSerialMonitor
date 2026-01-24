# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 658)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_data = QTextEdit(self.centralwidget)
        self.text_data.setObjectName(u"text_data")
        self.text_data.setGeometry(QRect(10, 70, 451, 191))
        self.text_data.setReadOnly(True)
        self.table_serial = QTableView(self.centralwidget)
        self.table_serial.setObjectName(u"table_serial")
        self.table_serial.setGeometry(QRect(480, 70, 481, 401))
        self.text_hex = QTextEdit(self.centralwidget)
        self.text_hex.setObjectName(u"text_hex")
        self.text_hex.setGeometry(QRect(10, 280, 451, 191))
        self.text_hex.setReadOnly(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 260, 121, 17))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 121, 17))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 50, 121, 17))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 530, 351, 25))
        self.pushButton_send = QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setGeometry(QRect(410, 530, 80, 25))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 570, 41, 17))
        self.comboBox_parity = QComboBox(self.centralwidget)
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.setObjectName(u"comboBox_parity")
        self.comboBox_parity.setGeometry(QRect(90, 570, 79, 25))
        self.comboBox_flow_control = QComboBox(self.centralwidget)
        self.comboBox_flow_control.setObjectName(u"comboBox_flow_control")
        self.comboBox_flow_control.setGeometry(QRect(320, 570, 79, 25))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 570, 91, 17))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(480, 580, 61, 17))
        self.comboBox_stop_bit = QComboBox(self.centralwidget)
        self.comboBox_stop_bit.addItem("")
        self.comboBox_stop_bit.addItem("")
        self.comboBox_stop_bit.addItem("")
        self.comboBox_stop_bit.setObjectName(u"comboBox_stop_bit")
        self.comboBox_stop_bit.setGeometry(QRect(540, 580, 121, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 490, 71, 17))
        self.comboBox_uart = QComboBox(self.centralwidget)
        self.comboBox_uart.setObjectName(u"comboBox_uart")
        self.comboBox_uart.setGeometry(QRect(110, 490, 141, 25))
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(540, 530, 80, 25))
        self.comboBox_bauds = QComboBox(self.centralwidget)
        self.comboBox_bauds.setObjectName(u"comboBox_bauds")
        self.comboBox_bauds.setGeometry(QRect(370, 490, 79, 25))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 490, 51, 17))
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setGeometry(QRect(490, 490, 80, 25))
        self.checkBox_add_time = QCheckBox(self.centralwidget)
        self.checkBox_add_time.setObjectName(u"checkBox_add_time")
        self.checkBox_add_time.setGeometry(QRect(160, 50, 88, 23))
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(610, 490, 80, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 986, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Advanced Serial Monitor", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Serial Data", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Serial Timing", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Parity:", None))
        self.comboBox_parity.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_parity.setItemText(1, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.comboBox_parity.setItemText(2, QCoreApplication.translate("MainWindow", u"Even", None))
        self.comboBox_parity.setItemText(3, QCoreApplication.translate("MainWindow", u"Mark", None))
        self.comboBox_parity.setItemText(4, QCoreApplication.translate("MainWindow", u"Space", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Flow Control:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stop Bit:", None))
        self.comboBox_stop_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"One", None))
        self.comboBox_stop_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"One Point Five", None))
        self.comboBox_stop_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"Two", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Serial Port", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bauds:", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.checkBox_add_time.setText(QCoreApplication.translate("MainWindow", u"Add time", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi


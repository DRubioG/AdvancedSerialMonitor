from PySide6.QtWidgets  import QMainWindow
from PySide6.QtGui import QTextCursor
from UI.user_interface import *
from serial.tools.list_ports import comports
import serial
from main_thread import UArtReceiver

class user_interface_gui(QMainWindow):
    BAUDS = ["50", "75", "110", "134", "150", "200", "300", "600", \
                      "1200", "1800", "2400", "4800", "9600", "19200", "38400",\
                      "57600", "115200", "230400", "460800", "500000",  \
                      "576000", "921600", "1000000", "1152000", "1500000",\
                      "2000000", "2500000", "3000000", "3500000", "4000000"]
    
    STOPBIT = ["One", "Two"]

    PARITY = ["None", "Odd", "Even"]

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()
        self.init()
        self.show()

    def init(self):
        self.data=[]
        self.ui.comboBox_bauds.addItems(self.BAUDS)
        self.ui.comboBox_stop_bit.addItems(self.STOPBIT)
        self.ui.comboBox_parity.addItems(self.PARITY)
        self.port_setup()
        

    def connections(self):
        self.ui.pushButton_open.clicked.connect(self.open_port)
        self.ui.pushButton_close.clicked.connect(self.close_port)
        self.ui.pushButton_send.clicked.connect(self.send_message)
        self.ui.lineEdit.textChanged.connect(self.change_data_send)
        self.ui.comboBox_uart.showPopup()
        self.ui.comboBox_uart.currentIndexChanged.connect(self.change_port)
        self.ui.pushButton_clear.clicked.connect(self.clear_data)



        
    def port_setup(self):
        self.ports = []
        for port in comports():
            if port[0].find("/dev/ttyS") == -1:
                self.ui.comboBox_uart.addItem(port[0])
                self.ports.append(port[0])

    def open_port(self):
        port = "/dev/ttyUSB0" # self.ports[self.index]


        self.receiver = UArtReceiver(port, 9600)
        self.receiver.data_received.connect(self.update_data)
        self.receiver.start()
        print("Open port")

    def close_port(self):
        self.receiver.stop()

    def send_message(self):
        text = self.ui.lineEdit.text()

        self.ui.lineEdit.clear()

    def change_data_send(self):
        self.ui.pushButton_send.setStyleSheet("background-color: #31F527")

    def change_port(self):
        index = self.ui.comboBox_uart.currentIndex()
        

    def update_data(self, msg):
        self.data.append(msg)
        # self.ui.text_data.clear()
        self.ui.text_data.insertPlainText(msg)
        hex_text = msg.encode('utf-8').hex()
        self.ui.text_hex.insertPlainText(hex_text + "\n")
        

        cursor = self.ui.text_data.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.ui.text_data.setTextCursor(cursor)


        cursor_hex = self.ui.text_hex.textCursor()
        cursor_hex.movePosition(QTextCursor.End)
        self.ui.text_hex.setTextCursor(cursor_hex)

    def clear_data(self):
        self.ui.text_data.clear()
        self.ui.text_hex.clear()
from PySide6.QtWidgets  import QMainWindow
from UI.user_interface import *
from serial.tools.list_ports import comports


class user_interface_gui(QMainWindow):
    def __init__(self):
        self.bauds = ["50", "75", "110", "134", "150", "200", "300", "600", \
                      "1200", "1800", "2400", "4800", "9600", "19200", "38400",\
                      "57600", "115200", "230400", "460800", "500000",  \
                      "576000", "921600", "1000000", "1152000", "1500000",\
                      "2000000", "2500000", "3000000", "3500000", "4000000"]

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Advanced Serial Monitor")
        self.connections()
        self.port_setup()
        self.show()

    def connections(self):
        self.ui.comboBox_bauds.addItems(self.bauds)

    def port_setup(self):
        for port in comports():
            if port[0].find("/dev/ttyS") == -1:
                self.ui.comboBox_uart.addItem(port[0])
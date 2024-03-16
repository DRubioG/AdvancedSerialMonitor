from PySide6.QtWidgets  import QMainWindow
from UI.user_interface import *
from serial.tools.list_ports import comports


class user_interface_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Advanced Serial Monitor")
        self.port_setup()
        self.show()

    def port_setup(self):
        for port in comports():
            self.ui.comboBox.addItem(port[0])
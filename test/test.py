import sys
import serial
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from main_thread import UArtReceiver

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UART con Pyside6")
        self.resize(400, 300)

        self.text_area = QTextEdit()
        self.send_button = QPushButton("Enviar mensaje")
        self.send_button1 = QPushButton("Enviar mensaje")
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_area)
        layout.addWidget(self.send_button)
        layout.addWidget(self.send_button1)


        port = "/dev/ttyUSB0"
        baudrate = 9600

        self.ser = serial.Serial(port, baudrate, timeout=1)

        self.receiver = UArtReceiver(port, baudrate)
        self.receiver.data_received.connect(self.update_text)
        self.receiver.start()




        self.send_button.clicked.connect(self.send_message)






    def update_text(self, msg):
        self.text_area.append(f"RX: {msg}")
        if msg.find("Adios") != -1:
            self.send_button1.setStyleSheet("background-color: green")

    def send_message(self):
        self.ser.write(b"hola\n")
        self.text_area.append("TX: hola")

    def closeEvent(self, event):
        self.receiver.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
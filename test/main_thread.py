from PySide6.QtCore import QThread, Signal
import serial
import time

class UArtReceiver(QThread):
    data_received = Signal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.running = True

    def run(self):
        while self.running:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode(errors="ignore").strip()
                self.data_received.emit(data)
            # time.sleep(0.05)

    def stop(self):
        self.running = False
        self.ser.close()
import sys
import serial
import threading
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton


class VentanaSerie(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Puerto Serie")
        self.resize(400, 300)

        # Configurar diseño
        layout = QVBoxLayout(self)
        self.texto_recibido = QTextEdit(self)
        self.texto_recibido.setReadOnly(True)  # Solo lectura para los datos recibidos
        self.texto_envio = QLineEdit(self)
        self.boton_enviar = QPushButton("Enviar", self)

        layout.addWidget(self.texto_recibido)
        layout.addWidget(self.texto_envio)
        layout.addWidget(self.boton_enviar)

        # Conectar el botón "Enviar" al método de envío
        self.boton_enviar.clicked.connect(self.enviar_datos)

        # Configurar puerto serie
        self.puerto = serial.Serial("COM3", baudrate=9600, timeout=1)

        # Iniciar hilo de lectura
        self.lectura_activa = True
        self.hilo_lectura = threading.Thread(target=self.leer_datos, daemon=True)
        self.hilo_lectura.start()

    def leer_datos(self):
        while self.lectura_activa:
            if self.puerto.in_waiting > 0:
                datos = self.puerto.readline().decode("utf-8").strip()
                self.texto_recibido.append(f"Recibido: {datos}")

    def enviar_datos(self):
        mensaje = self.texto_envio.text()
        if mensaje:
            self.puerto.write(mensaje.encode("utf-8"))
            self.texto_envio.clear()

    def closeEvent(self, event):
        self.lectura_activa = False
        self.puerto.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaSerie()
    ventana.show()
    sys.exit(app.exec())

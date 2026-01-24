from PySide6.QtWidgets import QApplication
from GUI.user_interface_gui import *
import sys

    
app = QApplication(sys.argv)    
ASM = user_interface_gui() 
ASM.setWindowTitle("Advanced Serial Monitor")
ASM.show()            
sys.exit(app.exec())           

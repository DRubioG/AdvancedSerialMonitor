from PySide6.QtWidgets import QApplication
from GUI.user_interface_gui import *
import sys

    
app = QApplication(sys.argv)    # call Qt application class
ASM = user_interface_gui() # call HDLHelper application
ASM.show()            # show the interface
sys.exit(app.exec())           # exit at the finish

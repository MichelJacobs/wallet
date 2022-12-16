from PyQt5 import uic,QtCore
from PyQt5.QtWidgets import QDialog 

class UiMnemonic(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('ui/Mnemonic.ui', self)
        self.show()
    
    
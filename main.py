import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from ui.ui_launcher import UiMnemonic
from ui.action_and_signals import UIActionAndSignals

# ==== MAIN PROGRAM =====
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = UiMnemonic()
    gui_signals = UIActionAndSignals(ui)
    app.exec_()
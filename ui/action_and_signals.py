from PyQt5 import uic
import mnemonic
from ui.result import UiResult
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import generate_mnemonic, is_mnemonic

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "english"  # Default is english
# Generate new mnemonic words
# MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)

class UIActionAndSignals():

  def __init__(self,ui_main_window):

    self.ui = ui_main_window
    print('ok')
    self.ui.generateBtn.clicked.connect(self.generateAccounts)
    self.ui.getMne.clicked.connect(self.generateMnemonic)
    self.result = None

  def generateAccounts(self):

    mnemonic = self.ui.mnemonic.toPlainText()
    count = self.ui.count.value()
    print(mnemonic)
    self.result = UiResult(mnemonic,count)

  def generateMnemonic(self):

    mnemonic = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
    self.ui.mnemonic.setPlainText(mnemonic)


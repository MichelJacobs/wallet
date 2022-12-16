from PyQt5 import uic,QtCore
from PyQt5.QtWidgets import QDialog 
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox, 
    QApplication, QVBoxLayout)

#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import generate_mnemonic, is_mnemonic

import json
import string
import random
from web3 import Web3

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "english"  # Default is english
# Generate new mnemonic words
# MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
# Secret passphrase/password for mnemonic
PASSPHRASE: str = "meherettfdsfds"
net = 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
web3 = Web3(Web3.HTTPProvider(net))

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

class UiResult(QDialog):

    def __init__(self,mne,num,parent=None):
        super().__init__(parent)
        uic.loadUi('ui/result.ui', self)
        
        vbox = QVBoxLayout(self)
        listWidget = QListWidget()
        # Check mnemonic words
        # assert is_mnemonic(mnemonic=mne, language=LANGUAGE)
        print(web3.eth.chain_id)
        # Initialize Litecoin mainnet HDWallet
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(
            cryptocurrency=Cryptocurrency, account=0, change=False, address=0
        )
        # Get Ethereum HDWallet from mnemonic
        for i in range(num):

          PASSPHRASE = self.generate_random_password()
          
          bip44_hdwallet.from_mnemonic(
              mnemonic=mne, passphrase=PASSPHRASE, language=LANGUAGE
          )
          address = bip44_hdwallet.p2pkh_address()
          print(address)
          listWidget.addItem(address) 
          balance = web3.eth.get_balance(address)
          print(str(balance)+"ETH")
          listWidget.addItem(str(balance)+"ETH")
          
        # for i in range(count):
        #   textLabel.setText("Hello World!")
        #   textLabel.move(110,85*i)
            
        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 550, 350)

        self.closeBtn.clicked.connect(self.closeButton)
        self.show()

    def closeButton(self):
        self.hide()


    def generate_random_password(self):
        ## length of password from the user
        length = random.randint(6,15)

        ## shuffling the characters
        random.shuffle(characters)
        
        ## picking random characters from the list
        password = []
        for i in range(length):
          password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        ## printing the list
        return "".join(password)

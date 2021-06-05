from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ecafeMathplotlib import *
from ecafegraph import * 

import sys

class myWindow(Ui_ControlPanel, QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)

        self.btop.clicked.connect(totalItemSold)
        self.bleast.clicked.connect(totalItemSoldInvert)
        self.bactive.clicked.connect(activeTime)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = myWindow()
    Window.show()
    sys.exit(App.exec_())

import sys
import test
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyMainWindow(QMainWindow, test.Ui_MainWindow):
    def __init__(self, ):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

    @staticmethod
    def btn1Clicked():
        print("btn1 clicked")


def main():
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

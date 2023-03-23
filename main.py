import sys
import test
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import serial


class MyMainWindow(QMainWindow, test.Ui_MainWindow):

    def __init__(self, ):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.dict = {}
        self.port = "COM14"
        self.baud = "115200"

    def getforceGAINin(self, forceGAINin):
        self.dict.update({"forceGAINin": forceGAINin})

    def getforceIIR1a0(self, forceIIR1a0):
        self.dict.update({"forceIIR1a0": forceIIR1a0})

    def getforceIIR1a1(self, forceIIR1a1):
        self.dict.update({"forceIIR1a1": forceIIR1a1})

    def getforceIIR1b1(self, forceIIR1b1):
        self.dict.update({"forceIIR1b1": forceIIR1b1})

    def getforceIIR2a0(self, forceIIR2a0):
        self.dict.update({"forceIIR2a0": forceIIR2a0})

    def getforceIIR2a1(self, forceIIR2a1):
        self.dict.update({"forceIIR2a1": forceIIR2a1})

    def getforceIIR2b1(self, forceIIR2b1):
        self.dict.update({"forceIIR2b1": forceIIR2b1})

    def getforceBIASout(self, forceBIASout):
        self.dict.update({"forceBIASout": forceBIASout})

    def getforceGAINout(self, forceGAINout):
        self.dict.update({"forceGAINout": forceGAINout})

    def gettrackBIASin(self, trackBIASin):
        self.dict.update({"trackBIASin": trackBIASin})

    def gettrackGAINin(self, trackGAINin):
        self.dict.update({"trackGAINin": trackGAINin})

    def gettrackIIR1a0(self, trackIIR1a0):
        self.dict.update({"trackIIR1a0": trackIIR1a0})

    def gettrackIIR1a1(self, trackIIR1a1):
        self.dict.update({"trackIIR1a1": trackIIR1a1})

    def gettrackIIR1b1(self, trackIIR1b1):
        self.dict.update({"trackIIR1b1": trackIIR1b1})

    def gettrackIIR2a0(self, trackIIR2a0):
        self.dict.update({"trackIIR2a0": trackIIR2a0})

    def gettrackIIR2a1(self, trackIIR2a1):
        self.dict.update({"trackIIR2a1": trackIIR2a1})

    def gettrackIIR2b1(self, trackIIR2b1):
        self.dict.update({"trackIIR2b1": trackIIR2b1})

    def gettrackBIASout(self, trackBIASout):
        self.dict.update({"trackBIASout": trackBIASout})

    def gettrackGAINout(self, trackGAINout):
        self.dict.update({"trackGAINout": trackGAINout})

    def getsledGAINin(self, sledGAINin):
        self.dict.update({"sledGAINin": sledGAINin})

    def getsledGAINout(self, sledGAINout):
        self.dict.update({"sledGAINout": sledGAINout})

    def getsledThreshold(self, sledThreshold):
        self.dict.update({"sledThreshold": sledThreshold})

    def getsledSpeed(self, sledSpeed):
        self.dict.update({"sledSpeed": sledSpeed})

    def getspindleSpeed(self, spindleSpeed):
        self.dict.update({"spindleSpeed": spindleSpeed})

    def useSpindleSpeed(self):
        if self.connectCheck():
            try:
                aSerial = self.connectMcu()
                if aSerial.isOpen():
                    aSerial.write(dict)
                    aSerial.close()
                else:
                    self.messageDialog("串口打开失败")
            except Exception:
                self.messageDialog("与串口通信异常")

    def connectCheck(self):
        if self.port == "" and self.baud == "":
            self.messageDialog("端口号和波特率不能为空")
            return False
        elif self.port == "":
            self.messageDialog("端口号不能为空")
            return False
        elif self.baud == "":
            self.messageDialog("波特率不能为空")
            return False
        return True

    @staticmethod
    def messageDialog(text):
        msg_box = QMessageBox(QMessageBox.Warning, "error", text)
        msg_box.exec_()

    def connectMcu(self):
        return serial.Serial(self.port, self.baud, timeout=2)


def main():
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

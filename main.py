import os
import sys
import test
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import serial


class MyMainWindow(QMainWindow, test.Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.dictNameToValue = {}
        self.port = "COM14"
        self.baud = "115200"
        self.dictNameToBtn = {"forceGAINin":self.forceGAIN_inLineEdit,
                              "forceIIR1a0":self.forceIIR1a0LineEdit,
                              "forceIIR1a1":self.forceIIR1a1LineEdit,
                              "forceIIR1b1":self.forceIIR1b1LineEdit,
                              "forceIIR2a0":self.forceIIR2a0LineEdit,
                              "forceIIR2a1":self.forceIIR2a1LineEdit,
                              "forceIIR2b1":self.forceIIR2b1LineEdit,
                              "forceBIASout":self.forceBIAS_outLineEdit,
                              "forceGAINout":self.forceGAIN_outLineEdit,
                              "trackBIASin":self.trackBIAS_inLineEdit,
                              "trackGAINin":self.trackGAIN_inLineEdit,
                              "trackIIR1a0":self.trackIIR1a0LineEdit,
                              "trackIIR1a1":self.trackIIR1a1LineEdit,
                              "trackIIR1b1":self.trackIIR1b1LineEdit,
                              "trackIIR2a0":self.trackIIR2a0LineEdit,
                              "trackIIR2a1":self.trackIIR2a1LineEdit,
                              "trackIIR2b1":self.trackIIR2b1LineEdit,
                              "trackBIASout":self.trackBIAS_outLineEdit,
                              "trackGAINout":self.trackGAIN_outLineEdit,
                              "sledGAINin":self.sledGAIN_inLineEdit,
                              "sledGAINout":self.sledGAIN_outLineEdit,
                              "sledThreshold":self.sledThresholdLineEdit,
                              "sledSpeed":self.sledSpeedLineEdit,
                              "spindleSpeed":self.spindleSpeedLineEdit}

    def getforceGAINin(self, forceGAINin):
        self.dictNameToValue.update({"forceGAINin": forceGAINin})

    def getforceIIR1a0(self, forceIIR1a0):
        self.dictNameToValue.update({"forceIIR1a0": forceIIR1a0})

    def getforceIIR1a1(self, forceIIR1a1):
        self.dictNameToValue.update({"forceIIR1a1": forceIIR1a1})

    def getforceIIR1b1(self, forceIIR1b1):
        self.dictNameToValue.update({"forceIIR1b1": forceIIR1b1})

    def getforceIIR2a0(self, forceIIR2a0):
        self.dictNameToValue.update({"forceIIR2a0": forceIIR2a0})

    def getforceIIR2a1(self, forceIIR2a1):
        self.dictNameToValue.update({"forceIIR2a1": forceIIR2a1})

    def getforceIIR2b1(self, forceIIR2b1):
        self.dictNameToValue.update({"forceIIR2b1": forceIIR2b1})

    def getforceBIASout(self, forceBIASout):
        self.dictNameToValue.update({"forceBIASout": forceBIASout})

    def getforceGAINout(self, forceGAINout):
        self.dictNameToValue.update({"forceGAINout": forceGAINout})

    def gettrackBIASin(self, trackBIASin):
        self.dictNameToValue.update({"trackBIASin": trackBIASin})

    def gettrackGAINin(self, trackGAINin):
        self.dictNameToValue.update({"trackGAINin": trackGAINin})

    def gettrackIIR1a0(self, trackIIR1a0):
        self.dictNameToValue.update({"trackIIR1a0": trackIIR1a0})

    def gettrackIIR1a1(self, trackIIR1a1):
        self.dictNameToValue.update({"trackIIR1a1": trackIIR1a1})

    def gettrackIIR1b1(self, trackIIR1b1):
        self.dictNameToValue.update({"trackIIR1b1": trackIIR1b1})

    def gettrackIIR2a0(self, trackIIR2a0):
        self.dictNameToValue.update({"trackIIR2a0": trackIIR2a0})

    def gettrackIIR2a1(self, trackIIR2a1):
        self.dictNameToValue.update({"trackIIR2a1": trackIIR2a1})

    def gettrackIIR2b1(self, trackIIR2b1):
        self.dictNameToValue.update({"trackIIR2b1": trackIIR2b1})

    def gettrackBIASout(self, trackBIASout):
        self.dictNameToValue.update({"trackBIASout": trackBIASout})

    def gettrackGAINout(self, trackGAINout):
        self.dictNameToValue.update({"trackGAINout": trackGAINout})

    def getsledGAINin(self, sledGAINin):
        self.dictNameToValue.update({"sledGAINin": sledGAINin})

    def getsledGAINout(self, sledGAINout):
        self.dictNameToValue.update({"sledGAINout": sledGAINout})

    def getsledThreshold(self, sledThreshold):
        self.dictNameToValue.update({"sledThreshold": sledThreshold})

    def getsledSpeed(self, sledSpeed):
        self.dictNameToValue.update({"sledSpeed": sledSpeed})

    def getspindleSpeed(self, spindleSpeed):
        self.dictNameToValue.update({"spindleSpeed": spindleSpeed})

    def downloadParamsToMcu(self):
        # 检测端口号和波特率是否为空
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

    def saveParamsToFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        filename = dlg.getSaveFileName(self, "保存文件", ".", "Text Files (*.txt)")
        f = open(filename[0], 'w')
        with f:
            for key in self.dictNameToValue.keys():
                f.write(key + ":" + self.dictNameToValue.get(key) + "\n")

    def getParamsFromFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        filename = dlg.getOpenFileName(self, "打开文件", ".", "Text Files (*.txt)")
        for key in self.dictNameToValue.keys():
            self.dictNameToBtn.get(key).setText("")
        self.dictNameToValue.clear()
        f = open(filename[0], 'r')
        with f:
            for line in f:
                pair = line.rstrip().split(":")
                self.dictNameToValue.update({pair[0]: pair[1]})
                self.dictNameToBtn.get(pair[0]).setText(pair[1])

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

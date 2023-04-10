import os
import sys

from PyQt5 import QtGui

import test
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import serial
import threading
import time
from threading import Event


class MyMainWindow(QMainWindow, test.Ui_MainWindow):
    """通过串口传递参数和命令时，串口写入的数据第一部分分为：parameter和command两种"""

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.aSerial = None
        self.setupUi(self)
        self.dictNameToValue = {}
        # 串口连接和通信参数
        self.port = ""
        self.baud = "115200"
        self.databits = "1"
        self.checkbits = "0"
        self.stopbits = "0"
        self.dictNameToBtn = {"forceGAINin": self.forceGAIN_inLineEdit,
                              "forceIIR1a0": self.forceIIR1a0LineEdit,
                              "forceIIR1a1": self.forceIIR1a1LineEdit,
                              "forceIIR1b1": self.forceIIR1b1LineEdit,
                              "forceIIR2a0": self.forceIIR2a0LineEdit,
                              "forceIIR2a1": self.forceIIR2a1LineEdit,
                              "forceIIR2b1": self.forceIIR2b1LineEdit,
                              "forceBIASout": self.forceBIAS_outLineEdit,
                              "forceGAINout": self.forceGAIN_outLineEdit,
                              "trackBIASin": self.trackBIAS_inLineEdit,
                              "trackGAINin": self.trackGAIN_inLineEdit,
                              "trackIIR1a0": self.trackIIR1a0LineEdit,
                              "trackIIR1a1": self.trackIIR1a1LineEdit,
                              "trackIIR1b1": self.trackIIR1b1LineEdit,
                              "trackIIR2a0": self.trackIIR2a0LineEdit,
                              "trackIIR2a1": self.trackIIR2a1LineEdit,
                              "trackIIR2b1": self.trackIIR2b1LineEdit,
                              "trackBIASout": self.trackBIAS_outLineEdit,
                              "trackGAINout": self.trackGAIN_outLineEdit,
                              "sledGAINin": self.sledGAIN_inLineEdit,
                              "sledGAINout": self.sledGAIN_outLineEdit,
                              "sledThreshold": self.sledThresholdLineEdit,
                              "sledSpeed": self.sledSpeedLineEdit,
                              "spindleSpeed": self.spindleSpeedLineEdit}
        self.event = Event()
        self.infoReceivedThread = None

    def getportB(self, portB):
        self.port = portB

    def getbaudB(self, baudB):
        self.baud = baudB

    def getdatabitsB(self, databits):
        self.databits = databits

    def getcheckbitsB(self, checkbits):
        self.checkbits = checkbits

    def getstopbitsB(self, stopbits):
        self.stopbits = stopbits

    # def getorderInput(self, orderInput):
    #     self.orderInput = orderInput

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

    def openSerial(self):
        if self.connectCheck():
            try:
                self.aSerial = self.connectMcu()
                # 创建接收从嵌入式处理器传回信息的线程
                self.infoReceivedThread = threading.Thread(target=self.updateInfoReceived, args=(self.event,))
                self.infoReceivedThread.start()
            except Exception:
                self.messageError("与串口通信异常")

    def closeSerial(self):
        if self.checkSerial():
            self.event.set()
            self.aSerial.close()
        else:
            self.messageError("串口未打开")

    def sendInfo(self):
        if self.checkSerial():
            try:
                self.aSerial.write(str("order#" + self.orderInput.text()).encode("utf-8"))
            except Exception:
                self.messageError("发送失败")
        else:
            self.messageError("请先打开串口")

    def clearWindow(self):
        self.InfoReceived.clear()

    def downloadParamsToMcu(self):
        if self.checkSerial():
            self.aSerial.write(str("parameter#" + str(dict)).encode("utf-8"))
            self.messageSuccess("参数发送成功")
        else:
            self.messageError("串口未打开")

    def connectCheck(self):
        if self.port == "":
            self.messageError("端口号不能为空")
            return False
        return True

    def saveParamsToFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        filename = dlg.getSaveFileName(self, "保存文件", ".", "Text Files (*.txt)")
        if filename[0] == '' and filename[1] == '':
            return
        f = open(filename[0], 'w')
        with f:
            for key in self.dictNameToValue.keys():
                f.write(key + ":" + self.dictNameToValue.get(key) + "\n")

    def getParamsFromFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        filename = dlg.getOpenFileName(self, "打开文件", ".", "Text Files (*.txt)")
        if filename[0] == '' and filename[1] == '':
            return
        f = open(filename[0], 'r')
        for key in self.dictNameToValue.keys():
            self.dictNameToBtn.get(key).setText("")
        self.dictNameToValue.clear()
        with f:
            for line in f:
                pair = line.rstrip().split(":")
                self.dictNameToValue.update({pair[0]: pair[1]})
                self.dictNameToBtn.get(pair[0]).setText(pair[1])

    @staticmethod
    def messageError(text):
        msg_box = QMessageBox(QMessageBox.Warning, "error", text)
        msg_box.exec_()

    @staticmethod
    def messageSuccess(text):
        msg_box = QMessageBox(QMessageBox.Information, "成功", text)
        msg_box.exec_()

    def connectMcu(self):
        return serial.Serial(self.port, self.baud, timeout=2, bytesize=self.databits, parity=self.checkbits,
                             stopbits=self.stopbits)

    def checkSerial(self):
        return self.aSerial is not None and self.aSerial.isOpen()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.checkSerial():
            self.aSerial.close()
        self.event.set()
        super().closeEvent(a0)

    def updateInfoReceived(self, event):
        while 1:
            if self.checkSerial() and self.aSerial.available() > 0:
                self.InfoReceived.append(self.aSerial.readline().decode("utf-8"))
            if event.is_set():
                event.clear()
                break
            time.sleep(0.1)


def main():
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    myMainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

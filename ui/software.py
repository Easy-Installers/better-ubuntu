import softwareui
import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

SUDO = "gksudo -- bash -c "
UPDATE = "apt-get update; "
UPGRADE = "apt-get upgrade; "
INSTALL = "apt-get install -y "

def getInstallablePackets(ui):
    packets = []
    for i in range(100):
        current = None
        try:
          exec("current = ui.checkBox_%d" % i)
        except:
          pass
        if current is not None and current.isChecked():
          packets.append(str(current.text()))
    packets = sorted(packets)
    #print(packets)
    packetlist = " ".join(packets)
    #print(packetlist)
    install_packets = INSTALL + packetlist
    cmd = SUDO + "'" + UPDATE + UPGRADE + install_packets + "'"
    #print(cmd)
    os.system(cmd)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = softwareui.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    result = app.exec_()
    #print(result)
    getInstallablePackets(ui)
    sys.exit(result)


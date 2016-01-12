# -*- coding: utf-8 -*-

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

class Ui_Dialog(object):
    def setupUi(self, Dialog, title, items):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -406, 368, 795))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        
        for i in range(len(items)):
            self.addCheckbox(i, items)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog, title, items)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def addCheckbox(self, i, items):
        exec("self.checkBox_%d = QtGui.QCheckBox(self.scrollAreaWidgetContents)" % i)
        if "checked" in items[i] and items[i]["checked"]:
            exec("self.checkBox_%d.setChecked(True)" % i)
        else:
            exec("self.checkBox_%d.setChecked(False)" % i)
        exec('self.checkBox_%d.setObjectName(_fromUtf8("checkBox_%d"))' % (i, i))
        exec("self.verticalLayout_2.addWidget(self.checkBox_%d)" %  i)

    def retranslateCheckbox(self, i, items):
        exec('self.checkBox_%d.setText(_translate("Dialog", "%s", None))' % (i, items[i]["packet"]))

    def retranslateUi(self, Dialog, title, items):
        Dialog.setWindowTitle(_translate("Dialog", "Better Ubuntu - %s" % title, None))
        
        for i in range(len(items)):
            self.retranslateCheckbox(i, items)

    def getInstallablePackets(self):
        packets = []
        for i in range(100):
            current = None
            try:
                exec("current = self.checkBox_%d" % i)
            except:
                pass
            if current is not None and current.isChecked():
                packets.append(str(current.text()))
        packets = sorted(packets)
        return packets

def askDialog(title, items):
    app = QtGui.QApplication([])
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, title, items)
    Dialog.show()
    result = app.exec_()
    return ui.getInstallablePackets()

if __name__ == "__main__":
    import sys
    print(askDialog("Test", [{"packet":"cinnamon"}, {"checked": True, "packet":"git"}]))
    sys.exit(0)

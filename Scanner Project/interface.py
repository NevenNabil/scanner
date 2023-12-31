# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compilers.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 354)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(26, 175, 231, 121), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.insertButton = QtWidgets.QPushButton(self.centralwidget)
        self.insertButton.setObjectName("insertButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.insertButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label)
        self.addressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addressLineEdit.setReadOnly(True)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)
        self.alertLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.alertLineEdit.setReadOnly(True)
        self.alertLineEdit.setObjectName("alertLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.alertLineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tokensLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tokensLineEdit.setReadOnly(True)
        self.tokensLineEdit.setObjectName("tokensLineEdit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.tokensLineEdit)
        self.startScanningButton = QtWidgets.QPushButton(self.centralwidget)
        self.startScanningButton.setMinimumSize(QtCore.QSize(5, 20))
        self.startScanningButton.setIconSize(QtCore.QSize(15, 15))
        self.startScanningButton.setObjectName("startScanningButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.startScanningButton)
        self.generateScannerOutput = QtWidgets.QPushButton(self.centralwidget)
        self.generateScannerOutput.setObjectName("generateScannerOutput")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.generateScannerOutput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">SCANNER</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SCANNER</span></p></body></html>"))
        self.insertButton.setText(_translate("MainWindow", "Insert file"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">File address :</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Output:</span></p></body></html>"))
        self.startScanningButton.setText(_translate("MainWindow", "Start scanning"))
        self.generateScannerOutput.setText(_translate("MainWindow", "Generate scanner output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

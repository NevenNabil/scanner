from  PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import compilers
#from PyQt5.uic import loadUiType
#MainUI,_ = loadUiType('compilers.ui')
import re

#from NEW_ERROR_FINAL import *

from interface import Ui_MainWindow


class Main(QMainWindow,Ui_MainWindow):


    def __init__(self,parent=None):

        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.generateScannerOutput.setEnabled(False)
        self.startScanningButton.setEnabled(False)
        self.insertButton.clicked.connect(self.import_file)
        #self.generateScannerOutput.connect(self.import_output_file)
        #self.d = self.addressLineEdit.text()
        self.generateScannerOutput.clicked.connect(self.importOutputFile)
        self.startScanningButton.clicked.connect(self.behavior)




    def behavior(self):
        self.alertLineEdit.setText("THe file is being scanned......")
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        self.alertLineEdit.setText("File is finished !")
        self.generateScannerOutput.setEnabled(True)



    def import_file(self):
        global line
        file_filter='Data File(*.txt)'

        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File(*.txt)'
        )
        print(response[0])
        word_url =str(response[0]).replace('[','')
        word_url = word_url.replace(']', '')
        word_url = word_url.replace("'", '')
        self.addressLineEdit.setText(word_url)
        self.startScanningButton.setEnabled(True)
        #file_name = re.split('/', word_url)
        #print(file_name[-1])
        #os.startfile(word_url)
        line=compilers.scannerMain(word_url)
        #compilers.getUrl(word_url)
        return word_url


    def importOutputFile(self):
        #compilers.scannerMain(self.import_file())
        #output=compilers.scannerMain(self.import_file())
        os.startfile("outputTokens.txt")
        self.tokensLineEdit.setText(line)





def main():
    app=QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
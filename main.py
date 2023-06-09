import sys
from PyQt5 import QtWidgets
from DESIGNS.MainUI import Ui_MainWindow
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from screenshotproto import ScreenshotWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        ScreenshotWidget()
        self.ui.takescreenshotbtn.clicked.connect(lambda:ScreenshotWidget)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
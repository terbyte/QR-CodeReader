# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:lightgray")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(301, 270))
        self.label.setStyleSheet("background-color:gray;")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.choosefilebtn = QtWidgets.QPushButton(self.frame)
        self.choosefilebtn.setObjectName("choosefilebtn")
        self.verticalLayout.addWidget(self.choosefilebtn)
        self.takescreenshotbtn = QtWidgets.QPushButton(self.frame)
        self.takescreenshotbtn.setObjectName("takescreenshotbtn")
        self.verticalLayout.addWidget(self.takescreenshotbtn)
        self.verticalLayout.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(141, 16))
        self.label_3.setMaximumSize(QtCore.QSize(250, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(511, 271))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("Background-color:white")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setIndent(6)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.encryptbtn = QtWidgets.QPushButton(self.frame)
        self.encryptbtn.setObjectName("encryptbtn")
        self.verticalLayout_2.addWidget(self.encryptbtn)
        self.decryptbtn = QtWidgets.QPushButton(self.frame)
        self.decryptbtn.setObjectName("decryptbtn")
        self.verticalLayout_2.addWidget(self.decryptbtn)
        self.Clearbtn = QtWidgets.QPushButton(self.frame)
        self.Clearbtn.setObjectName("Clearbtn")
        self.verticalLayout_2.addWidget(self.Clearbtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Preview"))
        self.choosefilebtn.setText(_translate("MainWindow", "Choose File"))
        self.takescreenshotbtn.setText(_translate("MainWindow", "Take Screenshot"))
        self.label_3.setText(_translate("MainWindow", "Encypt-Decrypt QR CODE"))
        self.encryptbtn.setText(_translate("MainWindow", "Encrypt"))
        self.decryptbtn.setText(_translate("MainWindow", "Decrypt"))
        self.Clearbtn.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

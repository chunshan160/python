# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDateEdit,QDateTimeEdit,QTimeEdit, QCalendarWidget, QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtCore import  QDate

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(664, 500)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 641, 79))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # 项目
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)

        # 模块
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 4, 1, 1)

        # 创建时间
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(self)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        # self.dateEdit.dateChanged.connect(self.showdate)
        self.gridLayout.addWidget(self.dateEdit, 2, 2, 1, 1)

        # 结束时间
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.dateEdit_2 = QDateEdit(self)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        # self.dateEdit_2.dateChanged.connect(self.showdate)
        self.gridLayout.addWidget(self.dateEdit_2, 2, 4, 1, 1)

        #水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 查询
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.showdate)

        # 关闭
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 4, 1, 1)


        # 输出
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 641, 360))
        self.groupBox.setObjectName("groupBox")



        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def showdate(self):
        print(self.comboBox.currentText())
        print(self.comboBox_2.currentText())
        print(self.dateEdit.text())
        print(self.dateEdit_2.text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "项目"))
        self.comboBox.setItemText(0, _translate("Form", "项目A"))
        self.comboBox.setItemText(1, _translate("Form", "项目B"))

        self.label_2.setText(_translate("Form", "模块"))
        self.comboBox_2.setItemText(0, _translate("Form", "模块A"))
        self.comboBox_2.setItemText(1, _translate("Form", "模块B"))

        self.label_3.setText(_translate("Form", "创建时间"))
        self.label_4.setText(_translate("Form", "结束时间"))

        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "关闭"))
        self.groupBox.setTitle(_translate("Form", "输出"))

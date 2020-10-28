# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appStore.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 800)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setStyleSheet("background-color: rgb(49, 70,95);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(849, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton_help = QtWidgets.QToolButton(self.widget)
        self.toolButton_help.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_help.setAutoRaise(True)
        self.toolButton_help.setObjectName("toolButton_help")
        self.horizontalLayout.addWidget(self.toolButton_help)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.toolButton_manage = QtWidgets.QToolButton(self.widget)
        self.toolButton_manage.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_manage.setAutoRaise(True)
        self.toolButton_manage.setObjectName("toolButton_manage")
        self.horizontalLayout.addWidget(self.toolButton_manage)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setStyleSheet("background-color: rgb(49, 70, 95);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_4.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/color/source/theme/color/icons/useLeftAll.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_3.addWidget(self.toolButton_4)
        self.toolButton_5 = QtWidgets.QToolButton(self.widget_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/color/source/theme/color/icons/mIconModelLayer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_3.addWidget(self.toolButton_5)
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(436, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 35))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);border:0px groove gray;border-radius:5px;padding:2px 4px")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.toolButton_3 = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_3.setMaximumSize(QtCore.QSize(40, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/color/source/theme/color/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyMiner应用商店"))
        self.toolButton_help.setText(_translate("Form", "帮助"))
        self.toolButton_manage.setText(_translate("Form", "应用管理"))
        self.toolButton_4.setText(_translate("Form", "..."))
        self.toolButton_5.setText(_translate("Form", "..."))
        self.label.setText(_translate("Form", "应用商店"))
        self.lineEdit.setPlaceholderText(_translate("Form", "在应用商店中搜索"))
        self.toolButton_3.setText(_translate("Form", "..."))
import pyqtsource_rc
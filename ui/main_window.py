# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 542)
        MainWindow.setMinimumSize(QtCore.QSize(668, 542))
        MainWindow.setMaximumSize(QtCore.QSize(668, 542))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chb_index = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_index.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chb_index.sizePolicy().hasHeightForWidth())
        self.chb_index.setSizePolicy(sizePolicy)
        self.chb_index.setObjectName("chb_index")
        self.verticalLayout.addWidget(self.chb_index)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_find = QtWidgets.QLineEdit(self.centralwidget)
        self.le_find.setObjectName("le_find")
        self.horizontalLayout.addWidget(self.le_find)
        self.btn_find = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find.setObjectName("btn_find")
        self.horizontalLayout.addWidget(self.btn_find)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb_mode = QtWidgets.QComboBox(self.centralwidget)
        self.cb_mode.setObjectName("cb_mode")
        self.cb_mode.addItem("")
        self.cb_mode.addItem("")
        self.cb_mode.addItem("")
        self.horizontalLayout.addWidget(self.cb_mode)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chb_index.setText(_translate("MainWindow", "???????????????????? ???????????????? ????????????"))
        self.btn_find.setText(_translate("MainWindow", "??????????"))
        self.cb_mode.setItemText(0, _translate("MainWindow", "??????????"))
        self.cb_mode.setItemText(1, _translate("MainWindow", "??????????????"))
        self.cb_mode.setItemText(2, _translate("MainWindow", "????????????"))

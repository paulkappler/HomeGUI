# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Thu Dec 14 22:29:19 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(780, 471)
        Widget.setMinimumSize(QtCore.QSize(0, 259))
        font = QtGui.QFont()
        font.setPointSize(16)
        Widget.setFont(font)
        Widget.setMouseTracking(True)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMouseTracking(True)
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.kitDimButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitDimButton.sizePolicy().hasHeightForWidth())
        self.kitDimButton.setSizePolicy(sizePolicy)
        self.kitDimButton.setObjectName("kitDimButton")
        self.gridLayout_2.addWidget(self.kitDimButton, 2, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMouseTracking(True)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 6, 10, 1)
        self.kitOnButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitOnButton.sizePolicy().hasHeightForWidth())
        self.kitOnButton.setSizePolicy(sizePolicy)
        self.kitOnButton.setObjectName("kitOnButton")
        self.gridLayout_2.addWidget(self.kitOnButton, 1, 2, 1, 1)
        self.downOffButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downOffButton.sizePolicy().hasHeightForWidth())
        self.downOffButton.setSizePolicy(sizePolicy)
        self.downOffButton.setObjectName("downOffButton")
        self.gridLayout_2.addWidget(self.downOffButton, 3, 1, 1, 1)
        self.downDimButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downDimButton.sizePolicy().hasHeightForWidth())
        self.downDimButton.setSizePolicy(sizePolicy)
        self.downDimButton.setObjectName("downDimButton")
        self.gridLayout_2.addWidget(self.downDimButton, 2, 1, 1, 1)
        self.downOnButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downOnButton.sizePolicy().hasHeightForWidth())
        self.downOnButton.setSizePolicy(sizePolicy)
        self.downOnButton.setObjectName("downOnButton")
        self.gridLayout_2.addWidget(self.downOnButton, 1, 1, 1, 1)
        self.hallOnButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hallOnButton.sizePolicy().hasHeightForWidth())
        self.hallOnButton.setSizePolicy(sizePolicy)
        self.hallOnButton.setObjectName("hallOnButton")
        self.gridLayout_2.addWidget(self.hallOnButton, 1, 3, 1, 1)
        self.hallDimButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hallDimButton.sizePolicy().hasHeightForWidth())
        self.hallDimButton.setSizePolicy(sizePolicy)
        self.hallDimButton.setObjectName("hallDimButton")
        self.gridLayout_2.addWidget(self.hallDimButton, 2, 3, 1, 1)
        self.upOffButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upOffButton.sizePolicy().hasHeightForWidth())
        self.upOffButton.setSizePolicy(sizePolicy)
        self.upOffButton.setObjectName("upOffButton")
        self.gridLayout_2.addWidget(self.upOffButton, 3, 3, 1, 1)
        self.kitOffButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitOffButton.sizePolicy().hasHeightForWidth())
        self.kitOffButton.setSizePolicy(sizePolicy)
        self.kitOffButton.setObjectName("kitOffButton")
        self.gridLayout_2.addWidget(self.kitOffButton, 3, 2, 1, 1)
        self.allOffButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allOffButton.sizePolicy().hasHeightForWidth())
        self.allOffButton.setSizePolicy(sizePolicy)
        self.allOffButton.setMouseTracking(True)
        self.allOffButton.setObjectName("allOffButton")
        self.gridLayout_2.addWidget(self.allOffButton, 5, 1, 1, 4)
        self.outOffButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOffButton.sizePolicy().hasHeightForWidth())
        self.outOffButton.setSizePolicy(sizePolicy)
        self.outOffButton.setObjectName("outOffButton")
        self.gridLayout_2.addWidget(self.outOffButton, 2, 4, 1, 1)
        self.outOnButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOnButton.sizePolicy().hasHeightForWidth())
        self.outOnButton.setSizePolicy(sizePolicy)
        self.outOnButton.setObjectName("outOnButton")
        self.gridLayout_2.addWidget(self.outOnButton, 1, 4, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMouseTracking(True)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ipValue = QtWidgets.QLabel(self.tab_2)
        self.ipValue.setMouseTracking(True)
        self.ipValue.setObjectName("ipValue")
        self.gridLayout_3.addWidget(self.ipValue, 0, 1, 1, 1)
        self.ipName = QtWidgets.QLabel(self.tab_2)
        self.ipName.setMouseTracking(True)
        self.ipName.setObjectName("ipName")
        self.gridLayout_3.addWidget(self.ipName, 0, 0, 1, 1)
        self.rebootButton = QtWidgets.QPushButton(self.tab_2)
        self.rebootButton.setMouseTracking(True)
        self.rebootButton.setObjectName("rebootButton")
        self.gridLayout_3.addWidget(self.rebootButton, 2, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.tab_2)
        self.exitButton.setMouseTracking(True)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_3.addWidget(self.exitButton, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMouseTracking(True)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.debugText = QtWidgets.QPlainTextEdit(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.debugText.setFont(font)
        self.debugText.setMouseTracking(True)
        self.debugText.setObjectName("debugText")
        self.gridLayout_4.addWidget(self.debugText, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.kitDimButton.setText(_translate("Widget", "Kitchen\n"
"Dim"))
        self.kitOnButton.setText(_translate("Widget", "Kitchen\n"
"On"))
        self.downOffButton.setText(_translate("Widget", "Downstairs\n"
"Off"))
        self.downDimButton.setText(_translate("Widget", "Downstairs\n"
"Dim"))
        self.downOnButton.setText(_translate("Widget", "Downstairs\n"
"On"))
        self.hallOnButton.setText(_translate("Widget", "Hall\n"
"On"))
        self.hallDimButton.setText(_translate("Widget", "Hall\n"
"Dim"))
        self.upOffButton.setText(_translate("Widget", "Upstairs\n"
"Off"))
        self.kitOffButton.setText(_translate("Widget", "Kitchen\n"
"Off"))
        self.allOffButton.setText(_translate("Widget", "All Off"))
        self.outOffButton.setText(_translate("Widget", "Outside\n"
"Off"))
        self.outOnButton.setText(_translate("Widget", "Outside\n"
"On"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Widget", "Control"))
        self.ipValue.setText(_translate("Widget", "TextLabel"))
        self.ipName.setText(_translate("Widget", "IP Address"))
        self.rebootButton.setText(_translate("Widget", "Reboot"))
        self.exitButton.setText(_translate("Widget", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Widget", "System"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Widget", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())


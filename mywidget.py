# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 489)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QtCore.QSize(700, 400))
        Widget.setMaximumSize(QtCore.QSize(800, 489))
        font = QtGui.QFont()
        font.setPointSize(17)
        Widget.setFont(font)
        Widget.setMouseTracking(True)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabControl = QtWidgets.QWidget()
        self.tabControl.setMouseTracking(True)
        self.tabControl.setObjectName("tabControl")
        self.gridControl = QtWidgets.QGridLayout(self.tabControl)
        self.gridControl.setContentsMargins(11, 11, 11, 11)
        self.gridControl.setSpacing(6)
        self.gridControl.setObjectName("gridControl")
        self.kitDimButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitDimButton.sizePolicy().hasHeightForWidth())
        self.kitDimButton.setSizePolicy(sizePolicy)
        self.kitDimButton.setObjectName("kitDimButton")
        self.gridControl.addWidget(self.kitDimButton, 3, 3, 1, 1)
        self.kitOnButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitOnButton.sizePolicy().hasHeightForWidth())
        self.kitOnButton.setSizePolicy(sizePolicy)
        self.kitOnButton.setObjectName("kitOnButton")
        self.gridControl.addWidget(self.kitOnButton, 2, 3, 1, 1)
        self.downOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downOffButton.sizePolicy().hasHeightForWidth())
        self.downOffButton.setSizePolicy(sizePolicy)
        self.downOffButton.setObjectName("downOffButton")
        self.gridControl.addWidget(self.downOffButton, 4, 1, 1, 1)
        self.downDimButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downDimButton.sizePolicy().hasHeightForWidth())
        self.downDimButton.setSizePolicy(sizePolicy)
        self.downDimButton.setObjectName("downDimButton")
        self.gridControl.addWidget(self.downDimButton, 3, 1, 1, 1)
        self.downOnButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downOnButton.sizePolicy().hasHeightForWidth())
        self.downOnButton.setSizePolicy(sizePolicy)
        self.downOnButton.setObjectName("downOnButton")
        self.gridControl.addWidget(self.downOnButton, 2, 1, 1, 1)
        self.hallOnButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hallOnButton.sizePolicy().hasHeightForWidth())
        self.hallOnButton.setSizePolicy(sizePolicy)
        self.hallOnButton.setObjectName("hallOnButton")
        self.gridControl.addWidget(self.hallOnButton, 2, 4, 1, 1)
        self.hallDimButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hallDimButton.sizePolicy().hasHeightForWidth())
        self.hallDimButton.setSizePolicy(sizePolicy)
        self.hallDimButton.setObjectName("hallDimButton")
        self.gridControl.addWidget(self.hallDimButton, 3, 4, 1, 1)
        self.kitOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitOffButton.sizePolicy().hasHeightForWidth())
        self.kitOffButton.setSizePolicy(sizePolicy)
        self.kitOffButton.setObjectName("kitOffButton")
        self.gridControl.addWidget(self.kitOffButton, 4, 3, 1, 1)
        self.hallOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hallOffButton.sizePolicy().hasHeightForWidth())
        self.hallOffButton.setSizePolicy(sizePolicy)
        self.hallOffButton.setObjectName("hallOffButton")
        self.gridControl.addWidget(self.hallOffButton, 4, 4, 1, 1)
        self.downHallOnButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downHallOnButton.sizePolicy().hasHeightForWidth())
        self.downHallOnButton.setSizePolicy(sizePolicy)
        self.downHallOnButton.setObjectName("downHallOnButton")
        self.gridControl.addWidget(self.downHallOnButton, 2, 2, 1, 1)
        self.downHallDimButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downHallDimButton.sizePolicy().hasHeightForWidth())
        self.downHallDimButton.setSizePolicy(sizePolicy)
        self.downHallDimButton.setObjectName("downHallDimButton")
        self.gridControl.addWidget(self.downHallDimButton, 3, 2, 1, 1)
        self.downHallOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downHallOffButton.sizePolicy().hasHeightForWidth())
        self.downHallOffButton.setSizePolicy(sizePolicy)
        self.downHallOffButton.setObjectName("downHallOffButton")
        self.gridControl.addWidget(self.downHallOffButton, 4, 2, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.tabControl)
        self.statusLabel.setObjectName("statusLabel")
        self.gridControl.addWidget(self.statusLabel, 0, 1, 1, 8)
        self.upOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upOffButton.sizePolicy().hasHeightForWidth())
        self.upOffButton.setSizePolicy(sizePolicy)
        self.upOffButton.setObjectName("upOffButton")
        self.gridControl.addWidget(self.upOffButton, 4, 5, 1, 1)
        self.outOnButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOnButton.sizePolicy().hasHeightForWidth())
        self.outOnButton.setSizePolicy(sizePolicy)
        self.outOnButton.setObjectName("outOnButton")
        self.gridControl.addWidget(self.outOnButton, 2, 5, 1, 1)
        self.outOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOffButton.sizePolicy().hasHeightForWidth())
        self.outOffButton.setSizePolicy(sizePolicy)
        self.outOffButton.setObjectName("outOffButton")
        self.gridControl.addWidget(self.outOffButton, 3, 5, 1, 1)
        self.allOffButton = QtWidgets.QPushButton(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allOffButton.sizePolicy().hasHeightForWidth())
        self.allOffButton.setSizePolicy(sizePolicy)
        self.allOffButton.setObjectName("allOffButton")
        self.gridControl.addWidget(self.allOffButton, 5, 1, 1, 5)
        self.listWidget = QtWidgets.QListWidget(self.tabControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.gridControl.addWidget(self.listWidget, 2, 6, 4, 2)
        self.tabWidget.addTab(self.tabControl, "")
        self.tabRoom = QtWidgets.QWidget()
        self.tabRoom.setObjectName("tabRoom")
        self.gridRooms = QtWidgets.QGridLayout(self.tabRoom)
        self.gridRooms.setContentsMargins(11, 11, 11, 11)
        self.gridRooms.setSpacing(6)
        self.gridRooms.setObjectName("gridRooms")
        self.roomBlueButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomBlueButton.setObjectName("roomBlueButton")
        self.gridRooms.addWidget(self.roomBlueButton, 13, 4, 1, 1)
        self.roomRedButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomRedButton.setObjectName("roomRedButton")
        self.gridRooms.addWidget(self.roomRedButton, 14, 4, 1, 1)
        self.room50Button = QtWidgets.QPushButton(self.tabRoom)
        self.room50Button.setObjectName("room50Button")
        self.gridRooms.addWidget(self.room50Button, 2, 4, 1, 1)
        self.roomDimButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomDimButton.setObjectName("roomDimButton")
        self.gridRooms.addWidget(self.roomDimButton, 5, 4, 1, 1)
        self.room12Button = QtWidgets.QPushButton(self.tabRoom)
        self.room12Button.setObjectName("room12Button")
        self.gridRooms.addWidget(self.room12Button, 4, 4, 1, 1)
        self.room100Button = QtWidgets.QPushButton(self.tabRoom)
        self.room100Button.setObjectName("room100Button")
        self.gridRooms.addWidget(self.room100Button, 1, 4, 1, 1)
        self.room25Button = QtWidgets.QPushButton(self.tabRoom)
        self.room25Button.setObjectName("room25Button")
        self.gridRooms.addWidget(self.room25Button, 3, 4, 1, 1)
        self.roomOnButton = QtWidgets.QPushButton(self.tabRoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomOnButton.sizePolicy().hasHeightForWidth())
        self.roomOnButton.setSizePolicy(sizePolicy)
        self.roomOnButton.setObjectName("roomOnButton")
        self.gridRooms.addWidget(self.roomOnButton, 1, 3, 7, 1)
        self.roomSkyButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomSkyButton.setObjectName("roomSkyButton")
        self.gridRooms.addWidget(self.roomSkyButton, 9, 4, 1, 1)
        self.roomBrightButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomBrightButton.setObjectName("roomBrightButton")
        self.gridRooms.addWidget(self.roomBrightButton, 10, 4, 1, 1)
        self.roomNormalButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomNormalButton.setObjectName("roomNormalButton")
        self.gridRooms.addWidget(self.roomNormalButton, 11, 4, 1, 1)
        self.roomWarmButton = QtWidgets.QPushButton(self.tabRoom)
        self.roomWarmButton.setObjectName("roomWarmButton")
        self.gridRooms.addWidget(self.roomWarmButton, 12, 4, 1, 1)
        self.roomOffButton = QtWidgets.QPushButton(self.tabRoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomOffButton.sizePolicy().hasHeightForWidth())
        self.roomOffButton.setSizePolicy(sizePolicy)
        self.roomOffButton.setObjectName("roomOffButton")
        self.gridRooms.addWidget(self.roomOffButton, 8, 3, 7, 1)
        self.roomVerticalSlider = QtWidgets.QSlider(self.tabRoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomVerticalSlider.sizePolicy().hasHeightForWidth())
        self.roomVerticalSlider.setSizePolicy(sizePolicy)
        self.roomVerticalSlider.setStyleSheet("QSlider::handle{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #111111, stop:1 #CCCCCC);\n"
"    border-radius: 5px;\n"
"    border-color: #000000;\n"
"\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    height: 30px;\n"
"    width: 10px;\n"
"\n"
"    margin: 5px 5px; \n"
"}\n"
"\n"
"QSlider::groove\n"
"{\n"
"    margin-top: 20px;\n"
"    margin-bottom: 20px;\n"
"    background: qlineargradient(x1:.5, y1:0, x2:.5, y2:1, stop:0 #999999, stop:1 #FFFFFF);\n"
"\n"
"}  \n"
"")
        self.roomVerticalSlider.setMinimum(0)
        self.roomVerticalSlider.setMaximum(254)
        self.roomVerticalSlider.setPageStep(30)
        self.roomVerticalSlider.setProperty("value", 254)
        self.roomVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.roomVerticalSlider.setTickInterval(16)
        self.roomVerticalSlider.setObjectName("roomVerticalSlider")
        self.gridRooms.addWidget(self.roomVerticalSlider, 1, 2, 15, 1)
        self.listWidgetRoom = QtWidgets.QListWidget(self.tabRoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetRoom.sizePolicy().hasHeightForWidth())
        self.listWidgetRoom.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidgetRoom.setFont(font)
        self.listWidgetRoom.setObjectName("listWidgetRoom")
        self.gridRooms.addWidget(self.listWidgetRoom, 1, 0, 15, 1)
        self.tabWidget.addTab(self.tabRoom, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMouseTracking(False)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.insideLabel = QtWidgets.QLabel(self.tab_2)
        self.insideLabel.setObjectName("insideLabel")
        self.gridLayout_3.addWidget(self.insideLabel, 3, 1, 1, 1)
        self.rebootButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rebootButton.sizePolicy().hasHeightForWidth())
        self.rebootButton.setSizePolicy(sizePolicy)
        self.rebootButton.setMouseTracking(True)
        self.rebootButton.setObjectName("rebootButton")
        self.gridLayout_3.addWidget(self.rebootButton, 7, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMouseTracking(True)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_3.addWidget(self.exitButton, 6, 0, 1, 1)
        self.targetTitleLabel = QtWidgets.QLabel(self.tab_2)
        self.targetTitleLabel.setObjectName("targetTitleLabel")
        self.gridLayout_3.addWidget(self.targetTitleLabel, 4, 0, 1, 1)
        self.windowLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowLabel.sizePolicy().hasHeightForWidth())
        self.windowLabel.setSizePolicy(sizePolicy)
        self.windowLabel.setObjectName("windowLabel")
        self.gridLayout_3.addWidget(self.windowLabel, 3, 3, 1, 1)
        self.insideTitleLabel = QtWidgets.QLabel(self.tab_2)
        self.insideTitleLabel.setObjectName("insideTitleLabel")
        self.gridLayout_3.addWidget(self.insideTitleLabel, 3, 0, 1, 1)
        self.targetLeftLabel = QtWidgets.QLabel(self.tab_2)
        self.targetLeftLabel.setObjectName("targetLeftLabel")
        self.gridLayout_3.addWidget(self.targetLeftLabel, 4, 1, 1, 1)
        self.outsideTitlelabel = QtWidgets.QLabel(self.tab_2)
        self.outsideTitlelabel.setObjectName("outsideTitlelabel")
        self.gridLayout_3.addWidget(self.outsideTitlelabel, 2, 0, 1, 1)
        self.autoLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoLabel.sizePolicy().hasHeightForWidth())
        self.autoLabel.setSizePolicy(sizePolicy)
        self.autoLabel.setObjectName("autoLabel")
        self.gridLayout_3.addWidget(self.autoLabel, 2, 3, 1, 1)
        self.ipValue = QtWidgets.QLabel(self.tab_2)
        self.ipValue.setMouseTracking(True)
        self.ipValue.setObjectName("ipValue")
        self.gridLayout_3.addWidget(self.ipValue, 0, 1, 1, 1)
        self.ipName = QtWidgets.QLabel(self.tab_2)
        self.ipName.setMouseTracking(True)
        self.ipName.setObjectName("ipName")
        self.gridLayout_3.addWidget(self.ipName, 0, 0, 1, 1)
        self.outsideLabel = QtWidgets.QLabel(self.tab_2)
        self.outsideLabel.setObjectName("outsideLabel")
        self.gridLayout_3.addWidget(self.outsideLabel, 2, 1, 1, 1)
        self.targetRightLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetRightLabel.sizePolicy().hasHeightForWidth())
        self.targetRightLabel.setSizePolicy(sizePolicy)
        self.targetRightLabel.setObjectName("targetRightLabel")
        self.gridLayout_3.addWidget(self.targetRightLabel, 4, 3, 1, 1)
        self.autoWindowButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoWindowButton.sizePolicy().hasHeightForWidth())
        self.autoWindowButton.setSizePolicy(sizePolicy)
        self.autoWindowButton.setObjectName("autoWindowButton")
        self.gridLayout_3.addWidget(self.autoWindowButton, 6, 1, 1, 1)
        self.closeWindowButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeWindowButton.sizePolicy().hasHeightForWidth())
        self.closeWindowButton.setSizePolicy(sizePolicy)
        self.closeWindowButton.setObjectName("closeWindowButton")
        self.gridLayout_3.addWidget(self.closeWindowButton, 7, 1, 1, 1)
        self.openWindowButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openWindowButton.sizePolicy().hasHeightForWidth())
        self.openWindowButton.setSizePolicy(sizePolicy)
        self.openWindowButton.setObjectName("openWindowButton")
        self.gridLayout_3.addWidget(self.openWindowButton, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMouseTracking(False)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.debugText = QtWidgets.QPlainTextEdit(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.debugText.setFont(font)
        self.debugText.setMouseTracking(True)
        self.debugText.setObjectName("debugText")
        self.gridLayout_4.addWidget(self.debugText, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Widget)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.kitDimButton.setText(_translate("Widget", "Kitchen\n"
"Dim"))
        self.kitOnButton.setText(_translate("Widget", "Kitchen\n"
"On"))
        self.downOffButton.setText(_translate("Widget", "Down\n"
"Off"))
        self.downDimButton.setText(_translate("Widget", "Down\n"
"Dim"))
        self.downOnButton.setText(_translate("Widget", "Down\n"
"On"))
        self.hallOnButton.setText(_translate("Widget", "Hall\n"
"On"))
        self.hallDimButton.setText(_translate("Widget", "Hall\n"
"Dim"))
        self.kitOffButton.setText(_translate("Widget", "Kitchen\n"
"Off"))
        self.hallOffButton.setText(_translate("Widget", "Hall\n"
"Off"))
        self.downHallOnButton.setText(_translate("Widget", "Down\n"
"Hall\n"
"On"))
        self.downHallDimButton.setText(_translate("Widget", "Down\n"
"Hall\n"
"Dim"))
        self.downHallOffButton.setText(_translate("Widget", "Down\n"
"Hall\n"
"Off"))
        self.upOffButton.setText(_translate("Widget", "Upstairs\n"
"Off"))
        self.outOnButton.setText(_translate("Widget", "Outside\n"
"On"))
        self.outOffButton.setText(_translate("Widget", "Outside\n"
"Off"))
        self.allOffButton.setText(_translate("Widget", "All\n"
"Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabControl), _translate("Widget", "Control"))
        self.roomBlueButton.setText(_translate("Widget", "Blue"))
        self.roomRedButton.setText(_translate("Widget", "Red"))
        self.room50Button.setText(_translate("Widget", "50%"))
        self.roomDimButton.setText(_translate("Widget", "Dim"))
        self.room12Button.setText(_translate("Widget", "12%"))
        self.room100Button.setText(_translate("Widget", "100%"))
        self.room25Button.setText(_translate("Widget", "25%"))
        self.roomOnButton.setText(_translate("Widget", "On"))
        self.roomSkyButton.setText(_translate("Widget", "Sky"))
        self.roomBrightButton.setText(_translate("Widget", "Bright"))
        self.roomNormalButton.setText(_translate("Widget", "Normal"))
        self.roomWarmButton.setText(_translate("Widget", "Warm"))
        self.roomOffButton.setText(_translate("Widget", "Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRoom), _translate("Widget", "Rooms"))
        self.insideLabel.setText(_translate("Widget", "TextLabel"))
        self.rebootButton.setText(_translate("Widget", "Reboot"))
        self.exitButton.setText(_translate("Widget", "Exit"))
        self.targetTitleLabel.setText(_translate("Widget", "Target Temp"))
        self.windowLabel.setText(_translate("Widget", "TextLabel"))
        self.insideTitleLabel.setText(_translate("Widget", "Inside Temp"))
        self.targetLeftLabel.setText(_translate("Widget", "TextLabel"))
        self.outsideTitlelabel.setText(_translate("Widget", "Outside Temp"))
        self.autoLabel.setText(_translate("Widget", "TextLabel"))
        self.ipValue.setText(_translate("Widget", "TextLabel"))
        self.ipName.setText(_translate("Widget", "IP Address"))
        self.outsideLabel.setText(_translate("Widget", "TextLabel"))
        self.targetRightLabel.setText(_translate("Widget", "TextLabel"))
        self.autoWindowButton.setText(_translate("Widget", "Automatic Windows"))
        self.closeWindowButton.setText(_translate("Widget", "Close Windows"))
        self.openWindowButton.setText(_translate("Widget", "Open Windows"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Widget", "System"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Widget", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Widget", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())


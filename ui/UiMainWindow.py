# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 450)
        MainWindow.setMinimumSize(QtCore.QSize(350, 450))
        MainWindow.setMaximumSize(QtCore.QSize(350, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 365, 27))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.row1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.row1.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.row1.setContentsMargins(4, 2, 2, 2)
        self.row1.setSpacing(2)
        self.row1.setObjectName("row1")
        self.lblChooseEmulator = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChooseEmulator.sizePolicy().hasHeightForWidth())
        self.lblChooseEmulator.setSizePolicy(sizePolicy)
        self.lblChooseEmulator.setMinimumSize(QtCore.QSize(80, 23))
        self.lblChooseEmulator.setMaximumSize(QtCore.QSize(80, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblChooseEmulator.setFont(font)
        self.lblChooseEmulator.setObjectName("lblChooseEmulator")
        self.row1.addWidget(self.lblChooseEmulator)
        self.listEmulator = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listEmulator.sizePolicy().hasHeightForWidth())
        self.listEmulator.setSizePolicy(sizePolicy)
        self.listEmulator.setMinimumSize(QtCore.QSize(180, 20))
        self.listEmulator.setMaximumSize(QtCore.QSize(180, 20))
        self.listEmulator.setObjectName("listEmulator")
        self.row1.addWidget(self.listEmulator)
        self.btnConnectEmulator = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConnectEmulator.sizePolicy().hasHeightForWidth())
        self.btnConnectEmulator.setSizePolicy(sizePolicy)
        self.btnConnectEmulator.setMinimumSize(QtCore.QSize(80, 23))
        self.btnConnectEmulator.setMaximumSize(QtCore.QSize(80, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnConnectEmulator.setFont(font)
        self.btnConnectEmulator.setObjectName("btnConnectEmulator")
        self.row1.addWidget(self.btnConnectEmulator)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row1.addItem(spacerItem)
        self.row1.setStretch(0, 2)
        self.row1.setStretch(1, 3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 30, 351, 204))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.row2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.row2.setContentsMargins(2, 2, 2, 2)
        self.row2.setSpacing(2)
        self.row2.setObjectName("row2")
        self.col2_1 = QtWidgets.QGridLayout()
        self.col2_1.setContentsMargins(2, 2, 2, 2)
        self.col2_1.setSpacing(2)
        self.col2_1.setObjectName("col2_1")
        self.txtMinFishSize = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMinFishSize.sizePolicy().hasHeightForWidth())
        self.txtMinFishSize.setSizePolicy(sizePolicy)
        self.txtMinFishSize.setObjectName("txtMinFishSize")
        self.col2_1.addWidget(self.txtMinFishSize, 4, 1, 1, 1)
        self.lblMinFishSize = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lblMinFishSize.setObjectName("lblMinFishSize")
        self.col2_1.addWidget(self.lblMinFishSize, 4, 0, 1, 1)
        self.cbFreeMouse = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.cbFreeMouse.setObjectName("cbFreeMouse")
        self.col2_1.addWidget(self.cbFreeMouse, 6, 0, 1, 1)
        self.cbShowFish = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.cbShowFish.setObjectName("cbShowFish")
        self.col2_1.addWidget(self.cbShowFish, 11, 0, 1, 1)
        self.cbFishDetection = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.cbFishDetection.setObjectName("cbFishDetection")
        self.col2_1.addWidget(self.cbFishDetection, 9, 0, 1, 1)
        self.lblTimeWaitMark = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblTimeWaitMark.setFont(font)
        self.lblTimeWaitMark.setObjectName("lblTimeWaitMark")
        self.col2_1.addWidget(self.lblTimeWaitMark, 3, 0, 1, 1)
        self.lblTimePullingFish = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblTimePullingFish.setFont(font)
        self.lblTimePullingFish.setObjectName("lblTimePullingFish")
        self.col2_1.addWidget(self.lblTimePullingFish, 2, 0, 1, 1)
        self.txtWaitingFishTime = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtWaitingFishTime.sizePolicy().hasHeightForWidth())
        self.txtWaitingFishTime.setSizePolicy(sizePolicy)
        self.txtWaitingFishTime.setObjectName("txtWaitingFishTime")
        self.col2_1.addWidget(self.txtWaitingFishTime, 3, 1, 1, 1)
        self.txtPullingFishTime = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPullingFishTime.sizePolicy().hasHeightForWidth())
        self.txtPullingFishTime.setSizePolicy(sizePolicy)
        self.txtPullingFishTime.setObjectName("txtPullingFishTime")
        self.col2_1.addWidget(self.txtPullingFishTime, 2, 1, 1, 1)
        self.lblRodPosition = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblRodPosition.setFont(font)
        self.lblRodPosition.setObjectName("lblRodPosition")
        self.col2_1.addWidget(self.lblRodPosition, 1, 0, 1, 1)
        self.txtFishingRodPosition = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFishingRodPosition.sizePolicy().hasHeightForWidth())
        self.txtFishingRodPosition.setSizePolicy(sizePolicy)
        self.txtFishingRodPosition.setObjectName("txtFishingRodPosition")
        self.col2_1.addWidget(self.txtFishingRodPosition, 1, 1, 1, 1)
        self.col2_1.setColumnStretch(0, 6)
        self.col2_1.setColumnStretch(1, 4)
        self.row2.addLayout(self.col2_1)
        self.lblShowFish = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblShowFish.sizePolicy().hasHeightForWidth())
        self.lblShowFish.setSizePolicy(sizePolicy)
        self.lblShowFish.setMinimumSize(QtCore.QSize(200, 200))
        self.lblShowFish.setMaximumSize(QtCore.QSize(200, 200))
        self.lblShowFish.setAlignment(QtCore.Qt.AlignCenter)
        self.lblShowFish.setObjectName("lblShowFish")
        self.row2.addWidget(self.lblShowFish)
        self.row2.setStretch(0, 3)
        self.row2.setStretch(1, 4)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 240, 351, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.row3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.row3.setContentsMargins(2, 2, 2, 2)
        self.row3.setSpacing(2)
        self.row3.setObjectName("row3")
        self.btnGetMarkPosition = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGetMarkPosition.sizePolicy().hasHeightForWidth())
        self.btnGetMarkPosition.setSizePolicy(sizePolicy)
        self.btnGetMarkPosition.setObjectName("btnGetMarkPosition")
        self.row3.addWidget(self.btnGetMarkPosition, 0, 0, 1, 1)
        self.col3_1 = QtWidgets.QHBoxLayout()
        self.col3_1.setContentsMargins(0, 0, 0, 0)
        self.col3_1.setSpacing(2)
        self.col3_1.setObjectName("col3_1")
        self.lcdMarkX = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMarkX.sizePolicy().hasHeightForWidth())
        self.lcdMarkX.setSizePolicy(sizePolicy)
        self.lcdMarkX.setObjectName("lcdMarkX")
        self.col3_1.addWidget(self.lcdMarkX)
        self.lcdMarkY = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMarkY.sizePolicy().hasHeightForWidth())
        self.lcdMarkY.setSizePolicy(sizePolicy)
        self.lcdMarkY.setObjectName("lcdMarkY")
        self.col3_1.addWidget(self.lcdMarkY)
        self.row3.addLayout(self.col3_1, 1, 0, 1, 1)
        self.col3_2 = QtWidgets.QHBoxLayout()
        self.col3_2.setSpacing(2)
        self.col3_2.setObjectName("col3_2")
        self.lcdRodX = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdRodX.sizePolicy().hasHeightForWidth())
        self.lcdRodX.setSizePolicy(sizePolicy)
        self.lcdRodX.setObjectName("lcdRodX")
        self.col3_2.addWidget(self.lcdRodX)
        self.lcdRodY = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdRodY.sizePolicy().hasHeightForWidth())
        self.lcdRodY.setSizePolicy(sizePolicy)
        self.lcdRodY.setObjectName("lcdRodY")
        self.col3_2.addWidget(self.lcdRodY)
        self.row3.addLayout(self.col3_2, 1, 1, 1, 1)
        self.btnGetBobberPosition = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGetBobberPosition.sizePolicy().hasHeightForWidth())
        self.btnGetBobberPosition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnGetBobberPosition.setFont(font)
        self.btnGetBobberPosition.setObjectName("btnGetBobberPosition")
        self.row3.addWidget(self.btnGetBobberPosition, 0, 1, 1, 1)
        self.btnStartFishing = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartFishing.sizePolicy().hasHeightForWidth())
        self.btnStartFishing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnStartFishing.setFont(font)
        self.btnStartFishing.setObjectName("btnStartFishing")
        self.row3.addWidget(self.btnStartFishing, 0, 2, 1, 1)
        self.btnStopFishing = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStopFishing.sizePolicy().hasHeightForWidth())
        self.btnStopFishing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnStopFishing.setFont(font)
        self.btnStopFishing.setObjectName("btnStopFishing")
        self.row3.addWidget(self.btnStopFishing, 1, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 380, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.row4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.row4.setContentsMargins(2, 2, 2, 2)
        self.row4.setSpacing(2)
        self.row4.setObjectName("row4")
        self.lblStatus = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStatus.sizePolicy().hasHeightForWidth())
        self.lblStatus.setSizePolicy(sizePolicy)
        self.lblStatus.setObjectName("lblStatus")
        self.row4.addWidget(self.lblStatus)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 320, 351, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.row3_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.row3_2.setContentsMargins(2, 2, 2, 2)
        self.row3_2.setSpacing(2)
        self.row3_2.setObjectName("row3_2")
        self.lblNumFishing = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNumFishing.sizePolicy().hasHeightForWidth())
        self.lblNumFishing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNumFishing.setFont(font)
        self.lblNumFishing.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNumFishing.setObjectName("lblNumFishing")
        self.row3_2.addWidget(self.lblNumFishing, 0, 1, 1, 1)
        self.lblNumFish = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNumFish.sizePolicy().hasHeightForWidth())
        self.lblNumFish.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNumFish.setFont(font)
        self.lblNumFish.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNumFish.setObjectName("lblNumFish")
        self.row3_2.addWidget(self.lblNumFish, 0, 2, 1, 1)
        self.lcdNumFish = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumFish.sizePolicy().hasHeightForWidth())
        self.lcdNumFish.setSizePolicy(sizePolicy)
        self.lcdNumFish.setObjectName("lcdNumFish")
        self.row3_2.addWidget(self.lcdNumFish, 1, 2, 1, 1)
        self.lcdTime = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdTime.sizePolicy().hasHeightForWidth())
        self.lcdTime.setSizePolicy(sizePolicy)
        self.lcdTime.setObjectName("lcdTime")
        self.row3_2.addWidget(self.lcdTime, 1, 0, 1, 1)
        self.lcdNumFishing = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumFishing.sizePolicy().hasHeightForWidth())
        self.lcdNumFishing.setSizePolicy(sizePolicy)
        self.lcdNumFishing.setObjectName("lcdNumFishing")
        self.row3_2.addWidget(self.lcdNumFishing, 1, 1, 1, 1)
        self.lblTime = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTime.sizePolicy().hasHeightForWidth())
        self.lblTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setTextFormat(QtCore.Qt.AutoText)
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.row3_2.addWidget(self.lblTime, 0, 0, 1, 1)
        self.row3_2.setColumnStretch(0, 8)
        self.row3_2.setColumnStretch(1, 5)
        self.row3_2.setColumnStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Fishing"))
        self.lblChooseEmulator.setText(_translate("MainWindow", "Chọn giả lập"))
        self.btnConnectEmulator.setText(_translate("MainWindow", "Kết nối"))
        self.txtMinFishSize.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">60</span></p></body></html>"))
        self.lblMinFishSize.setText(_translate("MainWindow", "Kích thước cá min"))
        self.cbFreeMouse.setText(_translate("MainWindow", "Chuột tự do"))
        self.cbShowFish.setText(_translate("MainWindow", "Hiện bóng cá"))
        self.cbFishDetection.setText(_translate("MainWindow", "Lọc bóng cá"))
        self.lblTimeWaitMark.setText(_translate("MainWindow", "Thời gian chờ cá"))
        self.lblTimePullingFish.setText(_translate("MainWindow", "Thời gian kéo cá"))
        self.txtWaitingFishTime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">60</span></p></body></html>"))
        self.txtPullingFishTime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">60</span></p></body></html>"))
        self.lblRodPosition.setText(_translate("MainWindow", "Vị trí cần câu"))
        self.txtFishingRodPosition.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">60</span></p></body></html>"))
        self.lblShowFish.setText(_translate("MainWindow", "Image"))
        self.btnGetMarkPosition.setText(_translate("MainWindow", "Lấy tọa độ chấm than"))
        self.btnGetBobberPosition.setText(_translate("MainWindow", "Lấy tọa độ phao câu"))
        self.btnStartFishing.setText(_translate("MainWindow", "START"))
        self.btnStopFishing.setText(_translate("MainWindow", "STOP"))
        self.lblStatus.setText(_translate("MainWindow", "TextLabel"))
        self.lblNumFishing.setText(_translate("MainWindow", "Lượt câu"))
        self.lblNumFish.setText(_translate("MainWindow", "Vật phẩm"))
        self.lblTime.setText(_translate("MainWindow", "Thời gian"))

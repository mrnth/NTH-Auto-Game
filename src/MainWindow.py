import time
import threading
import subprocess
import base64
import urllib.request
import sys

import cv2
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QUrl, QSize, QCoreApplication, pyqtSignal
from PyQt5 import QtGui, QtCore

from ui.UiMainWindow import Ui_MainWindow
from src.config import Config
from src.AutoFishing import AutoFishing
from src.common import *
from src.ReadMemory import *
import logging as log


class MainWindow(QMainWindow):
    mSignalUpdate = pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.mConfig = Config()
        self.mAutoFishing = AutoFishing()
        self.mReadMemory = ReadMemory()

        self.mLogo = None
        self.mAutoFishingThread = None
        self.mTimer = QTimer()
        self.mCheckExpand = False

        self.mSignalUpdate.connect(self.SlotUpdateNotice)
        threading.Thread(target=self.SlotCheckUpdate).start()

        self.SlotOpenApp()

    def __del__(self):
        self.mAutoFishing.mAutoFishRunning = False
        self.mAutoFishing.mCheckMouseRunning = False

    def SlotCheckUpdate(self):
        log.info('Checking update')
        listCurrentVersion = self.mConfig.mVersion.split('.')
        intCurrentVersion = int(listCurrentVersion[0] + listCurrentVersion[1] + listCurrentVersion[2])
        try:
            response = urllib.request.urlopen(
                "https://drive.google.com/uc?export=download&id=1JMo9ghFQWGcjlOkSMGEyemC7OJt_MSfy")
        except (ValueError, Exception):
            log.info('Check update fail')
            return
        data = response.read()
        strNewVersion = str(data).split("'")[1]
        listNewVersion = strNewVersion.split('.')
        intNewVersion = int(listNewVersion[0] + listNewVersion[1] + listNewVersion[2])
        if intNewVersion > intCurrentVersion:
            log.info(f'New update {strNewVersion}')
            self.mSignalUpdate.emit(strNewVersion)
        else:
            log.info('No update')

    def SlotUpdateNotice(self, strNewVersion: str):
        mMsgBox = QMessageBox()
        mMsgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        reply = mMsgBox.question(self, 'Th??ng b??o',
                                 f"Phi??n b???n ??ang s??? d???ng  {self.mConfig.mVersion}\n???? c?? phi??n b???n m???i {strNewVersion}\nH??y ch???n\nYes ????? t???i phi??n b???n m???i\nNo ????? s??? d???ng phi??n b???n hi???n t???i?",
                                 mMsgBox.Yes | mMsgBox.No, mMsgBox.No)
        if reply == mMsgBox.Yes:
            self.SlotOpenMediafire()
            sys.exit()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Th??ng b??o', "Ch???c ch???n tho??t?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mAutoFishing.mAutoFishRunning = False
            self.mAutoFishing.mCheckMouseRunning = False
            event.accept()
        else:
            event.ignore()

    def Show(self):
        self.show()

    def SlotOpenApp(self):
        log.info('Opening App')
        self.setMaximumSize(QtCore.QSize(350, 540))
        self.mLogo = self.Base64ToQImage(self.mConfig.mAppLogo)

        self.setWindowTitle(QCoreApplication.translate("MainWindow", self.mConfig.mAppTitle))

        # Hien thi cac du lieu da luu trong config.ini
        self.uic.txtEmulatorName.setText(self.mConfig.mWindowName)
        self.uic.txtEmulatorName.setAlignment(Qt.AlignLeft)

        self.uic.txtFishingRodPosition.setText(str(self.mConfig.mFishingRodIndex))
        self.uic.txtFishingRodPosition.setAlignment(Qt.AlignCenter)

        self.uic.txtFishingPeriod.setText(str(self.mConfig.mFishingPeriod))
        self.uic.txtFishingPeriod.setAlignment(Qt.AlignCenter)

        self.uic.txtWaitingFishTime.setText(str(self.mConfig.mWaitingFishTime))
        self.uic.txtWaitingFishTime.setAlignment(Qt.AlignCenter)

        self.uic.txtWaitingMarkTime.setText(str(self.mConfig.mWaitingMarkTime))
        self.uic.txtWaitingMarkTime.setAlignment(Qt.AlignCenter)

        self.uic.txtMinFishSize.setText(str(self.mConfig.mFishSize))
        self.uic.txtMinFishSize.setAlignment(Qt.AlignCenter)

        self.uic.txtShutdownTime.setText("0")
        self.uic.txtShutdownTime.setAlignment(Qt.AlignCenter)

        self.uic.txtDelayTime.setText(str(self.mConfig.mDelayTime))
        self.uic.txtDelayTime.setAlignment(Qt.AlignCenter)

        self.SlotShowNumFish()
        self.ShowListEmulatorSize()
        self.uic.listAdbAddress.addItem(self.mConfig.mAdbAddress)
        self.uic.listPID.addItem('None')

        self.uic.cbKeyBoard.setChecked(self.mConfig.mSendKeyCheck)
        self.uic.cbFishDetection.setChecked(self.mConfig.mFishDetectionCheck)
        self.uic.cbShutdownPC.setChecked(False)

        # Show logo
        self.uic.lblShowFish.setPixmap(QtGui.QPixmap.fromImage(self.mLogo).scaled(200, 200))
        self.uic.btnYoutube.setIcon(QtGui.QIcon(self.mConfig.mYoutubeImgPath))
        self.uic.btnYoutube.setIconSize(QSize(40, 40))
        self.uic.btnYoutube.setFlat(True)
        self.uic.btnFacebook.setIcon(QtGui.QIcon(self.mConfig.mFacebookImgPath))
        self.uic.btnFacebook.setIconSize(QSize(40, 40))
        self.uic.btnFacebook.setFlat(True)
        self.uic.btnHelp.setIcon(QtGui.QIcon(self.mConfig.mHelpIconPath))
        self.uic.btnHelp.setIconSize(QSize(38, 38))
        self.uic.btnHelp.setFlat(True)
        self.uic.btnExpand.setIcon(QtGui.QIcon(self.mConfig.mMoreIconPath))
        self.uic.btnExpand.setIconSize(QSize(28, 28))
        self.uic.btnExpand.setFlat(True)

        # Show time
        self.uic.lcdTime.setNumDigits(8)
        self.uic.lcdTime.setSegmentStyle(2)
        self.uic.lcdTime.display('00:00:00')
        self.uic.lcdNumFish.setSegmentStyle(2)
        self.uic.lcdNumFishing.setSegmentStyle(2)
        self.uic.lcdRodX.setSegmentStyle(2)
        self.uic.lcdRodY.setSegmentStyle(2)
        self.uic.lcdMarkX.setSegmentStyle(2)
        self.uic.lcdMarkY.setSegmentStyle(2)

        # Show Fish txt
        self.uic.txtVioletFish.setText(str(self.mAutoFishing.mVioletFish))
        self.uic.txtVioletFish.setDisabled(True)
        self.uic.txtVioletFish.setStyleSheet(
            f'border: 0px; background-color: rgba({self.mConfig.mVioletColorRGB[0]},'
            f' {self.mConfig.mVioletColorRGB[1]}, {self.mConfig.mVioletColorRGB[2]}, 255);')
        self.uic.txtVioletFish.setAlignment(Qt.AlignCenter)

        self.uic.txtBlueFish.setText(str(self.mAutoFishing.mBlueFish))
        self.uic.txtBlueFish.setDisabled(True)
        self.uic.txtBlueFish.setStyleSheet(
            f'border: 0px; background-color: rgba({self.mConfig.mBlueColorRGB[0]},'
            f' {self.mConfig.mBlueColorRGB[1]}, {self.mConfig.mBlueColorRGB[2]}, 255);')
        self.uic.txtBlueFish.setAlignment(Qt.AlignCenter)

        self.uic.txtGreenFish.setText(str(self.mAutoFishing.mGreenFish))
        self.uic.txtGreenFish.setDisabled(True)
        self.uic.txtGreenFish.setStyleSheet(
            f'border: 0px; background-color: rgba({self.mConfig.mGreenColorRGB[0]},'
            f' {self.mConfig.mGreenColorRGB[1]}, {self.mConfig.mGreenColorRGB[2]}, 255);')
        self.uic.txtGreenFish.setAlignment(Qt.AlignCenter)

        self.uic.txtGrayFish.setText(str(self.mAutoFishing.mGrayFish))
        self.uic.txtGrayFish.setDisabled(True)
        self.uic.txtGrayFish.setStyleSheet(
            f'border: 0px; background-color: rgba({self.mConfig.mGrayColorRGB[0]},'
            f' {self.mConfig.mGrayColorRGB[1]}, {self.mConfig.mGrayColorRGB[2]}, 255);')
        self.uic.txtGrayFish.setAlignment(Qt.AlignCenter)

        self.uic.txtOtherFish.setText(str(self.mAutoFishing.mOtherFish))
        self.uic.txtOtherFish.setDisabled(True)
        self.uic.txtOtherFish.setStyleSheet(
            f'border: 0px; background-color: rgba({self.mConfig.mYellowColorRGB[0]},'
            f' {self.mConfig.mYellowColorRGB[1]}, {self.mConfig.mYellowColorRGB[2]}, 255);')
        self.uic.txtOtherFish.setAlignment(Qt.AlignCenter)

        self.uic.txtBrokenWire.setText(str(self.mAutoFishing.mBrokenWire))
        self.uic.txtBrokenWire.setDisabled(True)
        self.uic.txtBrokenWire.setStyleSheet(
            f'border: 0px; background-color: rgba({self.mConfig.mWhiteColorRGB[0]},'
            f' {self.mConfig.mWhiteColorRGB[1]}, {self.mConfig.mWhiteColorRGB[2]}, 255);')
        self.uic.txtBrokenWire.setAlignment(Qt.AlignCenter)

        # Connect btn
        self.uic.btnConnectWindowTitle.clicked.connect(self.OnClickConnectWindowTitle)
        self.uic.btnStartFishing.clicked.connect(self.OnClickStart)
        self.uic.btnPauseFishing.clicked.connect(self.OnClickPause)
        self.uic.btnGetMarkPosition.clicked.connect(self.OnClickGetMarkPosition)
        self.uic.btnGetBobberPosition.clicked.connect(self.OnClickGetBobberPosition)
        self.uic.btnConnectAdb.clicked.connect(self.OnClickConnectAdbAddress)
        self.uic.btnFacebook.clicked.connect(self.SlotOpenFacebook)
        self.uic.btnYoutube.clicked.connect(self.SlotOpenYoutube)
        self.uic.btnHelp.clicked.connect(self.OnClickHelp)
        self.uic.btnExpand.clicked.connect(self.OnClickExpand)
        self.uic.btnMarkScanner.clicked.connect(self.OnClickMarkScanner)
        self.uic.btnFishScanner.clicked.connect(self.OnClickFishScanner)
        self.uic.btnFilterDescription.clicked.connect(self.OnClickFilterDescription)
        self.uic.btnClearFish.clicked.connect(self.OnLickClear)
        self.uic.btnFishLevelList.clicked.connect(self.OnClickFishLevelList)

        # Connect from auto fishing class to def in this class
        self.mAutoFishing.mSignalSetPixelPos.connect(self.SlotShowMarkPosition)
        self.mAutoFishing.mSignalSetFishingBobberPos.connect(self.SlotShowBobberPosition)
        self.mAutoFishing.mSignalUpdateFishingNum.connect(self.SlotShowFishingNum)
        self.mAutoFishing.mSignalUpdateFishNum.connect(self.SlotShowNumFish)
        self.mAutoFishing.mSignalUpdateImageShow.connect(self.SlotShowImage)
        self.mAutoFishing.mSignalMessage.connect(self.SlotShowMsgBox)
        self.mAutoFishing.mSignalUpdateStatus.connect(self.SlotShowStatus)
        self.mAutoFishing.mSignalUpdateMarkAddress.connect(self.SlotUpdateMarkAddress)
        self.mAutoFishing.mSignalUpdateFishAddress.connect(self.SlotUpdateFishAddress)
        self.mAutoFishing.mSignalUpdateFishID.connect(self.SlotShowFishID)
        self.mAutoFishing.mSignalUpdatePID.connect(self.SlotUpdatePID)

        # Connect timer to slot
        self.mTimer.timeout.connect(self.SlotShowTime)
        self.mTimer.timeout.connect(self.SlotCheckThread)
        self.mTimer.timeout.connect(self.ShowShutdownPCTime)

        # Disable btnPauseFishing
        self.uic.btnPauseFishing.setDisabled(True)

        # Show Author
        self.SlotShowStatus(self.mConfig.mLicenseText)

        # Show status bar
        self.uic.statusbar.showMessage("Ph???n m???m mi???n ph??. T??c gi??? NTH Auto Game")

        # self.uic.cbFilterMode1.hide()
        # self.uic.cbFilterMode2.hide()
        # self.uic.cbFilterMode3.hide()
        # self.uic.cbFilterMode4.hide()
        # self.uic.cbFilterMode5.hide()
        # self.uic.cbFilterBaba.hide()
        # self.uic.cbFilterKyNhong.hide()
        # self.uic.cbFilter15Fish.hide()
        # self.uic.labelFilterMode.hide()
        # self.uic.labelFishTypeKeep.hide()
        # self.uic.lblFilterBaseAddress.hide()
        # self.uic.btnFishScanner.hide()
        # self.uic.btnFilterDescription.hide()
        # self.uic.lcdFishID.hide()
        # self.uic.lblFishID.hide()

    def OnClickConnectWindowTitle(self):
        self.uic.lblControlBaseAddress.setText("Ch??a qu??t ch???m than")
        self.uic.lblFilterBaseAddress.setText("Ch??a qu??t b??ng c??")
        self.mConfig.SetWindowName(self.uic.txtEmulatorName.toPlainText())
        self.mConfig.SetEmulatorSize(self.uic.listEmulatorSize.currentIndex())

        if self.mAutoFishing.CheckRegionEmulator() is True:
            self.SlotShowStatus(f"K???t n???i th??nh c??ng gi??? l???p {self.mAutoFishing.mEmulatorType}\n"
                                f"{self.mAutoFishing.mEmulatorBox}")
            if self.mAutoFishing.mEmulatorType == NOX:
                self.uic.cbKeyBoard.setDisabled(True)
                self.uic.cbKeyBoard.setChecked(True)
            else:
                self.uic.cbKeyBoard.setDisabled(False)
        else:
            self.uic.listAdbAddress.clear()
            self.uic.listAdbAddress.addItem("None")
            return

        if self.mAutoFishing.AdbServerConnect() is False:
            self.UpdateListAdbAddress()
            self.SaveConfig()
            return

        self.UpdateListAdbAddress()
        if self.SaveConfig() is False:
            return
        self.SlotShowMsgBox(
            f"K???t n???i th??nh c??ng gi??? l???p {self.mAutoFishing.mEmulatorType}\nCh???n ?????a ch??? ADB c???a gi??? l???p v?? k???t n???i")
        if len(self.mAutoFishing.mListAdbDevicesSerial) > 4:
            self.SlotShowMsgBox("C??y thu?? nhi???u t??i kho???n th??? bro\n"
                                "Ki???m ???????c nhi???u th?? donate ???ng h??? t??c gi??? c?? ?????ng l???c update nh??!\n"
                                "Thanks!")
        return

    def OnClickMarkScanner(self):
        self.uic.lblControlBaseAddress.setText("Ch??a qu??t ch???m than")
        threading.Thread(target=self.mAutoFishing.MarkScanner).start()

    def OnClickFishScanner(self):
        self.uic.lblFilterBaseAddress.setText("Ch??a qu??t b??ng c??")
        threading.Thread(target=self.mAutoFishing.FishScanner).start()

    def SlotUpdateMarkAddress(self):
        self.uic.lblControlBaseAddress.setText(self.mReadMemory.hexControlBaseAddress)
        if self.mReadMemory.hexControlBaseAddress == "ERROR":
            self.uic.lblControlBaseAddress.setText("Ch???m than l???i")
        elif self.mReadMemory.hexControlBaseAddress == "":
            self.uic.lblControlBaseAddress.setText("Ch??a qu??t ch???m than")
        else:
            self.uic.lblControlBaseAddress.setText("Ch???m than OK")

    def SlotUpdateFishAddress(self):
        if self.mReadMemory.hexFilterBaseAddress == "ERROR":
            self.uic.lblFilterBaseAddress.setText("B??ng c?? l???i")
        elif self.mReadMemory.hexFilterBaseAddress == "":
            self.uic.lblFilterBaseAddress.setText("Ch??a qu??t b??ng c??")
        else:
            self.uic.lblFilterBaseAddress.setText("B??ng c?? OK")

    def SlotUpdatePID(self):
        self.uic.listPID.clear()
        if not self.mReadMemory.mListPID:
            self.uic.listPID.addItem('None')
            return
        for mPID in self.mReadMemory.mListPID:
            self.uic.listPID.addItem(str(mPID))
        self.uic.listPID.setCurrentIndex(0)

    def OnClickConnectAdbAddress(self):
        if self.uic.listAdbAddress.currentText() == "None":
            self.SlotShowMsgBox("X??c nh???n l???i c???a s??? gi??? l???p ????? t??m ?????a ch??? Adb")
            return False
        self.mConfig.SetAdbAddress(self.uic.listAdbAddress.currentText())
        if self.mAutoFishing.AdbDeviceConnect() is True:
            self.SlotShowStatus("K???t n???i ?????a ch??? Adb gi??? l???p th??nh c??ng")
            self.SlotShowMsgBox("K???t n???i ?????a ch??? Adb gi??? l???p th??nh c??ng")
            return True
        else:
            self.SlotShowMsgBox("K???t n???i ?????a ch??? Adb gi??? l???p th???t b???i\n Restart l???i gi??? l???p")
            return False

    def OnClickStart(self):
        log.info('********************************************************')
        # Apply and save all config
        if self.SaveConfig() is False:
            return
        log.info(f'mWindowName = {self.mConfig.mWindowName}')
        log.info(f'mSendKeyCheck = {self.mConfig.mSendKeyCheck}')
        log.info(f'mSendKeyCheck = {self.mConfig.mFishingPeriod}')
        log.info(f'mPullingFishTime = {self.mConfig.mWaitingFishTime}')
        log.info(f'mWaitingFishTime = {self.mConfig.mWaitingMarkTime}')
        log.info(f'mFishDetectionCheck = {self.mConfig.mFishDetectionCheck}')
        log.info(f'mFishingRodIndex = {self.mConfig.mFishingRodIndex}')
        log.info(f'mDelayTime = {self.mConfig.mDelayTime}')

        # Hide button
        self.uic.btnConnectWindowTitle.setDisabled(True)
        self.uic.btnConnectAdb.setDisabled(True)
        self.uic.btnStartFishing.setDisabled(True)
        self.uic.btnGetMarkPosition.setDisabled(True)
        self.uic.btnGetBobberPosition.setDisabled(True)
        self.uic.btnFishScanner.setDisabled(True)
        self.uic.btnMarkScanner.setDisabled(True)
        self.uic.btnClearFish.setDisabled(True)

        # Hide text box
        self.uic.txtFishingPeriod.setDisabled(True)
        self.uic.txtWaitingFishTime.setDisabled(True)
        self.uic.txtWaitingMarkTime.setDisabled(True)
        self.uic.txtFishingRodPosition.setDisabled(True)
        self.uic.txtMinFishSize.setDisabled(True)
        self.uic.txtShutdownTime.setDisabled(True)
        self.uic.txtEmulatorName.setDisabled(True)
        self.uic.txtDelayTime.setDisabled(True)

        # Hide list box
        self.uic.listAdbAddress.setDisabled(True)
        self.uic.listEmulatorSize.setDisabled(True)
        self.uic.listPID.setDisabled(True)

        # Hide check box
        self.uic.cbShutdownPC.setDisabled(True)
        self.uic.cbFishDetection.setDisabled(True)
        self.uic.cbKeyBoard.setDisabled(True)
        self.uic.cbReadMemory.setDisabled(True)
        self.uic.cbFilterMode1.setDisabled(True)
        self.uic.cbFilterMode2.setDisabled(True)
        self.uic.cbFilterMode3.setDisabled(True)
        self.uic.cbFilterMode4.setDisabled(True)
        self.uic.cbFilterMode5.setDisabled(True)
        self.uic.cbFilterBaba.setDisabled(True)
        self.uic.cbFilterKyNhong.setDisabled(True)
        self.uic.cbFilter15Fish.setDisabled(True)

        # All thread flag = False
        self.mAutoFishing.mCheckMouseRunning = False
        self.mAutoFishing.mAutoFishRunning = False

        # Define thread start fishing
        if self.mConfig.mReadMemoryCheck is True:
            self.mAutoFishingThread = threading.Thread(name="ReadMemoryAutoFishing",
                                                       target=self.mAutoFishing.RMAutoFishing)
        else:
            self.mAutoFishingThread = threading.Thread(name="ComputerVisionAutoFishing",
                                                       target=self.mAutoFishing.CVAutoFishing)

        # Set time start fishing
        self.mAutoFishing.mStartTime = time.time()

        self.mTimer.start(200)
        # Start thread auto fishing
        self.mAutoFishingThread.start()

        # Check thread is not live, return
        if self.mAutoFishingThread.is_alive() is False:
            return

        # Disable Pause button
        self.uic.btnPauseFishing.setDisabled(False)

    def OnClickPause(self):
        log.info('****************************************************************************')
        # Disable Pause button
        self.uic.btnPauseFishing.setDisabled(True)

        # Pause all thread flag
        self.mAutoFishing.mCheckMouseRunning = False
        self.mAutoFishing.mAutoFishRunning = False

        # Show status notice doing Pause
        self.SlotShowStatus("")

    def OnClickGetMarkPosition(self):
        self.mAutoFishing.mCheckMouseRunning = False
        threading.Thread(name="SetMarkPosition", target=self.mAutoFishing.SetMarkPos).start()

    @staticmethod
    def OnClickFilterDescription():
        mMsgBox = QMessageBox()
        mMsgBox.setText("Ch??? ????? th?????ng d??ng:\n"
                        "- Mode 1. Tr???ng VM tr??? l??n. B??? qua m?? s??? 1, 7, 13\n"
                        "- Mode 2. Xanh tr??? l??n. B??? qua m?? s??? 1, 3, 7, 9, 10, 13, 15\t\t\n"
                        "- Mode 3. B??ng 3 VM tr??? l??n. B??? qua m?? s??? d?????i 16\n"
                        "- Mode 4. B??ng 4 tr??? l??n. B??? qua m?? s??? d?????i 20\n"
                        "- Mode 5. B??ng 5 tr??? l??n. B??? qua m?? s??? d?????i 25\n"
                        "\nGi??? l???i c??c lo???i c??:\n"
                        "- K??? Nh??ng. Mini. Gi??? l???i m?? s??? 4, 6\n"
                        "- Ba ba. Ch??p v??ng. Gi??? l???i m?? s??? 10, 12\n"
                        "- Xanh-Home.Camp. Gi??? l???i m?? s??? 15")
        mMsgBox.setWindowTitle("M?? t??? c??c ch??? ????? l???c b??ng b???ng ?????c data game")
        mMsgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        mMsgBox.exec()

    def OnClickFishLevelList(self):
        img = cv2.imread(self.mConfig.mFishLevelImgPath)
        cv2.namedWindow('Danh sach ma so ca', cv2.WINDOW_NORMAL)
        cv2.imshow('Danh sach ma so ca', img)

    def ShowListEmulatorSize(self):
        for mSize in self.mConfig.mStrListEmulatorSize:
            self.uic.listEmulatorSize.addItem(mSize)
        self.uic.listEmulatorSize.setCurrentIndex(self.mConfig.mEmulatorSizeId)

    def ShowShutdownPCTime(self):
        if self.mConfig.mShutdownCheckBox is False:
            return
        if self.mAutoFishing.mAutoFishRunning is False:
            return
        mCountDownTime = (self.mConfig.mShutdownTime * 60 - (time.time() - self.mAutoFishing.mStartTime)) / 60
        self.uic.txtShutdownTime.setText(str(int(mCountDownTime) + 1))
        self.uic.txtShutdownTime.setAlignment(Qt.AlignCenter)
        if mCountDownTime < 0:
            log.info(f'Shutting down PC')
            subprocess.call(["shutdown", "/s"], creationflags=0x08000000)
            self.mAutoFishing.mCheckMouseRunning = False
            self.mAutoFishing.mAutoFishRunning = False

    def SlotShowMarkPosition(self, x: int, y: int):
        self.uic.lcdMarkX.display(str(x))
        self.uic.lcdMarkY.display(y)

    def SlotShowFishingNum(self):
        self.uic.lcdNumFishing.display(str(self.mAutoFishing.mFishingNum))

    def SlotShowNumFish(self):
        self.uic.lcdNumFish.display(str(self.mAutoFishing.mAllFish))
        self.uic.txtVioletFish.setText(str(self.mAutoFishing.mVioletFish))
        self.uic.txtVioletFish.setAlignment(Qt.AlignCenter)
        self.uic.txtBlueFish.setText(str(self.mAutoFishing.mBlueFish))
        self.uic.txtBlueFish.setAlignment(Qt.AlignCenter)
        self.uic.txtGreenFish.setText(str(self.mAutoFishing.mGreenFish))
        self.uic.txtGreenFish.setAlignment(Qt.AlignCenter)
        self.uic.txtGrayFish.setText(str(self.mAutoFishing.mGrayFish))
        self.uic.txtGrayFish.setAlignment(Qt.AlignCenter)
        self.uic.txtOtherFish.setText(str(self.mAutoFishing.mOtherFish))
        self.uic.txtOtherFish.setAlignment(Qt.AlignCenter)
        self.uic.txtBrokenWire.setText(str(self.mAutoFishing.mBrokenWire))
        self.uic.txtBrokenWire.setAlignment(Qt.AlignCenter)

    def OnLickClear(self):
        mMsgBox = QMessageBox()
        mMsgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        reply = mMsgBox.question(self, 'C???nh b??o',
                                 f"B???n mu???n x??a h???t d??? li???u th???ng k?? hi???n t???i?\n",
                                 mMsgBox.Yes | mMsgBox.No, mMsgBox.No)
        if reply == mMsgBox.Yes:
            self.mAutoFishing.mFishingNum = 0
            self.mAutoFishing.mAllFish = 0
            self.mAutoFishing.mVioletFish = 0
            self.mAutoFishing.mBlueFish = 0
            self.mAutoFishing.mGreenFish = 0
            self.mAutoFishing.mGrayFish = 0
            self.mAutoFishing.mOtherFish = 0
            self.mAutoFishing.mBrokenWire = 0
            self.uic.lcdTime.display('00:00:00')
            self.mAutoFishing.mSaveTime = 0
            self.mAutoFishing.mStartTime = time.time()
            self.SlotShowTime()
            self.SlotShowNumFish()
            self.SlotShowFishingNum()

    def OnClickGetBobberPosition(self):
        self.mAutoFishing.mCheckMouseRunning = False
        time.sleep(0.1)
        threading.Thread(name="SetBobberPosition", target=self.mAutoFishing.SetFishingBobberPos).start()

    def SlotShowBobberPosition(self, x: int, y: int):
        self.uic.lcdRodX.display(str(x))
        self.uic.lcdRodY.display(y)

    def SlotShowImage(self):
        mMatImage = self.mAutoFishing.mImageShow.copy()
        width = mMatImage.shape[1]
        height = mMatImage.shape[0]
        if width > height:
            height = int(height * 200 / width)
            width = 200
        else:
            width = int(height * 200 / width)
            height = 200

        mMatImage = cv2.resize(mMatImage, (width, height), interpolation=cv2.INTER_AREA)
        mQImage = QtGui.QImage(mMatImage.data, width, height, QtGui.QImage.Format_RGB888).rgbSwapped()
        mQPixmap = QtGui.QPixmap.fromImage(mQImage).scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.uic.lblShowFish.setPixmap(mQPixmap)

    def SlotShowTime(self):
        mShowTime = self.mAutoFishing.mSaveTime + int(time.time() - self.mAutoFishing.mStartTime)
        h = mShowTime // 3600
        m = (mShowTime - h * 3600) // 60
        s = ((mShowTime - h * 3600) - m * 60)
        str_h = str(h)
        str_m = str(m)
        str_s = str(s)
        if h < 10:
            str_h = f'0{h}'
        if m < 10:
            str_m = f'0{m}'
        if s < 10:
            str_s = f'0{s}'
        self.uic.lcdTime.display(f'{str_h}:{str_m}:{str_s}')

    def SlotShowFishID(self, mFishID: int):
        self.uic.lcdFishID.display(f'{mFishID}')

    def SlotShowStatus(self, mText: str):
        if mText == self.mConfig.mLicenseText:
            self.uic.lblStatus.setText(self.mConfig.mLicenseText)
        elif self.uic.btnStartFishing.isEnabled() is False and self.uic.btnPauseFishing.isEnabled() is False:
            self.uic.lblStatus.setText(self.mConfig.mWaitStatus)
        else:
            self.uic.lblStatus.setText(mText)
        self.uic.lblStatus.setAlignment(Qt.AlignLeft)
        self.uic.lblStatus.setAlignment(Qt.AlignVCenter)
        self.uic.lblStatus.setWordWrap(True)

    # Watchdog thread auto fishing
    def SlotCheckThread(self):
        if self.mAutoFishingThread.is_alive() is False:
            log.info(f'Auto Fishing Thread is not alive')
            # Disable thread flag
            self.mAutoFishing.mAutoFishRunning = False

            # Show all button
            self.uic.btnConnectWindowTitle.setDisabled(False)
            self.uic.btnConnectAdb.setDisabled(False)
            self.uic.btnGetMarkPosition.setDisabled(False)
            self.uic.btnGetBobberPosition.setDisabled(False)
            self.uic.btnFishScanner.setDisabled(False)
            self.uic.btnMarkScanner.setDisabled(False)
            self.uic.btnClearFish.setDisabled(False)

            # Show all check box
            self.uic.cbShutdownPC.setDisabled(False)
            self.uic.cbFishDetection.setDisabled(False)
            if self.mAutoFishing.mEmulatorType == MEMU or self.mAutoFishing.mEmulatorType == '':
                self.uic.cbKeyBoard.setDisabled(False)
            self.uic.cbReadMemory.setDisabled(False)
            self.uic.cbFilterMode1.setDisabled(False)
            self.uic.cbFilterMode2.setDisabled(False)
            self.uic.cbFilterMode3.setDisabled(False)
            self.uic.cbFilterMode4.setDisabled(False)
            self.uic.cbFilterMode5.setDisabled(False)
            self.uic.cbFilterBaba.setDisabled(False)
            self.uic.cbFilterKyNhong.setDisabled(False)
            self.uic.cbFilter15Fish.setDisabled(False)

            # Show all text box
            self.uic.txtFishingPeriod.setDisabled(False)
            self.uic.txtWaitingFishTime.setDisabled(False)
            self.uic.txtWaitingMarkTime.setDisabled(False)
            self.uic.txtFishingRodPosition.setDisabled(False)
            self.uic.txtMinFishSize.setDisabled(False)
            self.uic.txtShutdownTime.setDisabled(False)
            self.uic.txtEmulatorName.setDisabled(False)
            self.uic.txtDelayTime.setDisabled(False)

            # show all list
            self.uic.listAdbAddress.setDisabled(False)
            self.uic.listEmulatorSize.setDisabled(False)
            self.uic.listPID.setDisabled(False)

            self.uic.txtShutdownTime.setText(str(self.mConfig.mShutdownTime))
            self.uic.txtShutdownTime.setAlignment(Qt.AlignCenter)
            self.uic.lblShowFish.setPixmap(QtGui.QPixmap.fromImage(self.mLogo).scaled(200, 200))

            self.uic.btnPauseFishing.setDisabled(True)
            self.uic.btnStartFishing.setDisabled(False)

            self.uic.lblStatus.setText(self.mConfig.mLicenseText)

            self.mTimer.stop()
            self.mAutoFishing.mSaveTime += int(time.time() - self.mAutoFishing.mStartTime)

    def SlotOpenFacebook(self):
        QtGui.QDesktopServices.openUrl(QUrl(self.mConfig.mFacebookLink))

    def SlotOpenMediafire(self):
        QtGui.QDesktopServices.openUrl(QUrl(self.mConfig.mMediaFire))

    def SlotOpenYoutube(self):
        QtGui.QDesktopServices.openUrl(QUrl(self.mConfig.mYoutubeLink))

    def OnClickHelp(self):
        QtGui.QDesktopServices.openUrl(QUrl(self.mConfig.mDocumentLink))

    def OnClickExpand(self):
        if self.mCheckExpand is True:
            self.mCheckExpand = False
            self.setMaximumSize(QtCore.QSize(350, 540))
            self.resize(350, 540)
            self.uic.btnExpand.setIcon(QtGui.QIcon(self.mConfig.mMoreIconPath))
            return

        self.mCheckExpand = True
        self.setMaximumSize(QtCore.QSize(480, 540))
        self.resize(480, 540)
        self.uic.btnExpand.setIcon(QtGui.QIcon(self.mConfig.mLessIconPath))

    def SaveConfig(self):
        if (self.uic.txtFishingPeriod.toPlainText()).isnumeric() is False:
            self.SlotShowMsgBox("Chu k??? c??u sai ?????nh d???ng")
            return False

        if (self.uic.txtWaitingFishTime.toPlainText()).isnumeric() is False:
            self.SlotShowMsgBox("Th???i gian ch??? c?? ?????n sai ?????nh d???ng")
            return False

        if (self.uic.txtWaitingMarkTime.toPlainText()).isnumeric() is False:
            self.SlotShowMsgBox("Th???i gian ch??? ch???m than sai ?????nh d???ng")
            return False

        if (self.uic.txtFishingRodPosition.toPlainText()).isnumeric() is False:
            self.SlotShowMsgBox("V??? tr?? c???n c??u c?? sai ?????nh d???ng")
            return False

        if int(self.uic.txtFishingRodPosition.toPlainText()) not in range(1, 7, 1):
            self.SlotShowMsgBox("V??? tr?? c???n c??u ph???i t??? 1 ?????n 6")
            return False

        if (self.uic.txtMinFishSize.toPlainText()).isnumeric() is False:
            self.SlotShowMsgBox("L???c c??? nh??? sai ?????nh d???ng")
            return False

        if self.uic.txtShutdownTime.toPlainText().isnumeric() is False:
            self.SlotShowMsgBox("H???n gi??? t???t PC sai ?????nh d???ng")
            return False

        try:
            mDelayTime = float(self.uic.txtDelayTime.toPlainText())
        except ValueError:
            self.SlotShowMsgBox("????? tr??? thao t??c sai ?????nh d???ng")
            return False

        if mDelayTime < 0.3:
            self.SlotShowMsgBox("????? tr??? thao t??c ph???i cao h??n 0.3 gi??y")
            return False

        self.mConfig.SetWindowName(self.uic.txtEmulatorName.toPlainText())
        self.mConfig.SetShutdownTime(int(self.uic.txtShutdownTime.toPlainText()))
        self.mConfig.SetFishingRod(int(self.uic.txtFishingRodPosition.toPlainText()))
        self.mConfig.SetFishingPeriod(int(self.uic.txtFishingPeriod.toPlainText()))
        self.mConfig.SetWaitingMarkTime(int(self.uic.txtWaitingMarkTime.toPlainText()))
        self.mConfig.SetWaitingFishTime(int(self.uic.txtWaitingFishTime.toPlainText()))
        self.mConfig.SetFishSize(int(self.uic.txtMinFishSize.toPlainText()))

        self.mConfig.SetShutdownCheckBox(self.uic.cbShutdownPC.isChecked())
        self.mConfig.SetSendKey(self.uic.cbKeyBoard.isChecked())
        self.mConfig.SetFishDetection(self.uic.cbFishDetection.isChecked())
        self.mConfig.SetReadMemoryCheck(self.uic.cbReadMemory.isChecked())

        # Sua sau *************************************************************************************
        self.mConfig.mFilterMode1Check = self.uic.cbFilterMode1.isChecked()
        self.mConfig.mFilterMode2Check = self.uic.cbFilterMode2.isChecked()
        self.mConfig.mFilterMode3Check = self.uic.cbFilterMode3.isChecked()
        self.mConfig.mFilterMode4Check = self.uic.cbFilterMode4.isChecked()
        self.mConfig.mFilterMode5Check = self.uic.cbFilterMode5.isChecked()
        if self.mConfig.mFilterMode5Check is True or \
                self.mConfig.mFilterMode4Check is True or \
                self.mConfig.mFilterMode3Check is True or \
                self.mConfig.mFilterMode2Check is True or \
                self.mConfig.mFilterMode1Check is True:
            self.mConfig.mFilterMode0Check = False
        else:
            self.mConfig.mFilterMode0Check = True

        self.mConfig.mListUnIgnoreFish.clear()
        if self.uic.cbFilterKyNhong.isChecked() is True:
            self.mConfig.mListUnIgnoreFish.append(4)
            self.mConfig.mListUnIgnoreFish.append(6)
        if self.uic.cbFilterBaba.isChecked() is True:
            self.mConfig.mListUnIgnoreFish.append(10)
            self.mConfig.mListUnIgnoreFish.append(12)
        if self.uic.cbFilter15Fish.isChecked() is True:
            self.mConfig.mListUnIgnoreFish.append(15)

        self.mConfig.SetDelayTime(mDelayTime)

        if self.mReadMemory.mListPID:
            self.mReadMemory.mProcessID = self.mReadMemory.mListPID[self.uic.listPID.currentIndex()]

        self.mConfig.SaveConfig()
        return True

    def UpdateListAdbAddress(self):
        self.uic.listAdbAddress.clear()
        if len(self.mAutoFishing.mListAdbDevicesSerial) == 0:
            self.uic.listAdbAddress.addItem("None")
        for AdbDevicesSerial in self.mAutoFishing.mListAdbDevicesSerial:
            self.uic.listAdbAddress.addItem(AdbDevicesSerial)

    @staticmethod
    def SlotShowMsgBox(mText: str):
        mMsgBox = QMessageBox()
        mMsgBox.setText(mText)
        mMsgBox.setWindowTitle("Th??ng b??o")
        mMsgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        mMsgBox.exec()

    @staticmethod
    def Base64ToQImage(base64img: str):
        image_64_decode = base64.b64decode(base64img)
        image = QtGui.QImage()
        image.loadFromData(image_64_decode, 'PNG')
        return image

    @staticmethod
    def Base64ToQIcon(base64img: str):
        image_64_decode = base64.b64decode(base64img)
        image = QtGui.QImage()
        image.loadFromData(image_64_decode, 'PNG')
        icon = QtGui.QIcon(QtGui.QPixmap(image))
        return icon

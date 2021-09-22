import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from src.MainWindow import MainWindow
from src.config import Config


def main():
    mConfig = Config()
    mIconPath = mConfig.mIconPath
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(mIconPath))
    main_win = MainWindow()
    main_win.Show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

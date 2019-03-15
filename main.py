#!/usr/bin/python -u
import sys, os
from PyQt5 import QtWidgets
sys.path.insert(0, os.getcwd() +'\\src')

# Main Window Class
from LoggerGraph import LoggerGraphWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoggerGraphWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
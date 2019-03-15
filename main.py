#!/usr/bin/python -u
import sys, os
sys.path.insert(0, os.getcwd() +'\\ui')

from PyQt5 import QtWidgets

import graph_test

from xml_graph import show_graph # import MainWindow


class ExampleApp(QtWidgets.QMainWindow, graph_test.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Init design
        # Slot connecting
        self.pbClear.clicked.connect(self.clear_list)
        self.pbChooseDir.clicked.connect(self.directory_find)
        self.lwFiles.itemDoubleClicked.connect(self.press)
        self.__current_dir = ''

    def clear_list(self):
        self.lwFiles.clear()
    
    def directory_find(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose directory with logs (*xml)")
        if directory:  # if not directory break
            self.__current_dir = directory
            print("__current_dir: " + self.__current_dir)
            for file_name in os.listdir(directory):  # for each file in dir
                self.lwFiles.addItem(file_name)      # added to lwFiles
    
    def press(self, item):
        path = self.__current_dir + '/' + item.text()
        print(path)
        show_graph(path)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
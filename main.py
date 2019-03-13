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

    def clear_list(self):
        self.lwFiles.clear()
    
    def directory_find(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose directory with logs (*xml)")
        if directory:  # if not directory break
            for file_name in os.listdir(directory):  # for each file in dir
                self.lwFiles.addItem(file_name)      # added to lwFiles
    
    def press(self, item):
        print('press item: ' + item.text())
        current_path = os.path.dirname(os.path.realpath(__file__))
        data_path = current_path + '\\data'
        dir_list = os.listdir(data_path)
        path = data_path + '\\' + dir_list[0] + '\\' + item.text()
        print(path)
        show_graph(path)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
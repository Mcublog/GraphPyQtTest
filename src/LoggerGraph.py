import sys, os
from PyQt5 import QtWidgets
sys.path.insert(0, os.getcwd() +'\\ui')
sys.path.insert(0, os.getcwd() +'\\src\\graph')

# Main Window ui
from SelectDialog       import SelectDialogWindow
from SelectJornal       import SelectJornalDialogWindow
import graph_test
from LoggerXmlGraphViewer import (show_acc_graph, show_tph_graph, show_jrnl_graph)


class LoggerGraphWindow(QtWidgets.QMainWindow, graph_test.Ui_MainWindow):
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
        self.clear_list()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose directory with logs (*xml)")
        if directory:  # if not directory break
            self.__current_dir = directory
            print("__current_dir: " + self.__current_dir)
            for file_name in os.listdir(directory):  # for each file in dir
                self.lwFiles.addItem(file_name)      # added to lwFiles

    def press(self, item):
        type = ''
        path = self.__current_dir + '/' + item.text()
        print(path)
        if not os.path.isfile(path):
            return
            
        if 'tph_report' in item.text():
            type = SelectDialogWindow.get_graph_type(self)
            if type:
                show_tph_graph(path, type)
        elif 'acc_report' in item.text():
            show_acc_graph(path)
        elif 'jornal' in item.text():
            type = SelectJornalDialogWindow.get_graph_type(self)
            if type:
                show_jrnl_graph(path, type)

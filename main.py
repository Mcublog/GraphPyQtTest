#!/usr/bin/python -u
import sys, os
sys.path.insert(0, os.getcwd() +'\\ui')
sys.path.insert(0, os.getcwd() +'\\ui\\select_dialog')

from PyQt5 import QtWidgets

# Main Window ui
import graph_test
# Select Dialog
import select_dialog

from xml_graph import show_graph # import MainWindow


class SelectDialog(QtWidgets.QDialog, select_dialog.Ui_SelectDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Init design
        # Slot connecting
        self.rbTemperature.clicked.connect(lambda: self.select('Temperature'))
        self.rbHumidity.clicked.connect(lambda: self.select('Humidity'))
        self.rbPressure.clicked.connect(lambda: self.select('Pressure'))
        self.show()
        self.__state = ''
    
    def select(self, name):
        self.__state = name
        self.close()

    def get_selected(self):
        return self.__state
    
    @staticmethod
    def get_graph_type():
        sel = SelectDialog()
        result = sel.exec_()
        return sel.get_selected()

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
        self.clear_list()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose directory with logs (*xml)")
        if directory:  # if not directory break
            self.__current_dir = directory
            print("__current_dir: " + self.__current_dir)
            for file_name in os.listdir(directory):  # for each file in dir
                self.lwFiles.addItem(file_name)      # added to lwFiles


    def press(self, item):
        print(SelectDialog.get_graph_type())
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
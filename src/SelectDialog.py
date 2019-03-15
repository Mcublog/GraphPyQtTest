import sys, os
from PyQt5 import QtWidgets

sys.path.insert(0, os.getcwd() +'\\ui\\select_dialog')

import select_dialog

class SelectDialogWindow(QtWidgets.QDialog, select_dialog.Ui_SelectDialog):

    def __init__(self, parent_wnd):
        super().__init__(parent_wnd)
        self.setupUi(self)  # Init design
        # Slot connecting
        self.rbTemperature.clicked.connect(lambda: self.select('Temperature'))
        self.rbHumidity.clicked.connect(lambda: self.select('Humidity'))
        self.rbPressure.clicked.connect(lambda: self.select('Pressure'))
        self.show()
        self.__state = 'Temperature'
    
    def select(self, name):
        self.__state = name
        self.close()

    def get_selected(self):
        return self.__state
    
    @staticmethod
    def get_graph_type(parant_wnd):
        sel = SelectDialogWindow(parant_wnd)
        result = sel.exec_()
        return sel.get_selected()
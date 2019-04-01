import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

sys.path.insert(0, os.getcwd() +'\\ui\\select_journal')

import select_journal

class SelectJornalDialogWindow(QtWidgets.QDialog, select_journal.Ui_SelectDialog):

    def __init__(self, parent_wnd):
        super().__init__(parent_wnd)
        self.setupUi(self)  # Init design
        # Slot connecting
        self.rbTemperature.clicked.connect(lambda: self.select('Temperature'))
        self.rbHumidity.clicked.connect(lambda: self.select('Humidity'))
        self.rbPressure.clicked.connect(lambda: self.select('Pressure'))
        self.rbVoltage.clicked.connect(lambda: self.select('Voltage'))
        self.rbAcc.clicked.connect(lambda: self.select('Acc'))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.show()
        self.__state = ''
    
    def select(self, name):
        self.__state = name
        self.close()

    def get_selected(self):
        return self.__state
    
    @staticmethod
    def get_graph_type(parant_wnd):
        sel = SelectJornalDialogWindow(parant_wnd)
        result = sel.exec_()
        return sel.get_selected()
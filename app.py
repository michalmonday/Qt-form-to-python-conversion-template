''' This is example application making use of the ".py" file produced
by the conversion script. '''

import sys
import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import traceback

from qt_worker import Worker
from MainWindow import Ui_MainWindow

def set_row_color(table, row_index, clr):
    for i in range(table.columnCount()):
        table.item(row_index, i).setBackground(clr)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_download.clicked.connect(self.begin_download)
        self.set_item_icon(self.btn_download, 'SP_ArrowDown')
        self.threadpool = QThreadPool()
        self.settings = QSettings('organisation', 'program_name')

    def set_item_icon(self, item, icon_name):
        ''' Icon names: https://www.pythonguis.com/faq/built-in-qicons-pyqt/ 
            For example:
            - SP_BrowserReload 
            - SP_DialogApplyButton   '''
        pixmapi = getattr(QStyle.StandardPixmap, icon_name)
        icon = self.style().standardIcon(pixmapi) 
        item.setIcon(icon)
        return icon

    def browse_output_dir(self):
        dir_ = QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir_:
            dir_ = str(dir_)
            self.line_edit_output_dir.setText(dir_)
            self.settings.setValue('output_dir', dir_)
            self.output_dir = dir_

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


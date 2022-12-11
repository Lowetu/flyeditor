import os

from PySide6.QtCore import QUrl, QRect
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QGridLayout

from ui.main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.setWindowTitle(u"Fly Editor--fly with you idea")
        self.browser = ui.index_web_view
        self.setGeometry(5,30,400,400)
        url = os.getcwd()+'/front/html/index.html'

        self.file_list = ui.file_list
        self.directory_tree = ui.directory_tree
        self.btn_twoCol = ui.btn_two_col
        self.btn_threeCol = ui.btn_three_col
        self.btn_fullScreen = ui.btn_fullscreen
        self.gridLayout = ui.gridLayout
        self.btn_twoCol.clicked.connect(self.show_two_col)


        self.browser.load(QUrl.fromLocalFile(url))

        # self.setCentralWidget(self.browser)

    def show_two_col(self):
        self.btn_twoCol.hide()
        self.btn_fullScreen.hide()
        # self.browser.hide()
        self.gridLayout.removeWidget(self.file_list)

        self.gridLayout.setColumnStretch(0, 20)
        self.gridLayout.setColumnStretch(1, 200)
        self.gridLayout.setColumnMinimumWidth(0,20)
        self.gridLayout.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.gridLayout.addWidget(self.directory_tree,1,0,1,1)
        self.gridLayout.addWidget(self.browser,1,1,1,1)
        #self.browser.setGeometry(0, 0, self.width(), self.height())




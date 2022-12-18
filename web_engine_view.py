import os

from PySide6.QtCore import QUrl, QRect
from PySide6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QGridLayout, QApplication

from ui.main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(u"Fly Editor--fly with you idea")
        self.browser = self.ui.index_web_view
        self.full_screen_flag = False
        self.setGeometry(5,30,400,400)
        self.url = os.getcwd()+'/front/html/index.html'
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.resize(self.screen.width(),self.screen.height())
        self.file_list = self.ui.file_list  # 文件列表栏
        self.directory_tree = self.ui.directory_tree  # 文件夹列表栏
        self.btn_twoCol = self.ui.btn_two_col
        self.btn_threeCol = self.ui.btn_three_col
        self.btn_threeCol.hide()
        self.btn_fullScreen = self.ui.btn_fullscreen
        self.directory_tree_test()

        # 点击按钮信号槽
        # # 点击两栏按钮
        self.btn_twoCol.clicked.connect(self.show_two_col)
        # # 点击三栏按钮
        self.btn_threeCol.clicked.connect(self.show_three_col)
        # # 点击全屏
        self.btn_fullScreen.clicked.connect(self.show_full_screen)

        self.browser.load(QUrl.fromLocalFile(self.url))

        # self.browser.resize(self.width(), self.height())

    def show_two_col(self):
        """
        显示两栏：文件夹和编辑器
        """
        self.file_list.hide()
        self.btn_twoCol.hide()
        # self.btn_fullScreen.show()
        self.directory_tree.show()
        self.btn_threeCol.show()
        self.browser.resize(self.width(),self.height())
        self.browser.load(QUrl.fromLocalFile(self.url))

        # self.browser.setGeometry(0, 0, self.screen.width(),self.screen.height())

    def show_three_col(self):
        """
        显示三栏，文件夹，文件列表和编辑器
        :return:
        """
        self.btn_twoCol.show()
        self.btn_fullScreen.show()
        self.file_list.show()
        self.directory_tree.show()
        self.btn_threeCol.hide()
        # self.browser.setGeometry(0, 0, self.screen.width(), self.screen.height())
        self.browser.resize(self.width(),self.height())
        self.browser.load(QUrl.fromLocalFile(self.url))


    def show_full_screen(self):
        if not self.full_screen_flag:
            self.btn_twoCol.hide()
            self.btn_threeCol.hide()
            self.btn_fullScreen.setText("退出全屏")
            self.btn_fullScreen.show()
            self.file_list.hide()
            self.directory_tree.hide()
            self.full_screen_flag = True
        else:
            self.btn_fullScreen.setText("全屏")

            self.show_three_col()
            self.full_screen_flag = False
            self.btn_threeCol.show()
        self.browser.resize(self.width(),self.height())
        self.browser.load(QUrl.fromLocalFile(self.url))




    def directory_tree_test(self):
        model = QStandardItemModel(self.directory_tree)
        model.setHorizontalHeaderLabels(["笔记目录"])
        item_directory_1 = QStandardItem("文件夹1")
        model.appendRow(item_directory_1)
        item_file_1 = QStandardItem("文件1")
        item_file_2 = QStandardItem("文件2")
        item_directory_1.appendRow(item_file_1)
        item_directory_1.appendRow(item_file_2)
        self.directory_tree.setModel(model)







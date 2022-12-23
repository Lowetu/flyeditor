import os
import pathlib
import time

from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QResizeEvent

from ui.main import Ui_MainWindow

MY_MD = None


class MainWindow(QMainWindow):
    md = None

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(u"Fly Editor--fly with you idea")
        self.browser = self.ui.index_web_view
        self.full_screen_flag = False
        # self.setGeometry(5, 30, 400, 400)
        self.maximumSize()
        self.url = os.getcwd() + '/front/html/index.html'
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.resize(self.screen.width(), self.screen.height())
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
        self.init_file()

    def init_file(self):
        """暂存文件初始化"""
        if os.path.exists('temp'):
            os.remove('temp')

    def show_two_col(self):
        """
        显示两栏：文件夹和编辑器
        """
        self.file_list.hide()
        self.btn_twoCol.hide()
        self.directory_tree.show()
        self.btn_threeCol.show()

        self.browser.setZoomFactor(1.3)

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

        self.browser.setZoomFactor(1.0)

    def run_js_get_content(self, content_type):
        """运行js，获取markdown内容"""
        if content_type == "md":
            return '''contentEditor.getMarkdown();'''
        elif content_type == "html":
            return '''contentEditor.getHTML();'''

    def js_callback(self, res=None):
        # self.browser.page().runJavaScript(
        #     f'''alert("{res}")''')
        print(res)

    def show_full_screen(self):
        """
        全屏显示
        :return:
        """

        if not self.full_screen_flag:
            self.btn_twoCol.hide()
            self.btn_threeCol.hide()
            self.btn_fullScreen.setText("退出全屏")
            self.btn_fullScreen.show()
            self.file_list.hide()
            self.directory_tree.hide()
            self.full_screen_flag = True

            self.browser.setZoomFactor(1.7)
        else:
            self.btn_fullScreen.setText("全屏")

            self.show_three_col()
            self.full_screen_flag = False
            self.browser.setZoomFactor(1.0)

    def directory_tree_test(self):
        """
        测试目录树
        :return:
        """
        model = QStandardItemModel(self.directory_tree)
        model.setHorizontalHeaderLabels(["笔记目录"])
        item_directory_1 = QStandardItem("文件夹1")
        model.appendRow(item_directory_1)
        item_file_1 = QStandardItem("文件1")
        item_file_2 = QStandardItem("文件2")
        item_directory_1.appendRow(item_file_1)
        item_directory_1.appendRow(item_file_2)
        self.directory_tree.setModel(model)

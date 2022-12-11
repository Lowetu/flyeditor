# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLayout, QListView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolBar, QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 600)
        self.actionNew_File = QAction(MainWindow)
        self.actionNew_File.setObjectName(u"actionNew_File")
        self.actionNew_Folder = QAction(MainWindow)
        self.actionNew_Folder.setObjectName(u"actionNew_Folder")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionNew_File_2 = QAction(MainWindow)
        self.actionNew_File_2.setObjectName(u"actionNew_File_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-9, 21, 1337, 585))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_three_col = QPushButton(self.layoutWidget)
        self.btn_three_col.setObjectName(u"btn_three_col")

        self.horizontalLayout.addWidget(self.btn_three_col)

        self.btn_two_col = QPushButton(self.layoutWidget)
        self.btn_two_col.setObjectName(u"btn_two_col")

        self.horizontalLayout.addWidget(self.btn_two_col)

        self.btn_fullscreen = QPushButton(self.layoutWidget)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")

        self.horizontalLayout.addWidget(self.btn_fullscreen)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.directory_tree = QTreeView(self.layoutWidget)
        self.directory_tree.setObjectName(u"directory_tree")

        self.gridLayout.addWidget(self.directory_tree, 1, 0, 1, 1)

        self.file_list = QListView(self.layoutWidget)
        self.file_list.setObjectName(u"file_list")

        self.gridLayout.addWidget(self.file_list, 1, 1, 1, 1)

        self.index_web_view = QWebEngineView(self.layoutWidget)
        self.index_web_view.setObjectName(u"index_web_view")
        self.index_web_view.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.index_web_view, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1089, 29))
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_File_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_File.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.actionNew_Folder.setText(QCoreApplication.translate("MainWindow", u"New Folder", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionNew_File_2.setText(QCoreApplication.translate("MainWindow", u"New File", None))
        self.btn_three_col.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u680f", None))
        self.btn_two_col.setText(QCoreApplication.translate("MainWindow", u"\u4e24\u680f", None))
        self.btn_fullscreen.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


import sys
from ui.main2 import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

from web_engine_view import MainWindow

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

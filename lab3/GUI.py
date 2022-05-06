import os

from PyQt6.QtCore import Qt
import pickle

from PyQt6.QtGui import QPixmap

from reader import Reader
from text_processing import *
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QMenuBar, QTableWidget, \
    QTableWidgetItem, QFileDialog, QMessageBox, QHBoxLayout, QLineEdit, QTextEdit, QGraphicsView, QLabel


class GUI:
    def run(self):
        self.init_main_window()

    def init_main_window(self):
        app = QApplication([])
        self.window = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(self.init_menu_bar())
        self.plain_text = QTextEdit()
        vbox.addWidget(self.plain_text)
        analyze_button = QPushButton("Анализировать")
        analyze_button.clicked.connect(lambda _: analyse(self.plain_text.toPlainText()))
        vbox.addWidget(analyze_button)
        vbox.setStretch(1, 0)
        self.window.setLayout(vbox)
        self.window.setWindowTitle("Анализ текста")
        self.window.show()
        app.exec()


    def file_open(self):
        path = QFileDialog.getOpenFileName(self.window, 'Open file', '', "Text files (*.doc)")[0]
        if not path == '':
            self.plain_text.setText(Reader.read(path))

    def init_menu_bar(self):
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("Файл")
        file_menu.addSeparator()
        open_file = file_menu.addAction("Открыть")
        open_file.triggered.connect(self.file_open)
        help_button = menu_bar.addAction("Help")
        help_button.triggered.connect(self.help_button)
        return menu_bar

    def help_button(self):
        q = QMessageBox()
        q.setText('''                    
    Программа предназначена для для обработки текстов на английском языке.

    Делает дерево семантико-синтаксического разбора предложения.

    Поддерживаемые форматы входных текстовых файлов - doc.
    
    Файл дерева разбора автоматически сохраняется в test.ps

''')
        q.exec()
        pass



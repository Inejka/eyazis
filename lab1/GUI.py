import os

from PyQt6.QtCore import Qt
import pickle
from reader import Reader
from text_processing import *
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QMenuBar, QTableWidget, \
    QTableWidgetItem, QFileDialog, QMessageBox, QHBoxLayout, QLineEdit, QTextEdit


class GUI:
    def run(self):
        self.init_main_window()

    def init_main_window(self):
        app = QApplication([])
        self.window = QWidget()
        vbox = QVBoxLayout()
        menu_bar = self.init_menu_bar()
        vbox.addWidget(menu_bar)
        self.plain_text = QTextEdit()
        vbox.addWidget(self.plain_text)
        analyze_button = QPushButton("Анализировать")
        analyze_button.clicked.connect(lambda : (main_dictionary.clear(),parser(self.plain_text.toPlainText()),self.update_table()))
        vbox.addWidget(analyze_button)
        self.table = self.init_table()
        vbox.addWidget(self.init_search())
        vbox.addWidget(self.table)
        vbox.setStretch(1, 0)
        self.window.setLayout(vbox)
        self.window.setWindowTitle("Анализ текста")
        self.window.show()
        app.exec()

    def init_search(self):
        costya = QWidget()
        hbox = QHBoxLayout()
        self.s1 = QLineEdit()
        self.s1.setPlaceholderText("Поиск по лемме")
        self.s2 = QLineEdit()
        self.s2.setPlaceholderText("Поиск по тэгам")
        self.s3 = QLineEdit()
        self.s3.setPlaceholderText("Поиск по роли")
        self.s1.textEdited.connect(self.update_table)
        self.s2.textEdited.connect(self.update_table)
        self.s3.textEdited.connect(self.update_table)
        hbox.addWidget(self.s1)
        hbox.addWidget(self.s2)
        hbox.addWidget(self.s3)
        costya.setLayout(hbox)
        return costya


    def file_open(self):
        path = QFileDialog.getOpenFileName(self.window, 'Open file', '', "Text files (*.txt *.rtf)")[0]
        if not path == '':
            main_dictionary.clear()
            parser(Reader.read(path))
            self.update_table()

    def update_table(self):
        self.table.clearContents()
        self.table.setRowCount(len(main_dictionary))
        for i in range(len(main_dictionary)):
            self.table.setItem(i, 0, QTableWidgetItem(main_dictionary[i].lexeme))
            self.table.setItem(i, 1, QTableWidgetItem(main_dictionary[i].tags))
            self.table.setItem(i, 2, QTableWidgetItem(main_dictionary[i].part_of_sent))
            self.table.setRowHidden(i, False)
        if self.s1.text():
            text = self.s1.text()
            for i in range(len(main_dictionary)):
                if text not in main_dictionary[i][0]:
                    self.table.setRowHidden(i,True)
        if self.s2.text():
            text = self.s2.text()
            for i in range(len(main_dictionary)):
                if text not in main_dictionary[i][1]:
                    self.table.setRowHidden(i,True)
        if self.s3.text():
            text = self.s3.text()
            for i in range(len(main_dictionary)):
                if text not in main_dictionary[i][3]:
                    self.table.setRowHidden(i,True)

        self.table.resizeColumnsToContents()

    def init_table(self):
        table = QTableWidget()
        table.setColumnCount(3)  # Set three columns
        table.setHorizontalHeaderLabels(["Лексемма", "Тэги", "Роль в предложении"])
        # Set the tooltips to headings
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # Set the alignment to the headers
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignmentFlag.AlignRight)
        table.resizeColumnsToContents()
        table.itemChanged.connect(self.table_changed)
        return table

    def table_changed(self,item):
        if item.column()==0:
            main_dictionary[item.row()].lexeme = item.text()
        if item.column()==1:
            main_dictionary[item.row()].tags = item.text()
        if item.column()==2:
            main_dictionary[item.row()].part_of_sent = item.text()

    def init_menu_bar(self):
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("Файл")
        file_menu.addSeparator()
        open_file = file_menu.addAction("Открыть")
        open_file.triggered.connect(self.file_open)
        table_menu = menu_bar.addMenu("Таблица")
        save_table = table_menu.addAction("Сохранить")
        save_table.triggered.connect(self.save_table)
        load_table = table_menu.addAction("Загрузить")
        load_table.triggered.connect(self.load_table)
        add_row = table_menu.addAction("Добавить запись")
        add_row.triggered.connect(self.add_row)
        help_button = menu_bar.addAction("Help")
        help_button.triggered.connect(self.help_button)
        return menu_bar

    def add_row(self):
        main_dictionary.append(Lexeme())
        self.update_table()

    def help_button(self):
        q = QMessageBox()
        q.setText('''                    

    Программа предназначена для для обработки текстов на руском языке.

    Проверяет текст на наличие слов, определяет их характеристики и на их основе
делает вывод о возможной роли конкретного слова в составе предложения (если
существительное в именительномо падеже, то возм. подлежащее).


    Поддерживаемые форматы входных текстовых файлов - rtf и txt.

    Для редактирования записи кликните по ней дважды.
''')
        q.exec()
        pass

    def save_table(self):
        pickle.dump(main_dictionary,open("dict.dict",'wb'))
        q = QMessageBox()
        q.setText("Словарь сохранён в "+os.getcwd()+"/dict.dict")
        q.exec()

    def load_table(self):
        main_dictionary.clear()
        temp = pickle.load(open("dict.dict",'rb'))
        main_dictionary.extend(temp)
        self.update_table()
        q = QMessageBox()
        q.setText("Загружен словарь из" + os.getcwd() + "/dict.dict")
        q.exec()


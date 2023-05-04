from PyQt5.QtWidgets import QLabel, QPushButton, QDialog
from PyQt5.QtCore import Qt


class WinDataDel(QDialog):
    """Своё окно подтверждения удаление данных"""
    def __init__(self, host):
        self.host = host
        super().__init__()
        self.setGeometry(700, 400, 460, 260)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.fon = QLabel(self)
        self.fon.setGeometry(0, 0, 460, 260)

        self.exclamation_sign = QLabel(self)
        self.exclamation_sign.setGeometry(10, 40, 76, 67)

        self.title_text = QLabel(self)
        self.title_text.setText('Внимание!')
        self.title_text.setGeometry(2, -35, 150, 100)
        self.information_text = QLabel(self)
        self.information_text.setText('''Внимание!\n\nВы собираетесь удалить данные!\nЭто действие необратимо!''')

        self.information_text.setGeometry(80, 0, 300, 200)

        # кнопка Ок
        self.btn_ok = QPushButton(self)
        self.btn_ok.setGeometry(140, 203, 80, 36)
        self.btn_ok.setText('Продолжить')
        # кнопка Cancel
        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setGeometry(260, 203, 80, 36)
        self.btn_cancel.setText('Отменить')

        # Запускаем метод, который применит стили к кнопкам
        self.adjust_appearence()

        self.btn_ok.clicked.connect(self.ok_button_clicked)
        self.btn_cancel.clicked.connect(self.cancel_button_clicked)

        self.exec()

    def adjust_appearence(self):

        btn_ok_style = 'QPushButton { background-color: rgb(228, 0, 0); color: white; font-size:10px; }'
        btn_cancel_style = 'QPushButton { background-color: rgb(0, 124, 0); color: white; font-size:10px; }'
        background_style = 'QLabel { qproperty-pixmap: url(source/background_picture.png); }'
        exclamation_sign_style = 'QLabel { qproperty-pixmap: url(source/exclamation_sign.png); }'
        title_text_style = 'QLabel {font-size:17px; color: brown; }'
        information_text_style = 'QLabel {font-size:19px; color: black; text-align: center; }'

        self.btn_ok.setStyleSheet(btn_ok_style)
        self.btn_cancel.setStyleSheet(btn_cancel_style)
        self.fon.setStyleSheet(background_style)
        self.exclamation_sign.setStyleSheet(exclamation_sign_style)
        self.title_text.setStyleSheet(title_text_style)
        self.information_text.setStyleSheet(information_text_style)

    def ok_button_clicked(self):
        # Забираем выделенные индексы
        selected_indexes = self.host.QTableView.selectedIndexes()
        print(selected_indexes[0].row())
        rows = set([index.row() for index in selected_indexes])
        # remove rows in *REVERSE* order!
        for row in sorted(rows, reverse=True):
            self.host.model.removeRow(row)
            self.host.model.select()
        self.close()

    def cancel_button_clicked(self):
        pass
        self.close()





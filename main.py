import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView

from delete_dialog import WinDataDel


class WinAdmin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        # таблица "Список пользователей"
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("handler/base.db")
        self.model = QSqlTableModel(self)
        self.model.setTable("Users")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "ФИО")
        self.model.setHeaderData(2, Qt.Horizontal, "Логин")
        self.model.setHeaderData(3, Qt.Horizontal, "Пароль")
        self.model.setHeaderData(4, Qt.Horizontal, "Статус")

        self.model.select()

        # Set up the view
        self.QTableView = QTableView(self)
        self.QTableView.setGeometry(QtCore.QRect(200, 200, 670, 300))
        self.QTableView.setObjectName("view")
        self.QTableView.setModel(self.model)
        self.QTableView.setColumnHidden(0, True)  # скрыть столбец id
        self.QTableView.resizeColumnsToContents()
        self.QTableView.setColumnWidth(1, 200)
        self.QTableView.setColumnWidth(2, 100)
        self.QTableView.setColumnWidth(3, 100)
        self.QTableView.setColumnWidth(4, 130)

        # контекстное меню для удаления пользователя
        self.QTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.QTableView.customContextMenuRequested.connect(self.table_menu)

    def table_menu(self, pos):
        selected = self.QTableView.selectedIndexes()
        if not selected:
            return None
        menu = QtWidgets.QMenu()
        deleteAction = menu.addAction('Удалить пользователя')
        deleteAction.triggered.connect(lambda: self.remove_row())
        menu.exec_(QtGui.QCursor.pos())

    def remove_row(self):
        """Вызов кастомизированного диалогового окна для удаления ряда данных"""
        # Создаем экземпляр класса диалогового окна, передаем в качестве аргумента ссылку
        # на основное приложение из которого вызывается диалоговое окно, для того, чтобы внутри него были
        # доступны его состояния.
        remove_dialog_result = WinDataDel(self)
        print(remove_dialog_result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WinAdmin()
    window.show()
    sys.exit(app.exec_())

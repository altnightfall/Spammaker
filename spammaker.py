import copy
import sys
import json
from PyQt5 import QtWidgets
import design
import const_design
import re
from more_itertools import unique_everseen
from main import send_mail, check_mail


class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Авторизация')
        self.login = QtWidgets.QLineEdit()
        self.login.setPlaceholderText('Введите почту...')

        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText('Введите пароль...')

        self.okButton = QtWidgets.QPushButton(text='Войти')
        self.okButton.clicked.connect(self.close)

        layout = QtWidgets.QFormLayout()
        layout.addRow('Mail:', self.login)
        layout.addRow('Password:', self.password)
        layout.addRow(self.okButton)
        self.setLayout(layout)


class ConstApp(QtWidgets.QMainWindow, const_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.parent_w = None
        self.data = {}
        self.pushButton.clicked.connect(self.save_const)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderLabels(["Ключ", "Значение"])

    def save_const(self):
        index = self.tabWidget.currentIndex()
        tab = self.tabWidget.tabText(index)
        key = self.lineEdit.text()
        if self.parent_w.const.get(key) is None:
            if tab == "Константа":
                key = self.lineEdit.text()
                value = self.lineEdit_2.text()
                self.parent_w.const[key] = value
                self.listWidget.addItem(key)
            elif tab == "Словарь":
                str_dict = ""
                for i in range(self.tableWidget.rowCount()):
                    if self.tableWidget.item(i, 0) is not None and self.tableWidget.item(i, 1) is not None:
                        str_dict += '– {}: {}<br>'.format(self.tableWidget.item(i, 0).text(),
                                                          self.tableWidget.item(i, 1).text())
                self.parent_w.const[key] = str_dict
                self.listWidget.addItem(key)
            elif tab == "Из файла":
                if self.parent_w.in_file.get(key) is None:
                    self.parent_w.in_file[key] = self.spinBox.value()
                    self.listWidget.addItem(key)


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_html)
        self.pushButton_3.clicked.connect(self.onen_const)
        self.const_widow = ConstApp()
        self.const_widow.parent_w = self
        self.const = {}
        self.in_file = {}
        self.mail = ''
        self.password = ''
        self.addEmailTableRowButton.clicked.connect(self.addEmailTableRow)
        self.addEmailTableColumnButton.clicked.connect(self.addEmailTableColumn)
        self.deleteEmailTableColumnButton.clicked.connect(self.deleteEmailTableColumn)
        self.deleteEmailTableRowButton.clicked.connect(self.deleteEmailTableRow)
        self.importEmailTableButton.clicked.connect(self.importEmailTable)
        self.selectEmailButton.clicked.connect(self.selectEmail)

        #Судя по всему придется использовать CSV, а не JSON
        with open('constants.json', encoding='utf-8') as json_file:
            constants = json.load(json_file)
            for key in constants:
                self.constantListWidget.addItem(key)
        self.constants = constants
        self.constantListWidget.clicked.connect(self.constantSelect)
        self.saveConstButton.clicked.connect(self.constantSave)
        self.deleteConstButton.clicked.connect(self.constantsDelete)
        self.importConstButton.clicked.connect(self.importConstants)

    def create_html(self):
        if self.mail == '':
            msg = QtWidgets.QMessageBox.question(
                self,
                'Отсутствет почта',
                "Не выбрана почта для отправки",
                QtWidgets.QMessageBox.Close
            )
            return
        text = self.plainTextEdit.toPlainText()
        consts = re.findall(r'(?<={)\w+(?=})', text)
        consts = list(unique_everseen(consts))
        temp_const = copy.copy(self.constants)
        for c in consts:
            if temp_const.get(c) is None:
                temp_const[c] = "{" + c + "}"
        text = text.format(**temp_const)
        html_text = """<html><head></head><body><p>{}</p></body></html>""".format(text.replace("\n", "<br>"))
        msg_header = self.emailHeaderEdit.text()
        send_mail(self.in_file, self.mail, self.password, msg_header, html_text)


    def selectEmail(self):
        login = LoginWindow()
        login.open()
        login.exec_()
        if check_mail(login.login.text(), login.password.text()):
            self.mail = login.login.text()
            self.password = login.password.text()
            #Тут нужно сделать вывод почты в лейбл на формочке
        else:
            msg = QtWidgets.QMessageBox.question(
                self,
                'Ошибка авторизации',
                "Не удалось выполнить вход в почту",
                QtWidgets.QMessageBox.Close
            )


    def onen_const(self):
        self.const_widow.show()
        print(self.const, self.in_file)


    #variables table buttons
    def addEmailTableRow(self):
        self.variablesTableWidget.insertRow(self.variablesTableWidget.rowCount())

    def deleteEmailTableRow(self):
        self.variablesTableWidget.removeRow(self.variablesTableWidget.currentRow())

    def addEmailTableColumn(self):
        self.variablesTableWidget.insertColumn(self.variablesTableWidget.columnCount()) #Can't change name of the header yet...


    def deleteEmailTableColumn(self):
        self.variablesTableWidget.removeColumn(self.variablesTableWidget.currentColumn())

    def importEmailTable(self):
        pass #add import

    #constants functions
    def constantSelect(self):
        self.constNameEdit.setText(self.constantListWidget.currentItem().text())
        self.constTextEdit.setPlainText(self.constants[self.constantListWidget.currentItem().text()])

    def constantSave(self):
        if self.constNameEdit.text() != '':
            if self.constNameEdit.text() not in self.constants:
                self.constantListWidget.addItem(self.constNameEdit.text())
            self.constants[self.constNameEdit.text()] = self.constTextEdit.toPlainText()
            with open('constants.json', 'w', encoding='utf-8') as json_file:
                json.dump(self.constants, json_file)

    def constantsDelete(self):
        item = self.constantListWidget.currentItem()
        if item is not None:
            self.constants.pop(item.text())
            self.constantListWidget.takeItem(self.constantListWidget.row(item))
            with open('constants.json', 'w', encoding='utf-8') as json_file:
                json.dump(self.constants, json_file)
            self.constNameEdit.clear()
            self.constTextEdit.clear()

    def importConstants(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть файл для импорта', str(sys.path) + '/', '*.json')[0]
        if fname != '':
            with open(fname, encoding='utf-8') as json_file:
                constants = json.load(json_file)
                for key in constants:
                    if isinstance(constants[key], str):
                        if key not in self.constants:
                            self.constantListWidget.addItem(key)
                        self.constants[key] = constants[key]
        with open('constants.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.constants, json_file)

    #connect buttons




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

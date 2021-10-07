import sys
import json
from PyQt5 import QtWidgets
import design
import const_design
import re
from more_itertools import unique_everseen
from main import send_mail


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
        self.addEmailTableRowButton.clicked.connect(self.addEmailTableRow)
        self.addEmailTableColumnButton.clicked.connect(self.addEmailTableColumn)
        self.deleteEmailTableColumnButton.clicked.connect(self.deleteEmailTableColumn)
        self.deleteEmailTableRowButton.clicked.connect(self.deleteEmailTableRow)
        self.importEmailTableButton.clicked.connect(self.importEmailTable)

        #Судя по всему придется использовать CSV, а не JSON
        with open('constants.json', encoding='utf-8') as json_file:
            constants = json.load(json_file)
            for key in constants:
                self.constantListWidget.addItem(key)
        self.constantListWidget.clicked.connect(lambda: self.constantSelect(constants))
        self.saveConstToBufferButton.clicked.connect(lambda: self.saveConstToBufferButton(constants))




    def create_html(self):
        text = self.plainTextEdit.toPlainText()
        consts = re.findall(r'(?<={)\w+(?=})', text)
        consts = list(unique_everseen(consts))
        for c in consts:
            if self.const.get(c) is None:
                self.const[c] = "{" + c + "}"
        text = text.format(**self.const)
        html_text = """<html><head></head><body><p>{}</p></body></html>""".format(text.replace("\n", "<br>"))
        msg_header = self.emailHeaderEdit.text()
        send_mail(self.in_file, '', '', msg_header, html_text)

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
    def constantSelect(self, constants):
        self.constNameEdit.setText(self.constantListWidget.currentItem().text())
        self.constTextEdit.setPlainText(constants[self.constantListWidget.currentItem().text()])

    def saveConstToBufferButton(self, constants):
        pass
    #connect buttons




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

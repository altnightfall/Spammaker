# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spammaker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.emailHeaderEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailHeaderEdit.setObjectName("emailHeaderEdit")
        self.verticalLayout_2.addWidget(self.emailHeaderEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.variablesTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.variablesTableWidget.setObjectName("variablesTableWidget")
        self.variablesTableWidget.setColumnCount(2)
        self.variablesTableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.variablesTableWidget.setItem(1, 1, item)
        self.horizontalLayout.addWidget(self.variablesTableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.constNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.constNameEdit.setObjectName("constNameEdit")
        self.verticalLayout_4.addWidget(self.constNameEdit)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.constTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.constTextEdit.setObjectName("constTextEdit")
        self.verticalLayout_4.addWidget(self.constTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.constListView = QtWidgets.QListView(self.centralwidget)
        self.constListView.setObjectName("constListView")
        self.horizontalLayout_2.addWidget(self.constListView)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveConstToBufferButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveConstToBufferButton.setObjectName("saveConstToBufferButton")
        self.horizontalLayout_3.addWidget(self.saveConstToBufferButton)
        self.deleteConstButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteConstButton.setObjectName("deleteConstButton")
        self.horizontalLayout_3.addWidget(self.deleteConstButton)
        self.importConstButton = QtWidgets.QPushButton(self.centralwidget)
        self.importConstButton.setObjectName("importConstButton")
        self.horizontalLayout_3.addWidget(self.importConstButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система оповещения абитуриентов и студентов РХТУ имени Д. И. Менделеева"))
        self.label.setText(_translate("MainWindow", "Заголовок письма"))
        self.label_2.setText(_translate("MainWindow", "Текст письма"))
        item = self.variablesTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.variablesTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.variablesTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.variablesTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        __sortingEnabled = self.variablesTableWidget.isSortingEnabled()
        self.variablesTableWidget.setSortingEnabled(False)
        item = self.variablesTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "altnightfall@yandex.ru"))
        item = self.variablesTableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Юрий"))
        item = self.variablesTableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "krashr13@mail.ru"))
        item = self.variablesTableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Роман"))
        self.variablesTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Словарь"))
        self.label_5.setText(_translate("MainWindow", "Константа"))
        self.label_4.setText(_translate("MainWindow", "Значение"))
        self.saveConstToBufferButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteConstButton.setText(_translate("MainWindow", "Удалить"))
        self.importConstButton.setText(_translate("MainWindow", "Импортировать"))
        self.pushButton.setText(_translate("MainWindow", "Тестовое письмо"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать файл"))
        self.pushButton_3.setText(_translate("MainWindow", "Редактировать переменные"))
        self.pushButton_4.setText(_translate("MainWindow", "Выбрать почту для отправки"))

# Form implementation generated from reading ui file 'windows_ui/main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 588)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QtCore.QSize(20, 0))
        MainWindow.setStyleSheet("font: 10pt \"Calibri\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sale_line_items_view = QtWidgets.QListWidget(parent=self.centralwidget)
        self.sale_line_items_view.setGeometry(QtCore.QRect(10, 60, 321, 301))
        self.sale_line_items_view.setStyleSheet("font: 8pt;")
        self.sale_line_items_view.setObjectName("sale_line_items_view")
        item = QtWidgets.QListWidgetItem()
        self.sale_line_items_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.sale_line_items_view.addItem(item)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 491, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(381, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setSizeIncrement(QtCore.QSize(20, 0))
        self.frame.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.exit_button.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.username_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.username_label.setStyleSheet("color: rgb(255, 170, 0);")
        self.username_label.setObjectName("username_label")
        self.horizontalLayout.addWidget(self.username_label)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 60, 138, 254))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.make_new_sale_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.make_new_sale_button.setObjectName("make_new_sale_button")
        self.verticalLayout.addWidget(self.make_new_sale_button)
        self.enter_item_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.enter_item_button.setObjectName("enter_item_button")
        self.verticalLayout.addWidget(self.enter_item_button)
        self.delete_item_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.delete_item_button.setObjectName("delete_item_button")
        self.verticalLayout.addWidget(self.delete_item_button)
        self.end_sale_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.end_sale_button.setObjectName("end_sale_button")
        self.verticalLayout.addWidget(self.end_sale_button)
        self.make_payment_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.make_payment_button.setObjectName("make_payment_button")
        self.verticalLayout.addWidget(self.make_payment_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 370, 321, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.total_price_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.total_price_label.setObjectName("total_price_label")
        self.horizontalLayout_2.addWidget(self.total_price_label)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dialog = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.dialog.setGeometry(QtCore.QRect(10, 410, 461, 151))
        self.dialog.setObjectName("dialog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "POS IOO"))
        __sortingEnabled = self.sale_line_items_view.isSortingEnabled()
        self.sale_line_items_view.setSortingEnabled(False)
        item = self.sale_line_items_view.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.sale_line_items_view.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        self.sale_line_items_view.setSortingEnabled(__sortingEnabled)
        self.exit_button.setText(_translate("MainWindow", "Вихід"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.make_new_sale_button.setText(_translate("MainWindow", "Новий продаж"))
        self.enter_item_button.setText(_translate("MainWindow", "Додати"))
        self.delete_item_button.setText(_translate("MainWindow", "Видалити"))
        self.end_sale_button.setText(_translate("MainWindow", "Завершити"))
        self.make_payment_button.setText(_translate("MainWindow", "Розрахувати"))
        self.label.setText(_translate("MainWindow", "Остаточно:"))
        self.total_price_label.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "грн"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
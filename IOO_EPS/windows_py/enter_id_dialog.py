# Form implementation generated from reading ui file 'windows_ui/enter_id_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 153)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setStyleSheet("font: 12pt \"Calibri\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.id_entry = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.id_entry.setObjectName("id_entry")
        self.gridLayout.addWidget(self.id_entry, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.quantity_entry = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.quantity_entry.setObjectName("quantity_entry")
        self.gridLayout.addWidget(self.quantity_entry, 1, 1, 1, 1)
        self.ok_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 2, 0, 1, 2)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "id товару"))
        self.label.setText(_translate("Dialog", "id товару:"))
        self.ok_button.setText(_translate("Dialog", "ОК"))
        self.label_2.setText(_translate("Dialog", "Кількість"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
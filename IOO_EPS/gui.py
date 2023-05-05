import datetime
from domain import Store
from windows_py import main, payed, enter_id_dialog, authoriztion
from abc import ABC, abstractmethod


class PropertyListener(ABC):

    @abstractmethod
    def on_property_event(self, source, name, value):
        pass


class EnterIdWindows(enter_id_dialog.Ui_Dialog):

    def setup_buttons(self, register):
        self.ok_button.clicked.connect(lambda: self.on_ok_event(register))

    def on_ok_event(self, register):
        try:
            register.enter_item(self.id_entry.text(), int(self.quantity_entry.text()))
            self.close()
        except Exception as e:
            print(e)


class PayedWindow(payed.Ui_Dialog):

    def setup_buttons(self, register):
        self.ok_button.clicked.connect(lambda: self.on_ok_event(register))

    def on_ok_event(self, register):
        try:
            register.make_payment(float(self.payed_entry.text()))
            self.close()
        except Exception as e:
            pass


class POSMainWindow(main.Ui_MainWindow, PropertyListener):

    def on_property_event(self, source, name, value):
        if name == 'sale.total':
            self.total_price_label.setText(str(value))
        elif name == 'sale.new_item':
            self.sale_line_items_view.addItem(value)
        elif name == 'sale.payed':
            self.dialog.append(str(value))
        elif name == 'sale.change':
            self.dialog.append(str(value))

    def __init__(self, store):
        self.store = store
        self.register = store.register
        self.window = None

    def on_delete_event(self):
        try:
            selected_index = self.sale_line_items_view.selectedIndexes()[0].row()
            self.register.s.delete_item(selected_index)
            self.sale_line_items_view.takeItem(selected_index)
        except Exception as e:
            print(e)

    def setup_buttons(self, window, username):
        self.username_label.setText(username)
        self.make_new_sale_button.clicked.connect(self.on_make_new_sale_event)
        self.enter_item_button.clicked.connect(self.on_enter_item_event)
        self.end_sale_button.clicked.connect(self.on_end_sale_event)
        self.make_payment_button.clicked.connect(self.on_make_payment_event)
        self.delete_item_button.clicked.connect(self.on_delete_event)
        self.make_new_sale_button.setShortcut('1')
        self.enter_item_button.setShortcut('2')
        self.end_sale_button.setShortcut('3')
        self.make_payment_button.setShortcut('4')
        self.delete_item_button.setShortcut('-')
        self.exit_button.clicked.connect(self.on_exit_event)
        self.window = window

    def on_exit_event(self):
        self.window.close()
        MainWindow.show()

    def on_make_new_sale_event(self):
        try:
            if self.register.s is None or self.register.s.is_complete:
                self.register.make_new_sale()
                self.register.s.add_property_listener(self)
                self.total_price_label.setText('0')
                self.sale_line_items_view.clear()
                self.dialog.append(f'[{datetime.datetime.now()}] Продаж відкрито. Додайте товари клієнта.')
            else:
                self.dialog.append(f'[{datetime.datetime.now()}] Помилка. Завершіть попередній продаж.')
        except Exception as e:
            print(e)

    def on_enter_item_event(self):
        if self.register.s is not None and not self.register.s.is_complete:
            self.open_dialog(EnterIdWindows)
            self.register.s.get_total()
        else:
            self.dialog.append(f'[{datetime.datetime.now()}] Помилка. Відкрийте продаж.')

    def on_end_sale_event(self):
        self.register.end_sale()
        self.dialog.append(f'[{datetime.datetime.now()}] Продаж завершено. Розрахуйте клієнта.')

    def on_make_payment_event(self):
        if self.register.s is not None and self.register.s.is_complete:
            self.open_dialog(PayedWindow)
        else:
            self.dialog.append(f'[{datetime.datetime.now()}] Помилка. Завершіть продаж.')

    def open_dialog(self, cl):
        dialog = cl()
        dialog.setupUi(dialog)
        dialog.setup_buttons(self.register)
        dialog.exec()


class AuthorizationWindow(authoriztion.Ui_MainWindow):

    def __init__(self, storage):
        self.storage = storage
        self.storage.register.add_property_listener(self)
        self.u = None
        self.MainWindow1 = None

    def setup_buttons(self):
        self.authorize_button.clicked.connect(self.on_authorize_event)
        self.warning_label.hide()

    def on_authorize_event(self):
        try:
            print(self.storage.register)
            username = self.storage.register.authorize(self.login_entry.text(), self.password_entry.text())
            if username:
                self.MainWindow1 = main.QtWidgets.QMainWindow()
                self.u = POSMainWindow(self.storage)
                self.u.setupUi(self.MainWindow1)
                self.u.setup_buttons(self.MainWindow1, username)
                self.MainWindow1.show()
                self.login_entry.clear()
                self.password_entry.clear()
                MainWindow.close()
            else:
                self.warning_label.show()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = main.QtWidgets.QApplication(sys.argv)
    MainWindow = main.QtWidgets.QMainWindow()
    s = Store()
    ui = AuthorizationWindow(s)
    ui.setupUi(MainWindow)
    ui.setup_buttons()
    MainWindow.show()

    sys.exit(app.exec())

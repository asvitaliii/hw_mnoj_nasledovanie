from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from managers import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')

    def __set_slots(self):
        self.__win.producer_add.clicked.connect(self.producer_add)
        self.__win.producer_dell.clicked.connect(self.producer_del)
        self.__win.producer_info.clicked.connect(self.producer_info)
        self.__win.product_add.clicked.connect(self.product_add)
        self.__win.product_dell.clicked.connect(self.product_del)
        self.__win.product_info.clicked.connect(self.product_info)
        self.__win.show_all.clicked.connect(self.show_info)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def producer_add(self):
        dm = DataManager()
        pr = {'name': self.__win.producer_name.text(), 'rate': self.__win.producer_rate.text()}
        dm.add_producer(pr)

    def producer_del(self):
        dm = DataManager()
        pr = self.__win.producer_name.text()
        dm.del_producer(pr)

    def producer_info(self):
        dm = DataManager()
        QMessageBox.information(self, 'Инфо опродюсере:', f'{dm.get_producer(self.__win.producer_name.text())}')

    def product_add(self):
        dm = DataManager()
        pr = {'name': self.__win.product_name.text(), 'producer': self.__win.product_producer.text()}
        dm.add_product(pr)

    def product_del(self):
        dm = DataManager()
        pr = self.__win.product_name.text()
        dm.del_product(pr)

    def product_info(self):
        dm = DataManager()
        QMessageBox.information(self, 'Инфо о продукте:', f'{dm.get_product(self.__win.product_name.text())}')

    def show_info(self):
        dm = DataManager()
        QMessageBox.information(self, 'Вся инфо:', f'{dm.load_data()}')
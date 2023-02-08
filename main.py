from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QTableWidgetItem
from PyQt5.uic import loadUi
import sys 
import sqlite3

foods = sqlite3.connect('dodopizza.db')
connect  = foods.cursor()

connect.execute("""CREATE TABLE IF NOT EXISTS foods(
    name VARCHAR(255),
    surname VARCHAR(255),
    number INTEGER,
    address VARCHAR(255),
    food VARCHAR(255)


    );
    """)

class MenuWindow(QWidget):
    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi('menu.ui', self)
        print("Ok")

class AdminTable(QMainWindow):
    def __init__(self):
        super(AdminTable, self).__init__()
        loadUi('admin_table.ui', self)
        cur  = foods.cursor()
        cur.execute(f"SELECT name FROM foods")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.name.addItem(res1)
            
        cur.execute(f"SELECT surname FROM foods")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.surname.addItem(res1)
            
        cur.execute(f"SELECT number FROM foods")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.number.addItem(res1)
            
        cur.execute(f"SELECT address FROM foods")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.address.addItem(res1)
            
        cur.execute(f"SELECT food FROM foods")
        for i in cur:
            res = "".join(list(str(i))).replace(",", "").replace('"', "").replace("(", "").replace(")", "")
            res1 = "".join(list(str(res))).replace("'", "").replace(" ", "")
            
            self.food.addItem(res1)

class AdminWindow(QWidget):
    def __init__(self):
        super(AdminWindow, self).__init__()
        loadUi('admin.ui', self)
        self.admin_table = AdminTable()

        self.confirm.clicked.connect(self.check_password)

    def check_password(self):
        get_password = self.password.text()
        if get_password == "1111":
            self.result.setText("Good")
            self.admin_table.show()

        else:
            self.result.setText("Incorrect")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('main.ui', self)
        self.menu_window = MenuWindow()
        self.admin_window = AdminWindow()
        self.hide_input_order()
        self.order.clicked.connect(self.show_input_order)
        self.send.clicked.connect(self.send_order)
        self.menu.clicked.connect(self.show_menu_window)
        self.admin.clicked.connect(self.show_admin_window)

    def show_menu_window(self):
        self.menu_window.show()

    def show_admin_window(self):
        self.admin_window.show()

    def hide_input_order(self):
        self.name.hide()
        self.surname.hide()
        self.number.hide()
        self.address.hide()
        self.food.hide()
        self.send.hide()

    def show_input_order(self):
        self.name.show()
        self.surname.show()
        self.number.show()
        self.address.show()
        self.food.show()
        self.send.show()

    def send_order(self):
        self.show_input_order()
        get_name = self.name.text()
        get_surname = self.surname.text()
        get_number = self.number.text()
        get_address = self.address.text()
        get_food = self.food.text()
        connect = foods.cursor()
        connect = connect.execute(f"INSERT INTO foods VALUES ('{get_name}','{get_surname}', '{get_number}','{get_address}','{get_food}');")
        foods.commit()
        print(get_name, get_surname, get_number, get_address, get_food)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()








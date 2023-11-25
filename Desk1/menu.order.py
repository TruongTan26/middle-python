import tkinter as tk
from db import *
import sys

def order_item(item_name, table_num):
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    sql = "INSERT INTO tbl_item (table_number, item_name) VALUES (%s, %s)"
    val = (table_num, item_name)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def select_menu_from_db():
    # Thực hiện truy vấn để lấy dữ liệu từ bảng menu trong cơ sở dữ liệu
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute("SELECT item_name FROM menu")
    menu_items = mycursor.fetchall()

    mydb.close()
    return menu_items

def select_chat_bot_from_db():
    # Thực hiện truy vấn để lấy dữ liệu từ bảng chat_bot trong cơ sở dữ liệu
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute("SELECT message FROM chat_bot")
    chat_messages = mycursor.fetchall()

    mydb.close()
    return chat_messages

def select_orders_from_db():
    # Thực hiện truy vấn để lấy dữ liệu từ bảng orders trong cơ sở dữ liệu
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute("SELECT order_name FROM orders")
    orders_list = mycursor.fetchall()

    mydb.close()
    return orders_list

def show_menu(table_num):
    root = tk.Tk()
    root.title(f"Menu - Bàn {table_num}")

    tab_control = tk.Notebook(root)

    menu_tab = tk.Frame(tab_control)
    chat_bot_tab = tk.Frame(tab_control)
    orders_tab = tk.Frame(tab_control)

    tab_control.add(menu_tab, text='Menu')
    tab_control.add(chat_bot_tab, text='Chat Bot')
    tab_control.add(orders_tab, text='Đã Gọi')

    menu_items = select_menu_from_db()
    chat_messages = select_chat_bot_from_db()
    orders_list = select_orders_from_db()

    for item in menu_items:
        item_button = tk.Button(menu_tab, text=item[0], command=lambda item_name=item[0]: order_item(item_name, table_num))
        item_button.pack()

    # Các công việc tương tự có thể được thực hiện cho các tab khác

    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Vui lòng nhập số bàn.")
    else:
        table_number = int(sys.argv[1])
        show_menu(table_number)

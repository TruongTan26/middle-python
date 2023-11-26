# import tkinter as tk
# from db import *
# import sys

# def order_item(item_name, table_num):
#     mydb = connect_db()
#     mycursor = create_cursor(mydb)

#     sql = "INSERT INTO tbl_item (table_number, item_name) VALUES (%s, %s)"
#     val = (table_num, item_name)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     mydb.close()

# def show_menu(table_num):
#     mydb = connect_db()
#     mycursor = create_cursor(mydb)

#     mycursor.execute("SELECT item_name FROM tbl_item")
#     menu_items = mycursor.fetchall()
    
#     root = tk.Tk()
#     root.title(f"Menu - Bàn {table_num}")
    
#     for item in menu_items:
#         item_button = tk.Button(root, text=item[0], command=lambda item_name=item[0]: order_item(item_name, table_num))
#         item_button.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Vui lòng nhập số bàn.")
#     else:
#         table_number = int(sys.argv[1])
#         show_menu(table_number)

import tkinter as tk
from tkinter import ttk
from db import *
import sys, datetime

def order_item(item_name,item_price, table_num):
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    current_time = datetime.datetime.now().strftime("%H:%M %d/%m/%Y")
    mycursor.execute("INSERT INTO tbl_item (table_number, item_name,item_price, time) VALUES (%s, %s, %s, %s)", (table_num, item_name,item_price, current_time))
    mydb.commit()
    mydb.close()

def select_menu_from_db():
    # Thực hiện truy vấn để lấy dữ liệu từ bảng menu trong cơ sở dữ liệu
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute("SELECT menu_name, menu_price FROM tbl_menu")
    menu_items = mycursor.fetchall()

    mydb.close()
    return menu_items

def select_chat_bot_from_db():
    # Thực hiện truy vấn để lấy dữ liệu từ bảng chat_bot trong cơ sở dữ liệu
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute("SELECT id FROM bot_chat")
    chat_messages = mycursor.fetchall()

    mydb.close()
    return chat_messages

def select_orders_from_db(tbnum):
    # Thực hiện truy vấn để lấy dữ liệu từ bảng orders trong cơ sở dữ liệu
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute(f"SELECT item_name, item_price FROM tbl_item WHERE table_number = {tbnum}")
    orders_list = mycursor.fetchall()

    mydb.close()
    return orders_list

def show_menu(table_num):
    root = tk.Tk()
    root.title(f"Menu - Bàn {table_num}")
    root.geometry("700x500")

    tab_control = ttk.Notebook(root)

    menu_tab = ttk.Frame(tab_control)
    chat_bot_tab = ttk.Frame(tab_control)
    orders_tab = ttk.Frame(tab_control)

    tab_control.add(menu_tab, text='Menu')
    tab_control.add(chat_bot_tab, text='Chat Bot')
    tab_control.add(orders_tab, text='Đã Gọi')

    menu_items = select_menu_from_db()
    chat_messages = select_chat_bot_from_db()
    orders_list = select_orders_from_db(table_num)

    for item in menu_items:
        item_button = tk.Button(menu_tab, text=f"{item[0]} - {item[1]}", command=lambda item_name=item[0], item_price=item[1]: order_item(item_name,item_price, table_num))
        item_button.pack()

    # Các công việc tương tự có thể được thực hiện cho các tab khác

    # Tạo khung mới
    orders_frame = ttk.Frame(tab_control)

    # Tạo bảng
    orders_table = ttk.Treeview(orders_frame)
    orders_table['columns'] = ['Tên món ăn', 'Giá món ăn', 'Số lượng']
    orders_table.column('#0', width=0, stretch=False)
    orders_table.column('Tên món ăn', width=150)
    orders_table.column('Giá món ăn', width=100)
    orders_table.column('Số lượng', width=50)
    orders_table.heading('#0', text='')
    orders_table.heading('Tên món ăn', text='Tên món ăn')
    orders_table.heading('Giá món ăn', text='Giá món ăn')
    orders_table.heading('Số lượng', text='Số lượng')
    for order in orders_list:
        if order[0] == table_num:
            orders_table.insert('', 'end', values=(order[1], order[2]))


    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Vui lòng nhập số bàn.")
    else:
        table_number = int(sys.argv[1])
        show_menu(table_number)

import tkinter as tk
from tkinter import ttk
from db import *
import sys, datetime, os,subprocess

current_time = datetime.datetime.now().strftime("%H:%M %d/%m/%Y")
month=datetime.datetime.now().month
day=datetime.datetime.now().day

def order_item(item_name,item_price, table_num):
    mydb = connect_db()
    mycursor = create_cursor(mydb)

    mycursor.execute("SELECT * FROM tbl_item WHERE table_number = %s AND item_name = %s", (table_num, item_name))
    existing_item = mycursor.fetchone()

    if existing_item:
        # Nếu món ăn đã tồn tại, cập nhật số lượng bằng cách tăng giá trị hiện tại lên một đơn vị
        new_quantity = existing_item[4] + 1  # Cột thứ tư trong database lưu số lượng
        mycursor.execute("UPDATE tbl_item SET quantity = %s, time = %s WHERE table_number = %s AND item_name = %s", (new_quantity, current_time, table_num, item_name))
    else:
        # Nếu món ăn chưa tồn tại, thêm một bản ghi mới vào cơ sở dữ liệu với số lượng ban đầu là 1
        mycursor.execute("INSERT INTO tbl_item (table_number, item_name, item_price, quantity, time) VALUES (%s, %s, %s, %s, %s)", (table_num, item_name, item_price, 1, current_time))

    mydb.commit()
    mydb.close()

def select_menu_from_db():
    mydb = connect_db()
    mycursor = create_cursor(mydb)
    # Thực hiện truy vấn để lấy dữ liệu từ bảng menu trong cơ sở dữ liệu
    mycursor.execute("SELECT menu_name, menu_price FROM tbl_menu")
    menu_items = mycursor.fetchall()

    mydb.close()
    return menu_items

def open_chat_db(table_number):
    os.system('python chat_db.py {}'.format(table_number))

def select_orders_from_db(tbnum):
    mydb = connect_db()
    mycursor = create_cursor(mydb)
    # Thực hiện truy vấn để lấy dữ liệu từ bảng orders trong cơ sở dữ liệu
    mycursor.execute("SELECT item_name, item_price, quantity, time FROM tbl_item WHERE table_number = %s",(tbnum,))
    orders_list = mycursor.fetchall()

    mydb.close()
    return orders_list

def show_menu(table_num):
    root = tk.Tk()
    root.title(f"Menu - Bàn {table_num}")
    root.geometry("810x500")

    tab_control = ttk.Notebook(root)

    menu_tab = ttk.Frame(tab_control)
    chat_bot_tab = ttk.Frame(tab_control)
    orders_tab = ttk.Frame(tab_control)

    tab_control.add(menu_tab, text='Menu')
    tab_control.add(chat_bot_tab, text='Chat')
    tab_control.add(orders_tab, text='Đã Gọi')
    
    # Widgets trong tab Menu
    label_menu = tk.Label(menu_tab, text="Đây là tab Menu")
    label_menu.pack()

    label_orders = tk.Label(orders_tab, text="Đây là orders_tab Đã Gọi")
    label_orders.pack()

    menu_items = select_menu_from_db()
    # chat_messages = select_chat_bot_from_db()
    orders_list = select_orders_from_db(table_num)

    for item in menu_items:
        item_button = tk.Button(menu_tab, text=f"{item[0]} - {item[1]}", command=lambda item_name=item[0], item_price=item[1]: order_item(item_name,item_price, table_num))
        item_button.pack()

    tree = ttk.Treeview(orders_tab, columns=('Item Name', 'Item Price', 'Quantity', 'Time'), show='headings')
    tree.heading('Item Name', text='Item Name')
    tree.heading('Item Price', text='Item Price')
    tree.heading('Quantity', text='Quantity')
    tree.heading('Time', text='Time')
    tree.pack(fill='both', expand=True)

    for list in orders_list:
        tree.insert('', 'end', values=list)

    total_quantity = sum(item[2] for item in orders_list)  # Tính tổng cột Quantity
    total_price = sum(item[2] * int(item[1]) for item in orders_list)  # Tính tổng cột Item Price (giá * số lượng)

    def thanh_toan():
        # print("Thanh toán")
        mydb = connect_db()
        mycursor = create_cursor(mydb)

        date_to = datetime.datetime.now()
        mycursor.execute("INSERT INTO bill (bill_table, bill_date, total, day, month) VALUES (%s, %s, %s, %s, %s)", (table_num, date_to, total_price, day, month))

        mycursor.execute("SELECT bill_id FROM bill WHERE bill_date = %s",(date_to,))
        lay_id = mycursor.fetchone()[0]
        print(lay_id)

        for order in orders_list:
            menu_name = order[0]
            menu_price = order[1]
            quantity = order[2]

            # Thêm đơn hàng đã gọi vào cơ sở dữ liệu bill_detail
            mycursor.execute("INSERT INTO bill_detail (bill_id, menu_name, menu_price, quantity, total, month) VALUES (%s, %s, %s, %s, %s, %s)", (lay_id, menu_name, menu_price, quantity, int(menu_price)*int(quantity), month))

        # Xóa các đơn hàng đã gọi từ tbl_item
        mycursor.execute("DELETE FROM tbl_item WHERE table_number = %s", (table_num,))

        mydb.commit()
        mydb.close()

    payment_button = tk.Button(orders_tab, text="Thanh toán", command= thanh_toan)
    payment_button.pack(side=tk.RIGHT, padx=10)

    # Hiển thị tổng trong giao diện
    total_quantity_label = tk.Label(orders_tab, text=f'Total Quantity: {total_quantity}')
    total_quantity_label.pack(side=tk.RIGHT, padx=120)

    total_price_label = tk.Label(orders_tab, text=f'Total Price: {total_price}')
    total_price_label.pack(side=tk.RIGHT, padx=10)

    def open_chat_bot():
        subprocess.Popen(["python", "chat_db.py", str(table_number)])
    def open_chat_live():
        subprocess.Popen(["python", "client.py", str(table_number)])

    chat_button = tk.Button(chat_bot_tab, text="Chat bot", command=open_chat_bot)
    chat_buttons = tk.Button(chat_bot_tab, text="Chat Live", command=open_chat_live)
    chat_button.place(relx=0.5, rely=0.5, anchor=tk.S)
    chat_buttons.place(relx=0.5, rely=0.5, anchor=tk.W)

    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Vui lòng nhập số bàn.")
    else:
        table_number = int(sys.argv[1])
        show_menu(table_number)
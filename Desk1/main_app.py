import tkinter as tk
import subprocess

def open_menu(table_number):
    subprocess.Popen(["python", "menu_order.py", str(table_number)]) # sử dụng Popen thì mở đc nhiều tab, còn call thì chỉ 1 thôi

root = tk.Tk()
root.title("Quản lý nhà hàng")
root.geometry("700x500")

table_list = [f"Bàn {i+1}" for i in range(10)]

def open_tab(table_num):
    table_number = table_num + 1
    open_menu(table_number)

# Hiển thị danh sách các bàn
for i, table in enumerate(table_list):
    table_button = tk.Button(root, text=table, command=lambda num=i: open_tab(num))
    table_button.pack()

root.mainloop()
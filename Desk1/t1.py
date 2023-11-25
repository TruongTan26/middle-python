import tkinter as tk
from tkinter import ttk

def open_table(tab_num):
    print(f"Mở tab cho bàn số {tab_num}")

root = tk.Tk()
root.title("Quản lý nhà hàng")

table_list = [f"Bàn {i+1}" for i in range(10)]

def open_tab(table_num):
    new_tab = tk.Toplevel(root)
    new_tab.title(f"{table_list[table_num]}")
    
    # Tạo các tab con
    tab_control = ttk.Notebook(new_tab)
    
    menu_tab = ttk.Frame(tab_control)
    chat_tab = ttk.Frame(tab_control)
    order_tab = ttk.Frame(tab_control)
    
    tab_control.add(menu_tab, text="Menu")
    tab_control.add(chat_tab, text="Chat Bot")
    tab_control.add(order_tab, text="Đã Gọi")
    
    tab_control.pack(expand=1, fill="both")

# Hiển thị danh sách các bàn
for i, table in enumerate(table_list):
    table_button = tk.Button(root, text=table, command=lambda num=i: open_tab(num))
    table_button.pack()

root.mainloop()

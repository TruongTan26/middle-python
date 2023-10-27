import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
from tkinter import messagebox
from tkinter import *
from windows_services import *
from server import *

# def btnMenu():
#     print('Menu')

# def btnCallEmploy():
#     print('Call Employee')

# def btnBill():
#     print('Bill')

# def windows_services():
#     # new_window = tk.Tk()
#     # new_window.title("Cửa sổ giao dịch mới")
#     # new_window.geometry('555x500')
#     # btn_menu = tk.Button(new_window, text="Menu", width=25, command=btnMenu)
#     # btn_menu.grid(row=0, column=0)
#     # btn_callemploy = tk.Button(new_window, text="Chat", width=25, command=btnCallEmploy)
#     # btn_callemploy.grid(row=0, column=1)
#     # btn_bill = tk.Button(new_window, text="Tinh tien", width=25, command=btnBill)
#     # btn_bill.grid(row=0, column=2)
#     # lbl = Label(new_window, text="Test label", bg='#000', fg='#ff0')
#     # lbl.grid()
#     new_window = tk.Tk()
#     new_window.geometry("700x500")

#     frame = Frame(new_window)
#     frame.pack()
#     toolbar = Frame(frame, width=700, height=500, bg="black")
#     main = Frame(frame, width=700, height=400, bg="black")
#     # bottom = Frame(frame, width=700, height=500, bg="skyblue3")

#     toolbar.pack(side="top", fill="x")
#     main.pack(side="top", fill="both", expand=True)
#     # bottom.pack(side="top", fill="both", expand=False)
    
#     lbl = Button(toolbar, text="Menu", width=25, command=btnMenu)
#     lbl.pack(side=LEFT)

#     lbl1 = Button(toolbar, text="Chat", width=25, command=btnCallEmploy)
#     lbl1.pack(side = LEFT)

#     lbl2 = Button(toolbar, text="Tinh tien", width=25, command=btnBill)
#     lbl2.pack(side=RIGHT)

#     maintree = Label(main, text="Main tree", width=25)
#     maintree.pack(side="top")

#     # bot = Label(bottom, text="bottom")
#     # bot.pack()

def open_new_window():
    windows_services()
    # new_window = tk.Toplevel(root)
    # new_window.title("Cửa sổ mới")
    # label = tk.Label(new_window, text="Đây là cửa sổ mới!")
    # label.pack()

def on_click(event):
    for i, rect in enumerate(rects):
        contains, _ = rect.contains(event)
        if contains:
            if rect.get_facecolor() == 'yellow':
                rect.set_facecolor('brown')
            else:
                rect.set_facecolor('yellow')
            canvas.draw()
            open_new_window()
            break

# Tạo một cửa sổ gốc
root = tk.Tk()
root.title("Sơ đồ 5 chiếc bàn")

# Tạo một đối tượng hình vẽ
fig = Figure(figsize=(5, 3))
ax = fig.add_subplot(111)
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 3)
ax.axis('equal')

rects = []

# Vẽ 5 hình chữ nhật tượng trưng biểu thị 5 chiếc bàn
for i in range(5):
    x = i * 2
    y = 0
    width = 1.5
    height = 1.0
    table = "D"+str(i)
    rect = Rectangle((x, y), width, height, color='brown')
    ax.add_patch(rect)
    rects.append(rect)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Đăng ký sự kiện nhấn chuột
canvas.mpl_connect('button_press_event', on_click)

root.mainloop()

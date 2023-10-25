import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
from tkinter import messagebox

def windows_services():
    # r = tk.Tk()
    new_window = tk.Toplevel(root)
    new_window.title("Cửa sổ mới")
    label = tk.Label(new_window, text="Đây là cửa sổ mới!", width=100, height=50)
    btn_menu = tk.Button(new_window, text="Menu", width=25).grid(row=0, column=0) #command=new_windows.destroy
    btn_callemploy = tk.Button(new_window, text="Chat", width=25).grid(row=0, column=1) #command=new_windows.destroy
    btn_bill = tk.Button(new_window, text="Tinh tien", width=25).grid(row=0, column=2) #command=new_windows.destroy
    btn_menu.pack()
    btn_callemploy.pack()
    btn_bill.pack()
    label.pack()
    

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
    rect = Rectangle((x, y), width, height, color='brown')
    ax.add_patch(rect)
    rects.append(rect)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Đăng ký sự kiện nhấn chuột
canvas.mpl_connect('button_press_event', on_click)

root.mainloop()

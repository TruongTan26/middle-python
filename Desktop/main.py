# import tkinter as tk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.patches import Rectangle
# from tkinter import messagebox
# from tkinter import *
# from windows_services import *
from server import *
import threading
from application import Application
import time
import sys

# def open_new_window():
#     windows_services()

# def on_click(event):
#     for i, rect in enumerate(rects):
#         contains, _ = rect.contains(event)
#         if contains:
#             if rect.get_facecolor() == 'yellow':
#                 rect.set_facecolor('brown')
#             else:
#                 rect.set_facecolor('yellow')
#             canvas.draw()
#             open_new_window()
#             break

# # Tạo một cửa sổ gốc
# root = tk.Tk()
# root.title("Sơ đồ 5 chiếc bàn")

# # Tạo một đối tượng hình vẽ
# fig = Figure(figsize=(5, 3))
# ax = fig.add_subplot(111)
# ax.set_xlim(-1, 11)
# ax.set_ylim(-1, 3)
# ax.axis('equal')

# rects = []

# # Vẽ 5 hình chữ nhật tượng trưng biểu thị 5 chiếc bàn
# for i in range(5):
#     x = i * 2
#     y = 0
#     width = 1.5
#     height = 1.0
#     table = "D"+str(i)
#     rect = Rectangle((x, y), width, height, color='brown')
#     ax.add_patch(rect)
#     rects.append(rect)

# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack()

# # Đăng ký sự kiện nhấn chuột
# canvas.mpl_connect('button_press_event', on_click)

def runGUI():
    app = Application()
    app.geometry("700x500")
    app.title("App1")
    app.mainloop()


def runChatServer(kill):
    ChatServer(kill)


def KillThread(t1):
    chatServer = threading.Thread(target=lambda: runChatServer(False))
    chatServer.start()
    while t1.is_alive():
        time.sleep(1)
        if t1.is_alive() == False:
            chatServer = threading.Thread(target=lambda: runChatServer(True))
            chatServer.start()
            chatServer.join(0)
            print("Dit me may in ra di lam on")
    

stop_thread = threading.Event()

GUI = threading.Thread(target=runGUI)
GUI.start()

checkThread = threading.Thread(target=lambda: KillThread(GUI))
checkThread.start()

checkThread.join(0)
sys.exit()

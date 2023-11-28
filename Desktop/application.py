import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from windows_services import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=500, height=500, bg="#7698A6")
        self.canvas.pack(side=RIGHT)
        self.createTable()
    
    def createTable(self):
        list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        a = len(list)
        length = 500//a
        count = 0
        for i in range(a):
            y = i * length
            for j in range(a):
                tablename = 'D'+str(count)
                x = j * length
                self.canvas.create_rectangle(x, y, x+length, y+length, fill="#D97E4A", tags=tablename)
                self.canvas.create_text(x+length-50, y+length-50, text=f'D{count}', fill="white")
                self.canvas.tag_bind(tablename,"<Button-1>",lambda _, tablename=tablename: self.open_new_window(tablename))
                count+=1

    def on_click(self, event):
        for i, rect in enumerate(self.rects):
            contains, _ = rect.contains(event)
            if contains:
                if rect.get_facecolor() == 'yellow':
                    rect.set_facecolor('brown')
                else:
                    rect.set_facecolor('yellow')
                self.canvas.draw()
                self.open_new_window()
                break
    
    def open_new_window(self, tablename):
        app = Windows_Services()
        app.title(f'Cửa sổ giao dịch bàn {tablename}')
        app.geometry("700x500")
        # app.resizable(False, False)

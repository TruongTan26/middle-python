import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from windows_services import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # tk.Tk.__init__(self, master)
        # self.root = tk.Tk()
    
        self.fig = Figure(figsize=(5, 3))
        self.ax = self.fig.add_subplot(111)
        self.rects = []

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        # self.rect

        self.createRect()
        self.createFigure()

    def createFigure(self):
        # fig = Figure(figsize=(5, 3))
        # ax = fig.add_subplot(111)
        self.ax.set_xlim(-1, 11)
        self.ax.set_ylim(-1, 3)
        self.ax.axis('equal')

    def createRect(self):
        for i in range(5):
            x = i * 2
            y = 0
            width = 1.5
            height = 1.0
            table = "D"+str(i)
            rect = Rectangle((x, y), width, height, color='brown')
            self.ax.add_patch(rect)
            self.rects.append(rect)
        # canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()
        self.canvas.mpl_connect('button_press_event', self.on_click)

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
    
    def open_new_window(self):
        app = Windows_Services()
        app.title("Cửa sổ giao dịch bàn ...")
        app.geometry("700x500")
        # windows_services()

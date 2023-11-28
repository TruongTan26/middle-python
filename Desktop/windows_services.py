from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from data import *

class Windows_Services(tk.Tk):
    listProduct = dict()
    total = 0
    def __init__(self):
        super().__init__()
        # Create frame
        self.frame = Frame(self)
        self.frame.pack()

        # Create toolbar
        self.toolbar = Frame(self, height=100, bg="black")
        self.toolbar.pack(side="top", fill="x")

        # Create GUI for each function of project
        self.main = Frame(self, width=700, height=500, bg="red")
        self.main.pack(side="top", fill="both", expand=True)
        self.main.pack_propagate(False)
        self.createButton()

        # Create Scrollbar for frame
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, 
                                width = 200, height = 300,
                                yscrollcommand=vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command = self.canvas.yview)
 
        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
 
        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = Frame(self.canvas)
        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=NW)


    def _configure_interior(self, event):
    # Update the scrollbars to match the size of the inner frame.
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion=(0, 0, size[0], size[1]))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width = self.interior.winfo_reqwidth())
         
    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())


    def createButton(self):
        lbl = Button(self.toolbar, text="Menu", width=32, command=lambda: self.funcBtn("menu",self.main))
        lbl.pack(side=LEFT)

        lbl1 = Button(self.toolbar, text="Chat", width=32, command=lambda: self.funcBtn("chat",self.main))
        lbl1.pack(side = LEFT)

        lbl2 = Button(self.toolbar, text="Đơn hàng", width=32, command=lambda: self.funcBtn("bill",self.main))
        lbl2.pack(side=LEFT)

        self.funcBtn("menu",self.main)

        # maintree = Label(self.main, text="Main tree", width=25)
        # maintree.pack(side="top")

    def funcBtn(self, name, r):
        self.clearFrame(r)
        r.pack(side="top", fill="both", expand="True")
        match name:
            case "menu":
                # lbl = Label(r, text="Menu", width=25)
                # lbl.pack()
                self.menu_services(r)
                # print("Menu")
            case "chat":
                # chat_services(r)
                print("Chat")
            case "bill":
                self.bill(r)
    

    def clearFrame(self, r):
        # destroy all widgets from frame
        for widget in r.winfo_children():
            widget.destroy()
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        r.pack_forget()


    @classmethod
    def totalproduct(cls, name, price, typeofFood):
        convert = {
            "price": price,
            "total": 0
        }
        if name in cls.listProduct:
            total = cls.listProduct[name]["total"]
            total+=1
            convert["total"] = total
            cls.listProduct.__setitem__(name,convert)
        else:
            cls.listProduct.__setitem__(name,convert)
            
        print(cls.listProduct)


    def menu_services(self, r):
        print("Menu")
        # scrollbar = Scrollbar(r, orient="vertical")
        # scrollbar.grid(row=1, column=2,  sticky='w')
        # scrollbar.pack(side="right", fill="y")
        
        

    def bill(self, r):
         for i in range(20):
            ttk.Button(self.interior, text=f"Button {i}").pack(padx=10, pady=5)
        # ldrink = Label(r, text="Đồ uống")
        # ldrink.grid(row=0,column=1)
        # for k,v in storeDicDrink.items():
        #     ldrink = Label(r, text=v)
        #     ldrink.grid(row=k,column=1)
    

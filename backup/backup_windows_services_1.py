from tkinter import *
import tkinter as tk
from data import *

class Windows_Services(tk.Tk):
    listProduct = dict()
    total = 0
    def __init__(self):
        super().__init__()
        self.frame = Frame(self)
        self.frame.pack()

        self.toolbar = Frame(self, height=100, bg="black")
        self.main = Frame(self, width=700, height=500, bg="red")

        self.toolbar.pack(side="top", fill="x")
        
        self.main.pack(side="top", fill="both", expand=True)
        self.main.pack_propagate(False)

        self.createButton()
    
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
                # lbl = Label(r, text="Thanh toan", width=25)
                # lbl.pack()
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
        # total = 0
        convert = {
            "price": price,
            "total": 0
        }
        if name in cls.listProduct:
            total = cls.listProduct[name]["total"]
            # print(cls.listProduct[name])
            total+=1
            convert["total"] = total
            cls.listProduct.__setitem__(name,convert)
        else:
            cls.listProduct.__setitem__(name,convert)
            
        # cls.listProduct.append({name, price, typeofFood})
        print(cls.listProduct)
        # cls.total += 1
        # print(cls.total)
        # print(*args.name, *args.price)
        # print(name, price, typeofFood)

        # print(btn)



    def menu_services(self, r):
        scrollbar = Scrollbar(r, orient="vertical")
        scrollbar.grid(row=1, column=2,  sticky='w')
        
        # scrollbar.grid(row=0, column=1, sticky=NS)
        scrollbar.pack(side="right", fill="y")
        # storeDic = {1:"Cà phê", 2:"Sting vàng", 3:"Sting dâu", 4:"Bò cụng"}
        # for k,v in storeDic.items():
        #     lbl1 = Button(r, text=v, width=25)
        #     lbl1.pack(side=TOP)
        ldrink = Label(r, text="Đồ uống")
        ldrink.grid(row=0,column=1)
        for k,v in storeDicDrink.items():
            name = v["name"]
            price = v["price"]
            typeofFood = v["type"]
            lbl1 = Button(r, text=f'{v["name"]}\n {v["price"]}', width=24, height=5, command=lambda name=name, price=price, typeofFood=typeofFood: self.totalproduct(name, price, typeofFood))
            if k >= 5:
                if k%4 == 0:
                    lbl1.grid(row=k//4, column=4, pady=10)
                    # print(k//4)
                else:
                    lbl1.grid(row=k//4+1, column=k%4, pady=10)
            else:
                lbl1.grid(row=1, column=k, pady=10)
        
        
        lfastfood = Label(r, text="Đồ ăn nhanh")
        lfastfood.grid(row=len(storeDicDrink)//4+1,column=1)
        # print(len(storeDicDrink)//4+1)
        for k,v in storeDicFastFood.items():
            lbl1 = Button(r, text=v, width=24, height=5)
        #     lbl1.grid(row=3, column=k, pady=10)
            if k >= 5:
                if k%4 == 0:
                    lbl1.grid(row=k//4+len(storeDicFastFood)//4+3, column=4, pady=10)
                    # print(k//4+len(storeDicFastFood)//4+3)
                else:
                    lbl1.grid(row=k//4+len(storeDicFastFood)//4+4, column=k%4, pady=10)
            else:
                lbl1.grid(row=len(storeDicDrink)//4+2, column=k, pady=10)
        
        
        # lordermore = Label(r, text="Gọi thêm")
        # lordermore.grid(row=len(storeDicDrink)//4+1+len(storeDicFastFood)//4+1,column=1)
        # for k,v in storeDicOrderMore.items():
        #     lbl1 = Button(r, text=v, width=24, height=5)
        #     # lbl1.grid(row=5, column=k, pady=10)
        #     if k >= 5:
        #         if k%4 == 0:
        #             lbl1.grid(row=k//4+len(storeDicOrderMore)//4+1+len(storeDicDrink)//4+1, column=4, pady=10)
        #             # print(k//4)
        #         else:
        #             lbl1.grid(row=k//4+len(storeDicOrderMore)//4+1+len(storeDicDrink)//4+1, column=k%4, pady=10)
        #     else:
        #         lbl1.grid(row=len(storeDicFastFood)//4+2+len(storeDicDrink)//4+2, column=k, pady=10)
        # scrollbar.config(command=ldrink.yview)


    def bill(self, r):
        ldrink = Label(r, text="Đồ uống")
        ldrink.grid(row=0,column=1)
        for k,v in storeDicDrink.items():
            ldrink = Label(r, text=v)
            ldrink.grid(row=k,column=1)
            # lbl1 = Button(r, text=v width=24, height=5)
            # lbl1.grid(row=1, column=k, pady=10)
        # print(self.total)
    

# import tkinter as tk       
# import threading

# class Application(tk.Frame):              
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)   
#         self.grid()                       
#         self.createWidgets()

#     def printHello(self):
#         print("Hello")

#     def createWidgets(self):
#         self.quitButton = tk.Button(self, text='Quit',
#             command=self.quit) # exits background (gui) thread
#         self.quitButton.grid(row=1,column=0)    
#         self.printButton = tk.Button(self, text='Print',command=lambda: self.printHello())         
#         self.printButton.grid(row=1,column=1) 

# def runtk():  # runs in background thread
#     app = Application()                        
#     app.master.title('Sample application')     
#     app.mainloop()
    
# thd = threading.Thread(target=runtk)   # gui thread
# # thd.daemon = True  # background thread will exit if main thread exits
# thd.start()  # start tk loop

# Python program to create a table
  
from tkinter import *
from windows_services import *

list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
a = len(list)
# print(a)
length = 500//a 
ws = Tk()
ws.geometry("500x500")

# def clicked(*args):
#     print("test click")

def open_new_window(test):
        # print(test)
        app = Windows_Services()
        app.title(f'Cửa sổ giao dịch bàn {test}')
        app.geometry("700x500")

canvas = Canvas(ws, width=500, height=500, bg="#7698A6")
canvas.pack(side=RIGHT)
count = 0 
for i in range(a):
    y = i * length
    for j in range(a):
        tablename = 'D'+str(count)
        x = j * length
        canvas.create_rectangle(x, y, x+length, y+length, fill="#D97E4A", tags=tablename)
        canvas.create_text(x+length-50, y+length-50, text=f'D{count}', fill="white")
        canvas.tag_bind(tablename,"<Button-1>",lambda _, tablename=tablename: open_new_window(tablename))
        count+=1

f = Frame(ws, width=200, height=500, bg="#F23E2E")
f.pack(side=RIGHT)





ws.resizable(False, False) # fixed size disable resize
ws.mainloop()
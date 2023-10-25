from tkinter import *
import tkinter as tk

def clearFrame(r):
    # destroy all widgets from frame
    for widget in r.winfo_children():
       widget.destroy()
    
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    r.pack_forget()

def funcBtn(name, r):
    clearFrame(r)
    r.pack(side="top", fill="both", expand="True")
    match name:
        case "menu":
            # lbl = Label(r, text="Menu", width=25)
            # lbl.pack()
            menu_services(r)
        case "chat":
            chat_services(r)
        case "bill":
            lbl = Label(r, text="Thanh toan", width=25)
            lbl.pack()

def test(txt, r):
    res = txt.get()
    lbl = Label(r, text=res, width=25)
    lbl.pack(side="bottom")
    print(res)

def menu_services(r):
    storeDic = {1:"Cà phê", 2:"Sting vàng", 3:"Sting dâu", 4:"Bò cụng"}
    for k,v in storeDic.items():
        lbl1 = Button(r, text=v, width=25)
        lbl1.pack(side=TOP)

def chat_services(r):
    # lbl = Label(r, text="Nhap ten cua ban", width=25)
    # txt = Entry(r, width=25)
    # submit = Button(r, text="Xac nhan", width=25, command=lambda: test(txt, r))
    # lbl.pack(side="left")
    # txt.pack(side="left")
    # submit.pack(side="left")

    #GUI chat
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    #create new frame
    newFrame = Frame(r)
    newFrame.grid(row=0, column=0)
    
    txt = Text(newFrame, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=64, height=20)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.968)

    e = Entry(newFrame, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=59)
    e.grid(row=2, column=0)

    send = Button(newFrame, text="Gửi", font=FONT_BOLD, bg=BG_GRAY)
    send.grid(row=2, column=1)

def windows_services():
    new_window = tk.Tk()
    new_window.geometry("700x500")
    new_window.title("Cửa sổ giao dịch bàn số ...")

    frame = Frame(new_window)
    frame.pack()
    toolbar = Frame(frame, height=100, bg="black")
    main = Frame(frame, width=700, height=500, bg="red")
    # bottom = Frame(frame, width=700, height=500, bg="skyblue3")

    toolbar.pack(side="top", fill="x")
    main.pack(side="top", fill="both", expand=True)
    main.pack_propagate(False) # ngan khung tu dong co lai
    # bottom.pack(side="top", fill="both", expand=False)
    
    lbl = Button(toolbar, text="Menu", width=32, command=lambda: funcBtn("menu",main))
    lbl.pack(side=LEFT)

    lbl1 = Button(toolbar, text="Chat", width=32, command=lambda: funcBtn("chat",main))
    lbl1.pack(side = LEFT)

    lbl2 = Button(toolbar, text="Đơn hàng", width=32, command=lambda: funcBtn("bill",main))
    lbl2.pack(side=LEFT)

    # maintree = Label(main, text="Main tree", width=25)
    funcBtn("menu",main)
    # maintree.pack(side="top")

    # bot = Label(bottom, text="bottom")
    # bot.pack()
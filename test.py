from tkinter import *

m1 = PanedWindow()
m1.pack()

r = Tk()
btn_menu = Button(r, text="Menu", width=25)
lbl = Label(m1, text="test", width=100, height=100)
m1.add(lbl)
m1.add(r)

# m2 = PanedWindow(m1, orient=VERTICAL)
# m1.add(m2)

# top = Scale( m2, orient=HORIZONTAL)
# m2.add(top)

# bottom = Button(m2, text="OK")
# m2.add(bottom)

mainloop()
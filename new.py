from tkinter import *
root=Tk()
v=IntVar()
e1=Entry(root,textvariable=v)
e1.pack()

def prt():
    print(1+v.get())
Button(root,text='print',command=prt).pack()
mainloop()


import tkinter
from tkinter import *
import time
import math
from tkinter import messagebox

tk = Tk()
# 界面大小800x600
tk.geometry('1000x700')
# 在界面中画出一个800*500的画布，画布颜色白色
cv = Canvas(tk, bg='white', width=800, height=500)
b1=25  #白色宽度
a1 = 15 #竖线宽度
b2=15
a2 = 15
rad = 0.1

s=1
c=0


e=tkinter.Entry(tk,show=None)
e.pack()

num=6
bk=num/2*(a2+b2)
kuan=400-bk



for i in range(0,800,(a1+b1)):
    cv.create_rectangle(i+a1/2, -20, 0, 600, width=a1)

cv.pack()


def rightl():
    global c
    c=0
    cv.delete("bob")
    for i in range(num):  # 生成n行斜线
        cv.create_line(i * (a2 + b2), 0,800 * math.tan(rad) + i * (a2 + b2), 800, tags='bob', width=b2)

def leftl():
    global c
    c = 0
    cv.delete("bob")
    for i in range(num):
        cv.create_line(800 * math.tan(rad) + i * (a2 + b2), 0, i * (a2 + b2), 800,
                       tags='bob', width=b2)

def rightr():
    global c
    c =800
    cv.delete("bob")
    for i in range(num):  # 生成n行斜线
             cv.create_line(800 - 2 * bk + 800 * math.tan(rad) + i * (a2 + b2), 0, 800 - 2 * bk + i * (a2 + b2), 800,
                       tags='bob', width=b2)
def leftr():
    global c
    c = 800
    cv.delete("bob")
    for i in range(num):
        cv.create_line(800 - 2 * bk + i * (a2 + b2), 0, 800 - 2 * bk + 800 * math.tan(rad) + i * (a2 + b2), 800,
                       tags='bob', width=b2)


def right():#向右斜
    global c,d
    c=400
    d=0
    cv.delete("bob")
    for i in range(num):   #生成n行斜线
         cv.create_line(kuan+i * (a2+b2), 0, kuan+800 * math.tan(rad) + i * (a2+b2), 800, tags='bob', width=b2)

def goright():

    global s,c,toright,toleft
    toright=1
    toleft=0
    s=1
    while 1:
        if s==1:
            if c<=800:
                cv.move('bob', num, 0)
                cv.pack()
                tk.update()  # 更新框架，强制显示改变
                time.sleep(0.05)
                c+=(num)
            else:
                if d==0:
                    rightl()
                if d==1:
                    leftl()
                goright()
        else:

            return 0

def left():
    global c,d
    d=1
    c = 400
    cv.delete("bob")
    for i in range(num):
            cv.create_line((800 - (kuan+i * (a2+b2))), 0, 800 - (kuan+800 * math.tan(rad) + i * (a2+b2)), 800, tags='bob',width=b2)

def goleft():
    global s, c, toright, toleft
    toright = 0
    toleft = 1
    s=1

    while 1:
        if s==1:
            if c>=0:
                cv.move('bob', -num, 0)
                cv.pack()
                tk.update()  # 更新框架，强制显示改变
                time.sleep(0.05)
                c-=num
            else:
                if d == 1:
                    rightr()
                if d == 0:
                    leftr()
                goleft()
        else:

            return 0



def stop():

    global s
    s=-s
    print(s)

L = tkinter.Button(tk, text ="left", command = left)
R = tkinter.Button(tk, text ="right", command = right)
STOP=tkinter.Button(tk, text ="stop", command = stop)
gr=tkinter.Button(tk, text ="go right", command = goright)
gl=tkinter.Button(tk, text ="go left", command = goleft)

gl.pack()
gr.pack()
L.pack()
R.pack()
STOP.pack()
cv.mainloop()
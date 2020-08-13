import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import *
# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l.pack()  # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
cv = canvas(bg = 'white')
#创建一个矩形，坐标为(矩形左上角点的X坐标，矩形左上角点的Y坐标，矩形的长，矩形的宽)
cv.create_rectangle(10,10,110,110)
cv.pack()

# 第6步，主窗口循环显示
window.mainloop()
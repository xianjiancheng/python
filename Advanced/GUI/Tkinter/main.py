#/usr/bin/python

import Tkinter
import tkMessageBox
top = Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo("hello  Python", "Hello world")

B = Tkinter.Button(top, text = "hello" , command = helloCallBack )
B.pack()
top.mainloop()

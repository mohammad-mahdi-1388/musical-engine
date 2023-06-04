#import
from tkinter import *
import mojols
d=mojols.d
win=Tk()
#size
win.geometry("")
win.minsize(600,600)
win.maxsize(800,800)
# libel
libel=Label(win,text= 'inter yor user')
libel.pack()
# input
input1=Entry(win)
input1.pack()
input2=Entry(win)
input2.pack()
# Button def
def Button1 ():
    libel1=Label(win,)
    libel1.pack()
    if input1 in d and d[input1]==input2:
        libel1.config(win,text='wellcom')
        libel1.pack()
    else:
        libel1.config(win, text='try agen')
        libel1.pack()
    print('mmaahhddii')
button=Button(text='chlik here',command=Button1)
button.pack()
input2.pack()
win.mainloop()

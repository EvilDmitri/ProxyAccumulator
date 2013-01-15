__author__ = 'dmitri'
from Tkinter import *

root = Tk()


r = ['Linux','Python','Tk','Tkinter']
lis = Listbox(root,selectmode=SINGLE,height=4)
for i in r:
     lis.insert(END,i)

lis.pack()

root.mainloop()
from tkinter import *
from tkinter import ttk


win = Tk()
win.title('Book cafe')
win.geometry('520x400')
win.configure(bg='#000000')
win.resizable(width=False,height=False)

frame_up = Frame(win, width=520, height=30, bg='white')
frame_up.grid(row=0,column=0,padx=0,pady=1)
frame_down = Frame(win, width=520, height=150, bg='red')
frame_down.grid(row=1,column=0,padx=0,pady=1)
frame_table = Frame(win, width=520, height=300, bg='white')
frame_table.grid(row=2,column=0,columnspan=2, padx=0,pady=1,sticky=EW)

listheader = ['id','Название','Автор','Жанр','Секция']
tree = ttk.Treeview(frame_table,selectmode='extended',columns=listheader,show='headings')
vsb = ttk.Scrollbar(frame_table,orient='vertical',command=YView)
hsb = ttk.Scrollbar(frame_table,orient='horizontal',command=XView)

tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
tree.grid(column=0,row=0,sticky='nsew')
vsb.grid(column=1,row=0,sticky='ns')
hsb.grid(column=0,row=1,sticky='ew')

tree.heading(0, text='id', anchor=NW)
tree.heading(1, text='Название', anchor=NW)
tree.heading(2, text='Автор', anchor=NW)
tree.heading(3, text='Жанр', anchor=NW)
tree.heading(4, text='Секция', anchor=NW)

tree.column(0,width=40,anchor='nw')
tree.column(1,width=120,anchor='nw')
tree.column(2,width=120,anchor='nw')
tree.column(3,width=120,anchor='nw')
tree.column(4,width=120,anchor='nw')





from frame_books import *
from booksdb import *

books_data()


def add(event,book_name,author,style,section):
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO books ('name','author','style','section') VALUES (?,?,?,?)",
            (book_name,
            author,
            style,
            section))
    view_data()

def view_data():
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute('''SELECT * FROM books''')
        [tree.delete(i) for i in tree.get_children()]
        rows = cur.fetchall()
        [tree.insert('','end',values=row) for row in rows]
    


def delete_rec():
    for selection_item in tree.selection():
        with sq.connect('books.db') as con:
            cur = con.cursor()
            cur.execute('''DELETE FROM books WHERE book_id=?''',(tree.set(selection_item,'#1'),))
        view_data()

def search(event,book_name,author,style,section):
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(
            '''SELECT * FROM books WHERE name=? OR author=? OR style=? OR section=?''',
            (book_name,author,style,section))
        [tree.delete(i) for i in tree.get_children()]
        rows = cur.fetchall()
        [tree.insert('','end',values=row) for row in rows]

def update(event,book_name,author,style,section):
    with sq.connect('books.db') as con:
        cur = con.cursor()
        cur.execute(
            '''UPDATE books SET name=?, author=?, style=?, section=? WHERE book_id=?''',
            (book_name,author,style,section,tree.set(tree.selection()[0],'#1')))
    view_data()

app_name = Label(frame_up,text='Book cafe', height=1, font=('Verdana 15 bold'),fg='red',bg='white' )
app_name.place(x=5,y=5)

#frame_down widgets
l_name = Label(frame_down, text='Название', width=20,height=1, font=('Ivy 13'),bg='red',anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_name.place(x=80,y=20)

l_style = Label(frame_down, text='Жанр', width=20,height=1, font=('Ivy 13'),bg='red',anchor=NW)
l_style.place(x=10,y=50)
e_style = ttk.Combobox(frame_down,width=25)
e_style['values'] = ['Фэнтэзи','Роман','Детектив']
e_style.place(x=80,y=50)

l_author = Label(frame_down, text='Автор', width=20,height=1, font=('Ivy 13'),bg='red',anchor=NW)
l_author.place(x=10,y=80)
e_author = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_author.place(x=80,y=80)

l_section = Label(frame_down, text='Секция', width=20,height=1, font=('Ivy 13'),bg='red',anchor=NW)
l_section.place(x=10,y=110)
e_section = ttk.Combobox(frame_down,width=25)
e_section['values'] = ['A','B','C','D']
e_section.place(x=80,y=110)



b_search = Button(frame_down, text='Найти', height=1,bg='white',fg='red',font=('Ivy 8 bold'))
b_search.place(x=400,y=20)
b_search.bind('<Button-1>',lambda event:search(event,e_name.get(),e_author.get(),e_style.get(),e_section.get()) )

b_add = Button(frame_down, text='Добавить', height=1,bg='white',fg='red',font=('Ivy 8 bold'))
b_add.bind('<Button-1>',lambda event:add(event,e_name.get(),e_author.get(),e_style.get(),e_section.get()) )
b_add.place(x=400,y=50) 
b_update = Button(frame_down, text='Редактировать', height=1,bg='white',fg='red',font=('Ivy 8 bold'))
b_update.bind('<Button-1>',lambda event:update(event,e_name.get(),e_author.get(),e_style.get(),e_section.get()) )
b_update.place(x=400,y=80)

b_delete = Button(frame_down, text='Удалить', height=1,bg='white',fg='red',font=('Ivy 8 bold'),command=delete_rec)
b_delete.place(x=400,y=110)

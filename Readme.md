# GUI Pyhton приложение 'Book cafe' c использованием Tkinter и sqlite3

## Информационная система 'Book cafe' позволяет вносить,редактировать,удалять в базу данных а также искать информацию о книгах

## Приложение разбито на 4 модуля:

* **frame_books**
  * Создал окно с помощью класса tk.TK()
  * Создал три контейнера класса Frame (frame_up,frame_down,frame_table)
  * импортирован модуль ttk и реализован виджет Treeview c колонками (id, name, author, style, section)

* **btn**
  *  Созданы поля ввода Entry и кнопки Buttons
  *  при нажатии на соответствующие кнопки через метод bind вызываеться одна из функций - add, delete, search, view  или update. И с помощью execute извлекаеться SQL запрос из БД books_db
  
* **booksdb** 
  * в фунцкции books_data реализованно соединение с БД books_db с помощью модуля sqlite3 c полями (book_id,name, author,style и section)

* **main**
  * Импорт мoдулей booksdb , btn и запуск win.mainloop()
  


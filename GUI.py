from tkinter import *

root = Tk()


def create_new_list():
    create_new_list_window = Toplevel()
    l1 = Label(create_new_list_window,
               text='Тут будет описано создание нового списка. Потом :)',
               height=0,
               width=100
               )
    l1.pack()

    b1 = Button(create_new_list_window,
                text='Выход',
                height=2,
                width=6,
                command=exit
                )

    b1.pack()


new_list = Button(
            text="Новый список",
            command=create_new_list
)

new_list.pack()


root.mainloop()

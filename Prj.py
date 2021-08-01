from tkinter import *

def add_item():
    box.insert(END, entry.get())
    entry.delete(0, END)

def add_item1():
    box1.insert(END, entry.get())
    entry.delete(0,END)

def del_list():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)

def save_list():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(box.get(0, END)))
    f.close()

def a():
    box1.insert(END, box.get([0],[-1]))
    box.insert(END,box1.get([0],[-1]))
root = Tk()
root.geometry('500x500')

box = Listbox(selectmode=EXTENDED)
box.pack(side=LEFT)

box1 = Listbox(selectmode=EXTENDED)
box1.pack(side=RIGHT)


f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
Button(f, text='Add to 1st listbox', command=add_item) \
    .pack(fill=X)
Button(f, text='>>', command=a) \
    .pack(fill=X)
Button(f, text='<<', command=a) \
    .pack(fill=X)
Button(f, text='Add to 2nd listbox', command=add_item1) \
    .pack(fill=X)

# for i in ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница','Cуббота','Воскресенье'):
#     lbox.insert(0, i)

root.mainloop()

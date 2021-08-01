from tkinter import *


def motion(x, y):
    if c.coords(ball)[2] < x:
        x_dir = 1
    elif c.coords(ball)[2] > x:
        x_dir = -1
    else:
        x_dir = 0

    if c.coords(ball)[3] < y:
        y_dir = 1
    if c.coords(ball)[3] > y:
        y_dir = -1
    else:
        y_dir = 0

    if c.coords(ball)[2] != x or c.coords(ball)[3] != y:
        c.move(ball, x_dir, y_dir)
        # print(c.coords(ball))
        if c.coords(ball)[2] != x or c.coords(ball)[3] != y:
            root.after(10, motion(x, y))
    # print(c.coords(ball), )


root = Tk()
c = Canvas(root, width=600, height=400,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')


# motion()


def mousecords(event):
    print(event.x, event.y)


def clicked(event):
    x = event.x
    y = event.y
    motion(x + 20, y + 20)


root.bind('<Motion>', mousecords)
root.bind('<Button-1>', clicked)
root.mainloop()

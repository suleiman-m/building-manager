from tkinter import Tk, Canvas

def callback(event):
    draw(event.x, event.y)

def draw(x, y):
    paint.coords(circle, x-20, y-20, x+20, y+20)

root = Tk()
paint = Canvas(root)
circle = paint.create_oval(0, 0, 0, 0)
paint.tag_bind(circle,'<Motion>', callback)
paint.pack()

circle = paint.create_oval(0, 0, 0, 0)
root.mainloop()
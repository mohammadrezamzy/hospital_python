import tkinter as tk
from tkinter import messagebox as mb

top = tk.Tk()
top.geometry("250x170")

def hi_there():
    msg = mb.showinfo("text","hi_there")
    b.destroy()

b = tk.Button(top,text = "hello" , command = hi_there)
b.place(x = 50 , y= 50)
g = tk.Text(top,height = 5 , width =10)
fact = "hello"
g.insert(tk.END,fact)
g.pack()
top.mainloop()

















from tkinter import *
from tkinter import ttk
import tkinter as tk
"""
root = Tk()
frm = ttk.Frame(root, padding= 10)
frm.grid()
ttk.Label(frm, text= "Hello world!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
frm.geometry("300x200")

window = tk.Tk()
window.title("Hello world in another form")
window.geometry("200x300")
label = tk.Label(window, text="Hello world in a label:D")
label.pack(pady=20)
window.mainloop()
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My application")
root.geometry("640x400")

ttk.Label(root, text="Hello").pack(padx=20, pady=20)
ttk.Button(root, text="Button ola").pack(padx=20, pady=30)
root.mainloop()


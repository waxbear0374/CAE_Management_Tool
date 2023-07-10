import tkinter as tk 
from tkinter import ttk

from project_add import AddProject

#-- Main Setting
root = tk.Tk()
root.geometry("500x400")

#-- Style 지정
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.Labelframe(frame, text="Insert Row")
widgets_frame.grid(row=0, column=0)

name_label = ttk.Label(text="Test :", style="BW.TLabel")
name_label.pack()

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
name_entry.grid(row=2, column=0, sticky="ew")

button = ttk.Button(
    widgets_frame, 
    text="Add Project")
button.grid(row=3, column=0, sticky="nsew")

#AA=OnAddProjectLayout()

root.mainloop()
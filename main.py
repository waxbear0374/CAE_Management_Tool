import tkinter as tk 
from tkinter import * 
from tkinter import ttk
#from tkinter import messgaebox  

#from project_add import AddProject
def OnAddProjectLayout():
    win_add_project = tk.Tk()
    win_add_project.geometry("500x400")
    win_add_project.title("Add Project")
    
    #-- Style 지정
    style = ttk.Style(win_add_project)
    win_add_project.tk.call("source", "forest-light.tcl")
    win_add_project.tk.call("source", "forest-dark.tcl")
    style.theme_use("forest-dark")

    #-- Main Frame
    label_frame_add_project = ttk.Labelframe(win_add_project, text="Add Project")
    label_frame_add_project.pack(side="top", fill="both", expand=True)

    #-------------------------------------
    #-- Project Name
    #-------------------------------------
    #-- Frame
    frame_project_name = ttk.Frame(label_frame_add_project)
    frame_project_name.pack(side="top", fill="both")

    #-- Label
    label_project_name = ttk.Label(frame_project_name, text="Project Name :", style="BW.TLabel")
    label_project_name.pack(side="left", padx=2)

    #-- Entry
    entry_prject_name = ttk.Entry(frame_project_name)
    entry_prject_name.pack(side="left")

    print("ADD")
    #messagebox.showinfo("Button Clicked", "Somebody clicked!")

    win_add_project.mainloop()


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
    text="Add Project",
    command=OnAddProjectLayout)
button.grid(row=3, column=0, sticky="nsew")



root.mainloop()
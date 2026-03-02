import tkinter as tk
import crud

def add_item():
    item = entry.get()
    if item:
        crud.create(item)
        entry.delete(0, tk.END)
        refresh_list()

def refresh_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(crud.read()):
        listbox.insert(tk.END, f"{i}: {item}")

root = tk.Tk()
root.title("CRUD Básico")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Agregar", command=add_item).pack()

listbox = tk.Listbox(root)
listbox.pack()

refresh_list()
root.mainloop()
# import tkinter as tk

# window = tk.Tk()

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)

#     for j in range(0, 3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)

#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# window.mainloop()


import tkinter as tk
parent = tk.Tk()
parent.geometry("250x200")
label1 = tk.Label(parent,text = "A list of favourite languages...")
listbox = tk.Listbox(parent)
listbox.insert(1,"PHP")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")
label1.pack()
listbox.pack()
parent.mainloop()





import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)  # Place Label 1 at row 0, column 0

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)  # Place Label 2 at row 1, column 1

root.mainloop()
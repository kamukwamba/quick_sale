import customtkinter


app = customtkinter.CTk()
app.geometry("400x400")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tab_3 = tabview.add("tab 3")

tabview.set("tab 1")  # set currently visible tab

button = customtkinter.CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)

button2 = customtkinter.CTkButton(tab_3, text="working")
button2.pack(padx=20, pady=20)


app.mainloop()
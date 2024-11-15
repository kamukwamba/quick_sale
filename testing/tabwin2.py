import customtkinter


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.tab_one = self.add("tab 1")
        self.tab_two = self.add("tab 2")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab_one, text="Tab One")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self.tab_two, text="Tab Two")
        self.label2.grid(row=0, column=0, padx=20, pady=10)






class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self, anchor = "ne", corner_radius=3)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()


# master	root, frame, top-level
# width	width in px, tabs will be slightly smaller
# height	height in px, tabs will be slightly smaller
# corner_radius	corner radius in px
# border_width	border width in px
# fg_color	foreground color of the tabview itself and the tabs, tuple: (light_color, dark_color) or single color
# border_color	border color, tuple: (light_color, dark_color) or single color
# segmented_button_fg_color	foreground color of segmented button, tuple: (light_color, dark_color) or single color
# segmented_button_selected_color	selected color of segmented button, tuple: (light_color, dark_color) or single color
# segmented_button_selected_hover_color	selected hover color of segmented button, tuple: (light_color, dark_color) or single color
# segmented_button_unselected_color	unselected color of segmented button, tuple: (light_color, dark_color) or single color
# segmented_button_unselected_hover_color	unselected hover color of segmented button, tuple: (light_color, dark_color) or single color
# text_color	text color of segmented button, tuple: (light_color, dark_color) or single color
# text_color_disabled	text color of segmented buttons when widget is disabled, tuple: (light_color, dark_color) or single color
# command	function will be called when segmented button is clicked
# anchor	position of the segmneted button, default is "n", values are "nw", "n", "ne", "sw", "s", "se"
# state	"normal" or "disabled"


# Methods
# .configure(attribute=value, ...)

# All attributes can be configured and updated.
# .cget(attribute_name)

# Get values of all attributes specified as string.
# .tab(name)

# Returns reference to tab with given name. Can be used like a frame like this:

# button = customtkinter.CTkButton(master=tabview.tab("tab name"))

# .insert(index, name)

# Insert tab with name at position of index, name must be unique.
# .add(name)

# Add tab with name at the end, name must be unique.
# .index(name)

# Get index of tab with given name.
# .move(new_index, name)

# Move tab with name to given index.
# .rename(old_name, new_name)

# Rename tab.
# .delete(name)

# Delete tab with name.
# .set(name)

# Set tab with name to be visible.
# .get()
# Get name of tab that's currently visible.
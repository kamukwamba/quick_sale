import customtkinter
from CTkTable import *

root = customtkinter.CTk()

value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         []]

def row_selected(item_selected):
    row_number= item_selected['row']
    column_number= item_selected['column'] 
    value_out = item_selected['value']

    print(f"Row Number: {row_number}\nColumn Number: {column_number}\nValue: {value_out}")

table = CTkTable(master=root, row=5, column=5, values=value, hover_color="red", corner_radius=4, command=row_selected)
table.pack(expand=True, fill="both", padx=20, pady=20)


new_items = [5,4,3,2,1]
table.add_row(index = -1 ,values= [5,4,3,2,1])

root.mainloop()

# insert(row, column, value, *args): change specific cell index data
# .add_row(index, values)
# .add_column(index, values)
# .edit_row(row_num, *args): edit one full row at once
# .edit_column(column_num, *args): edit one full column at once
# .delete_row(index): remove one row
# .delete_column(index): remove one column
# .delete_rows(indices): remove mutliple rows
# .delete_columns(indices): remove multiple columns
# .edit(row, column): edit specific cell without changing the value
# .select(row, column): select one cell
# .select_row(row): select a row
# .get_selected_row(): get the values of the selected row
# .deselect_row(row): deselect a row
# .select_column(column): select a column
# .get_selected_column(): get the values of selected column
# .deselect_column(column): deselect a column
# .update_values(values): update all values at once
# .delete(row, column, *args): delete the data from specific index
# .get(): get all values
# .get(row, column): get specific cell value
# .get_row(row): get all values of a specific row
# .get_column(column): get all values of a specific column
# .configure(arguments): change other table attributes

# Parameter 	Description
# master 	parent widget
# values 	the default values for table
# row 	optional, set number of default rows
# column 	optional, set number of default columns
# padx 	add internal padding in x
# pady 	add internal padding in y
# colors 	set two fg_colors for the table (list), eg: colors=["yellow", "green"]
# color_phase 	set color phase based on rows or columns, eg: color_phase="vertical"
# orientation 	change the orientation of table, vertical or horizontal
# header_color 	define the topmost row color
# corner_radius 	define the corner roundness of the table
# hover_color 	enable hover effect on the cells
# wraplength 	set the width of cell text
# justify 	anchor the position of the cell text
# command 	specify a command when a table cell is pressed, [returns row, column, value]
# *other button parameters 	all other ctk button parameters can be passed
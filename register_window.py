import customtkinter as ctk
import pywinstyles
import os
from PIL import Image
from datetime import date
from CTkTable import *

from variables import *





class Register_Window(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.background()
        self.storeDetails()
        self.register_window()
        
    
    def background(self):
        background_image = ctk.CTkImage(light_image=Image.open(BACKGROUND_IMAGE), size=(int(WINDOW_WIDTH) +10,int(WINDOW_HEIGHT) + 10))
        
        background_image_label = ctk.CTkLabel(self, image=background_image, text="")
        background_image_label.place(relx = 0.5, rely=0.5, anchor = "center")


    def storeDetails(self):
        global BUSSINES_NAME
        global TEXT_COLOR
        global USER_LOGGED_IN
        header_frame = ctk.CTkFrame(master=self, corner_radius=(0), fg_color="#282A36")



        store_name = ctk.CTkLabel(master = header_frame, text=BUSSINES_NAME, text_color="white" ,font=("Times", 40))

        user_loggedd_in = ctk.CTkLabel(master = header_frame, text=USER_LOGGED_IN, text_color="white", font=("Times", 25))

        current_date = ctk.CTkLabel(master = header_frame, text="Enter Date", text_color="white", font=("Times", 20))


        store_name.pack(anchor="center")
        user_loggedd_in.pack(padx = 10, anchor = "nw")
        current_date.pack(padx = 10, anchor = "nw")

        header_frame.place(relheight = .15, relwidth=1, anchor='nw')
    

    
    
    def register_window(self):
        global FONT_NAME_N1
        global FONT_S1

        #THE MAIN REGISTER WINDOW
        register_frame = ctk.CTkFrame(master=self, corner_radius=(0))

        self.sale_Details(register_frame)
        self.sales_frame(register_frame)


        register_frame.place(relx=0, rely = 0.15,relheight = .85, relwidth = 1, anchor="nw")

    def sale_Details(self, parent):
        global ENTRY_FONT_DETAILS

        ENTRY_FONT_DETAILS = ("Times", 20)

        sales_frame = ctk.CTkFrame(master=parent, corner_radius=(0), fg_color="#282A36")

        entry_filds = ctk.CTkFrame(master=sales_frame, corner_radius=(0), fg_color="#282A36")

        buttons_frame =ctk.CTkFrame(master=sales_frame, corner_radius=(0), fg_color="#282A36")

        product_name = ctk.CTkLabel(master=entry_filds, text="Product ID",text_color="white", font=(FONT_NAME_N1, FONT_S1 ))
        product_name.grid(row = 1, column = 1, pady = 2, padx = 10, sticky="w" )

        product_quantity = ctk.CTkLabel(master=entry_filds, text="Qty",text_color="white" ,font=(FONT_NAME_N1, FONT_S1) )
        product_quantity.grid(row = 1, column = 2, pady = 2, padx = 2, sticky="w")

        cash_entered = ctk.CTkLabel(master=entry_filds, text="Cash",text_color="white" ,font=(FONT_NAME_N1, FONT_S1))
        cash_entered.grid(row = 1, column=3, pady = 2, padx=2, sticky="w")

        product_name_in = ctk.CTkEntry(master=entry_filds, font=ENTRY_FONT_DETAILS, corner_radius=(5), width=200, border_width=1)
        product_name_in.grid(row =2, column = 1, pady = 2, padx = 10, sticky="w", ipadx=10 )

        product_quantity_in = ctk.CTkEntry(master=entry_filds, font=ENTRY_FONT_DETAILS, corner_radius=(5), width=200, border_width=1)
        product_quantity_in.grid(row = 2, column = 2, pady = 2, padx = 2, sticky="w", ipadx=10)

        cash_entered_in = ctk.CTkEntry(master=entry_filds, font=ENTRY_FONT_DETAILS, corner_radius=(5), width=200, border_width=1)

        cash_entered_in.grid(row = 2, column = 3, pady = 2, padx = 2, sticky="w", ipadx=10)

    

        # BUTTONS 
        make_sale = ctk.CTkButton(master=buttons_frame, text="Sale",  corner_radius=3, height=35)
        next_customer = ctk.CTkButton(master=buttons_frame, text="Next Customer",  corner_radius=3, height=35)
        delete_sale = ctk.CTkButton(master=buttons_frame, text="Delete Sale",  corner_radius=3, height=35)


        make_sale.grid(row = 0, column = 0, pady=(10), padx=(10, 5), sticky="w", ipadx=0)
        next_customer.grid(row = 0, column = 1, pady=(10), padx=(0, 5), sticky="w", ipadx=0)
        delete_sale.grid(row = 0, column = 2 , pady=(10), padx=(0, 5), sticky="w", ipadx=0)

        

        


        entry_filds.place(relx = 0, rely = 0, relheight = .5, relwidth=1, anchor="nw")
        buttons_frame.place(relx = 0, rely = 0.5,relheight =5, relwidth=1, anchor="nw")
        sales_frame.place(relheight = .22, relwidth = 1, anchor="nw")


    

    def sales_frame(self, parent):

        table_frame = ctk.CTkFrame(master = parent, corner_radius = 0, fg_color="white")

        # WATCH COLOR CHANGE
        left_frame = ctk.CTkFrame(master=table_frame, corner_radius = 0, fg_color = "white")

        self.sales_table(left_frame)



        right_frame = ctk.CTkFrame(master=table_frame, corner_radius = 3)

        self.right_div(right_frame)


        # PLACING CODE ON SCREEN

        left_frame.place(relheight = 1, relwidth = .7, anchor="nw")
        right_frame.place(relx = 0.7, relheight=1, relwidth = .3, anchor="nw")

        table_frame.place(relx=0, rely = .22,relheight = .78, relwidth = 1, anchor="nw")


    def sales_table(self, parent):

        value = [["Product ID", "Price", "Qty", "Discount", "Tax", "Total"],]
        table_frame = ctk.CTkScrollableFrame(master = parent, corner_radius=0, fg_color="white")

        result_frame = ctk.CTkFrame(master=parent, corner_radius=0, fg_color="white")

        table = CTkTable(master=table_frame, row=1, column=6, values = value, corner_radius=(5), height=30)
        
        table.pack(expand=False, fill="both", padx=20, pady=20)


        total_text  = ctk.CTkLabel(master=result_frame, text="Total: ", font=(FONT_NAME_N1, FONT_S2))
        total_text.place(relx = 0, rely= .5,anchor = "nw")

        result_frame.place(relheight = .15, relwidth=1,relx=0, rely=.85, anchor="nw")

        table_frame.place(relheight = .85, relwidth = 1, anchor="nw")



    def right_div(self, parent):
        tab_view = ctk.CTkTabview(master=parent, anchor="nw", corner_radius=3, bg_color="#282A36", fg_color="#282A36")

        
        tab_view.add("Product IDs")
        tab_view.add("Key Pad")
        tab_view.add("Order")

        
        search_product = ctk.CTkFrame(master = tab_view.tab("Product IDs"), fg_color="white", corner_radius=0)
        
        product_name = ctk.CTkEntry(master=search_product, width=250, corner_radius=4, border_width=1, placeholder_text="Product Name")

        product_name.grid(row=0, column=0, pady=2, padx=4, sticky="w")

        

        search_button = ctk.CTkButton(master=search_product, text="Search", corner_radius=4, height=22)
        search_button.grid(row = 1, column = 0,  pady=2, padx=4, sticky="w")
        
        search_product.place(relheight=.14, relwidth=1, anchor="nw")

    

        pro_details_frame = ctk.CTkScrollableFrame(master=tab_view.tab("Product IDs"), fg_color="white", corner_radius=0)

        value = [["Product Name", "Product ID", "Price"]]
        pro_details_table = CTkTable(master=pro_details_frame, row=1, column=3, values = value, corner_radius=5, height=30)

        pro_details_table.pack(expand=False, fill="both", padx=20, pady=20)

        # working = ctk.CTkLabel(master=pro_details_frame, text="Workking")
        # working.pack()

        pro_details_frame.place(relheight=.86, relwidth=1, rely=.14, anchor="nw")


        tab_view.place(relheight=1, relwidth=1,anchor="nw")


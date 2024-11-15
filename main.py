import customtkinter as ctk
import pywinstyles
import os
from PIL import Image
from datetime import date
from CTkTable import *
from variables import *




from register_window import Register_Window

        
class Main(ctk.CTk):
    global WINDOW_HEIGHT
    global WINDOW_WIDTH
    global APP_ICON

    def __init__(self):
        super().__init__()
        self.title("Easy POS")
        self.iconbitmap(APP_ICON)
        self.geometry('400x550')
        self.resizable(False, False)
        self.centerwindow(WINDOW_WIDTH, WINDOW_HEIGHT)

        # LOGIN WINDOW  
        # self.loggin_window()
        
        #REGISTER WINDOW
        self.register_window()
        

        

        pywinstyles.change_border_color(self, color="#00ffff")

    def loggin_window(self):
        self.frame_one = Login_Window(parent=self, corner_radius=(0), fg_color = "white")
        self.frame_one.place(relheight = 1, relwidth=1, anchor='nw')

    def logger_window(self):
        self.frame_one = Logger_Window(parent=self, corner_radius=(0), fg_color = "white")
        self.frame_one.place(relheight = 1, relwidth=1, anchor='nw')


    def register_window(self):
        self.resize_window()
        self.frame_one = Register_Window(parent=self, corner_radius=(0), fg_color = "white")
        self.frame_one.place(relheight=1, relwidth=1, anchor="nw")
        

        self.set_resize()
        
        

    def centerwindow(self, window_width, window_height):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (int(window_width)/2))
        y_cordinate = int((screen_height/2) - (int(window_height)/2))

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def resize_window(self):
        self.resizable(True, True)
        self.state("zoomed")
    
    def set_resize(self):
        self.resizable(False, False)


 
        
        # screen_width = self.winfo_screenwidth()
       

    def full_window(self):
        self.wm_attributes("-fullscreen", True)

        
        
        





        



class Login_Window(ctk.CTkFrame):
    global LOGIN_IMAGE
    global BACKGROUND_IMAGE
    global ENTRY_FONTSIZE
    def __init__(self,parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.custome_background_image()
        self.user_image()
        self.login_entry(parent)
        self.water_mark()


    

    def custome_background_image(self):
        background_image = ctk.CTkImage(light_image=Image.open(BACKGROUND_IMAGE), size=(int(WINDOW_WIDTH) +10,int(WINDOW_HEIGHT) + 10))
        
        background_image_label = ctk.CTkLabel(self, image=background_image, text="")
        background_image_label.place(relx = 0.5, rely=0.5, anchor = "center")


    def user_image(self):
        login_image = ctk.CTkImage(light_image=Image.open(LOGIN_IMAGE), size=(190,190))
        
        image_label = ctk.CTkLabel(self, image=login_image, text="")
        image_label.place(relx = 0.25, rely=0.24, anchor = "center")
    
    def login_entry(self, parent):
        self.user_name_text = ctk.StringVar(value= "User Name")
        self.user_password_text = ctk.StringVar(value="User Password")
        self.user_name = ctk.CTkEntry(self, 
                                placeholder_text="User Name",
                                height=39,
                                width=250,
                                font=("", ENTRY_FONTSIZE))

        self.user_password = ctk.CTkEntry(self, 
                                    placeholder_text="User Password",
                                    height = 39,
                                    width=250,
                                    show="*",
                                    font=("", ENTRY_FONTSIZE))

        login_submit_button = ctk.CTkButton(self, 
                                            text="Login",
                                            height=35,
                                            fg_color=('#0761DC'),
                                            width=170,
                                            command=self.get_user_data)


        self.user_name.place(relx = 0.25,
                        rely = 0.55,
                        anchor="center")
        
        self.user_password.place(relx = 0.25,
                            rely = 0.66,
                            anchor="center")

        login_submit_button.place(relx = 0.25,
                            rely = 0.77,
                            anchor="center")
    

    def get_user_data(self):

        # GET USER NAME AND PASSWORD
        print("User Name: ", self.user_name.get())
        print("User Password: ", self.user_password.get())

        #CLEAR THE USER NAME AND PASSWORD ENTRY WIDGETS
        self.user_name.delete(0, "end")
        self.user_password.delete(0, "end")

        #FORGET THE LOGIN FRAME AND CREATE NEW WINDOW
        self.destroy()

        #LOAD LOGGER WINDOW
        self.parent.logger_window()
        


    def water_mark(self):
        water_mark = ctk.CTkLabel(master=self, 
                            width=150, height=25, 
                            corner_radius=5,
                            text='mulubwa technologies', 
                            bg_color="#000001", 
                            fg_color="#033B85", 
                            text_color="white",
                            font=("", 9)) 
        
        water_mark.place(relx=.5, rely=.97, anchor="center")
        pywinstyles.set_opacity(water_mark, color="#000001") 
    

class Logger_Window(ctk.CTkFrame):
    global ADMIN_IMAGE
    global STORE_COUNTER_IMAGE

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.custome_background_image()
        self.buttons_switch()

    def custome_background_image(self):
        background_image = ctk.CTkImage(light_image=Image.open(BACKGROUND_IMAGE), size=(int(WINDOW_WIDTH) +10,int(WINDOW_HEIGHT) + 10))
        
        background_image_label = ctk.CTkLabel(self, image=background_image, text="")
        background_image_label.place(relx = 0.5, rely=0.5, anchor = "center")


    def buttons_switch(self):
        admin_login_image =  ctk.CTkImage(light_image=Image.open(ADMIN_IMAGE), size=(150,150))
        store_counter_image =  ctk.CTkImage(light_image=Image.open(STORE_COUNTER_IMAGE), size=(150,150))
        image_back = ctk.CTkImage(light_image=Image.open(LOGOUT_LEFT), size=(40,40))

        
        admin_login_button  = ctk.CTkButton(master=self, 
                                            image=admin_login_image,
                                            width=150, 
                                            height=150,
                                            bg_color="white",
                                            command=self.admin_button,
                                            text="") 
        

        store_counter_button  = ctk.CTkButton(master=self, 
                                            image=store_counter_image,
                                            width=150, 
                                            height=150, 
                                            bg_color="#07A4EB", 
                                            command=self.store_button,
                                            text="") 
        
        store_back_button = ctk.CTkButton(master=self,
                                        image=image_back,
                                        width=10,
                                        height=10,
                                        bg_color="#07A4EB", 
                                        command=self.return_to_login,
                                        text="")

        store_counter_button.place(relx=0.70, rely=0.5 ,anchor="center")
        admin_login_button.place(relx=0.30, rely=0.5 ,anchor="center")
        store_back_button.place(relx=0.04, rely=0.06 ,anchor="center")



        pywinstyles.set_opacity(store_back_button, color="#000001")
        pywinstyles.set_opacity(admin_login_button, color="white") 
        pywinstyles.set_opacity(store_counter_button, color="#07A4EB") 

        # admin_login_button.bind("<ButtonPress-1>", self.admin_button)  
        # store_counter_button.bind("<ButtonPress-1>", self.store_button)  


    def store_button(self):
        self.destroy()

        #LOAD LOGGER WINDOW
        self.parent.register_window()

    def admin_button(self):
        print("admin button pressed")
        
    def return_to_login(self):

        #FORGET THE LOGIN FRAME AND CREATE NEW WINDOW
        self.destroy()

        #LOAD LOGGER WINDOW
        self.parent.loggin_window()
        



    
  
        

      
    


app = Main()


app.mainloop()
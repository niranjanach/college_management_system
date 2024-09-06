import subprocess
import sys

try:
    from tkintertable import TableCanvas, TableModel


except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'tkintertable'])
    from tkintertable import TableCanvas, TableModel
try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox as mb
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'tk'])
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox as mb

    print('sucss')

from PIL import ImageTk, Image
import os
import csv
import time,pickle,datetime,re


class main:

    def __init__(self, master):

        self.window_base_height = 1440
        self.window_base_width = 2560
        self.master = master
        self.window_height = master.winfo_screenheight()
        self.window_width = master.winfo_screenwidth()
        self.master.geometry('%dx%d+0+0' % (self.window_width, self.window_height))
        self.counter = 0
        self.department_values = []
        self.jobtitle_values = []
        self.username = StringVar()
        self.password = StringVar()

        self.textbox_variable_password = StringVar()
        self.textbox_variable_username = StringVar()
        self.idno = StringVar()
        self.basicpay = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.contactnumber = StringVar()
        self.dateofjoining = StringVar()
        self.qualification = StringVar()
        self.department = StringVar()
        self.jobtitle = StringVar()

        self.reg_var = StringVar()
        self.sub_var = StringVar()
        self.add_sub_var = StringVar()

        with open('database\\text\department.txt', 'r') as file:
            self.department_values = file.read().split(',')
        with open('database\\text\job title.txt', 'r') as file:
            self.jobtitle_values = file.read().split(',')

    def resize_image(self, img_loc, img_width, img_height):
        self.img = Image.open(img_loc)
        self.resized = self.img.resize((img_width, img_height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resized)
        if '.png' in img_loc:

            self.resized.save('img/login.png', quality=100)
        else:
            self.resized.save('img/login.gif', quality=100)
        return self.img

    def widgets_resizer(self, height=0, width=0):

        self.widget_height = height
        self.widget_width = width

        self.window_height_ratio = self.window_height / self.window_base_height
        self.window_widht_ratio = self.window_width / self.window_base_width

        if self.widget_width == 0:
            return int(self.widget_height * self.window_height_ratio)
        elif self.widget_height == 0:
            return int(self.widget_width * self.window_widht_ratio)

    def login_window(self, back=None):
        if back == 'true':
            self.background_image_login_window.destroy()
            self.frame_login_window.destroy()
        elif back == 'true1':
            self.save_window(loc='logout')
            self.background_image_main_window.destroy()
            self.frame_main_window.destroy()

        self.database_initiation(filename='staff')

        # self.resize_image("img\login_background.png",self.window_width,self.window_height)

        # self.img = Image.open("img\login_background.png")
        # self.resized = self.img.resize((self.window_width,self.window_height),Image.ANTIALIAS)
        # self.img = ImageTk.PhotoImage(self.resized)

        self.master.title('LOGIN')
        self.background_image_login_window = Canvas(self.master, width=self.window_width, height=self.window_height)
        self.background_image_login_window.pack()
        self.background_image = self.resize_image("img\login_background.png", self.window_width, self.window_height)
        self.background_image_login_window.create_image(0, 0, anchor=NW, image=self.background_image)

        self.frame_login_window = Frame(self.background_image_login_window,
                                        height=self.widgets_resizer(height=1440 // 2 + 100),
                                        width=self.widgets_resizer(width=2560 // 2 + 100), bg='#00cfff',
                                        highlightthickness=10, highlightbackground='#002639', highlightcolor='black',
                                        bd=10, relief='groove')
        self.frame_login_window.place(relx=0.5, rely=0.5, anchor=CENTER)

        # self.panel = Label(self.frame_login_window)
        # self.panel.pack(side="bottom", fill="both", expand="yes")
        # self.panel.

        self.login_button = Button(self.frame_login_window, text='LOGIN', height=self.widgets_resizer(height=2),
                                   width=self.widgets_resizer(width=60), font=('Courier ', 15, 'bold'), bg='#0040ef',
                                   activebackground='#0040ef',
                                   relief='groove', bd=4, command=self.login_process)
        self.login_button.place(relx=0.498, rely=0.75, anchor=CENTER)

        root.bind('<Return>',lambda event=None:self.login_button.invoke())

        self.lable_login = Label(self.frame_login_window, text='USER LOGIN', font=('Courier', 30, 'underline', 'bold'),
                                 bg='#00cfff')
        self.lable_login.place(relx=0.5, rely=0.2, anchor=CENTER)

        # self.username_lable = Label(self.frame_login_window,height=self.widgets_resizer(height=3), width=self.widgets_resizer(width=3),image=self.resize_image("img\lable_username.png",self.username_lable.winfo_reqwidth(), self.username_lable.winfo_reqheight()))
        # self.username_lable.place(relx=0.25,rely=0.4,anchor=CENTER)

        # self.username_lable.create_image(0, 0, anchor=NW,image=self.resize_image("img\username_lable.png",self.username_lable.winfo_reqwidth(), self.username_lable.winfo_reqheight()))

        self.lable_password = Label(self.frame_login_window, height=self.widgets_resizer(height=65),
                                    width=self.widgets_resizer(width=80), borderwidth=1, bg='#00bff5',
                                    highlightcolor='black', relief=GROOVE, )
        self.lable_password.place(relx=0.248, rely=0.55, anchor=CENTER)
        # self.lable_password.update()
        # self.lable_login.update()

        self.lable_password_image = self.resize_image("img\lable_password.gif", self.widgets_resizer(width=40),
                                                      self.widgets_resizer(height=55))
        self.lable_password.configure(image=self.lable_password_image)

        self.lable_username = Label(self.frame_login_window, height=self.widgets_resizer(height=65),
                                    width=self.widgets_resizer(width=80), borderwidth=1, bg='#00bff5',
                                    highlightcolor='black', relief=GROOVE, )
        self.lable_username.place(relx=0.248, rely=0.4, anchor=CENTER)

        self.lable_username_image = self.resize_image("img\lable_username.gif", self.widgets_resizer(width=40),
                                                      self.widgets_resizer(height=55))
        self.lable_username.configure(image=self.lable_username_image)

        # self.lable_password.create_image(0, 0, anchor=NW, image=self.resize_image("img\lable_password.png",self.lable_password.winfo_reqwidth(),self.lable_password.winfo_reqheight()))

        self.textbox_username = Entry(self.frame_login_window, textvariable=self.username,
                                      width=self.widgets_resizer(width=21), bg='#F5F5F5',
                                      font='Hlvetica 32 bold')
        self.textbox_username.place(relx=0.30, rely=0.4006, anchor=W)
        self.textbox_password = Entry(self.frame_login_window, textvariable=self.password,
                                      width=self.widgets_resizer(width=21), bg='#F5F5F5',
                                      font='Hlvetica 32 bold', show='*')
        self.textbox_password.place(relx=0.3, rely=0.5506, anchor=W)

        self.register_button = Button(self.frame_login_window, text='IF NOT REGISTERED',
                                      height=self.widgets_resizer(height=int(0.5)), width=self.widgets_resizer(width=30),
                                      activebackground='#00cfff',
                                      font=('Courier'), relief='flat', bg='#00cfff', command=lambda :self.registaration_window('1'))
        self.register_button.place(relx=0.698, rely=0.85, anchor=CENTER, )
        self.textbox_username.delete(0, END)
        self.textbox_password.delete(0, END)

    def database_initiation(self, filename):
        self.table_database_frame = Frame(self.master)
        self.table_database_frame.pack_forget()
        self.table_database = TableCanvas(self.table_database_frame)
        name = 'database\project\\' + filename + '.csv'

        self.table_database.importCSV(name)
        name = 'database\\' + filename + '.table'

        self.table_database.load(name)

    def login_process(self):
        search = [('Name', self.username.get(), '=', 'OR')]
        search_username = (self.table_database.model.getColumnData(columnIndex=0, filters=search))
        search_password = ''
        print(search_username)
        # print(self.username.get())
        if search_username == [self.username.get()]:  ### retreving password from the database
            for i in self.table_database.model.getAllCells():
                print([self.table_database.model.getAllCells()[i][0]])
                # print(search_username)
                if [self.table_database.model.getAllCells()[i][0]] == search_username:
                    print(self.table_database.model.getAllCells()[i][11])

                    search_password = self.table_database.model.getAllCells()[i][11]

            if search_password == self.password.get():

                self.background_image_login_window.destroy()
                self.frame_login_window.destroy()
                self.main_window()
        else:
            mb.showerror("Username/Passowrd Error", "Please enter correct username/Password")

            self.textbox_username.delete(0, END)
            self.textbox_password.delete(0, END)

    def registaration_window(self,value):
        if value=='1':
            try:
                self.background_image_login_window.destroy()
                self.frame_login_window.destroy()
            except:
                pass
            self.registaration_process_value = 1
            root.title('REGISTRATION')
            self.background_image_login_window = Canvas(root, width=self.window_width, height=self.window_height)
            self.background_image_login_window.pack()
            self.background_image = self.resize_image("img\login_background.png", self.window_width, self.window_height)
            self.background_image_login_window.create_image(0, 0, anchor=NW, image=self.background_image)

            self.frame_login_window = Frame(self.background_image_login_window,
                                            height=self.widgets_resizer(height=int(1440 / 1.5)),
                                            width=self.widgets_resizer(width=int(2560 / 1.5)), bg='#00cfff',
                                            highlightthickness=10, highlightbackground='#002639',
                                            highlightcolor='black',
                                            bd=10, relief='groove')
            self.frame_login_window.place(relx=0.5, rely=0.5, anchor=CENTER)

            self.login_button = Button(self.frame_login_window, text='CREATE ACCOUNT',
                                       height=self.widgets_resizer(height=2),
                                       width=self.widgets_resizer(width=60), font=('Courier ', 15, 'bold'),
                                       bg='#0040ef',
                                       relief='groove', bd=4,
                                       command=lambda: self.registaration_process(self.registaration_process_value))
            self.login_button.place(relx=0.5, rely=0.92, anchor=CENTER)

            self.lable_login = Label(self.frame_login_window, text='SIGN UP', font=('Ariel', 27, 'bold'), bg='#00cfff')
            self.lable_login.place(relx=0.5, rely=0.08, anchor=CENTER)

            self.lable_username = Label(self.frame_login_window,
                                        text='USERNAME', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_username.place(relx=0.2, rely=0.2, anchor=CENTER)

            self.lable_ID = Label(self.frame_login_window,
                                  text='ID No.', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_ID.place(relx=0.2, rely=0.3, anchor=CENTER)

            self.lable_gender = Label(self.frame_login_window,
                                      text='GENDER', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_gender.place(relx=0.2, rely=0.4, anchor=CENTER)

            self.lable_dob = Label(self.frame_login_window,
                                   text='DATE OF BIRTH', borderwidth=0, bg='#00cfff', font=('systemfixed', 10, 'bold'))
            self.lable_dob.place(relx=0.2, rely=0.5, anchor=CENTER)

            self.lable_address = Label(self.frame_login_window,
                                       text='ADDRESS', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_address.place(relx=0.2, rely=0.6, anchor=CENTER)

            self.lable_contactnumber = Label(self.frame_login_window,
                                             text='CONTACT NUMBER', borderwidth=0, bg='#00cfff',
                                             font=('systemfixed', 10, 'bold'))
            self.lable_contactnumber.place(relx=0.2, rely=0.7, anchor=CENTER)

            self.lable_dateofjoining = Label(self.frame_login_window,
                                             text='DATE OF JOINING', borderwidth=0, bg='#00cfff',
                                             font=('systemfixed', 10, 'bold'))
            self.lable_dateofjoining.place(relx=0.62, rely=0.2, anchor=CENTER)

            self.lable_qualification = Label(self.frame_login_window,
                                             text='QUALIFICATION', borderwidth=0, bg='#00cfff',
                                             font=('systemfixed', 12, 'bold'))
            self.lable_qualification.place(relx=0.62, rely=0.3, anchor=CENTER)

            self.lable_department = Label(self.frame_login_window,
                                          text='DEPARTMENT', borderwidth=0, bg='#00cfff',
                                          font=('systemfixed', 12, 'bold'))
            self.lable_department.place(relx=0.62, rely=0.4, anchor=CENTER)

            self.lable_jobtitle = Label(self.frame_login_window,
                                        text='JOB TITLE', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_jobtitle.place(relx=0.62, rely=0.5, anchor=CENTER)

            self.lable_basicpay = Label(self.frame_login_window,
                                        text='BASIC PAY', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_basicpay.place(relx=0.62, rely=0.6, anchor=CENTER)

            self.lable_password = Label(self.frame_login_window,
                                        text='PASSWORD', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_password.place(relx=0.62, rely=0.7, anchor=CENTER)

            self.lable_admin = Label(self.frame_login_window,
                                     text='ACCEPT IF YOU ARE AN ADMIN', borderwidth=0, bg='#00cfff',
                                     font=('systemfixed', 12, 'bold'))
            self.lable_admin.place(relx=0.65, rely=0.8, anchor=CENTER)
            self.back_button_image = self.resize_image('img\\back.png', self.widgets_resizer(width=78),
                                                       self.widgets_resizer(height=50))
            self.back_button = Button(self.frame_login_window,
                                      height=self.widgets_resizer(height=50), border=0,
                                      width=self.widgets_resizer(width=70), bg='#00cfff', activebackground='#00cfff',
                                      relief='groove', image=self.back_button_image,
                                      command=lambda: self.login_window(back='true'))
            self.back_button.place(relx=0.03, rely=0.03, anchor=CENTER)

            self.gender = StringVar()
            admin_value = StringVar()
            self.textbox_username = Entry(self.frame_login_window, width=self.widgets_resizer(width=21), relief='groove',
                                          textvariable=self.textbox_variable_username,
                                          bd=2,
                                          bg='#F5F5F5', )
            self.textbox_username.place(relx=0.32, rely=0.2, anchor=W)

            self.textbox_idno = Entry(self.frame_login_window, width=self.widgets_resizer(width=21), relief='groove',
                                      bd=2,
                                      textvariable=self.idno,
                                      bg='#F5F5F5', )
            self.textbox_idno.place(relx=0.32, rely=0.3, anchor=W)

            self.textbox_gender_male = Radiobutton(self.frame_login_window, text='MALE', variable=self.gender, value='M',
                                                   activebackground='#00cfff',
                                                   bg='#00cfff', font=('systemfixed'))
            self.textbox_gender_male.place(relx=0.285, rely=0.4, anchor=W)
            self.textbox_gender_female = Radiobutton(self.frame_login_window, text='FEMALE', variable=self.gender,
                                                     value='F', activebackground='#00cfff',
                                                     bg='#00cfff', font=('systemfixed'))
            self.textbox_gender_female.place(relx=0.38, rely=0.4, anchor=W)

            self.textbox_dob = Entry(self.frame_login_window, width=self.widgets_resizer(width=21), relief='groove',
                                     bd=2,
                                     textvariable=self.dob,
                                     bg='#F5F5F5', )
            self.textbox_dob.place(relx=0.32, rely=0.5, anchor=W)
            self.textbox_dob.insert(0, 'dd-mm-yyyy')
            self.textbox_dob.bind('<FocusIn>', lambda a: self.textbox_dob.delete(0, 'end'))

            self.textbox_address = Entry(self.frame_login_window, width=self.widgets_resizer(width=21), relief='groove',
                                         textvariable=self.address,
                                         bd=2,
                                         bg='#F5F5F5', )
            self.textbox_address.place(relx=0.32, rely=0.6, anchor=W)
            # self.textbox_address.xview_scroll(0,'units')

            self.textbox_contactnumber = Entry(self.frame_login_window, width=self.widgets_resizer(width=21),
                                               textvariable=self.contactnumber,
                                               relief='groove', bd=2,
                                               bg='#F5F5F5', )
            self.textbox_contactnumber.place(relx=0.32, rely=0.7, anchor=W)

            self.textbox_dateofjoining = Entry(self.frame_login_window, width=self.widgets_resizer(width=21),
                                               textvariable=self.dateofjoining,
                                               relief='groove', bd=2,
                                               bg='#F5F5F5', )
            self.textbox_dateofjoining.place(relx=0.74, rely=0.2, anchor=W)
            self.textbox_dateofjoining.insert(0, 'dd-mm-yyyy')
            self.textbox_dateofjoining.bind('<FocusIn>', lambda a: self.textbox_dateofjoining.delete(0, 'end'))

            self.textbox_qualification = Entry(self.frame_login_window, width=self.widgets_resizer(width=21),
                                               textvariable=self.qualification,
                                               relief='groove', bd=2,
                                               bg='#F5F5F5', )
            self.textbox_qualification.place(relx=0.74, rely=0.3, anchor=W)

            self.textbox_department = ttk.Combobox(self.frame_login_window, width=self.widgets_resizer(width=21),
                                                   textvariable=self.department, )

            self.textbox_department['values'] = self.department_values
            self.textbox_department.current(1)
            self.textbox_department.config(state='readonly')
            self.textbox_department.place(relx=0.74, rely=0.4, anchor=W)

            self.textbox_jobtitle = ttk.Combobox(self.frame_login_window, width=self.widgets_resizer(width=21),
                                                 textvariable=self.jobtitle, )
            self.textbox_jobtitle['values'] = self.jobtitle_values
            self.textbox_jobtitle.current(1)
            self.textbox_jobtitle.config(state='readonly')
            self.textbox_jobtitle.place(relx=0.74, rely=0.5, anchor=W)

            self.textbox_basicpay = Entry(self.frame_login_window, width=self.widgets_resizer(width=21), relief='groove',
                                          textvariable=self.basicpay,
                                          bd=2,
                                          bg='#F5F5F5', )
            self.textbox_basicpay.place(relx=0.74, rely=0.6, anchor=W)

            self.textbox_password = Entry(self.frame_login_window, width=self.widgets_resizer(width=21), relief='groove',
                                          textvariable=self.textbox_variable_password,
                                          bd=2,
                                          bg='#F5F5F5', show='*')
            self.textbox_password.place(relx=0.74, rely=0.7, anchor=W)

            a = id_no_generator()
            self.textbox_idno.insert(0, a)
            self.textbox_idno.config(state='disabled')

            self.checkboutton_admin = Checkbutton(self.frame_login_window, variable=admin_value, onvalue='admin',
                                                  activebackground='#00cfff',
                                                  offvalue='not admin', bg='#00cfff', command=admin_signup)
            self.checkboutton_admin.place(relx=0.85, rely=0.8, anchor=CENTER)
            self.checkboutton_admin.deselect()

        if value =='2':
            #self.background_image_main_window.destroy()
            #self.frame_main_window.destroy()
            #root.lift()
            self.master7=Toplevel(self.master2)
            self.registaration_process_value = 1
            self.master7.title('REGISTRATION')
            self.background_image_login_windo = Canvas(self.master7, width=self.window_width-500, height=self.window_height-500)
            self.background_image_login_windo.pack()

            self.background_imag = self.resize_image("img\login_backgroun.png", self.window_width-500, self.window_height-500)
            self.background_image_login_windo.create_image(0, 0, anchor=NW, image=self.background_imag)

            self.frame_login_windo = Frame(self.background_image_login_windo,
                                            height=self.widgets_resizer(height=int((1440-500)/ 1.5)),
                                            width=self.widgets_resizer(width=int((2560 -500)/ 1.5)), bg='#00cfff',
                                            highlightthickness=10, highlightbackground='#002639',
                                            highlightcolor='black',
                                            bd=10, relief='groove')
            self.frame_login_windo.place(relx=0.5, rely=0.5, anchor=CENTER)

            self.login_button = Button(self.frame_login_windo, text='CREATE ACCOUNT',
                                       height=self.widgets_resizer(height=2),
                                       width=self.widgets_resizer(width=60), font=('Courier ', 15, 'bold'),
                                       bg='#0040ef',
                                       relief='groove', bd=4,
                                       command=lambda: self.registaration_process(self.registaration_process_value))
            self.login_button.place(relx=0.5, rely=0.92, anchor=CENTER)

            self.lable_login = Label(self.frame_login_windo, text='SIGN UP', font=('Ariel', 27, 'bold'), bg='#00cfff')
            self.lable_login.place(relx=0.5, rely=0.08, anchor=CENTER)

            self.lable_username = Label(self.frame_login_windo,
                                        text='USERNAME', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_username.place(relx=0.2, rely=0.2, anchor=CENTER)

            self.lable_ID = Label(self.frame_login_windo,
                                  text='ID No.', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_ID.place(relx=0.2, rely=0.3, anchor=CENTER)

            self.lable_gender = Label(self.frame_login_windo,
                                      text='GENDER', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_gender.place(relx=0.2, rely=0.4, anchor=CENTER)

            self.lable_dob = Label(self.frame_login_windo,
                                   text='DATE OF BIRTH', borderwidth=0, bg='#00cfff', font=('systemfixed', 10, 'bold'))
            self.lable_dob.place(relx=0.2, rely=0.5, anchor=CENTER)

            self.lable_address = Label(self.frame_login_windo,
                                       text='ADDRESS', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_address.place(relx=0.2, rely=0.6, anchor=CENTER)

            self.lable_contactnumber = Label(self.frame_login_windo,
                                             text='CONTACT NUMBER', borderwidth=0, bg='#00cfff',
                                             font=('systemfixed', 10, 'bold'))
            self.lable_contactnumber.place(relx=0.2, rely=0.7, anchor=CENTER)

            self.lable_dateofjoining = Label(self.frame_login_windo,
                                             text='DATE OF JOINING', borderwidth=0, bg='#00cfff',
                                             font=('systemfixed', 10, 'bold'))
            self.lable_dateofjoining.place(relx=0.62, rely=0.2, anchor=CENTER)

            self.lable_qualification = Label(self.frame_login_windo,
                                             text='QUALIFICATION', borderwidth=0, bg='#00cfff',
                                             font=('systemfixed', 12, 'bold'))
            self.lable_qualification.place(relx=0.62, rely=0.3, anchor=CENTER)

            self.lable_department = Label(self.frame_login_windo,
                                          text='DEPARTMENT', borderwidth=0, bg='#00cfff',
                                          font=('systemfixed', 12, 'bold'))
            self.lable_department.place(relx=0.62, rely=0.4, anchor=CENTER)

            self.lable_jobtitle = Label(self.frame_login_windo,
                                        text='JOB TITLE', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_jobtitle.place(relx=0.62, rely=0.5, anchor=CENTER)

            self.lable_basicpay = Label(self.frame_login_windo,
                                        text='BASIC PAY', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_basicpay.place(relx=0.62, rely=0.6, anchor=CENTER)

            self.lable_password = Label(self.frame_login_windo,
                                        text='PASSWORD', borderwidth=0, bg='#00cfff', font=('systemfixed', 12, 'bold'))
            self.lable_password.place(relx=0.62, rely=0.7, anchor=CENTER)

            self.lable_admin = Label(self.frame_login_windo,
                                     text='ACCEPT IF YOU ARE AN ADMIN', borderwidth=0, bg='#00cfff',
                                     font=('systemfixed', 12, 'bold'))
            self.lable_admin.place(relx=0.65, rely=0.8, anchor=CENTER)
           # self.back_button_image = self.resize_image('img\\back.png', self.widgets_resizer(width=78),
            #                                           self.widgets_resizer(height=50))
            #self.back_button = Button(self.frame_login_window,
            #                          height=self.widgets_resizer(height=50), border=0,
             #                         width=self.widgets_resizer(width=70), bg='#00cfff', activebackground='#00cfff',
            #                          relief='groove', image=self.back_button_image,
            #                          command=lambda: self.login_window(back='true'))
            #self.back_button.place(relx=0.03, rely=0.03, anchor=CENTER)

            self.gender = StringVar()
            admin_value = StringVar()
            self.textbox_username = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21), relief='groove',
                                          textvariable=self.textbox_variable_username,
                                          bd=2,
                                          bg='#F5F5F5', )
            self.textbox_username.place(relx=0.32, rely=0.2, anchor=W)

            self.textbox_idno = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21), relief='groove',
                                      bd=2,
                                      textvariable=self.idno,
                                      bg='#F5F5F5', )
            self.textbox_idno.place(relx=0.32, rely=0.3, anchor=W)

            self.textbox_gender_male = Radiobutton(self.frame_login_windo, text='MALE', variable=self.gender, value='M',
                                                   activebackground='#00cfff',
                                                   bg='#00cfff', font=('systemfixed'))
            self.textbox_gender_male.place(relx=0.285, rely=0.4, anchor=W)
            self.textbox_gender_female = Radiobutton(self.frame_login_windo, text='FEMALE', variable=self.gender,
                                                     value='F', activebackground='#00cfff',
                                                     bg='#00cfff', font=('systemfixed'))
            self.textbox_gender_female.place(relx=0.38, rely=0.4, anchor=W)

            self.textbox_dob = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21), relief='groove',
                                     bd=2,
                                     textvariable=self.dob,
                                     bg='#F5F5F5', )
            self.textbox_dob.place(relx=0.32, rely=0.5, anchor=W)
            self.textbox_dob.insert(0, 'dd-mm-yyyy')
            self.textbox_dob.bind('<FocusIn>', lambda a: self.textbox_dob.delete(0, 'end'))

            self.textbox_address = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21), relief='groove',
                                         textvariable=self.address,
                                         bd=2,
                                         bg='#F5F5F5', )
            self.textbox_address.place(relx=0.32, rely=0.6, anchor=W)
            # self.textbox_address.xview_scroll(0,'units')

            self.textbox_contactnumber = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21),
                                               textvariable=self.contactnumber,
                                               relief='groove', bd=2,
                                               bg='#F5F5F5', )
            self.textbox_contactnumber.place(relx=0.32, rely=0.7, anchor=W)

            self.textbox_dateofjoining = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21),
                                               textvariable=self.dateofjoining,
                                               relief='groove', bd=2,
                                               bg='#F5F5F5', )
            self.textbox_dateofjoining.place(relx=0.74, rely=0.2, anchor=W)
            self.textbox_dateofjoining.insert(0, 'dd-mm-yyyy')
            self.textbox_dateofjoining.bind('<FocusIn>', lambda a: self.textbox_dateofjoining.delete(0, 'end'))

            self.textbox_qualification = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21),
                                               textvariable=self.qualification,
                                               relief='groove', bd=2,
                                               bg='#F5F5F5', )
            self.textbox_qualification.place(relx=0.74, rely=0.3, anchor=W)

            self.textbox_department = ttk.Combobox(self.frame_login_windo, width=self.widgets_resizer(width=21),
                                                   textvariable=self.department, )

            self.textbox_department['values'] = self.department_values
            self.textbox_department.current(1)
            self.textbox_department.config(state='readonly')
            self.textbox_department.place(relx=0.74, rely=0.4, anchor=W)

            self.textbox_jobtitle = ttk.Combobox(self.frame_login_windo, width=self.widgets_resizer(width=21),
                                                 textvariable=self.jobtitle, )
            self.textbox_jobtitle['values'] = self.jobtitle_values
            self.textbox_jobtitle.current(1)
            self.textbox_jobtitle.config(state='readonly')
            self.textbox_jobtitle.place(relx=0.74, rely=0.5, anchor=W)

            self.textbox_basicpay = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21), relief='groove',
                                          textvariable=self.basicpay,
                                          bd=2,
                                          bg='#F5F5F5', )
            self.textbox_basicpay.place(relx=0.74, rely=0.6, anchor=W)

            self.textbox_password = Entry(self.frame_login_windo, width=self.widgets_resizer(width=21), relief='groove',
                                          textvariable=self.textbox_variable_password,
                                          bd=2,
                                          bg='#F5F5F5', show='*')
            self.textbox_password.place(relx=0.74, rely=0.7, anchor=W)

            a = id_no_generator()
            self.textbox_idno.insert(0, a)
            self.textbox_idno.config(state='disabled')

            self.checkboutton_admin = Checkbutton(self.frame_login_windo, variable=admin_value, onvalue='admin',
                                                  activebackground='#00cfff',
                                                  offvalue='not admin', bg='#00cfff', command=admin_signup)
            self.checkboutton_admin.place(relx=0.85, rely=0.8, anchor=CENTER)
            self.checkboutton_admin.deselect()


        def admin_signup():

            if admin_value.get() == 'admin':
                self.textbox_jobtitle.insert(0, 'Head Of Department')
                self.textbox_jobtitle.config(state='disabled', )

                self.registaration_process_value = 0

            else:

                self.textbox_jobtitle.delete(0, END)
                self.textbox_jobtitle.config(state='normal')
                self.registaration_process_value = 1

        def id_no_generator():
            self.database_initiation('staff')
            data = self.table_database.model.getAllCells()

            idno_generator_variable = data[len(data) - 1][1]
            return str(int(idno_generator_variable) + 1)



    def registaration_process(self, authority):
        if self.textbox_variable_username.get() == '' or self.textbox_variable_password.get() == '' or self.idno.get() == '' or self.gender.get() == '' or self.dob.get() == '' or self.address.get() == '' or self.contactnumber.get() == '' or self.dateofjoining.get() == '' or self.qualification.get() == '' or self.department.get() == '' or self.jobtitle.get() == '' or self.basicpay.get() == '':
            mb.showerror("EMPTY FIELDS", "Please fill all the fields")
        else:

            if authority == 0:

                self.database_initiation(filename='staff')
                self.table_database.addRow(Name=self.textbox_variable_username.get(), ID_No=self.idno.get(),
                                           Gender=self.gender.get(), Dob=self.dob.get(), Address=self.address.get(),
                                           Contact_number=self.contactnumber.get(),
                                           Date_of_Joining=self.dateofjoining.get(),
                                           Qualification=self.qualification.get(), Department=self.department.get(),
                                           Job_title=self.jobtitle.get(), Basic_pay=self.basicpay.get(),
                                           Password=self.textbox_variable_password.get())
                self.table_database.save(self.file_name_converter(files='staff'))
                self.background_image_login_window.destroy()
                self.frame_login_window.destroy()
                self.main_window()


            else:
                self.database_initiation(filename='staff')
                self.table_database.addRow(Name=self.textbox_variable_username.get(), ID_No=self.idno.get(),
                                           Gender=self.gender.get(), Dob=self.dob.get(), Address=self.address.get(),
                                           Contact_number=self.contactnumber.get(),
                                           Date_of_Joining=self.dateofjoining.get(),
                                           Qualification=self.qualification.get(),
                                           Department=self.department.get(), Job_title=self.jobtitle.get(),
                                           Basic_pay=self.basicpay.get(), Password=self.textbox_variable_password.get())

                self.table_database.save(self.file_name_converter(files='staff'))
                self.background_image_login_window.destroy()
                self.frame_login_window.destroy()
                self.main_window()

    def main_window(self):

        self.background_image_main_window = Canvas(root, width=self.window_width, height=self.window_height)
        self.background_image_main_window.pack()
        root.title('College Management System (CMS)')
        self.background_image = self.resize_image("img\login_background.png", self.window_width, self.window_height)
        self.background_image_main_window.create_image(0, 0, anchor=NW, image=self.background_image)
        self.frame_main_window = Frame(self.background_image_main_window,
                                       height=self.widgets_resizer(height=int(1440 / 1.5)),
                                       width=self.widgets_resizer(width=int(2560 / 1.5)), bg='#00cfff',
                                       highlightthickness=10, highlightbackground='#002639', highlightcolor='black',
                                       bd=10, relief='groove')
        self.frame_main_window.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.button_image = self.resize_image('img\\button_image.png', self.widgets_resizer(width=1500),
                                              self.widgets_resizer(height=200))

        self.logout_button = Button(self.frame_main_window, text='LOGOUT',
                                    width=self.widgets_resizer(width=15), font=('Courier ', 10, 'bold'), bg='#00cfff',
                                    activebackground='#00cfff', relief='groove',
                                    command=lambda: self.login_window(back='true1'))
        self.logout_button.place(relx=0.93, rely=0.04, anchor=CENTER)

        self.staff_button = Button(self.frame_main_window, text='STAFF REGISTER',
                                   height=self.widgets_resizer(height=200), compound=CENTER, border=0,
                                   command=lambda: self.create_window('database\project\staff'),
                                   width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'), bg='#00cfff',
                                   activebackground='#00cfff',
                                   relief='groove', image=self.button_image)
        self.staff_button.place(relx=0.5, rely=0.18, anchor=CENTER)

        self.student_button = Button(self.frame_main_window, text='STUDENT REGISTER', compound=CENTER, border=0,
                                     bg='#00cfff', activebackground='#00cfff',
                                     command=lambda: self.create_window('database\project\student'),
                                     width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                     relief='groove', image=self.button_image)
        self.student_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.result_button = Button(self.frame_main_window, text='RESULT REGISTER',
                                    height=self.widgets_resizer(height=200), compound=CENTER, border=0, bg='#00cfff',
                                    activebackground='#00cfff',
                                    command=lambda: self.create_window('database\project\\result'),
                                    width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                    relief='groove', image=self.button_image)
        self.result_button.place(relx=0.5, rely=0.62, anchor=CENTER)
        self.details_button = Button(self.frame_main_window, text='DETAILS', height=self.widgets_resizer(height=200),
                                     compound=CENTER, border=0, bg='#00cfff', activebackground='#00cfff',
                                     command=lambda: self.create_window(' '),
                                     width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                     relief='groove', image=self.button_image)
        self.details_button.place(relx=0.5, rely=0.84, anchor=CENTER)

    def back(self):
        self.frame_main_window = Frame(self.background_image_main_window,
                                       height=self.widgets_resizer(height=int(1440/1.5)),
                                       width=self.widgets_resizer(width=int(2560/1.5)), bg='#00cfff',
                                       highlightthickness=10, highlightbackground='#002639', highlightcolor='black',
                                       bd=10, relief='groove')
        self.frame_main_window.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.button_image = self.resize_image('img\\button_image.png', self.widgets_resizer(width=1500),
                                              self.widgets_resizer(height=200))

        self.staff_button = Button(self.frame_main_window, text='STAFF REGISTER',
                                   height=self.widgets_resizer(height=200), compound=CENTER, border=0,
                                   command=lambda: self.create_window('database\project\staff'),
                                   width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'), bg='#00cfff',
                                   activebackground='#00cfff',
                                   relief='groove', image=self.button_image)
        self.staff_button.place(relx=0.5, rely=0.18, anchor=CENTER)
        self.logout_button = Button(self.frame_main_window, text='LOGOUT',
                                    width=self.widgets_resizer(width=15), font=('Courier ', 10, 'bold'), bg='#00cfff',
                                    activebackground='#00cfff', relief='groove',
                                    command=lambda: self.login_window(back='true1'))
        self.logout_button.place(relx=0.93, rely=0.04, anchor=CENTER)

        self.student_button = Button(self.frame_main_window, text='STUDENT REGISTER', compound=CENTER, border=0,
                                     bg='#00cfff', activebackground='#00cfff',
                                     command=lambda: self.create_window('database\project\student'),
                                     width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                     relief='groove', image=self.button_image)
        self.student_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.result_button = Button(self.frame_main_window, text='RESULT REGISTER',
                                    height=self.widgets_resizer(height=200), compound=CENTER, border=0, bg='#00cfff',
                                    activebackground='#00cfff',
                                    command=lambda: self.create_window('database\project\\result'),
                                    width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                    relief='groove', image=self.button_image)
        self.result_button.place(relx=0.5, rely=0.62, anchor=CENTER)
        self.details_button = Button(self.frame_main_window, text='DETAILS', height=self.widgets_resizer(height=200),
                                     compound=CENTER, border=0, bg='#00cfff', activebackground='#00cfff',
                                     command=lambda: self.create_window(' '),
                                     width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                     relief='groove', image=self.button_image)
        self.details_button.place(relx=0.5, rely=0.84, anchor=CENTER)

    def add_rows(self, file, name):
        self.master4.destroy()
        rows = []

        self.student_table.addRow(Registration=str(int(name) + 1), DateOfAdmission=self.textbox_doa_variable.get(),
                                  Rollnumber=self.textbox_roll_variable.get(), Name=self.textbox_name_variable.get(),
                                  Gender=self.textbox_gender_variable.get(),
                                  DateofBirth=self.textbox_dob_variable.get(),
                                  Address=self.textbox_address_variable.get(),
                                  ParentPhoneNumber=self.textbox_ppno_variable.get(),
                                  Class=self.textbox_class_variable.get(), Section=self.textbox_section_variable.get())

        print(file)
        self.student_table.save(filename=self.file_name_converter(files=file))
        print(self.file_name_converter(files=file))

        b = self.open_data_files('database\\text\subject.dat')
        for i in b:
            print(i)
            print(self.textbox_class_variable.get())
            if i == self.textbox_class_variable.get():
                for c in b[i]:
                    rows += [c]
        print(rows)
        for a in range(len(rows)):
            if rows[a] == 'computerscience engineering':
                rows[a] = 'CSE'
            elif rows[a] == 'information technology':
                rows[a] = 'IT'
            elif rows[a] == 'mechanical engineering':
                rows[a] = 'MECH'
            elif rows[a] == 'civil engineering':
                rows[a] = 'CIVIL'

        with open('database\\project\\result register %d.csv' % (int(name) + 1), 'w', newline='') as file1:
            writer = csv.writer(file1)
            writer.writerow(['Registration Number', 'Subject Name',
                             'Mark Obtained', 'Pass Mark',
                             'Maximum',
                             'Result'])

            for data in rows:
                writer.writerow([str(int(name) + 1), data, '0', '0', '0', 'P'])

        if mb.askyesno('MODIFY', 'Want to Add Marks Obtained,Pass Mark,Maximum Mark and Result Now?'):
            self.search_reg(number=str(int(name) + 1))

    def create_window(self, file, ):
        def save_table():
            print(file)
            self.student_table.save(filename=self.file_name_converter(files=file))
            print(self.file_name_converter(files=file))
            self.master2.destroy()

        if file == ' ':
            self.back_button_image = self.resize_image('img\\back.png', self.widgets_resizer(width=78),
                                                       self.widgets_resizer(height=50))
            self.back_button = Button(self.frame_main_window,
                                      height=self.widgets_resizer(height=50), border=0,
                                      width=self.widgets_resizer(width=70), bg='#00cfff', activebackground='#00cfff',
                                      relief='groove', image=self.back_button_image, command=lambda: self.back())
            self.back_button.place(relx=0.03, rely=0.03, anchor=CENTER)

            self.staff_date_of_joining_button = Button(self.frame_main_window, text='STAFF DATE OF JOINING',
                                                       height=self.widgets_resizer(height=200), compound=CENTER,
                                                       border=0,
                                                       command=lambda: self.sort_staff_joining(),
                                                       width=self.widgets_resizer(width=1500),
                                                       font=('Courier ', 15, 'bold'),
                                                       bg='#00cfff', activebackground='#00cfff',
                                                       relief='groove', image=self.button_image)
            self.staff_date_of_joining_button.place(relx=0.5, rely=0.18, anchor=CENTER)

            self.date_of_admission_button = Button(self.frame_main_window, text='DATE OF ADMISSION', compound=CENTER,
                                                   border=0,
                                                   bg='#00cfff', activebackground='#00cfff',
                                                   command=lambda: self.sort_students_admission(),
                                                   width=self.widgets_resizer(width=1500),
                                                   font=('Courier ', 15, 'bold'),
                                                   relief='groove', image=self.button_image)
            self.date_of_admission_button.place(relx=0.5, rely=0.4, anchor=CENTER)
            self.class_button = Button(self.frame_main_window, text='STUDENTS CLASSES',
                                       height=self.widgets_resizer(height=200), compound=CENTER, border=0,
                                       bg='#00cfff', activebackground='#00cfff',
                                       command=lambda: self.sort_student_class(),
                                       width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                       relief='groove', image=self.button_image)
            self.class_button.place(relx=0.5, rely=0.62, anchor=CENTER)
            self.students_marks_button = Button(self.frame_main_window, text='STUDENTS MARKS',
                                                height=self.widgets_resizer(height=200), compound=CENTER, border=0,
                                                bg='#00cfff', activebackground='#00cfff',
                                                command=lambda: self.exam_results(),
                                                width=self.widgets_resizer(width=1500), font=('Courier ', 15, 'bold'),
                                                relief='groove', image=self.button_image)
            self.students_marks_button.place(relx=0.5, rely=0.84, anchor=CENTER)
        elif file == 'database\project\staff':
            self.database_initiation('staff')
            search = [('Name', self.username.get(), '=', 'OR')]
            search_username = (self.table_database.model.getColumnData(columnIndex=9, filters=search))
            print(search_username)
            if search_username != ['Head Of Department']:
                mb.showerror("Prmission Not Granted", "Sorry, contents can't be accessed")

            else:
                self.master2 = Toplevel(self.master)
                self.master2.title('Staff Register')

                self.master2.geometry(
                    '%dx%d+%d+%d' % (self.window_width, self.window_height - self.widgets_resizer(height=100), 0, 0))
                self.table_frame = Frame(self.master2, width=self.window_width - self.widgets_resizer(width=170),
                                         height=self.window_height - self.widgets_resizer(height=600))
                self.table_frame.place(relx=0, rely=0)
                self.student_table = TableCanvas(self.table_frame,
                                                 width=self.window_width - self.widgets_resizer(width=170),
                                                 height=self.window_height - self.widgets_resizer(height=600))
                self.student_table.importCSV(filename=file + '.csv', )
                self.student_table.load(filename=self.file_name_converter(files=file))
                self.student_table.show()
                self.style = ttk.Style()
                self.style.configure('W.TButton', font=
                ('calibri', 15, 'bold', 'underline'),
                                     foreground='black')
                self.style.map("W.TButton",
                               foreground=[('pressed', 'red'), ('active', 'blue')],
                               background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                               )
                frame2 = Frame(self.master2, height=self.widgets_resizer(height=600))
                frame2.pack(fill=X, side=BOTTOM)
                self.add_new_staff_button = ttk.Button(frame2, text='ADD NEW STAFF', style='W.TButton',
                                                       width=self.widgets_resizer(width=30),
                                                       command=lambda :self.registaration_window('2'))
                self.add_new_staff_button.pack(side=LEFT, pady=100, padx=10)
                self.add_new_department = ttk.Button(frame2, text='ADD NEW DEPARTMENT', style='W.TButton',
                                                     width=self.widgets_resizer(width=30),
                                                     command=lambda: self.modify_window('department'))
                self.add_new_department.pack(side=LEFT, ipadx=55, pady=100, padx=10)
                self.add_new_job_title = ttk.Button(frame2, text='ADD NEW JOB TITLE', style='W.TButton',
                                                    width=self.widgets_resizer(width=30),
                                                    command=lambda: self.modify_window('job title'))
                self.add_new_job_title.pack(side=LEFT, ipadx=25, pady=100, padx=10)
                self.popup_window()


                self.master2.protocol('WM_DELETE_WINDOW', save_table)

        elif file == 'database\project\student':
            self.master2 = Toplevel(self.master)
            self.master2.title('Students Register')

            self.master2.geometry(
                '%dx%d+%d+%d' % (self.window_width, self.window_height - self.widgets_resizer(height=100), 0, 0))
            self.table_frame = Frame(self.master2, width=self.window_width - self.widgets_resizer(width=170),
                                     height=self.window_height - self.widgets_resizer(height=600))
            self.table_frame.place(relx=0, rely=0)
            self.student_table = TableCanvas(self.table_frame,
                                             width=self.window_width - self.widgets_resizer(width=170),
                                             height=self.window_height - self.widgets_resizer(height=600))
            self.student_table.importCSV(filename=file + '.csv', )
            self.student_table.load(filename=self.file_name_converter(files=file))
            self.student_table.show()
            col1_values = max(self.student_table.model.getColCells(colIndex=0))
            # print(max(self.student_table.model.getColCells(colIndex=0)))
            self.style = ttk.Style()
            self.style.configure('W.TButton', font=
            ('calibri', 15, 'bold', 'underline'),
                                 foreground='black')
            self.style.map("W.TButton",
                           foreground=[('pressed', 'red'), ('active', 'blue')],
                           background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                           )
            frame2 = Frame(self.master2, height=self.widgets_resizer(height=600))
            frame2.pack(fill=X, side=BOTTOM)
            self.add_new_staff_button = ttk.Button(frame2, text='ADD NEW STUDENT', style='W.TButton',
                                                   width=self.widgets_resizer(width=30),
                                                   command=lambda: self.modify_window(col1_values, file))
            self.add_new_staff_button.pack(side=LEFT, pady=100, padx=10)

            self.popup_window()

            self.master2.protocol('WM_DELETE_WINDOW', save_table)
        elif file == 'database\project\\result':
            a = []
            self.master2 = Toplevel(self.master)
            self.master2.configure(bg='#00cfff')
            self.master2.title('Result Details')

            reg_lable = Label(self.master2, text='SEARCH BY \n REGISTRATION NUMBER', font=('Ariel', 27, 'bold'),
                              bg='#00dff5')
            reg_lable.grid(row=0, column=0, pady=2)
            sub_lable = Label(self.master2, text='SEARCH BY \n SUBJECT NAME', font=('Ariel', 27, 'bold'), bg='#00dff5')
            sub_lable.grid(row=1, column=0, pady=2)
            add_sub_lable = Label(self.master2, text='ADD SUBJECT', font=('Ariel', 27, 'bold'), bg='#00dff5')
            add_sub_lable.grid(row=2, column=0, pady=2)

            textbox_reg = Entry(self.master2,
                                relief='groove', textvariable=self.reg_var,
                                bd=2,
                                bg='#F5F5F5', )
            textbox_reg.grid(row=0, column=1, pady=2)

            textbox_sub = ttk.Combobox(self.master2,
                                       textvariable=self.sub_var)
            b = self.open_data_files('database\\text\subject.dat')
            for i in b:
                for c in b[i]:
                    a += [c]
            textbox_sub['values'] = a
            textbox_sub.grid(row=1, column=1, pady=2)
            textbox_sub.current(1)
            textbox_sub.config(state='readonly')

            textbox_add_sub = ttk.Combobox(self.master2,
                                           textvariable=self.add_sub_var)
            with open('database\\text\department.txt') as file:
                data = file.read()
            textbox_add_sub['values'] = data.split(',')
            textbox_add_sub.current(1)
            textbox_add_sub.config(state='readonly')
            textbox_add_sub.grid(row=2, column=1, pady=2)

            self.style = ttk.Style()
            self.style.configure('W.TButton', font=
            ('calibri', 15, 'bold', 'underline'),
                                 foreground='black')
            self.style.map("W.TButton",
                           foreground=[('pressed', 'red'), ('active', 'blue')],
                           background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                           )

            button_search_reg = ttk.Button(self.master2, text='SEARCH', style='W.TButton',
                                           command=lambda: self.search_reg(self.reg_var.get()))
            button_search_reg.grid(row=0, column=2, pady=2, )
            button_search_sub = ttk.Button(self.master2, text='SEARCH', style='W.TButton',
                                           command=lambda: self.search_sub(self.sub_var.get()))
            button_search_sub.grid(row=1, column=2, pady=2, )
            button_add_sub = ttk.Button(self.master2, text='ADD SUBJECT', style='W.TButton',
                                        command=lambda: self.add_sub(self.add_sub_var.get()))
            button_add_sub.grid(row=2, column=2, pady=2, )

    def exam_results(self):
        self.master6 = Toplevel(self.master)
        self.master6.title('Results')
        self.master6.configure(bg='#00cfff')
        reg_lable = Label(self.master6, text='RESULTS LESS THAN 50', font=('Ariel', 27, 'bold'),
                          bg='#00dff5')
        reg_lable.grid(row=0, column=0, pady=2)
        sub_lable = Label(self.master6, text='RESULTS EQUAL TO 50', font=('Ariel', 27, 'bold'), bg='#00dff5')
        sub_lable.grid(row=1, column=0, pady=2)
        add_sub_lable = Label(self.master6, text='RESULTS MORE THAN 50', font=('Ariel', 27, 'bold'), bg='#00dff5')
        add_sub_lable.grid(row=2, column=0, pady=2)

        self.style = ttk.Style()
        self.style.configure('W.TButton', font=
        ('calibri', 15, 'bold', 'underline'),
                             foreground='black')
        self.style.map("W.TButton",
                       foreground=[('pressed', 'red'), ('active', 'blue')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                       )

        button_search_reg = ttk.Button(self.master6, text='SEARCH', style='W.TButton',
                                       command=lambda: self.display_results('less'))
        button_search_reg.grid(row=0, column=1, pady=2, )
        button_search_sub = ttk.Button(self.master6, text='SEARCH', style='W.TButton',
                                       command=lambda: self.display_results('equal'))
        button_search_sub.grid(row=1, column=1, pady=2, )
        button_add_sub = ttk.Button(self.master6, text='SEARCH', style='W.TButton',
                                    command=lambda: self.display_results('greater'))
        button_add_sub.grid(row=2, column=1, pady=2, )

    def display_results(self, value):
        total_marks = {}
        inidi_marks_total = 0
        max_marks_total = 0
        self.database_initiation('student')
        reg_no = self.table_database.model.getColCells(colIndex=0)
        name = self.table_database.model.getColCells(colIndex=3)
        class_name = self.table_database.model.getColCells(colIndex=8)
        print(reg_no[0])

        for data in range(len(reg_no)):
            inidi_marks_total = 0
            max_marks_total = 0
            self.database_initiation('result register %d' % int(reg_no[data]))
            inidi_marks = self.table_database.model.getColCells(colIndex=2)
            max_marks = self.table_database.model.getColCells(colIndex=4)
            for ele in range(0, len(inidi_marks)):
                inidi_marks_total += int(inidi_marks[ele])
            for ele in range(0, len(max_marks)):
                max_marks_total += int(max_marks[ele])

            col_names = ['Registration', 'Name', 'Class', 'Total Mark', 'Max Mark', 'Result']

            if value == 'less':
                print(data, (inidi_marks_total * 100) / max_marks_total)
                try:
                    if int((inidi_marks_total * 100) / max_marks_total) <= 40 and int(
                            (inidi_marks_total * 100) / max_marks_total) > 30:

                        total_marks.update({data: {col_names[0]: reg_no[data], col_names[1]: name[data],
                                                   col_names[2]: class_name[data], col_names[3]: (inidi_marks_total),
                                                   col_names[4]: int(max_marks_total), col_names[5]: 'Pass'}})

                    elif int((inidi_marks_total * 100) / max_marks_total) <= 30:
                        total_marks.update({data: {col_names[0]: reg_no[data], col_names[1]: name[data],
                                                   col_names[2]: class_name[data], col_names[3]: (inidi_marks_total),
                                                   col_names[4]: int(max_marks_total), col_names[5]: 'Fail'}})


                except:
                    mb.showinfo("Less than 50", "No Student has got Less than 50")
            if value == 'greater':
                try:
                    if int((inidi_marks_total * 100) / max_marks_total) >= 60:
                        total_marks.update({data: {col_names[0]: reg_no[data], col_names[1]: name[data],
                                                   col_names[2]: class_name[data], col_names[3]: str(inidi_marks_total),
                                                   col_names[4]: str(max_marks_total), col_names[5]: 'Pass'}})
                except:
                    mb.showinfo("Greater than 50", "No Student has got Greater than 50")
            if value == 'equal':
                try:
                    if int((inidi_marks_total * 100) / max_marks_total) > 40 and int(
                            (inidi_marks_total * 100) / max_marks_total) < 60:
                        total_marks.update({data: {col_names[0]: reg_no[data], col_names[1]: name[data],
                                                   col_names[2]: class_name[data], col_names[3]: str(inidi_marks_total),
                                                   col_names[4]: str(max_marks_total), col_names[5]: 'Pass'}})
                except:
                    mb.showinfo("Equal 50", "No Student has got Equal to 50")
        try:
            self.master5 = Toplevel(self.master)
            self.master5.title('Final Results')
            self.master5.geometry(
                '%dx%d+%d+%d' % (self.window_width - self.widgets_resizer(width=170),
                                 self.window_height - self.widgets_resizer(width=600), 0, 0))

            self.table_frame = Frame(self.master5, width=self.window_width - self.widgets_resizer(width=180),
                                     height=self.window_height - self.widgets_resizer(height=610)
                                     )
            self.table_frame.place(relx=0, rely=0)
            self.student_table = TableCanvas(self.table_frame,
                                             width=self.window_width - self.widgets_resizer(width=180),
                                             height=self.window_height - self.widgets_resizer(height=610),
                                             data=total_marks)

            self.student_table.show()
            self.student_table.sortTable(columnIndex=3, reverse=True)
        except:
            mb.showinfo("Less than 50", "No Student has got Less than 50")

    def sort_student_class(self):

        class_name = []
        z = []
        dict = {}
        search = []
        file = self.open_data_files('database\\text\subject.dat')
        for i in file:
            class_name += [i]

        for a in range(len(class_name)):
            if class_name[a] == 'computerscience engineering':
                class_name[a] = 'CSE'
            elif class_name[a] == 'information technology':
                class_name[a] = 'IT'
            elif class_name[a] == 'mechanical engineering':
                class_name[a] = 'MECH'
            elif class_name[a] == 'civil engineering':
                class_name[a] = 'CIVIL'

        for a in class_name:
            search += [('Class', a, 'contains', 'OR')]
        register_data = []
        col_names = ['Class', 'Name', 'Section']
        self.database_initiation('student')
        section_no = self.table_database.model.getColumnData(columnIndex=9, filters=search)

        name = self.table_database.model.getColumnData(columnIndex=3, filters=search)
        class_na = self.table_database.model.getColCells(colIndex=8)
        for b in range(len(name)):
            z += [[class_na[b], name[b], section_no[b]]]

        for l in z:
            for b in class_name:
                if l[0] == b:
                    register_data += [l]
        for a in range(len(register_data)):
            dict.update({a: {col_names[0]: register_data[a][0], col_names[1]: register_data[a][1],
                             col_names[2]: register_data[a][2]}})
        self.master5 = Toplevel(self.master)
        self.master5.title('Student sort')
        self.master5.geometry(
            '%dx%d+%d+%d' % (
                self.window_width - self.widgets_resizer(width=170),
                self.window_height - self.widgets_resizer(width=600),
                0, 0))

        self.table_frame = Frame(self.master5, width=self.window_width - self.widgets_resizer(width=180),
                                 height=self.window_height - self.widgets_resizer(height=610)
                                 )
        self.table_frame.place(relx=0, rely=0)
        self.student_table = TableCanvas(self.table_frame, width=self.window_width - self.widgets_resizer(width=180),
                                         height=self.window_height - self.widgets_resizer(height=610),
                                         data=dict)

        self.student_table.show()

    def sort_staff_joining(self):
        dict = {}
        register_data = []
        admission_dates = []
        a = []
        z = []

        self.database_initiation('staff')
        dmission_dates = self.table_database.model.getColCells(colIndex=6, )
        reg_no = self.table_database.model.getColCells(colIndex=1, )
        name = self.table_database.model.getColCells(colIndex=0, )
        for q in range(len(reg_no)):
            z += [[reg_no[q], name[q], dmission_dates[q]]]
        print(z)

        for i in dmission_dates:
            a += [[x for x in re.compile('\s*[-/\s+]\s*').split(i)]]

        print((a))

        for b in range(len(a)):
            #   if int(a[b][2]) >= 30 and int(a[b][2]) <= 99:
            #   a[b][2] = '19' + a[b][2]
            #  else:
            #    a[b][2] = '20' + a[b][2]
            admission_dates += ['-'.join(a[b])]

        admission_dates.sort(key=lambda date: datetime.datetime.strptime(date, '%d-%m-%Y'))

        for x in range(len(admission_dates)):

            for y in range(len(z)):

                c = admission_dates[x]
                g = z[y][2]
                if c == g.replace('/', '-'):
                    register_data += [[z[y][0], z[y][1], admission_dates[x]]]
                    break

        col_names = ['ID_No', 'Name', 'Date_of_Joining', ]

        for a in range(len(register_data)):
            dict.update({a: {col_names[0]: register_data[a][0], col_names[1]: register_data[a][1],
                             col_names[2]: register_data[a][2], }})
        self.master6 = Toplevel(self.master)
        self.master6.title('Date Of Joining (STAFF)')
        self.master6.geometry(
            '%dx%d+%d+%d' % (
                self.window_width - self.widgets_resizer(width=170),
                self.window_height - self.widgets_resizer(width=600),
                0, 0))

        self.table_frame = Frame(self.master6, width=self.window_width - self.widgets_resizer(width=180),
                                 height=self.window_height - self.widgets_resizer(height=610)
                                 )
        self.table_frame.place(relx=0, rely=0)
        self.student_table = TableCanvas(self.table_frame, width=self.window_width - self.widgets_resizer(width=180),
                                         height=self.window_height - self.widgets_resizer(height=610),
                                         data=dict)

        self.student_table.show()

    def sort_students_admission(self):
        dict = {}
        register_data = []
        admission_dates = []
        a = []
        z = []

        self.database_initiation('student')
        dmission_dates = self.table_database.model.getColCells(colIndex=1, )
        reg_no = self.table_database.model.getColCells(colIndex=0, )
        name = self.table_database.model.getColCells(colIndex=3, )
        for q in range(len(reg_no)):
            z += [[reg_no[q], name[q], dmission_dates[q]]]
        for i in range (len(z)):
            if '-' in z[i][2]:
                a = [z[i][2].split('-')]
                print(a)
                if len(a[0][2]) == 2:
                    if a[0][2] >= '30' and a[0][2] <= '99':
                        a[0][2] = '19' + a[0][2]
                    else:
                        a[0][2] = '20' + a[0][2]
                else:
                    a[0][2] = a[0][2]

            else:
                a = [z[i][2].split('/')]
                if len(a[0][2]) == 2:
                    if a[0][2] >= '30' and a[0][2] <= '99':
                        a[0][2] = '19' + a[0][2]
                    else:
                        a[0][2] = '20' + a[0][2]
                else:
                    a[0][2] = a[0][2]
            z[i][2] = a[0][0] + '-' + a[0][1] + '-' + a[0][2]
        for i in dmission_dates:
            if '-' in i:
                a += [i.split('-')]
            else:
                a += [i.split('/')]
        for b in range(len(a)):
            if len(a[b][2]) == 2 :
                if a[b][2] >= '30' and a[b][2] <= '99':
                    a[b][2] = '19' + a[b][2]
                else:
                    a[b][2] = '20' + a[b][2]
            else:
                a[b][2]=a[b][2]
            admission_dates += ['-'.join(a[b])]
        admission_dates.sort(key=lambda date: datetime.datetime.strptime(date, '%d-%m-%Y'))
        for x in range(len(admission_dates)):
            for y in range(len(z)):
                print('-->'+admission_dates[x])
                c = admission_dates[x]
                print('->'+c)
                print(z[y][2])
                if c == z[y][2]:
                    register_data += [[z[y][0], z[y][1], z[y][2]]]
                    break
        col_names = ['Registration', 'Name', 'DateOfAdmission', ]

        for a in range(len(register_data)):
            dict.update({a: {col_names[0]: register_data[a][0], col_names[1]: register_data[a][1],
                             col_names[2]: register_data[a][2], }})
        self.master5 = Toplevel(self.master)
        self.master5.title("Date Of Admission (STUDENTS)")
        self.master5.geometry(
            '%dx%d+%d+%d' % (
                self.window_width - self.widgets_resizer(width=170),
                self.window_height - self.widgets_resizer(width=600),
                0, 0))

        self.table_frame = Frame(self.master5, width=self.window_width - self.widgets_resizer(width=180),
                                 height=self.window_height - self.widgets_resizer(height=610)
                                 )
        self.table_frame.place(relx=0, rely=0)
        self.student_table = TableCanvas(self.table_frame, width=self.window_width - self.widgets_resizer(width=180),
                                         height=self.window_height - self.widgets_resizer(height=610),
                                         data=dict)

        self.student_table.show()

    def search_sub(self, sub_name):
        class_name = []
        dict = {}
        search = []
        b = self.open_data_files('database\\text\subject.dat')
        for i in b:
            for c in b[i]:

                if c == sub_name:
                    class_name += [i]

        for a in range(len(class_name)):
            if class_name[a] == 'computerscience engineering':
                class_name[a] = 'CSE'
            elif class_name[a] == 'information technology':
                class_name[a] = 'IT'
            elif class_name[a] == 'mechanical engineering':
                class_name[a] = 'MECH'
            elif class_name[a] == 'civil engineering':
                class_name[a] = 'CIVIL'
        print(class_name)
        for a in class_name:
            search += [('Class', a, 'contains', 'OR')]

        register_data = []
        col_names = ['Registration', 'Name', 'Mark Obtained', 'Pass Mark', 'Maximum Mark', 'Result']
        self.database_initiation('student')
        reg_no = self.table_database.model.getColumnData(columnIndex=0, filters=search)

        name = self.table_database.model.getColumnData(columnIndex=3, filters=search)

        for data in range(len(reg_no)):
            search1 = [('Subject Name', sub_name, 'contains', 'OR')]
            self.database_initiation('result register %d' % (int(reg_no[data])))
            marks = self.table_database.model.getColumnData(columnIndex=2, filters=search1)
            Pass_mark = self.table_database.model.getColumnData(columnIndex=3, filters=search1)
            Max_mark = self.table_database.model.getColumnData(columnIndex=4, filters=search1)
            result = self.table_database.model.getColumnData(columnIndex=5, filters=search1)
            register_data += [[reg_no[data], name[data], marks[0], Pass_mark[0], Max_mark[0], result[0]]]
        for a in range(len(register_data)):
            dict.update({a: {col_names[0]: register_data[a][0], col_names[1]: register_data[a][1],
                             col_names[2]: register_data[a][2], col_names[3]: register_data[a][3],
                             col_names[4]: register_data[a][4], col_names[5]: register_data[a][5], }})

        self.master2.geometry(
            '%dx%d+%d+%d' % (self.window_width, self.window_height - self.widgets_resizer(height=100), 0, 0))
        self.master2.title('Students-Subjects')
        self.table_frame = Frame(self.master2, width=self.window_width - self.widgets_resizer(width=170),
                                 height=self.window_height - self.widgets_resizer(height=600))
        self.table_frame.place(relx=0, rely=0)
        self.student_table = TableCanvas(self.table_frame, width=self.window_width - self.widgets_resizer(width=170),
                                         height=self.window_height - self.widgets_resizer(height=600), data=dict)

        self.student_table.show()

    def search_reg(self, number):
        def save_table():

            # self.student_table.save(filename='database\\result register %d.table' % (int(number)))
            # self.student_table.load(filename='database\\result register %d.table' % (int(number)))
            rows = self.student_table.model.getColCells(colIndex=0)
            print(self.student_table.model.getColCells(colIndex=2))

            with open('database\\project\\result register %d.csv' % (int(number)), 'w', newline='') as file1:
                writer = csv.writer(file1)
                writer.writerow(['Registration Number', 'Subject Name',
                                 'Mark Obtained', 'Pass Mark',
                                 'Maximum',
                                 'Result'])
                for data in range(len(rows)):
                    writer.writerow([rows[data], self.student_table.model.getColCells(colIndex=1)[data],
                                     self.student_table.model.getColCells(colIndex=2)[data],
                                     self.student_table.model.getColCells(colIndex=3)[data],
                                     self.student_table.model.getColCells(colIndex=4)[data],
                                     self.student_table.model.getColCells(colIndex=5)[data]])
            self.master5.destroy()

        self.database_initiation('student')
        reg_no = self.table_database.model.getColCells(colIndex=0)
        search = [('Registration', str(number), 'contains', 'OR')]

        name = self.table_database.model.getColumnData(columnIndex=3, filters=search)
        print(name)

        if number in reg_no:
            self.master5 = Toplevel(self.master)
            self.master5.title('Search On Registration Number')
            self.master5.geometry(
                '%dx%d+%d+%d' % (self.window_width - self.widgets_resizer(width=170),
                                 self.window_height - self.widgets_resizer(width=170), 0, 0))
            self.table_frame = Frame(self.master5, width=self.window_width - self.widgets_resizer(width=180),
                                     height=self.window_height - self.widgets_resizer(width=180))
            self.table_frame.grid(row=0, column=0, pady=2, )
            name_lable = Label(self.master5, text=name[0])
            name_lable.grid(row=1, column=0, pady=2, )
            self.student_table = TableCanvas(self.table_frame,
                                             width=self.window_width - self.widgets_resizer(width=170),
                                             height=self.window_height - self.widgets_resizer(height=600))

            self.student_table.importCSV(filename='database\project\\result register %d.csv' % (int(number)), )
            self.student_table.show()
        else:
            print('error')
            print(number)
        self.master5.protocol('WM_DELETE_WINDOW', save_table)

    def add_sub(self, data):
        var = StringVar()
        self.master4 = Toplevel(self.master)
        textbox = Entry(self.master4, textvariable=var)
        textbox.pack()
        button = Button(self.master4, text='ADD', command=lambda: self.add_sub_process(data, var.get()))
        button.pack()

    def add_sub_process(self, data, var):
        data_txt = self.open_data_files('database\\text\subject.dat')
        for i in data_txt:
            if i == data:
                data_txt[i] += var
        with open('database\\text\subject.dat', 'wb')as file:
            pickle.dump(data_txt, file)
        self.master4.destroy()

    def open_data_files(self, txtname):
        with open(txtname, 'rb')as file:
            a = pickle.load(file)

            return a

    def modify_window(self, name=None, file=None):
        self.master4 = Toplevel(self.master2)
        string = StringVar()
        self.textbox_gender_variable = StringVar()
        self.textbox_class_variable = StringVar()
        self.textbox_reg_variable = StringVar()
        self.textbox_roll_variable = StringVar()
        self.textbox_name_variable = StringVar()
        self.textbox_dob_variable = StringVar()
        self.textbox_doa_variable = StringVar()
        self.textbox_ppno_variable = StringVar()
        self.textbox_section_variable = StringVar()
        self.textbox_address_variable = StringVar()

        if name.isdigit():
            self.master4.configure(bg='#00cfff')
            self.master4.title('ADD STUDENTS')
            reg_lable = Label(self.master4, text='REGISTRATION NUMBER', font=('Ariel', 27, 'bold'), bg='#00cfff')
            name_lable = Label(self.master4, text='NAME', font=('Ariel', 27, 'bold'), bg='#00cfff')
            gender_lable = Label(self.master4, text='GENDER', font=('Ariel', 27, 'bold'), bg='#00cfff')
            dob_lable = Label(self.master4, text='DATE OF BIRTH', font=('Ariel', 27, 'bold'), bg='#00cfff')
            address_lable = Label(self.master4, text='ADDRESS', font=('Ariel', 27, 'bold'), bg='#00cfff')
            class_lable = Label(self.master4, text='CLASS', font=('Ariel', 27, 'bold'), bg='#00cfff')
            ppno_lable = Label(self.master4, text='PARENTS NUMBER', font=('Ariel', 27, 'bold'), bg='#00cfff')
            rono_lable = Label(self.master4, text='ROLL NUMBER', font=('Ariel', 27, 'bold'), bg='#00cfff')
            section_lable = Label(self.master4, text='SECTION', font=('Ariel', 27, 'bold'), bg='#00cfff')
            doa_lable = Label(self.master4, text='DATE OF ADMISSION', font=('Ariel', 27, 'bold'), bg='#00cfff')

            reg_lable.grid(row=0, column=0, pady=2)
            name_lable.grid(row=1, column=0, pady=2)
            gender_lable.grid(row=2, column=0, pady=2)
            dob_lable.grid(row=3, column=0, pady=2)
            class_lable.grid(row=4, column=0, pady=2)
            address_lable.grid(row=0, column=3, pady=2)
            ppno_lable.grid(row=1, column=3, pady=2)
            rono_lable.grid(row=2, column=3, pady=2)
            section_lable.grid(row=3, column=3, pady=2)
            doa_lable.grid(row=4, column=3, pady=2)

            # textbox = Entry(self.master4, textvariable=string)
            # textbox.grid(row=0,column=1,sticky=W,pady=2)
            textbox_username = Entry(self.master4,
                                     relief='groove', textvariable=self.textbox_name_variable,
                                     bd=2,
                                     bg='#F5F5F5', )
            textbox_reg = Entry(self.master4,
                                relief='groove', textvariable=self.textbox_reg_variable,
                                bd=2,
                                bg='#F5F5F5', )
            textbox_reg.insert(0, int(name) + 1)
            textbox_reg.config(state='disabled')

            textbox_address = Entry(self.master4,
                                    relief='groove', textvariable=self.textbox_address_variable,
                                    bd=2,
                                    bg='#F5F5F5', )
            textbox_ppno = Entry(self.master4,
                                 relief='groove', textvariable=self.textbox_ppno_variable,
                                 bd=2,
                                 bg='#F5F5F5', )
            textbox_class = ttk.Combobox(self.master4,
                                         textvariable=self.textbox_class_variable, )
            b = self.open_data_files('database\\text\subject.dat')
            h = []
            for i in b:
                h += [i]
            textbox_class['values'] = h
            textbox_class.current(1)
            textbox_class.config(state='readonly')
            textbox_section = Entry(self.master4,
                                    relief='groove', textvariable=self.textbox_section_variable,
                                    bd=2,
                                    bg='#F5F5F5', )
            textbox_roll = Entry(self.master4,
                                 relief='groove', textvariable=self.textbox_roll_variable,
                                 bd=2,
                                 bg='#F5F5F5', )
            textbox_doa = Entry(self.master4,
                                relief='groove', textvariable=self.textbox_doa_variable,
                                bd=2,
                                bg='#F5F5F5', )
            textbox_doa.insert(0, 'dd-mm-yyyy')
            textbox_doa.bind('<FocusIn>', lambda a: textbox_doa.delete(0, 'end'))
            textbox_dob = Entry(self.master4,
                                relief='groove', textvariable=self.textbox_dob_variable,
                                bd=2,
                                bg='#F5F5F5', )
            textbox_dob.insert(0, 'dd-mm-yyyy')
            textbox_dob.bind('<FocusIn>', lambda a: textbox_dob.delete(0, 'end'))

            textbox_gender = ttk.Combobox(self.master4,
                                          textvariable=self.textbox_gender_variable)
            textbox_gender['values'] = ('M', 'F')

            textbox_gender.current(1)
            textbox_gender.config(state='readonly')

            textbox_username.grid(row=1, column=1, pady=2)
            textbox_reg.grid(row=0, column=1, pady=2)
            textbox_address.grid(row=0, column=4, pady=2)
            textbox_ppno.grid(row=1, column=4, pady=2)
            textbox_class.grid(row=4, column=1, pady=2)
            textbox_section.grid(row=3, column=4, pady=2)
            textbox_roll.grid(row=2, column=4, pady=2)
            textbox_dob.grid(row=3, column=1, pady=2)
            textbox_doa.grid(row=4, column=4, pady=2)
            textbox_gender.grid(row=2, column=1, pady=2)

            button = ttk.Button(self.master4, text='ADD', style='W.TButton', width=70,
                                command=lambda: self.add_rows(file=file, name=name))
            button.grid(row=5, column=0, pady=2, columnspan=5)

        else:

            textbox = Entry(self.master4, textvariable=string)
            textbox.pack()
            button = ttk.Button(self.master4, text='ADD', style='W.TButton',
                                command=lambda: self.modify_process(name=name, secname=string.get()))
            button.pack()

    def modify_process(self, name, secname=None):
        if name == 'department':
            self.department_values += secname
            with open('database\\text\department.txt', 'w') as file:
                file.write(','.join(self.department_values))



        elif name == 'job title:':
            self.jobtitle_values += secname
            with open('database\\text\job title.txt', 'w') as file:
                file.write(','.join(self.jobtitle_values_values))

        self.master4.destroy()

    def file_name_converter(self, files):
        temp_var = files.split('\\')
        print(temp_var)
        files = temp_var[0] + '\\' + temp_var[2] + '.table'
        return files

    def popup_window(self, ):

        if self.counter == 0:
            self.counter += 1
            self.master3 = Toplevel(self.master2)
            self.master3.geometry(
                '%dx%d+%d+%d' % (self.widgets_resizer(width=1900), self.widgets_resizer(height=550), 500, 500))
            self.master3.title('IMPORTANT INSTRUCTIONS')

            self.lable_filtering = LabelFrame(self.master3, text="NOTE:", )

            self.text_for_popup = Label(self.lable_filtering,
                                        text="Right clicking on the table and choosing 'Filter Records' from the popup menu will display the filtering bar in a separate window below the table.\n "
                                             "This is a simple interface for adding multiple search conditions that are chained together by boolean operators (AND, OR, NOT).\n "
                                             "Any number of filters can be added for one search. The '-' button on the right of each filter is used to remove it.\n "
                                             "When you have entered the required search terms press go and the table will be updated to display just the found rows.\n "
                                             "Closing the filtering bar restores the whole table.\n \nVlaues are to be given in this order (Boolean,Column,Operator,Value) :\n\n "
                                             "1) Boolean determines how this filter is evaluated along with other filters (one of AND, OR, NOT).\n "
                                             "example: filter=[('col1',100,'>','AND')] means find all rows with a value greater than 100 for col1.\n "
                                             "In this case the 'AND' is not used as there is only one filter in the list.\n"
                                             "2) Column is the column name.\n "
                                             "3) Operator is one of -, !=, contains, <, >, haslength, isnumber\n "
                                             "4) Value is the integer, float or string value to compare against.\n "
                                        , borderwidth=0, font=('systemfixed', 12, 'bold'))
            self.lable_filtering.pack(padx=10, pady=10, fill='both', expand='yes')
            self.text_for_popup.pack()

        else:
            pass

    def save_window(self, loc=None):
        self.database_initiation('staff')
        a = self.table_database.model.getAllCells()
        with open('database\project\staff.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['Name', 'ID_No', 'Gender', 'Dob', 'Address', 'Contact_number', 'Date_of_Joining', 'Qualification',
                 'Department', 'Job_title', 'Basic_pay', 'Password'])

            for data in a:
                writer.writerow(a[data])
        self.database_initiation('student')
        a = self.table_database.model.getAllCells()
        with open('database\project\student.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Registration', 'DateOfAdmission',
                             'Rollnumber', 'Name',
                             'Gender', 'DateofBirth',
                             'Address', 'ParentPhoneNumber',
                             'Class', 'Section'])
            for data in a:
                writer.writerow(a[data])
        if loc != 'logout':
            self.master.destroy()
        print('suc')


root = Tk()

main_program = main(root)
main_program.login_window()
root.protocol('WM_DELETE_WINDOW', main_program.save_window)

root.mainloop()

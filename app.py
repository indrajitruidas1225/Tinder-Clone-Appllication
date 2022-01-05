import shutil
from tkinter import *
from db_helper import DB
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
class Tinder:
    def __init__(self):
        self.db = DB()
        self.root = Tk()
        # self.root.maxsize(300, 500)
        self.root.minsize(300, 500)
        self.root.maxsize(300, 500)
        self.root.configure(background='#2906A8')
        self.load_reg_gui()

    def load_reg_gui(self):
        self.clear_gui()
        self.label1 = Label(self.root, text='Tinder', bg='#2906A8', fg='#ffffff')
        self.label1.configure(font=('Times', 22, 'bold'))
        self.label1.pack(pady=(10, 10))
        self.root.title('Tinder Registration')
        self.label2 = Label(self.root, text='SignUp here', bg='#2906A8', fg='#ffffff')
        self.label2.pack(pady=(10, 10))
        self.label2.configure(font=('Verdana', 12, 'italic'))
        self.name_input = Entry(self.root)
        self.name_input.insert(0, 'Name')
        self.name_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.email_input = Entry(self.root)
        self.email_input.insert(0, 'E-mail')
        self.email_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.password_input = Entry(self.root)
        self.password_input.insert(0, 'Password')
        # self.password_input.configure(state=NORMAL)
        self.password_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.reg_btn = Button(self.root, text='Sign Up', bg='#ffffff', width=25, height=2,
                              command=lambda: self.perform_reg())
        self.reg_btn.pack(pady=(20, 20))
        self.reg_btn.configure(font=('Verdana', 10))
        self.label3 = Label(self.root, text='Already registered ?', bg='#2906A8', fg='#ffffff')
        self.label3.pack(pady=(10, 10))
        self.label3.configure(font=('Verdana', 9, 'italic'))
        self.log_btn = Button(self.root, text='Log In', bg='#ffffff', width=8, height=1,
                              command=lambda: self.load_login_gui())
        self.log_btn.pack(pady=(10, 10))
        self.log_btn.configure(font=('Bold', 10))
        self.root.mainloop()

    def perform_reg(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.db.register_user(name, email, password)
        if response == 1:
            print('Successful')
            messagebox.showinfo('Tinder', 'Registration Successful')
        else:
            print('fail')
            messagebox.showinfo('Tinder', 'Registration Failed')

    def clear_gui(self, i=0):
        for i in self.root.pack_slaves()[i:]:
            i.destroy()

    def load_login_gui(self):
        self.clear_gui()
        self.root.config(menu='')
        self.label1 = Label(self.root, text='Tinder', bg='#2906A8', fg='#ffffff')
        self.label1.pack(pady=(10, 10))
        self.label1.configure(font=('Times', 22, 'bold'))
        self.root.title('Tinder LogIn')
        self.label4 = Label(self.root, text='LogIn here', bg='#2906A8', fg='#ffffff')
        self.label4.pack(pady=(10, 10))
        self.label4.configure(font=('Verdana', 12, 'italic'))
        self.email_input = Entry(self.root)
        self.email_input.insert(0, 'E-mail')
        self.email_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.password_input = Entry(self.root)
        self.password_input.insert(0, 'Password')
        # self.password_input.configure(state=NORMAL)
        self.password_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.login_btn = Button(self.root, text='Log In', bg='#ffffff', width=25, height=2,
                                command=lambda: self.perform_login())
        self.login_btn.pack(pady=(20, 20))
        self.login_btn.configure(font=('Verdana', 10))
        self.label5 = Label(self.root, text='Not a member ?', bg='#2906A8', fg='#ffffff')
        self.label5.pack(pady=(10, 10))
        self.label5.configure(font=('Verdana', 10, 'italic'))
        self.sign_btn = Button(self.root, text='Register', bg='#ffffff', width=8, height=1,
                               command=lambda: self.load_reg_gui())
        self.sign_btn.pack(pady=(10, 10))
        self.sign_btn.configure(font=('Bold', 10))

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        data = self.db.login_user(email, password)
        if data == 0:
            messagebox.showerror('Tinder', 'Some error occurred')
        else:
            if len(data) == 0:
                messagebox.showerror('Tinder', 'Incorrect email/password')
            else:
                self.user_id = data[0][0]
                self.load_profile_gui()

    def load_header_menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Browse Profiles", command=lambda: self.browse_profiles())
        filemenu.add_command(label="My Profile",command=lambda:self.load_profile_gui())
        filemenu.add_command(label="Edit Profile",command=lambda:self.load_edit_page())
        filemenu.add_command(label="Log Out", command=lambda: self.logout())
        menubar.add_cascade(label="Profile", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="My Requests",command=lambda:self.fetch_requests())
        editmenu.add_command(label="My Proposals",command=lambda:self.fetch_proposals())
        editmenu.add_command(label="My Matches",command=lambda:self.fetch_matches())
        menubar.add_cascade(label="Options", menu=editmenu)
        self.root.config(menu=menubar)
    def load_edit_page(self):
        self.clear_gui()
        self.clear_gui()
        self.label1 = Label(self.root, text='Tinder', bg='#2906A8', fg='#ffffff')
        self.label1.configure(font=('Times', 30, 'bold'))
        self.label1.pack(pady=(10, 10))
        self.root.title('Edit Profile')
        self.label2 = Label(self.root, text='Edit Profile', bg='#2906A8', fg='#ffffff')
        self.label2.configure(font=('Times', 18))
        self.label2.pack(pady=(10, 10))
        self.gender_input = Entry(self.root)
        self.gender_input.insert(0, 'Gender')
        self.gender_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.age_input = Entry(self.root)
        self.age_input.insert(0, 'Age')
        self.age_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.city_input = Entry(self.root)
        self.city_input.insert(0, 'City')
        # self.password_input.configure(state=NORMAL)
        self.city_input.pack(pady=(10, 10), ipadx=85, ipady=10)
        self.edit_btn = Button(self.root, text='Edit', bg='#ffffff', width=25, height=2,
                              command=lambda: self.edit_user_profile())
        self.edit_btn.pack(pady=(20, 20))
        self.edit_btn.configure(font=('Verdana', 10))
    def edit_user_profile(self):
        gender=self.gender_input.get()
        age=self.age_input.get()
        city=self.city_input.get()
        result=self.db.edit_profile(self.user_id,gender,age,city)
        if result==1:
            messagebox.showinfo('Tinder','Profile Updated')
        else:
            messagebox.showerror('Tinder','Fail to Update Profile')
    def fetch_proposals(self):
        data = self.db.fetch_proposal_data(self.user_id)
        if data == 0:
            self.clear_gui()
            self.name = Label(self.root, text="You don't have any proposal !", bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(100, 10))
            self.name.configure(font=('Verdana', 15,))
        else:
            self.intermediate(data, show_propose_button=-1,email=0)
    def fetch_requests(self):
        data=self.db.fetch_request_data(self.user_id)
        if data==0:
            self.clear_gui()
            self.name = Label(self.root, text="You've not sent any proposal !", bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(100, 10))
            self.name.configure(font=('Verdana', 15,))
        else:
            self.intermediate(data,index=0,show_propose_button=0,email=0,request=1)
    def fetch_matches(self):
        data = self.db.fetch_matches_data(self.user_id)
        if data == 0:
            self.clear_gui()
            self.name = Label(self.root, text="You've no matches!", bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(100, 10))
            self.name.configure(font=('Verdana', 17,))
        else:
            self.intermediate(data, show_propose_button=0,email=0)

    def browse_profiles(self):
        data = self.db.fetch_profile_data(self.user_id)
        self.intermediate(data,request=0)
    def intermediate(self, data, index=0,show_propose_button=1,email=1,request=0):
        self.load_others_profile_gui(data, index,show_propose_button,email,request)
    def change_dp(self):
        pathname=filedialog.askopenfilename(initialdir="/images",title="something")
        filename=pathname.split('/')[-1]
        shutil.copyfile(pathname,"C:\\Users\\Indrajit\\PycharmProjects\\tinder\\img\\"+filename)
        k=self.db.update_dp(self.user_id,filename)
        if k==1:
            messagebox.showinfo('Tinder','Profile Picture\nChanged Successfully')
            self.load_profile_gui()
        elif k==0:
            messagebox.showerror('Tinder','Failed to Update Profile Picture !')
            self.db.update_dp(self.user_id, 'avatar.png')
            self.load_profile_gui()
        elif k==-1:
            messagebox.showerror('Tinder', 'Image form should be jpg/jpeg/png')
    def load_profile_gui(self):
        self.clear_gui()
        self.root.title('Tinder Profile')
        self.load_header_menu()
        data = self.db.fetch_user_data(self.user_id)
        imageUrl="img/{}".format(data[0][-1])
        load=Image.open(imageUrl)
        load=load.resize((200,200),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(image=render)
        img.image=render
        img.pack(pady=(10,10))
        self.dp=Button(self.root,text="Change Profile Picture", bg='#ffffff', width=20, height=1,command=lambda:self.change_dp())
        self.dp.pack(pady=(10,10))
        self.dp.configure(font=('Verdana', 10))
        data = self.db.fetch_user_data(self.user_id)
        # print(data)
        if data != 0:
            self.name = Label(self.root, text=data[0][1], bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(10, 10))
            self.name.configure(font=('Times', 19, 'bold'))
            text = "{} Years Old {} from {}".format(data[0][4], data[0][6], data[0][5])
            self.detail = Label(self.root, text=text, bg='#2906A8', fg='#ffffff')
            self.detail.pack(pady=(10, 10))
            self.detail.configure(font=('Verdana', 12,))
    def propose(self,juliet_id):
        response=self.db.propose_user(self.user_id,juliet_id)
        if response==1:
            messagebox.showinfo('Tinder','Proposal Sent Successfully')
        elif response==0:
            messagebox.showerror('Tinder','Proposal Already Sent Before!')
        else:
            messagebox.showerror('Tinder','Some Error Occurred !')

    def load_others_profile_gui(self, data, index,show_propose_button=1,email=1,request=0):
        self.clear_gui()
        self.load_header_menu()
        # print(data)
        if index >= len(data):
            index = 0
        if index < -len(data):
            index = len(data)-1
        if data != 0 and email==1 and request==0:
            imageUrl = "img/{}".format(data[index][-1])
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack(pady=(10, 10))
            self.name = Label(self.root, text=data[index][1], bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(10, 10))
            self.name.configure(font=('Times', 19, 'bold'))
            text = "{} Years Old {} from {}".format(data[index][4], data[index][6], data[index][5])
            self.detail = Label(self.root, text=text, bg='#2906A8', fg='#ffffff')
            self.detail.pack(pady=(10, 10))
            self.detail.configure(font=('Verdana', 12,))
        elif data!=0 and email==0 and request==0 and show_propose_button==-1:
            k=self.db.fetch_user_data(data[index][-2])
            imageUrl = "img/{}".format(k[0][-1])
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack(pady=(10, 10))
            self.name = Label(self.root, text=data[index][1], bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(10, 10))
            self.name.configure(font=('Times', 19, 'bold'))
            text = "{} Years Old {} from {}\n\nE-mail - {}".format(data[index][4], data[index][6], data[index][5],data[index][2])
            self.detail = Label(self.root, text=text, bg='#2906A8', fg='#ffffff')
            self.detail.pack(pady=(10, 10))
            self.detail.configure(font=('Verdana', 12,))
        elif data!=0 and email==0 and request==0:
            k=self.db.fetch_user_data(data[index][-1])
            imageUrl = "img/{}".format(k[0][-1])
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack(pady=(10, 10))
            self.name = Label(self.root, text=data[index][1], bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(10, 10))
            self.name.configure(font=('Times', 19, 'bold'))
            text = "{} Years Old {} from {}\n\nE-mail - {}".format(data[index][4], data[index][6], data[index][5],data[index][2])
            self.detail = Label(self.root, text=text, bg='#2906A8', fg='#ffffff')
            self.detail.pack(pady=(10, 10))
            self.detail.configure(font=('Verdana', 12,))
        elif data!=0 and email==0 and request==1:
            k=self.db.fetch_user_data(data[index][-1])
            imageUrl = "img/{}".format(k[0][-1])
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack(pady=(10, 10))
            self.name = Label(self.root, text=data[index][1], bg='#2906A8', fg='#ffffff')
            self.name.pack(pady=(10, 10))
            self.name.configure(font=('Times', 19, 'bold'))
            text = "{} Years Old {} from {}\n\nE-mail - {}".format(data[index][4], data[index][6], data[index][5],data[index][2])
            self.detail = Label(self.root, text=text, bg='#2906A8', fg='#ffffff')
            self.detail.pack(pady=(10, 10))
            self.detail.configure(font=('Verdana', 12,))
        frame = Frame(self.root)
        frame.pack()
        prev = Button(frame, text='Previous', bg='#ffffff', width=10, height=1,
                      command=lambda: self.intermediate(data, index - 1,show_propose_button,email,request))
        prev.pack(side=LEFT)
        if show_propose_button==1 or show_propose_button==-1:
            propose = Button(frame, text='Propose', bg='#ffffff', width=10, height=1,command=lambda:self.propose(data[index][0]))
            propose.pack(side=LEFT)
        next = Button(frame, text='Next', bg='#ffffff', width=10, height=1,
                      command=lambda: self.intermediate(data, index + 1,show_propose_button,email,request))
        next.pack(side=LEFT)

    def logout(self):
        self.user_id = None
        self.clear_gui(0)
        self.load_login_gui()
obj = Tinder()

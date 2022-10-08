from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criando Janelas
jan = Tk()
jan.title('DP Systems - Acess Panel')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False, height=False)
# jan.attributes('-alpha', 0.9)
# jan.iconbitmap(default='icons/LogoIcon.ico')

#Carregando imagens
logo = PhotoImage(file='icons/logo.png')


#Esses são os Widgets da Janela
LeftFrame = Frame(jan, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)

userLabel = Label(RightFrame, text='Username: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
userLabel.place(x=5, y=100)
userEntry = ttk.Entry(RightFrame, width=20)
userEntry.place(x=150, y=110)

#Password
passLabel = Label(RightFrame, text='Password: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
passLabel.place(x=5, y=150)
passEntry = ttk.Entry(RightFrame, width=20, show='*')
passEntry.place(x=150, y=160)

def login():
    user = userEntry.get()
    password = passEntry.get()
    
    DataBaser.cursor.execute('''
    SELECT * FROM Users 
    WHERE (User = ? and Password = ?)
    ''', (user, password))
    verifyLogin = DataBaser.cursor.fetchone()

    try:
        if user in verifyLogin and password in verifyLogin:
            messagebox.showinfo(title='Login info', message='Acess confirmed, Welcome!')
    except:
        messagebox.showinfo(title='Login Info', message='Blocked Acess')

#Buttons Login/ Register
loginButton = ttk.Button(RightFrame, text='Login', width=30, command=login)
loginButton.place(x=100, y=225)

#Functions
def register():
    '''Remove Widgets Login'''
    loginButton.place(x=5000)
    registerButton.place(x=5000)
    '''Insert Widgets Register'''
    nomeLabel = Label(RightFrame, text='Name: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
    nomeLabel.place(x=5, y=5)
    nomeEntry = ttk.Entry(RightFrame, width=35)
    nomeEntry.place(x=100, y=15)

    emailLabel = Label(RightFrame, text='Email: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
    emailLabel.place(x=5, y=55)
    emailEntry = ttk.Entry(RightFrame, width=35)
    emailEntry.place(x=100, y=66)

    def registerToDB():
        name = nomeEntry.get()
        email = emailEntry.get()
        user = userEntry.get()
        password = passEntry.get()

        if name == '' and email == '' and user == '' and password == '':
            messagebox.showerror(title = 'Register Error', message='Fill in all fields')
        else:
            DataBaser.cursor.execute('''
                INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?);
            ''', (name, email, user, password))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Register Info', message='Register Sucessfull')


    registerUser = ttk.Button(RightFrame, text='Register', width=30, command=registerToDB)
    registerUser.place(x=100, y=225)

    def backToLogin():
        '''Remove Widgets Register'''
        nomeLabel.place(x=5000)
        nomeEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        registerUser.place(x=5000)
        back.place(x=5000)
        '''Return Widgets Login'''
        loginButton.place(x=100)
        registerButton.place(x=125)


    back = ttk.Button(RightFrame, text='Back', width=20, command=backToLogin)
    back.place(x=137, y=260)



registerButton = ttk.Button(RightFrame, text='Register', width=20, command=register)
registerButton.place(x=138, y=260)

jan.mainloop()

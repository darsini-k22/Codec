from tkinter import *
from base64 import *

import time
import datetime as dt

import os


def Encode_Decode():
    win = Tk()

    win.geometry('600x500')
    win.resizable(0, 0)
    win.title("Message Encode and Decode")
    Label(win, text='ENCODE-DECODE', font='Helvetica  20 bold').pack()

    Label(win, text='Message encoder and decoder', font='courier 10 bold').pack(side=BOTTOM)

    Text = StringVar()
    Code = StringVar()
    mode = StringVar()
    Result = StringVar()

    def Encode(text):

        encd = b64encode(text.encode("utf-8"))
        en_str = str(encd, "utf-8")
        file = open(username1, "a")
        file.write("\n" + text + "   ")
        file.write(en_str)
        file.close()
        return en_str

    def Decode(Code):

        decd = b64decode(Code)
        en_str = str(decd.decode("UTF-8"))
        file = open(username1, "a")
        file.write("\n" + en_str + "   ")
        file.write(Code)
        file.close()
        return en_str

    def Mode():
        if mode.get() == 'e':
            Result.set(Encode(Text.get()))
        elif mode.get() == 'd':
            Result.set(Decode(Code.get()))
        else:
            Result.set('Invalid Mode')

    def Exit():
        win.destroy()

    def Reset():
        Text.set("")
        Code.set("")
        mode.set("")
        Result.set("")

    def History():
        global History_window
        History_window = Tk()
        History_window.title("History")
        History_window.geometry("600x300")
        Label(History_window, font=('Comic Sans MS bold', 15), text="HISTORY", bg='turquoise', width=50).pack()
        Label(History_window, text=" ", font=('Comic Sans MS', 12)).pack()
        file = open(username1, "r")
        content = file.readlines()
        history = content[2:]
        for code in history:
            code = code.rstrip('\n')
            Label(History_window, font=('Comic Sans MS', 11), text=code).pack()

        file.close()
        Label(History_window, text=" ", font=('Comic Sans MS', 12)).pack()
        Button(History_window, text="Clear History", command=clear_history, width=12, font=('Comic Sans MS', 10)).place(
            x=30, y=240)
        Button(History_window, text='Back', command=delete_history_window, width=6, font=('Comic Sans MS', 10)).place(
            x=500, y=240)

    def clear_history():
        file = open(username1, "r")
        erase = file.readlines()
        file.close()
        del erase[2:]

        file = open(username1, "w+")
        for line in erase:
            file.write(line)
        file.close()

        global history_clear_window
        history_clear_window = Tk()
        history_clear_window.title("History Cleared")
        history_clear_window.geometry("300x100")
        Label(history_clear_window, text="History successfully cleared", font=("Comic Sans MS", 12), fg="green").pack()
        Button(history_clear_window, text="OK", width=6, font=("Comic Sans MS", 10),
               command=lambda: [delete_history_clear_window(), delete_history_window()]).pack()

    Label(win, font='courier 12 bold', text='MESSAGE').place(x=60, y=60)
    Entry(win, font='courier 10', textvariable=Text, bg='ghost white').place(x=320, y=60)

    Label(win, font='courier 12 bold', text='CODE').place(x=60, y=90)
    Entry(win, font='courier 10', textvariable=Code, bg='ghost white').place(x=320, y=90)

    Label(win, font='courier 12 bold', text='MODE(e-encode, d-decode)').place(x=50, y=120)
    Entry(win, font='arial 10', textvariable=mode, bg='ghost white', width=4).place(x=320, y=120)
    Entry(win, font='courier', textvariable=Result, bg='ghost white', width=35).place(x=200, y=180)

    Button(win, font='courier', text='RESULT', padx=2, bg='green', command=Mode).place(x=90, y=175)

    Button(win, font=('Comic Sans MS', 12), text='RESET', width=10, height=1, command=Reset, fg='black', bg='grey',
           padx=2).place(x=275, y=250)

    Button(win, font=('Comic Sans MS', 12), text='VIEW HISTORY', bg='cyan', width=15, command=History).place(x=20,
                                                                                                             y=290)
    Button(win, font=('Comic Sans MS', 12), text='EXIT', width=6, command=Exit, bg='Red', padx=2, pady=2).place(x=510,
                                                                                                                y=420)

    def DClock():
        curr_time = time.strftime("%H:%M:%S")
        clock.config(text=curr_time)
        clock.after(100, DClock)

    clock = Label(win, font=("times", 150, "bold"), fg="black")
    clock.place()
    DClock()

    clock = Label(win, font="courier 15 bold", fg="black", text=DClock())
    clock.place(x=20, y=390)

    x = dt.datetime.now()

    Label(win, font="courier 13 bold", fg="black", text=x.strftime("%x")).place(x=20, y=420)#date
    Label(win, font="courier 15 bold", fg="black", text=x.strftime("%p")).place(x=130, y=390)#am/pm
    Label(win, font="courier 13 bold", fg="black", text=x.strftime("%A")).place(x=130, y=420)#day

    win.mainloop()


def register():
    global register_screen
    main_screen.destroy()
    register_screen = Tk()
    register_screen.title("Registration page")
    register_screen.geometry("400x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter your details below to register", font=("Comic Sans MS", 15)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username* ", font=("Comic Sans MS", 12))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, )
    username_entry.pack()
    password_lable = Label(register_screen, text="Password* ", font=("Comic Sans MS", 12))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="green", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    main_screen.destroy()
    login_screen = Tk()
    login_screen.title("Login page")
    login_screen.geometry("400x250")
    Label(login_screen, text="Enter your details below to Login", font=("Comic Sans MS", 15)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username* ", font=("Comic Sans MS", 12)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password* ", font=("Comic Sans MS", 12)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    try:
        global username1
        username1 = username.get()
        global password1
        password1 = password.get()

        if (password1 == ""):
            global Register_error_window
            Register_error_window = Tk()
            Register_error_window.title("Registeration Error")
            Register_error_window.geometry("250x100")
            Label(Register_error_window, text="Please enter valid Password.", font=("Comic Sans MS", 12),
                  fg="red").pack()
            Label(Register_error_window, text=" ", font=("Comic Sans MS", 12), ).pack()
            Button(Register_error_window, text="OK", font=("Comic Sans MS", 10), width=6,
                   command=delete_Register_error_window).pack()
            return

        file = open(username1, "w")
        file.write(username1 + "\n")
        file.write(password1)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)#to clear the content of the entry

        register_success()


    except FileNotFoundError:
        global file_not_found_screen
        file_not_found_screen = Tk()
        file_not_found_screen.geometry("300x100")
        file_not_found_screen.title("Error")
        Label(file_not_found_screen, text="Username and password required", fg="red", font=("Comic Sans MS", 12)).pack()
        Button(file_not_found_screen, text="OK", command=delete_file_not_found_screen).pack()


def login_verify():
    global username1
    username1 = username_verify.get()
    global password1
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, 'r')
        pwd = file1.readlines()
        if password1 == str(pwd[1].rstrip('\n')):
            login_success()


        else:
            password_not_recognised()

    else:
        user_not_found()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x100")
    Label(login_success_screen, text="Login Success!", fg="green", font=("Comic Sans MS", 15)).pack()
    Button(login_success_screen, text="OK", height=1, width=10, command=delete_login_success).pack()


def register_success():
    global register_success_screen
    register_success_screen = Toplevel(register_screen)
    register_success_screen.title("Success")
    register_success_screen.geometry("300x100")
    Label(register_success_screen, text="Registration Success!", fg="green", font=("Comic Sans MS", 15)).pack()
    Button(register_success_screen, text="OK", height=1, width=10, command=delete_register_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid Password")
    password_not_recog_screen.geometry("300x100")
    Label(password_not_recog_screen, text="Password not recognized!", fg="red2", font=("Comic Sans MS", 15)).pack()
    Button(password_not_recog_screen, text="OK", height=1, width=10, command=delete_password_not_recognised).pack()
    Label(password_not_recog_screen, text="Try again.", font=("Comic Sans MS", 12)).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Invalid user")
    user_not_found_screen.geometry("300x100")
    Label(user_not_found_screen, text="User Not Found", fg="red2", font=("Comic Sans MS", 15)).pack()
    Button(user_not_found_screen, text="OK", height=1, width=10, command=delete_user_not_found_screen).pack()
    Label(user_not_found_screen, text="Try again", font=("Comic Sans MS", 12)).pack()


def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    Encode_Decode()


def delete_register_success():
    register_success_screen.destroy()
    register_screen.destroy()
    Encode_Decode()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_file_not_found_screen():
    file_not_found_screen.destroy()


def delete_Register_error_window():
    Register_error_window.destroy()


def delete_error_window():
    error_window.destroy()


def delete_history_window():
    History_window.destroy()


def delete_history_clear_window():
    history_clear_window.destroy()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("550x350")
    main_screen.title("Account Login")
    Label(text="MESSAGE ENCODING AND DECODING", bg="turquoise", font=("Comic Sans MS", 18), width=50).pack()
    Label(text="What do you want to do?", width="300", height="2", font=("Comic Sans MS", 15)).pack()
    Label(text="Login here!", font=("Comic Sans MS", 12)).pack()
    Button(text="Login", height="2", width="35", fg="white", bg="gray35", command=login,
           font=("Comic Sans MS", 12)).pack()
    Label(text=" ", font=("Comic Sans MS", 12)).pack()
    Label(text="If you are new, register here!", font=("Comic Sans MS", 12)).pack()
    Button(text="Register", height="2", width="35", fg="white", bg="gray35", command=register,
           font=("Comic Sans MS", 12)).pack()

    main_screen.mainloop()


main_account_screen()

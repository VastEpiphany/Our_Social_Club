import tkinter as tk

def open_signup_window(window):
    #新界面基本内容确定
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up")

    tk.Label(signup_window,text="Freshman? Just give us your details to let us know!",font=("Helvetica",14)).pack(pady=10)
    tk.Entry(signup_window).pack()
    tk.Button(signup_window,text="Submit",font=("Helvetica",12)).pack(pady=10)
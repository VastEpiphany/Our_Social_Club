import tkinter
import ttkbootstrap as ttk
from Center_window import center_window
import csv

class SecurityQuestion_Config:
    def __init__(self,window,nickname):
        if nickname != None:
            self.file = "User_SecurityQuestion.csv"
            self.name = nickname
            self.window = ttk.Toplevel(window)

            center_window(self.window,800,400)
            self.window.title("Security Question Config")

            #标题label选择
            label1 = ttk.Label(self.window,text="Choose a category as your security question:")
            label1.place(x=200,y=30)

            #尝试使用ttk库中的RadioButton选项以作出问题选择
            c1 = ttk.Radiobutton(self.window,text="Your Birthday",command=lambda:self.c1_operation())
            c1.place(x=300,y=80)

            c2 = ttk.Radiobutton(self.window,text="Your Hometown",command=lambda:self.c2_operation())
            c2.place(x=300,y=120)

            c3 = ttk.Radiobutton(self.window,text="Your School",command=lambda:self.c3_operation())
            c3.place(x=300,y=160)


        else:
            self.window = tkinter.messagebox.showerror(title="Oops...",message="You even don't give a user name!")


    def c1_operation(self):
        window1 = ttk.Toplevel(self.window)
        center_window(window1,520,300)
        c1_category = "Birthday"

        window1.title("Birthday Question")

        label = ttk.Label(window1,text="Enter your nickname again:")
        label.place(x=80,y=70)

        name_Entry = ttk.Entry(window1,show=None)
        name_Entry.place(x=300,y=70)

        label1 = ttk.Label(window1,text="Enter your birthday:")
        label1.place(x=80,y=150)

        Dt_Entry = ttk.DateEntry(window1,bootstyle="dark")
        Dt_Entry.place(x=270,y=150)

        button = ttk.Button(window1,text="Submit",bootstyle="dark",command=lambda:self.handle_and_save(name_Entry.get(),c1_category,Dt_Entry.entry.get()))
        button.place(x=200,y=200)

    def c2_operation(self):
        window2 = ttk.Toplevel(self.window)
        center_window(window2, 520, 300)
        c2_category = "Hometown"

        window2.title("Hometown Question")

        label = ttk.Label(window2, text="Enter your nickname again:")
        label.place(x=80, y=70)

        name_Entry = ttk.Entry(window2, show=None)
        name_Entry.place(x=300, y=70)

        label1 = ttk.Label(window2, text="Enter your hometown:")
        label1.place(x=80, y=150)

        H_Entry = ttk.Entry(window2,show=None)
        H_Entry.place(x=270, y=150)

        button = ttk.Button(window2, text="Submit", bootstyle="dark",
                            command=lambda: self.handle_and_save(name_Entry.get(), c2_category, H_Entry.get()))
        button.place(x=200, y=200)

    def c3_operation(self):
        window3 = ttk.Toplevel(self.window)
        center_window(window3, 520, 300)
        c3_category = "School"

        window3.title("School Question")

        label = ttk.Label(window3, text="Enter your nickname again:")
        label.place(x=80, y=70)

        name_Entry = ttk.Entry(window3, show=None)
        name_Entry.place(x=300, y=70)

        label1 = ttk.Label(window3, text="Enter your school:")
        label1.place(x=80, y=150)

        S_Entry = ttk.Entry(window3, show=None)
        S_Entry.place(x=270, y=150)

        button = ttk.Button(window3, text="Submit", bootstyle="dark",
                            command=lambda: self.handle_and_save(name_Entry.get(), c3_category, S_Entry.get()))
        button.place(x=200, y=200)


    def handle_and_save(self, name, category, message):
        if not name:
            tkinter.messagebox.showerror("Error", "Nickname cannot be empty.")
            return

        try:
            with open(self.file, "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([name, category, message])
            tkinter.messagebox.showinfo("Success", "Security question set successfully.")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")


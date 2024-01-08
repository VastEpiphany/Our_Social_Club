import tkinter as tk
import ttkbootstrap as ttk
from hashlib import sha256
import csv
# change
class Main_ChangePsw:
    def __init__(self, window, user):
        self.user = user
        self.file = "User_file.csv"
        self.window = ttk.Toplevel(window)
        self.create_change_password_interface()

    def create_change_password_interface(self):
        self.window.title("Change Password")
        ttk.Label(self.window, text="Enter your current password:").grid(row=0, column=0, sticky='e')
        self.current_password_entry = ttk.Entry(self.window, show="*", width=50)
        self.current_password_entry.grid(row=0, column=1, pady=5, padx=5, sticky='ew')

        ttk.Label(self.window, text="Enter your new password:").grid(row=1, column=0, sticky='e')
        self.new_password_entry = ttk.Entry(self.window, show="*", width=50)
        self.new_password_entry.grid(row=1, column=1, pady=5, padx=5, sticky='ew')

        ttk.Label(self.window, text="Confirm your new password:").grid(row=2, column=0, sticky='e')
        self.confirm_password_entry = ttk.Entry(self.window, show="*", width=50)
        self.confirm_password_entry.grid(row=2, column=1, pady=5, padx=5, sticky='ew')

        submit_button = ttk.Button(self.window, text="Change Password", command=self.validate_and_change_password)
        submit_button.grid(row=3, column=1, pady=10, padx=5, sticky='ew')

    def validate_and_change_password(self):
        current_password_encrypted = sha256(self.current_password_entry.get().encode()).hexdigest()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not self.validate_current_password(current_password_encrypted):
            tk.messagebox.showerror("Error", "Current password is incorrect.")
            return

        if new_password != confirm_password:
            tk.messagebox.showerror("Error", "The new passwords do not match.")
            return

        if new_password:
            self.change_password_in_file(new_password)
        else:
            tk.messagebox.showwarning("Warning", "New password cannot be empty.")

    def validate_current_password(self, current_password_encrypted):
        try:
            with open(self.file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for user_id, user_nickname, user_psw in reader:
                    if user_nickname == self.user.nickname and current_password_encrypted == user_psw:
                        return True
                return False
        except FileNotFoundError:
            tk.messagebox.showerror("File Error", "User file not found.")
            return False

    def change_password_in_file(self, new_password):
        password_encrypt = sha256(new_password.encode()).hexdigest()
        try:
            users = []
            with open(self.file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for user_id, user_nickname, user_psw in reader:
                    if user_nickname == self.user.nickname:
                        users.append([user_id, user_nickname, password_encrypt])
                    else:
                        users.append([user_id, user_nickname, user_psw])

            with open(self.file, "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(users)

            tk.messagebox.showinfo("Success", "Password has been changed successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

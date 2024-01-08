import os
import shutil
import tkinter as tk
from Center_window import center_window
from tkinter import filedialog, messagebox

class FileSharingApp:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        master.title("File Sharing")
        center_window(self.master,800,600)

        # 设置共享文件夹路径为程序所在目录下的 "SharedFolder"
        self.shared_folder_path = os.path.join(os.path.dirname(__file__), "SharedFolder")

        # 创建上传和查看共享文件的按钮
        upload_button = tk.Button(self.master, text="Upload File", command=self.upload_file)
        upload_button.pack(pady=10)

        view_button = tk.Button(self.master, text="View Shared Files", command=self.view_shared_files)
        view_button.pack(pady=10)

    def upload_file(self):
        if not os.path.exists(self.shared_folder_path):
            os.makedirs(self.shared_folder_path)

        filename = filedialog.askopenfilename()
        if filename:
            shutil.copy(filename, self.shared_folder_path)
            messagebox.showinfo("Upload successfully", "The file has been uploaded to the shared folder.")

    def view_shared_files(self):
        try:
            os.startfile(self.shared_folder_path)
        except Exception as e:
            messagebox.showerror("Open failure", str(e))


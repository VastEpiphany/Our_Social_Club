import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Center_window import center_window
import os

class JobPosting:
    def __init__(self, master):
        self.master = master
        self.job_info_window = ttk.Toplevel(master)
        center_window(self.job_info_window, 600, 400)
        self.job_info_window.title("Post a Job")

        self.create_job_posting_interface()

    def create_job_posting_interface(self):
        ttk.Label(self.job_info_window, text="Job Title:").grid(row=0, column=0, sticky='e')
        self.job_title_entry = ttk.Entry(self.job_info_window, width=50)
        self.job_title_entry.grid(row=0, column=1, pady=5, padx=5, sticky='ew')

        ttk.Label(self.job_info_window, text="Job Description:").grid(row=1, column=0, sticky='e')
        self.job_desc_text = ttk.Text(self.job_info_window, width=50, height=10)
        self.job_desc_text.grid(row=1, column=1, pady=5, padx=5, sticky='ew')

        submit_button = ttk.Button(self.job_info_window, text="Post Job", command=self.save_job_info)
        submit_button.grid(row=2, column=1, pady=10, padx=5, sticky='ew')

        view_jobs_button = ttk.Button(self.job_info_window, text="View Posted Jobs", command=self.view_jobs)
        view_jobs_button.grid(row=3, column=1, pady=10, padx=5, sticky='ew')

    def save_job_info(self):
        job_title = self.job_title_entry.get()
        job_desc = self.job_desc_text.get("1.0", "end-1c")
        if job_title and job_desc:
            if not os.path.exists('job_posts'):
                os.mkdir('job_posts')
            with open(os.path.join('job_posts', f"{job_title}.txt"), 'w', encoding='utf-8') as file:
                file.write(f"Job Title: {job_title}\n")
                file.write("Job Description:\n")
                file.write(job_desc)
            tk.messagebox.showinfo("Success", "Job posted successfully.")
            self.job_info_window.destroy()
        else:
            tk.messagebox.showwarning("Warning", "Both title and description must be filled out.")

    def view_jobs(self):
        job_list_window = ttk.Toplevel(self.master)
        job_list_window.title("View Jobs")
        center_window(job_list_window, 600, 400)
        self.display_job_info(job_list_window)

    def display_job_info(self, job_list_window):
        job_text = ttk.Text(job_list_window, width=80, height=20)
        job_text.pack(side="left", fill="both", padx=10, pady=10)
        scrollbar = ttk.Scrollbar(job_list_window, orient="vertical", command=job_text.yview)
        scrollbar.pack(side="right", fill="y")
        job_text.config(yscrollcommand=scrollbar.set)

        if not os.path.exists('job_posts'):
            tk.messagebox.showinfo("Information", "No job postings are available.")
            return

        job_files = os.listdir('job_posts')
        if not job_files:
            tk.messagebox.showinfo("Information", "No job postings are available.")
            return

        combined_job_info = ""
        for job_file in job_files:
            with open(os.path.join('job_posts', job_file), 'r', encoding='utf-8') as file:
                job_info = file.read()
                combined_job_info += job_info + "\n" + "-" * 60 + "\n"

        job_text.insert("1.0", combined_job_info)
        job_text.config(state="disabled")

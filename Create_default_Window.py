import ttkbootstrap as ttk
import tkinter as tk
from Center_window import center_window

class Create_dafault_window:
    def __init__(self,window):
        self.window = ttk.Toplevel(window)
        center_window(self.window,800,600)
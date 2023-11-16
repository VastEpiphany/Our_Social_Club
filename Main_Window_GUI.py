import ttkbootstrap as ttk
from Center_window import center_window

def main():
    window = ttk.Window(themename='journal')
    window.title("Our Social Club")
    center_window(window, 1300, 900)

    window.mainloop()
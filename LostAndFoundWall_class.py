import tkinter as tk
import ttkbootstrap as ttk
from Center_window import center_window
from tkinter import filedialog, simpledialog, messagebox, Toplevel, Label, Entry, Text
from Create_default_Window import Create_dafault_window #导入基类
from PIL import Image, ImageTk
import datetime
import json


class LostAndFoundWall(Create_dafault_window):
    def __init__(self, root):
        super().__init__(root)   #调用父类构造函数
        self.window.title("Lost & Found")

        self.lost_items = {}
        self.file_path = 'lost_items.json'
        self.load_lost_items()

        lost_and_found_button = tk.Button(self.window, text="Lost And Found", command=self.open_lost_and_found)
        lost_and_found_button.pack()

    def load_lost_items(self):
        try:
            with open(self.file_path, 'r') as file:
                self.lost_items = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lost_items = []

    def save_lost_items(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.lost_items, file)

    def open_lost_and_found(self):
        option_window = tk.Toplevel(self.window)
        option_window.title("Options for Lost&Found")
        center_window(option_window,500,300)

        post_button = tk.Button(option_window, text="Upload the items",
                                command=lambda: [option_window.destroy(), self.create_post_window()])
        post_button.pack(pady=10)

        list_button = tk.Button(option_window, text="Check item lists",
                                command=lambda: [option_window.destroy(), self.show_lost_items()])
        list_button.pack(pady=10)

    def create_post_window(self):
        post_window = Toplevel(self.window)
        post_window.title("Upload the lost items")
        center_window(post_window,500,300)

        upload_button = tk.Button(post_window, text="Upload Image", command=lambda: self.upload_image(post_window))
        upload_button.pack()

        Label(post_window, text="Name:").pack()
        name_entry = Entry(post_window)
        name_entry.pack()

        Label(post_window, text="Detailed Description:").pack()
        description_text = Text(post_window, height=5, width=30)
        description_text.pack()

        submit_button = tk.Button(post_window, text="Submit", command=lambda: self.submit_post(name_entry.get(),
                                                                                               description_text.get(
                                                                                                   "1.0", tk.END),
                                                                                               post_window))
        submit_button.pack()

    def upload_image(self, window):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            self.temp_image = Image.open(self.filepath)
            self.temp_photo = ImageTk.PhotoImage(self.temp_image)
            canvas = tk.Canvas(window, width=300, height=300)
            canvas.pack()
            canvas.create_image(20, 20, anchor='nw', image=self.temp_photo)
            canvas.image = self.temp_photo
            self.selected_image_path = self.filepath

    def submit_post(self, name, description, window):
        if name and description.strip() and hasattr(self, 'temp_photo'):
            lost_item = {
                'name': name,
                'image_path': self.selected_image_path,
                'description': description,
                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.lost_items.append(lost_item)  # 将字典添加到列表中
            self.save_lost_items()
            window.destroy()
        else:
            messagebox.showwarning("Warning", "Please complete the information and upload an image!", parent=window)

    def show_lost_items(self):
        list_window = Toplevel(self.window)
        list_window.title("Lost Items List")

        listbox = tk.Listbox(list_window)
        listbox.pack()
        listbox.bind("<Double-Button-1>", lambda event: self.show_item_details(event, listbox))

        for name in self.lost_items:
            listbox.insert(tk.END, name)

    def show_item_details(self, event, listbox):
        selection = listbox.curselection()
        if selection:
            name = listbox.get(selection[0])
            item = self.lost_items[name]

            detail_window = Toplevel(self.window)
            detail_window.title("Detailed Information")
            center_window(detail_window,550,350)

            tk.Label(detail_window, text=f"Name: {name}").pack()
            tk.Label(detail_window, text=f"Description: {item['description']}").pack()
            tk.Label(detail_window, text=f"Date: {item['date']}").pack()

            tk.Label(detail_window, text="Lost Item Image:").pack()

            if item.get('image_path'):
                image = Image.open(item['image_path'])
                photo = ImageTk.PhotoImage(image)
                canvas = tk.Canvas(detail_window, width=300, height=300)
                canvas.pack()
                canvas.create_image(20, 20, anchor='nw', image=photo)
                detail_window.photo = photo

            delete_button = tk.Button(detail_window, text="Item Found",
                                      command=lambda: self.delete_item(name, selection[0], listbox, detail_window))
            delete_button.pack()

    def delete_item(self, name, index, listbox, detail_window):
        if name in self.lost_items:
            del self.lost_items[name]
            self.save_lost_items()
        listbox.delete(index)
        detail_window.destroy()


#Need Not To Know
    def select_and_display_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
        )
        if file_path:
            self.selected_image_path = file_path  # 保存选择的图片路径
            # 加载图片并调整大小以适应显示
            image = Image.open(file_path)
            image.thumbnail((200, 200), Image.ANTIALIAS)  # 调整图片大小
            self.photo = ImageTk.PhotoImage(image)  # 创建并保存PhotoImage对象

             # 如果还没有创建图片标签，则创建它
            if not self.image_label:
                self.image_label = tk.Label(self.window)
                self.image_label.pack(pady=5)

            # 如果photo属性已存在，则先销毁旧的Label
            if self.photo:
                self.image_label.destroy()

            # 创建新的PhotoImage对象
            self.photo = ImageTk.PhotoImage(image)

            # 在画布上显示图片
            self.canvas.create_image(100, 100, image=self.photo, anchor=tk.CENTER)
            self.canvas.image = self.photo  # 保持对PhotoImage对象的引用


    def update_lost_items_listbox(self):
        self.lost_items_listbox.delete(0, tk.END)  # 清空当前列表
        for item in self.lost_items:
            if not item["found"]:  # 只显示未找回的失物
                display_text = "{} - Posted on: {}".format(item["name"], item.get("post_date", "N/A"))
                self.lost_items_listbox.insert(tk.END, display_text)



    def view_item_details(self):
        selected_index = self.lost_items_listbox.curselection()
        if selected_index:
            selected_item = self.lost_items[selected_index[0]]
            details_window = tk.Toplevel(self.window)
            details_window.title("Item Details")
            center_window(details_window,600,300)

            tk.Label(details_window, text="Name: " + selected_item["name"]).pack()
            tk.Label(details_window, text="Description: " + selected_item["description"]).pack()

            # 加载并显示图片
            image_path = selected_item.get("image_path")
            if image_path:
                image = Image.open(image_path)
                image.thumbnail((200, 200))  # 缩小图片尺寸
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(details_window, image=photo)
                image_label.photo = photo  # 保存对photo的引用
                image_label.pack()


    def item_found(self):
        selected_index = self.lost_items_listbox.curselection()
        if selected_index:
            # 弹出窗口确认找回
            if tkinter.messagebox.askyesno("Confirm", "Mark this item as found?"):
                self.lost_items[selected_index[0]]["found"] = True
                self.update_lost_items_listbox()
                tkinter.messagebox.showinfo("Info", "Item marked as found successfully.")








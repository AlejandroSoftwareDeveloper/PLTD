# import uuid
# from tkinter import *

# print(uuid.uuid1())


# class ButtonsApp:
#     def __init__(self, main):
#         super().__init__()
#         self.frame = Frame(main)
#         self.lbl_saludo = Label(self.frame, text="Hola mundo")
#         self.lbl_saludo.pack()
#         self.frame.pack()


# if __name__ == "__main__":
#     root = Tk()
#     root.geometry("400x400")
#     app = ButtonsApp(root)
#     root.mainloop()
import tkinter as tk
import tkinter.filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = tk.Text(self, height=10, width=50)
        self.btn_save = tk.Button(self, text="Save", command=self.save_file)
        self.text.pack()
        self.btn_save.pack(pady=10, ipadx=5)

    def save_file(self):
        contents = self.text.get(1.0, tk.END)
        new_file = fd.asksaveasfile(
            title="Save file",
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"),),
        )

        if new_file:
            new_file.write(contents)
            new_file.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()

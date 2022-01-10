import  os
import tkinter as tk
from tkinter import ttk,filedialog

# # def greet():
# #     # print("Hello World")
# #     print(user_name.get() or 'Hello World')
#
# root = tk.Tk()
#
# main = ttk.Frame(root)
# main.pack(side="left", fill="both", expand=True)
#
#
# tk.Label(main, text="Label1 top", bg="red").pack(side="top", fill='both', expand=True)
# tk.Label(main, text="Label2 top", bg='red').pack(side='top', fill='both', expand=True)
#
# tk.Label(root, text="Label left", bg='green').pack(side='left', expand=True, fill='both')
#
#
# # root.title("Hello")
# #
# # user_name = tk.StringVar()
# #
# # greet_button = ttk.Button(root, text='Greet', command=greet)
# # greet_button.pack(side='left', fill='x', expand=True)
# #
# # quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# # quit_button.pack(side='left', fill='x', expand=True)
# #
# # name_label = ttk.Label(root, text="Name : ")
# # name_label.pack(side="left", padx=(0,10))
# #
# # name_entry = ttk.Entry(root, width=15, textvariable=user_name)
# # name_entry.pack(side='left')
# # name_entry.focus()


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill='both', expand=True)
    notebook.add(text_area, text='Untitled')
    notebook.select(text_area)


def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        filename = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")

        with open(file_path,"w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("File save operation cancelled")
        return

    notebook.tab("current", text=filename)

root = tk.Tk()
root.title("Penumatsa's First Text Editor")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx=1, pady=(4, 0))

menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")


file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Save as", command=save_file)






notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)
create_file()



root.mainloop()

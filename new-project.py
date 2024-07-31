import tkinter as tk
from tkinter import filedialog, Text, font, colorchooser, messagebox


root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, file.read())
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def undo_action():
    text_area.edit_undo()

def redo_action():
    text_area.edit_redo()

def change_font():
    font_choice = filedialog.askfont(root)
    if font_choice:
        text_area.config(font=(font_choice['family'], font_choice['size']))

def change_color():
    color_choice = colorchooser.askcolor()[1]
    if color_choice:
        text_area.config(fg=color_choice)

def count_words(event=None):
    text_content = text_area.get(1.0, tk.END)
    words = text_content.split()
    word_count = len(words)
    word_count_label.config(text=f"Word Count: {word_count}")


menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
menu_bar.add_cascade(label="Edit", menu=edit_menu)


format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Font", command=change_font)
format_menu.add_command(label="Color", command=change_color)
menu_bar.add_cascade(label="Format", menu=format_menu)

root.config(menu=menu_bar)


text_area = Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill="both")
word_count_label = tk.Label(root, text="Word Count: 0")
word_count_label.pack(side=tk.BOTTOM)

text_area.bind("<KeyRelease>", count_words)


root.mainloop()

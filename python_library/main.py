# import pandas
import tkinter as tk
from tkinter import filedialog

def open_file():
    """Open a file and display its content."""
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    filepaths = filedialog.askopenfilenames(
        initialdir="/Users/jose/Downloads",
        # initialdir="C:/Users/Cakow/PycharmProjects/Main",
        title="Open File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
        multiple=True
    )
    values = []
    for filepath in filepaths:
        with open(filepath, 'r') as file:
            content = file.read()
            print(content)
            values.append(content)
    return values  # Devuelve el contenido del archivo

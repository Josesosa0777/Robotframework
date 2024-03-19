import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from bs4 import BeautifulSoup

def open_file():
    """Open a file and display its content."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window of Tkinter

    filepaths = filedialog.askopenfilenames(
        initialdir=f'{os.path.expanduser("~")}/Downloads', # Downloads directory of main user
        title="Open File",
        filetypes=(("Text Files", "*.xls"), ("All Files", "*.*")),
        multiple=True
    )
    dfs = []  # List to storage the pandas DataFrames

    for filepath in filepaths:
        with open(filepath) as xml_file:
            soup = BeautifulSoup(xml_file.read(), 'xml')
            for sheet in soup.findAll('Worksheet'):
                sheet_as_list = []
                for row in sheet.findAll('Row'):
                    sheet_as_list.append([cell.Data.text if cell.Data else '' for cell in row.findAll('Cell')])
                sheet_name = sheet.attrs['ss:Name']  # Get the sheet name
                dfs.append((dfs, sheet_name))
    return dfs

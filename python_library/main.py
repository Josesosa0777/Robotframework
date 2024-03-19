import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from bs4 import BeautifulSoup

def open_file():
    """Open a file and display its content."""
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    filepaths = filedialog.askopenfilenames(
        # initialdir="/Users/jose/Downloads",
        initialdir=f'{os.path.expanduser("~")}/Downloads', # Downloads directory of main user
        title="Open File",
        filetypes=(("Text Files", "*.xls"), ("All Files", "*.*")),
        multiple=True
    )
    dfs = []  # Lista para almacenar los DataFrames de Pandas

    for filepath in filepaths:
        with open(filepath) as xml_file:
            soup = BeautifulSoup(xml_file.read(), 'xml')
            for sheet in soup.findAll('Worksheet'):
                sheet_as_list = []
                for row in sheet.findAll('Row'):
                    sheet_as_list.append([cell.Data.text if cell.Data else '' for cell in row.findAll('Cell')])
                sheet_name = sheet.attrs['ss:Name']  # Obtiene el nombre de la hoja de cálculo
                dfs.append((dfs, sheet_name))
                # df = pd.DataFrame(sheet_as_list)
                # print(df)
                # dfs.append(df)  # Agrega el DataFrame a la lista de DataFrames

    return dfs  # Devuelve la lista de DataFrames
    #     # Use pd.read_excel() to read the Excel file
    #     df = pd.read_excel(filepath, sheet_name="BOM")
    #     # Append the DataFrame to the values list
    #     values.append(df)
    #     # with open(filepath, 'r') as file:
    #     #     content = file.read()
    #     #     print(content)
    #     #     values.append(content)
    # return values # Devuelve el contenido del archivo
print(open_file())
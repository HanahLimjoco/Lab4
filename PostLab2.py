
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text files", "*.txt")])

print("Selected File:", file_path)

import tkinter as tk
from tkinter import filedialog
import json
from gui import GUI

def main():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        gui = GUI(data)
        gui.run()

if __name__ == '__main__':
    main()

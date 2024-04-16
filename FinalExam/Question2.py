# Question 2 - Christian Barrett

import tkinter as tk
from tkinter import ttk

FILE_LOCATION = 'preferences.txt'


def load_file():
    try:
        with open(FILE_LOCATION, 'r') as file:
            preferences = file.read().split(',')
            nameText.set(preferences[0].title())
            languageText.set(preferences[1].title())
            saveText.set(preferences[2])
    except FileNotFoundError:
        nameText.set("")
        languageText.set("English")
        saveText.set("10")


def save_file():
    name = nameText.get()
    language = languageText.get()
    save = saveText.get()
    isValid = True

    if name.strip(' ') == '':
        nameRequiredLabel.config(text="Required.")
        window.geometry("470x130")
        isValid = False

    if language.strip(' ') == '':
        languageRequiredLabel.config(text="Required.")
        window.geometry("470x130")
        isValid = False

    if save.strip(' ') == '' or not save.isnumeric():
        intLabel.config(text="Must be valid integer.")
        window.geometry("470x130")
        isValid = False

    if isValid:
        nameRequiredLabel.config(text="")
        languageRequiredLabel.config(text="")
        intLabel.config(text="")
        window.geometry("360x130")
        with open(FILE_LOCATION, 'w') as file:
            file.write(f"{name.lower()},{language.lower()},{save}")
        window.destroy()


def cancel():
    window.destroy()


window = tk.Tk()
window.title("Preferences")
window.geometry("360x130")
window.resizable(False, False)

frame = tk.Frame(window, padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)

nameLabel = ttk.Label(frame, text="Name: ")
nameLabel.grid(row=0, column=0, sticky=tk.E)
nameText = tk.StringVar()
nameEntry = ttk.Entry(frame, width=25, textvariable=nameText)
nameEntry.grid(row=0, column=1)

nameRequiredLabel = ttk.Label(frame, text="")
nameRequiredLabel.grid(row=0, column=2, sticky=tk.W)

languageLabel = ttk.Label(frame, text="Language: ")
languageLabel.grid(row=1, column=0, sticky=tk.E)
languageText = tk.StringVar()
languageEntry = ttk.Entry(frame, width=25, textvariable=languageText)
languageEntry.grid(row=1, column=1)

languageRequiredLabel = ttk.Label(frame, text="")
languageRequiredLabel.grid(row=1, column=2, sticky=tk.W)

saveLabel = ttk.Label(frame, text="Auto Save Every X Minutes: ")
saveLabel.grid(row=2, column=0, sticky=tk.E)
saveText = tk.StringVar()
saveEntry = ttk.Entry(frame, width=25, textvariable=saveText)
saveEntry.grid(row=2, column=1)

intLabel = ttk.Label(frame, text="")
intLabel.grid(row=2, column=2, sticky=tk.W)

saveButton = ttk.Button(frame, text="Save", command=save_file)
saveButton.grid(row=3, column=1, sticky=tk.W)

cancelButton = ttk.Button(frame, text="Cancel", command=cancel)
cancelButton.grid(row=3, column=1, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

load_file()
window.mainloop()

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox

# Create an empty window
main_window = tk.Tk()
main_window.title("Future Value Calculator")
main_window.geometry("500x250")

frame = ttk.Frame(main_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def save_changes():
    pass


def exit_window():
    main_window.destroy()


player_id_label = ttk.Label(frame, text="Player ID: ")
player_id_label.grid(column=0, row=0, sticky=tk.E)

player_id_text = tk.StringVar()
player_id_entry = ttk.Entry(frame, width=25, textvariable=player_id_text)
player_id_entry.grid(column=1, row=0)
player_id_entry.insert(0, "1")

first_name_label = ttk.Label(frame, text="First name: ")
first_name_label.grid(column=0, row=1, sticky=tk.E)

first_name_text = tk.StringVar()
first_name_entry = ttk.Entry(frame, width=25, textvariable=first_name_text)
first_name_entry.grid(column=1, row=1)

last_name_label = ttk.Label(frame, text="Last name: ")
last_name_label.grid(column=0, row=2, sticky=tk.E)

last_name_text = tk.StringVar()
last_name_entry = ttk.Entry(frame, width=25, textvariable=last_name_text)
last_name_entry.grid(column=1, row=2)

positions_label = ttk.Label(frame, text="Positions: ")
positions_label.grid(column=0, row=3, sticky=tk.E)


def show():
    tk.Label.config(text=clicked.get())



options = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(frame, clicked, *options)
drop.config(width=19)
drop.grid(column=1, row=3)

at_bats_label = ttk.Label(frame, text="At bats: ")
at_bats_label.grid(column=0, row=4, sticky=tk.E)

at_bats_text = tk.StringVar()
at_bats_entry = ttk.Entry(frame, width=25, textvariable=at_bats_text)
at_bats_entry.grid(column=1, row=4)

hits_label = ttk.Label(frame, text="Hits: ")
hits_label.grid(column=0, row=5, sticky=tk.E)

hits_text = tk.StringVar()
hits_entry = ttk.Entry(frame, width=25, textvariable=hits_text)
hits_entry.grid(column=1, row=5)

batting_average_label = ttk.Label(frame, text="Batting Avg: ")
batting_average_label.grid(column=0, row=6, sticky=tk.E)

batting_average_text = tk.StringVar()
batting_average_entry = ttk.Entry(frame, width=25, textvariable=batting_average_text)
batting_average_entry.grid(column=1, row=6)
batting_average_entry.config(state="readonly")

save_changes_button = ttk.Button(frame, text="Save Changes", command=save_changes)
save_changes_button.grid(column=1, row=7, sticky=tk.W)
exit_button = ttk.Button(frame, text="Exit", command=exit_window)
exit_button.grid(column=1, row=7, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)


main_window.mainloop()

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Create an empty window
main_window = tk.Tk()
main_window.title("Future Value Calculator")
main_window.geometry("310x165")

frame = ttk.Frame(main_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def calculate():
    response = messagebox.askokcancel("Calculate?", "Continue with entered values?")

    if response:
        try:
            year = str(float(yearly_interest_entry.get()))
            yearly_interest_entry.delete(0, tk.END)
            yearly_interest_entry.insert(0, year)
            total = 0.0
            for m in range(int(years_entry.get()) * 12):
                total += float(monthly_investment_entry.get())
                total += total * float(yearly_interest_entry.get()) / 100 / 12

            future_value_text.set(locale.currency(total, grouping=True))
        except ValueError as e:
            messagebox.showerror("ValueError", e)


def exit_window():
    main_window.destroy()


monthly_investment_label = ttk.Label(frame, text="Monthly Investment: ")
monthly_investment_label.grid(column=0, row=0, sticky=tk.E)

monthly_investment_text = tk.StringVar()
monthly_investment_entry = ttk.Entry(frame, width=25, textvariable=monthly_investment_text)
monthly_investment_entry.grid(column=1, row=0)
monthly_investment_entry.insert(0, "100")

yearly_interest_label = ttk.Label(frame, text="Yearly Interest Rate: ")
yearly_interest_label.grid(column=0, row=1, sticky=tk.E)

yearly_interest_text = tk.StringVar()
yearly_interest_entry = ttk.Entry(frame, width=25, textvariable=yearly_interest_text)
yearly_interest_entry.grid(column=1, row=1)
yearly_interest_entry.insert(0, "2.0")

years_label = ttk.Label(frame, text="Years: ")
years_label.grid(column=0, row=2, sticky=tk.E)

years_text = tk.StringVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(column=1, row=2)
years_entry.insert(0, "1")

future_value_label = ttk.Label(frame, text="Future Value: ")
future_value_label.grid(column=0, row=3, sticky=tk.E)

future_value_text = tk.StringVar()
future_value_entry = ttk.Entry(frame, width=25, textvariable=future_value_text)
future_value_entry.grid(column=1, row=3)
future_value_entry.insert(0, "$0,000.00")
future_value_entry.config(state="readonly")

calculate_button = ttk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(column=1, row=4, sticky=tk.W)
exit_button = ttk.Button(frame, text="Exit", command=exit_window)
exit_button.grid(column=1, row=4, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)


main_window.mainloop()
